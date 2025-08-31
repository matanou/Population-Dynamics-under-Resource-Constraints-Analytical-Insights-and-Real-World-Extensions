import io
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


# ------------------------------
# Core math: coupled P–R system
# ------------------------------
def f_rhs(t, y, r, c, q, k):
    """Right-hand side of the coupled ODE system.
       y = [P, R]
       dP/dt = r P (1 - cP/R)
       dR/dt = q - k P
       Handles R<=0 by softly clipping denominator to avoid division by ~0.
    """
    P, R = y
    R_safe = max(R, 1e-12)
    dP = r * P * (1.0 - (c * P) / R_safe)
    dR = q - k * P
    return np.array([dP, dR], dtype=np.float64)


def rk4_step(t, y, h, r, c, q, k):
    """One classical RK4 step for y' = f(t, y)."""
    k1 = f_rhs(t, y, r, c, q, k)
    k2 = f_rhs(t + 0.5*h, y + 0.5*h*k1, r, c, q, k)
    k3 = f_rhs(t + 0.5*h, y + 0.5*h*k2, r, c, q, k)
    k4 = f_rhs(t + h, y + h*k3, r, c, q, k)
    return y + (h/6.0)*(k1 + 2*k2 + 2*k3 + k4)


def integrate_ode(t0, T, N, y0, r, c, q, k, floor_R=0.0, floor_P=0.0):
    """Fixed-step RK4 integrator over [0, T] with N steps, starting at t0.
       Enforces non-negativity floors on P, R if desired.
    """
    t = np.linspace(t0, T, int(N), dtype=np.float64)
    Y = np.zeros((len(t), 2), dtype=np.float64)
    Y[0] = y0
    h = (T - t0) / (N - 1)
    for i in range(1, len(t)):
        y_next = rk4_step(t[i-1], Y[i-1], h, r, c, q, k)
        # Optional non-negativity (can be toggled if you wish)
        y_next[0] = max(y_next[0], floor_P)
        y_next[1] = max(y_next[1], floor_R)
        Y[i] = y_next
    return t, Y[:, 0], Y[:, 1]


def jacobian(P, R, r, c, q, k):
    """Jacobian matrix of the vector field at (P, R)."""
    R_safe = max(R, 1e-12)
    # d/dP of rP(1 - cP/R) = r(1 - 2cP/R)
    dF_dP = r * (1.0 - 2.0 * c * P / R_safe)
    # d/dR of rP(1 - cP/R) = rP * (cP/R^2)
    dF_dR = r * P * (c * P / (R_safe**2))
    # second row: d/dP(q - kP) = -k, d/dR(...) = 0
    dG_dP = -k
    dG_dR = 0.0
    return np.array([[dF_dP, dF_dR],
                     [dG_dP, dG_dR]], dtype=np.float64)


def equilibrium(r, c, q, k):
    """Analytic equilibrium (if q>0, k>0): P* = q/k, R* = c q/k."""
    if k <= 0:
        return None
    Pstar = q / k
    Rstar = c * Pstar
    return Pstar, Rstar


# ------------------------------
# Tkinter App
# ------------------------------
class CoupledPRApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Coupled Population–Resource Dynamics (Tk)")
        self.geometry("1400x940")
        self.minsize(1180, 760)

        # --- Tk variables ---
        self.dark_mode = tk.BooleanVar(value=True)
        self.show_axes = tk.BooleanVar(value=False)
        self.show_grid = tk.BooleanVar(value=False)

        self.show_nullclines = tk.BooleanVar(value=True)
        self.show_equilibrium = tk.BooleanVar(value=True)
        self.show_vector_field = tk.BooleanVar(value=True)
        self.lock_positive = tk.BooleanVar(value=True)

        self.r = tk.DoubleVar(value=0.6)
        self.c = tk.DoubleVar(value=0.8)
        self.q = tk.DoubleVar(value=20.0)
        self.k = tk.DoubleVar(value=0.2)

        self.T = tk.DoubleVar(value=60.0)
        self.steps = tk.IntVar(value=1200)
        self.linewidth = tk.DoubleVar(value=1.8)
        self.marker_size = tk.DoubleVar(value=0.0)  # 0 = off

        # vector field density
        self.p_samples = tk.IntVar(value=18)
        self.r_samples = tk.IntVar(value=18)

        # initial conditions (list of (P0, R0))
        self.ICs = [(10.0, 80.0), (30.0, 50.0), (80.0, 120.0)]
        self.ic_p = tk.DoubleVar(value=20.0)
        self.ic_r = tk.DoubleVar(value=60.0)

        # --- Layout ---
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        self.sidebar = ttk.Frame(self, padding=10)
        self.sidebar.grid(row=0, column=0, sticky="nsw")
        self.main = ttk.Frame(self, padding=(10, 10, 10, 10))
        self.main.grid(row=0, column=1, sticky="nsew")
        self.main.columnconfigure(0, weight=1)
        self.main.rowconfigure(0, weight=1)

        # Tabs & figures
        self.tabs = ttk.Notebook(self.main)
        self.tabs.grid(row=0, column=0, sticky="nsew")

        tab_time = ttk.Frame(self.tabs); tab_time.columnconfigure(0, weight=1); tab_time.rowconfigure(0, weight=1)
        tab_phase = ttk.Frame(self.tabs); tab_phase.columnconfigure(0, weight=1); tab_phase.rowconfigure(0, weight=1)
        self.tabs.add(tab_time, text="Time Series: P(t), R(t)")
        self.tabs.add(tab_phase, text="Phase Plane: R vs P")

        # time series fig
        self.fig_time = Figure(figsize=(8, 6), dpi=100)
        self.ax_time = self.fig_time.add_subplot(111)
        self.canvas_time = FigureCanvasTkAgg(self.fig_time, master=tab_time)
        self.canvas_time.get_tk_widget().grid(row=0, column=0, sticky="nsew")

        # phase plane fig
        self.fig_phase = Figure(figsize=(8, 6), dpi=100)
        self.ax_phase = self.fig_phase.add_subplot(111)
        self.canvas_phase = FigureCanvasTkAgg(self.fig_phase, master=tab_phase)
        self.canvas_phase.get_tk_widget().grid(row=0, column=0, sticky="nsew")

        # status
        self.status = ttk.Label(self.main, text="Ready.", anchor="w")
        self.status.grid(row=1, column=0, sticky="ew", pady=(8, 0))

        # Build sidebar & initial draw
        self._build_sidebar()
        self._apply_dark_mode()
        self._draw_all()

    # ------------- Sidebar -------------
    def _build_sidebar(self):
        sb = self.sidebar
        for c in (0, 1): sb.columnconfigure(c, weight=1 if c == 1 else 0)

        # Parameters
        pf = ttk.LabelFrame(sb, text="Model Parameters", padding=10)
        pf.grid(row=0, column=0, columnspan=2, sticky="new", pady=(0, 10))
        for c in (0, 1): pf.columnconfigure(c, weight=1 if c == 1 else 0)

        def row(r, text, widget):
            ttk.Label(pf, text=text).grid(row=r, column=0, sticky="w", padx=(0, 6), pady=2)
            widget.grid(row=r, column=1, sticky="ew", pady=2)

        row(0, "Growth rate r", ttk.Spinbox(pf, from_=0.0, to=10.0, increment=0.01, textvariable=self.r,
                                            command=self._draw_all))
        row(1, "Consumption coeff. c", ttk.Spinbox(pf, from_=0.0, to=100.0, increment=0.01, textvariable=self.c,
                                                   command=self._draw_all))
        row(2, "Resource inflow q", ttk.Spinbox(pf, from_=0.0, to=1e6, increment=0.1, textvariable=self.q,
                                                command=self._draw_all))
        row(3, "Per-capita usage k", ttk.Spinbox(pf, from_=0.0001, to=1e6, increment=0.01, textvariable=self.k,
                                                 command=self._draw_all))
        row(4, "Time horizon T", ttk.Spinbox(pf, from_=1.0, to=1e6, increment=1.0, textvariable=self.T,
                                             command=self._draw_all))
        row(5, "Steps (N)", ttk.Spinbox(pf, from_=50, to=200000, increment=50, textvariable=self.steps,
                                        command=self._draw_all))

        # Initial conditions
        icf = ttk.LabelFrame(sb, text="Initial Conditions (P₀, R₀)", padding=10)
        icf.grid(row=1, column=0, columnspan=2, sticky="new", pady=(0, 10))
        for c in (0, 1): icf.columnconfigure(c, weight=1 if c == 1 else 0)

        self.ic_listbox = tk.Listbox(icf, height=7, exportselection=False)
        self.ic_listbox.grid(row=0, column=0, columnspan=2, sticky="nsew", pady=(0, 6))
        self._refresh_ic_listbox()

        ttk.Label(icf, text="Add P₀").grid(row=1, column=0, sticky="w", padx=(0, 6))
        ttk.Spinbox(icf, from_=0.0, to=1e9, increment=1.0, textvariable=self.ic_p).grid(row=1, column=1, sticky="ew")
        ttk.Label(icf, text="Add R₀").grid(row=2, column=0, sticky="w", padx=(0, 6))
        ttk.Spinbox(icf, from_=0.0, to=1e9, increment=1.0, textvariable=self.ic_r).grid(row=2, column=1, sticky="ew")

        btns = ttk.Frame(icf); btns.grid(row=3, column=0, columnspan=2, sticky="ew", pady=(6, 0))
        btns.columnconfigure((0,1,2), weight=1)
        ttk.Button(btns, text="Add", command=self._add_ic).grid(row=0, column=0, sticky="ew")
        ttk.Button(btns, text="Remove selected", command=self._remove_selected_ic).grid(row=0, column=1, sticky="ew", padx=6)
        ttk.Button(btns, text="Clear", command=self._clear_ics).grid(row=0, column=2, sticky="ew")

        # Style
        sf = ttk.LabelFrame(sb, text="Style", padding=10)
        sf.grid(row=2, column=0, columnspan=2, sticky="new", pady=(0, 10))
        for c in (0, 1): sf.columnconfigure(c, weight=1 if c == 1 else 0)

        ttk.Checkbutton(sf, text="Dark mode", variable=self.dark_mode, command=self._apply_dark_mode)\
            .grid(row=0, column=1, sticky="w")
        ttk.Checkbutton(sf, text="Show axes", variable=self.show_axes, command=self._draw_all)\
            .grid(row=1, column=1, sticky="w")
        ttk.Checkbutton(sf, text="Show grid", variable=self.show_grid, command=self._draw_all)\
            .grid(row=2, column=1, sticky="w")

        ttk.Label(sf, text="Line width").grid(row=3, column=0, sticky="w", padx=(0,6))
        ttk.Scale(sf, from_=0.5, to=4.0, variable=self.linewidth, orient="horizontal",
                  command=lambda *_: self._draw_all()).grid(row=3, column=1, sticky="ew")
        ttk.Label(sf, text="Marker size").grid(row=4, column=0, sticky="w", padx=(0,6))
        ttk.Scale(sf, from_=0.0, to=8.0, variable=self.marker_size, orient="horizontal",
                  command=lambda *_: self._draw_all()).grid(row=4, column=1, sticky="ew")

        # Phase plane options
        ppf = ttk.LabelFrame(sb, text="Phase Plane Options", padding=10)
        ppf.grid(row=3, column=0, columnspan=2, sticky="new", pady=(0,10))
        for c in (0, 1): ppf.columnconfigure(c, weight=1 if c == 1 else 0)

        ttk.Checkbutton(ppf, text="Show nullclines", variable=self.show_nullclines, command=self._draw_phase)\
            .grid(row=0, column=1, sticky="w")
        ttk.Checkbutton(ppf, text="Show equilibrium", variable=self.show_equilibrium, command=self._draw_phase)\
            .grid(row=1, column=1, sticky="w")
        ttk.Checkbutton(ppf, text="Show vector field", variable=self.show_vector_field, command=self._draw_phase)\
            .grid(row=2, column=1, sticky="w")
        ttk.Checkbutton(ppf, text="Enforce P,R ≥ 0", variable=self.lock_positive, command=self._draw_all)\
            .grid(row=3, column=1, sticky="w")

        ttk.Label(ppf, text="P samples").grid(row=4, column=0, sticky="w", padx=(0,6))
        ttk.Spinbox(ppf, from_=6, to=200, increment=1, textvariable=self.p_samples,
                    command=self._draw_phase).grid(row=4, column=1, sticky="ew")
        ttk.Label(ppf, text="R samples").grid(row=5, column=0, sticky="w", padx=(0,6))
        ttk.Spinbox(ppf, from_=6, to=200, increment=1, textvariable=self.r_samples,
                    command=self._draw_phase).grid(row=5, column=1, sticky="ew")

        # Actions
        ttk.Button(sb, text="Plot", command=self._draw_all).grid(row=4, column=1, sticky="ew")
        ttk.Button(sb, text="Save PNG (Time Series)", command=self._save_png_time).grid(row=5, column=1, sticky="ew", pady=(6,0))
        ttk.Button(sb, text="Save PNG (Phase)", command=self._save_png_phase).grid(row=6, column=1, sticky="ew", pady=(6,0))
        ttk.Button(sb, text="Export CSV (Time Series)", command=self._export_csv).grid(row=7, column=1, sticky="ew", pady=(6,0))

        ttk.Label(sb, text="Tip: nullclines R=cP and P=q/k reveal the equilibrium.").grid(row=8, column=0, columnspan=2, sticky="ew", pady=(8,0))

    def _refresh_ic_listbox(self):
        self.ic_listbox.delete(0, tk.END)
        for (p0, r0) in self.ICs:
            self.ic_listbox.insert(tk.END, f"P₀={p0:g}, R₀={r0:g}")

    def _add_ic(self):
        try:
            p0 = float(self.ic_p.get()); r0 = float(self.ic_r.get())
            if p0 < 0 or r0 < 0:
                raise ValueError
        except Exception:
            messagebox.showerror("Invalid IC", "P₀ and R₀ must be non-negative numbers.")
            return
        self.ICs.append((p0, r0))
        self._refresh_ic_listbox()
        self._draw_all()

    def _remove_selected_ic(self):
        sel = list(self.ic_listbox.curselection())
        if not sel:
            return
        for i in reversed(sel):
            del self.ICs[i]
        self._refresh_ic_listbox()
        self._draw_all()

    def _clear_ics(self):
        self.ICs.clear()
        self._refresh_ic_listbox()
        self._draw_all()

    # ------------- Drawing & theming -------------
    def _apply_dark_mode(self):
        dark = self.dark_mode.get()
        bg = "#0e1117" if dark else "#ffffff"
        fg = "#e5e7eb" if dark else "#111827"

        for ax, fig in [(self.ax_time, self.fig_time), (self.ax_phase, self.fig_phase)]:
            ax.set_facecolor(bg); fig.patch.set_facecolor(bg)
            for s in ax.spines.values(): s.set_color(fg)
            ax.tick_params(colors=fg)
            ax.yaxis.label.set_color(fg); ax.xaxis.label.set_color(fg); ax.title.set_color(fg)
            leg = ax.get_legend()
            if leg is not None:
                leg.get_frame().set_facecolor(bg)
                for txt in leg.get_texts(): txt.set_color(fg)

        self.canvas_time.draw()
        self.canvas_phase.draw()

    def _toggle_axes_grid(self, ax):
        if self.show_axes.get():
            for s in ax.spines.values(): s.set_visible(True)
        else:
            for s in ax.spines.values(): s.set_visible(False)
        ax.grid(self.show_grid.get(), linewidth=0.5, alpha=0.3)

    def _draw_all(self):
        self._draw_time_series()
        self._draw_phase()

    def _read_params(self):
        try:
            r = float(self.r.get()); c = float(self.c.get())
            q = float(self.q.get()); k = float(self.k.get())
            T = float(self.T.get()); N = int(self.steps.get())
            assert T > 0 and N >= 2 and k > 0
        except Exception:
            messagebox.showerror("Invalid parameters",
                                 "Ensure T>0, steps≥2, k>0 (and numeric r,c,q).")
            return None
        return r, c, q, k, T, N

    def _draw_time_series(self):
        params = self._read_params()
        if params is None:
            return
        r, c, q, k, T, N = params

        self.ax_time.clear()
        self.ax_time.set_title("Coupled Dynamics: P(t) and R(t)")
        self.ax_time.set_xlabel("t")
        self.ax_time.set_ylabel("P(t), R(t)")
        self._toggle_axes_grid(self.ax_time)

        lw = float(self.linewidth.get())
        ms = float(self.marker_size.get())
        line_kwargs = dict(linewidth=lw)
        if ms > 0.0:
            line_kwargs["marker"] = "o"
            line_kwargs["markersize"] = ms
            line_kwargs["markevery"] = max(1, int(N)//40)

        count = 0
        for (P0, R0) in self.ICs:
            t, P, R = integrate_ode(
                t0=0.0, T=T, N=N, y0=np.array([P0, R0], dtype=np.float64),
                r=r, c=c, q=q, k=k,
                floor_R=(0.0 if not self.lock_positive.get() else 0.0),
                floor_P=(0.0 if not self.lock_positive.get() else 0.0)
            )
            self.ax_time.plot(t, P, label=f"P(t) | P₀={P0:g}, R₀={R0:g}", **line_kwargs)
            self.ax_time.plot(t, R, linestyle="--", label=f"R(t) | P₀={P0:g}, R₀={R0:g}", **line_kwargs)
            count += 1

        if count == 0:
            self.status.config(text="No initial conditions. Add (P₀, R₀) to plot.")
        else:
            leg = self.ax_time.legend(loc="best", frameon=True)
            if self.dark_mode.get() and leg:
                leg.get_frame().set_edgecolor("#e5e7eb")
            self.status.config(text=f"Plotted {count} trajectory set(s).")

        # Equilibrium readout
        eq = equilibrium(r, c, q, k)
        if eq is not None and self.show_equilibrium.get():
            Pstar, Rstar = eq
            self.ax_time.axhline(Pstar, linestyle=":", alpha=0.7, linewidth=1.0)
            self.ax_time.axhline(Rstar, linestyle=":", alpha=0.7, linewidth=1.0)
            self.ax_time.text(t[0], Pstar, "  P*", va="center", alpha=0.8)
            self.ax_time.text(t[0], Rstar, "  R*", va="center", alpha=0.8)

        self._apply_dark_mode()
        self.canvas_time.draw()

    def _draw_phase(self):
        params = self._read_params()
        if params is None:
            return
        r, c, q, k, T, N = params

        self.ax_phase.clear()
        self.ax_phase.set_title("Phase Plane: R vs P")
        self.ax_phase.set_xlabel("P")
        self.ax_phase.set_ylabel("R")
        self._toggle_axes_grid(self.ax_phase)

        # Determine plot window from ICs & a heuristic buffer
        Pmax = max([p for p, _ in self.ICs], default=50.0)
        Rmax = max([r0 for _, r0 in self.ICs], default=50.0)
        # include equilibrium scales
        eq = equilibrium(r, c, q, k)
        if eq is not None:
            Pstar, Rstar = eq
            Pmax = max(Pmax, Pstar * 1.4 + 10.0)
            Rmax = max(Rmax, Rstar * 1.4 + 10.0)
        Pmax = max(Pmax, 1.0); Rmax = max(Rmax, 1.0)

        # Vector field
        if self.show_vector_field.get():
            ps = max(6, int(self.p_samples.get()))
            rs = max(6, int(self.r_samples.get()))
            P_vals = np.linspace(0.0, Pmax, ps)
            R_vals = np.linspace(0.0, Rmax, rs)
            PP, RR = np.meshgrid(P_vals, R_vals)
            dP = np.zeros_like(PP); dR = np.zeros_like(RR)
            for i in range(RR.shape[0]):
                for j in range(PP.shape[1]):
                    v = f_rhs(0.0, np.array([PP[i, j], RR[i, j]]), r, c, q, k)
                    dP[i, j], dR[i, j] = v[0], v[1]

            # Normalize for plotting
            mag = np.hypot(dP, dR)
            mag[mag == 0] = 1.0
            U = dP / mag
            V = dR / mag
            self.ax_phase.quiver(PP, RR, U, V, angles="xy", scale_units="xy", scale=22.0,
                                 width=0.0022, alpha=0.33)

        # Nullclines: dP/dt=0 → P=0 (P-axis) or R=cP (line); dR/dt=0 → P=q/k (vertical)
        if self.show_nullclines.get():
            P_line = np.linspace(0.0, Pmax, 400)
            R_line = c * P_line
            self.ax_phase.plot(P_line, R_line, linestyle="--", linewidth=1.3, alpha=0.9, label="dP/dt=0 (R=cP)")

            if k > 0:
                P_vert = q / k
                self.ax_phase.axvline(P_vert, linestyle="--", linewidth=1.3, alpha=0.9, label="dR/dt=0 (P=q/k)")

        # Trajectories from ICs
        lw = float(self.linewidth.get())
        ms = float(self.marker_size.get())
        line_kwargs = dict(linewidth=lw)
        if ms > 0.0:
            line_kwargs["marker"] = None  # keep phase clean

        for (P0, R0) in self.ICs:
            t, P, R = integrate_ode(
                t0=0.0, T=T, N=N, y0=np.array([P0, R0]),
                r=r, c=c, q=q, k=k,
                floor_R=(0.0 if not self.lock_positive.get() else 0.0),
                floor_P=(0.0 if not self.lock_positive.get() else 0.0)
            )
            self.ax_phase.plot(P, R, **line_kwargs)
            # arrowheads along trajectory (subsample)
            idxs = np.linspace(0, len(P)-2, 12, dtype=int)
            for i in idxs:
                self.ax_phase.annotate("",
                    xy=(P[i+1], R[i+1]), xytext=(P[i], R[i]),
                    arrowprops=dict(arrowstyle="->", lw=max(0.8, lw-0.6), alpha=0.55))

        # Equilibrium marker & eigenvalues
        if eq is not None and self.show_equilibrium.get():
            Pstar, Rstar = eq
            self.ax_phase.scatter([Pstar], [Rstar], s=60, zorder=5)
            J = jacobian(Pstar, Rstar, r, c, q, k)
            lam = np.linalg.eigvals(J)
            lam_str = f"λ₁={lam[0]:.3g}, λ₂={lam[1]:.3g}"
            self.ax_phase.text(Pstar, Rstar, f"  * (P*,R*)\n  {lam_str}", va="bottom", ha="left", fontsize=9)

        leg = self.ax_phase.legend(loc="best", frameon=True)
        if self.dark_mode.get() and leg:
            leg.get_frame().set_edgecolor("#e5e7eb")

        # bounds
        self.ax_phase.set_xlim(0, Pmax)
        self.ax_phase.set_ylim(0, Rmax)

        self._apply_dark_mode()
        self.canvas_phase.draw()

    # ------------- Export / Save -------------
    def _save_png_time(self):
        path = filedialog.asksaveasfilename(defaultextension=".png",
                                            filetypes=[("PNG image", "*.png")])
        if not path:
            return
        buf = io.BytesIO(); self.fig_time.savefig(buf, format="png", dpi=200, bbox_inches="tight")
        with open(path, "wb") as f:
            f.write(buf.getvalue())
        self.status.config(text=f"Saved Time Series PNG → {path}")

    def _save_png_phase(self):
        path = filedialog.asksaveasfilename(defaultextension=".png",
                                            filetypes=[("PNG image", "*.png")])
        if not path:
            return
        buf = io.BytesIO(); self.fig_phase.savefig(buf, format="png", dpi=200, bbox_inches="tight")
        with open(path, "wb") as f:
            f.write(buf.getvalue())
        self.status.config(text=f"Saved Phase PNG → {path}")

    def _export_csv(self):
        if not self.ICs:
            messagebox.showinfo("Nothing to export", "Add at least one (P₀, R₀).")
            return

        params = self._read_params()
        if params is None:
            return
        r, c, q, k, T, N = params

        path = filedialog.asksaveasfilename(defaultextension=".csv",
                                            filetypes=[("CSV file", "*.csv")])
        if not path:
            return

        t = np.linspace(0.0, T, int(N), dtype=np.float64)
        # columns: t, then for each IC: P^(i), R^(i)
        headers = ["t"]
        data_cols = [t]
        for (P0, R0) in self.ICs:
            tt, P, R = integrate_ode(
                t0=0.0, T=T, N=N, y0=np.array([P0, R0], dtype=np.float64),
                r=r, c=c, q=q, k=k,
                floor_R=(0.0 if not self.lock_positive.get() else 0.0),
                floor_P=(0.0 if not self.lock_positive.get() else 0.0)
            )
            data_cols.extend([P, R])
            base = f"P0_{str(P0).replace('.','_')}_R0_{str(R0).replace('.','_')}"
            headers.extend([f"P_t_{base}", f"R_t_{base}"])

        arr = np.column_stack(data_cols)
        with open(path, "w", encoding="utf-8") as f:
            f.write(",".join(headers) + "\n")
            for row in arr:
                f.write(",".join(f"{v:.10g}" for v in row) + "\n")
        self.status.config(text=f"Exported CSV → {path}")


if __name__ == "__main__":
    app = CoupledPRApp()
    app.mainloop()
