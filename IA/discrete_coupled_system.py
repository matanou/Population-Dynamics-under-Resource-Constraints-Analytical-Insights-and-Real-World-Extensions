import io
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


# =========================
# Core math / integration
# =========================
def f_rhs(t, y, r, c, k):
    """Continuous dynamics between deliveries (no inflow):
       y = [P, R]
       dP/dt = r P (1 - cP/R)
       dR/dt = -k P
    """
    P, R = y
    R_safe = max(R, 1e-12)
    dP = r * P * (1.0 - (c * P) / R_safe)
    dR = -k * P
    return np.array([dP, dR], dtype=np.float64)


def rk4_step(t, y, h, r, c, k):
    k1 = f_rhs(t, y, r, c, k)
    k2 = f_rhs(t + 0.5*h, y + 0.5*h*k1, r, c, k)
    k3 = f_rhs(t + 0.5*h, y + 0.5*h*k2, r, c, k)
    k4 = f_rhs(t + h, y + h*k3, r, c, k)
    return y + (h/6.0)*(k1 + 2*k2 + 2*k3 + k4)


def integrate_interval(t0, y0, dt, M, r, c, k, clamp_nonneg=True):
    """Integrate over a single continuous interval of length dt (no impulses inside)."""
    M = max(2, int(M))
    t = np.linspace(t0, t0 + dt, M, dtype=np.float64)
    Y = np.zeros((M, 2), dtype=np.float64)
    Y[0] = y0
    h = dt / (M - 1)
    for i in range(1, M):
        Y[i] = rk4_step(t[i-1], Y[i-1], h, r, c, k)
        if clamp_nonneg:
            Y[i, 0] = max(0.0, Y[i, 0])
            Y[i, 1] = max(0.0, Y[i, 1])
    return t, Y[:, 0], Y[:, 1]


def simulate_impulsive(T, tau, steps_per_interval, y0, r, c, k, Q,
                       clamp_nonneg=True, include_final_partial=True):
    """
    Simulate up to time T with impulses every tau:
      After each full interval tau: R += Q (P unchanged).
    Returns:
      timeline (t_all, P_all, R_all) with np.nan gaps to render jumps cleanly,
      delivery arrays (n_list, P_plus_list, R_plus_list) for stroboscopic samples.
    """
    if tau <= 0:
        raise ValueError("tau must be > 0")

    t_all, P_all, R_all = [], [], []
    n_list, P_plus_list, R_plus_list = [], [], []

    t = 0.0
    y = np.array(y0, dtype=np.float64)
    # record initial post-impulse state as "n=0" (t=0 is after an implicit delivery? keep it transparent)
    # We'll NOT count t=0 as a delivery unless Q_at_t0 flag existed; keep stroboscopic from first jump.

    N_full = int(np.floor(T / tau))
    for n in range(N_full):
        # integrate for one full interval [t, t+tau]
        tt, PP, RR = integrate_interval(t, y, tau, steps_per_interval, r, c, k, clamp_nonneg)
        # append continuous segment
        t_all.extend(tt.tolist()); P_all.extend(PP.tolist()); R_all.extend(RR.tolist())

        # draw a jump at the end: add vertical separator by inserting NaN then two points
        t_end = tt[-1]
        P_end = PP[-1]
        R_before = RR[-1]
        R_after = R_before + Q
        if clamp_nonneg:
            R_after = max(0.0, R_after)

        # Insert a tiny vertical segment for the jump
        t_all.extend([np.nan, t_end, t_end])
        P_all.extend([np.nan, P_end, P_end])
        R_all.extend([np.nan, R_before, R_after])

        # Update state after impulse
        y = np.array([P_end, R_after], dtype=np.float64)
        t = t_end

        # stroboscopic (post-impulse)
        n_list.append(n + 1)
        P_plus_list.append(y[0])
        R_plus_list.append(y[1])

        # If we've reached or exceeded T exactly at a delivery boundary, break
        if abs(t - T) < 1e-12:
            break

    # final partial interval (no impulse at the end)
    if include_final_partial and t < T:
        tt, PP, RR = integrate_interval(t, y, T - t, steps_per_interval, r, c, k, clamp_nonneg)
        t_all.extend(tt.tolist()); P_all.extend(PP.tolist()); R_all.extend(RR.tolist())

    # to numpy
    return (np.array(t_all), np.array(P_all), np.array(R_all),
            np.array(n_list, dtype=int), np.array(P_plus_list), np.array(R_plus_list))


# =========================
# Tkinter App
# =========================
class ImpulsivePRApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Impulsive Population–Resource Dynamics (Discrete Replenishment)")
        self.geometry("1480x980")
        self.minsize(1200, 800)

        # ----- Tk variables -----
        self.dark_mode = tk.BooleanVar(value=True)
        self.show_axes = tk.BooleanVar(value=False)
        self.show_grid = tk.BooleanVar(value=False)

        self.show_vector_field = tk.BooleanVar(value=True)
        self.lock_nonneg = tk.BooleanVar(value=True)
        self.show_delivery_lines = tk.BooleanVar(value=True)
        self.show_Q_over_tau = tk.BooleanVar(value=True)

        # model params
        self.r = tk.DoubleVar(value=0.6)
        self.c = tk.DoubleVar(value=0.8)
        self.k = tk.DoubleVar(value=0.2)

        self.Q = tk.DoubleVar(value=25.0)
        self.tau = tk.DoubleVar(value=3.0)

        self.T = tk.DoubleVar(value=60.0)
        self.steps_per_interval = tk.IntVar(value=160)  # temporal resolution inside each interval

        self.linewidth = tk.DoubleVar(value=1.8)
        self.marker_size = tk.DoubleVar(value=0.0)

        # Vector field density (phase plane)
        self.p_samples = tk.IntVar(value=20)
        self.r_samples = tk.IntVar(value=20)

        # initial conditions: list of (P0, R0)
        self.ICs = [(20.0, 40.0), (40.0, 70.0), (80.0, 100.0)]
        self.ic_p = tk.DoubleVar(value=30.0)
        self.ic_r = tk.DoubleVar(value=60.0)

        # ----- Layout -----
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        self.sidebar = ttk.Frame(self, padding=10)
        self.sidebar.grid(row=0, column=0, sticky="nsw")
        self.main = ttk.Frame(self, padding=(10, 10, 10, 10))
        self.main.grid(row=0, column=1, sticky="nsew")
        self.main.columnconfigure(0, weight=1); self.main.rowconfigure(0, weight=1)

        # Tabs
        self.tabs = ttk.Notebook(self.main)
        self.tabs.grid(row=0, column=0, sticky="nsew")

        tab_time = ttk.Frame(self.tabs); tab_time.columnconfigure(0, weight=1); tab_time.rowconfigure(0, weight=1)
        tab_phase = ttk.Frame(self.tabs); tab_phase.columnconfigure(0, weight=1); tab_phase.rowconfigure(0, weight=1)
        tab_samples = ttk.Frame(self.tabs); tab_samples.columnconfigure(0, weight=1); tab_samples.rowconfigure(0, weight=1)
        self.tabs.add(tab_time, text="Time Series: P(t) & R(t)")
        self.tabs.add(tab_phase, text="Phase Plane (between deliveries)")
        self.tabs.add(tab_samples, text="Delivery Samples (P⁺ₙ, R⁺ₙ)")

        # Figures
        self.fig_time = Figure(figsize=(8.4, 6.2), dpi=100); self.ax_time = self.fig_time.add_subplot(111)
        self.canvas_time = FigureCanvasTkAgg(self.fig_time, master=tab_time)
        self.canvas_time.get_tk_widget().grid(row=0, column=0, sticky="nsew")

        self.fig_phase = Figure(figsize=(8.4, 6.2), dpi=100); self.ax_phase = self.fig_phase.add_subplot(111)
        self.canvas_phase = FigureCanvasTkAgg(self.fig_phase, master=tab_phase)
        self.canvas_phase.get_tk_widget().grid(row=0, column=0, sticky="nsew")

        self.fig_samples = Figure(figsize=(8.4, 6.2), dpi=100); self.ax_samples = self.fig_samples.add_subplot(111)
        self.canvas_samples = FigureCanvasTkAgg(self.fig_samples, master=tab_samples)
        self.canvas_samples.get_tk_widget().grid(row=0, column=0, sticky="nsew")

        # status
        self.status = ttk.Label(self.main, text="Ready.", anchor="w")
        self.status.grid(row=1, column=0, sticky="ew", pady=(8, 0))

        # Build UI and draw
        self._build_sidebar()
        self._apply_dark_mode()
        self._draw_all()

    # ----- Sidebar -----
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

        row(0, "Growth rate r", ttk.Spinbox(pf, from_=0.0, to=10.0, increment=0.01, textvariable=self.r, command=self._draw_all))
        row(1, "Consumption coeff. c", ttk.Spinbox(pf, from_=0.0, to=100.0, increment=0.01, textvariable=self.c, command=self._draw_all))
        row(2, "Per-capita usage k", ttk.Spinbox(pf, from_=0.0001, to=1e6, increment=0.01, textvariable=self.k, command=self._draw_all))
        row(3, "Batch size Q", ttk.Spinbox(pf, from_=0.0, to=1e9, increment=0.1, textvariable=self.Q, command=self._draw_all))
        row(4, "Delivery interval τ", ttk.Spinbox(pf, from_=0.1, to=1e6, increment=0.1, textvariable=self.tau, command=self._draw_all))
        row(5, "Time horizon T", ttk.Spinbox(pf, from_=1.0, to=1e6, increment=1.0, textvariable=self.T, command=self._draw_all))
        row(6, "Steps per interval", ttk.Spinbox(pf, from_=10, to=5000, increment=10, textvariable=self.steps_per_interval, command=self._draw_all))

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

        # Style / toggles
        sf = ttk.LabelFrame(sb, text="Style & Options", padding=10)
        sf.grid(row=2, column=0, columnspan=2, sticky="new", pady=(0, 10))
        for c in (0, 1): sf.columnconfigure(c, weight=1 if c == 1 else 0)

        ttk.Checkbutton(sf, text="Dark mode", variable=self.dark_mode, command=self._apply_dark_mode).grid(row=0, column=1, sticky="w")
        ttk.Checkbutton(sf, text="Show axes", variable=self.show_axes, command=self._draw_all).grid(row=1, column=1, sticky="w")
        ttk.Checkbutton(sf, text="Show grid", variable=self.show_grid, command=self._draw_all).grid(row=2, column=1, sticky="w")
        ttk.Checkbutton(sf, text="Vector field (phase)", variable=self.show_vector_field, command=self._draw_phase).grid(row=3, column=1, sticky="w")
        ttk.Checkbutton(sf, text="Enforce P,R ≥ 0", variable=self.lock_nonneg, command=self._draw_all).grid(row=4, column=1, sticky="w")
        ttk.Checkbutton(sf, text="Delivery markers", variable=self.show_delivery_lines, command=self._draw_time_series).grid(row=5, column=1, sticky="w")
        ttk.Checkbutton(sf, text="Show Q/τ label", variable=self.show_Q_over_tau, command=self._draw_time_series).grid(row=6, column=1, sticky="w")

        ttk.Label(sf, text="Line width").grid(row=7, column=0, sticky="w", padx=(0,6))
        ttk.Scale(sf, from_=0.5, to=4.0, variable=self.linewidth, orient="horizontal",
                  command=lambda *_: self._redraw_all_figs()).grid(row=7, column=1, sticky="ew")
        ttk.Label(sf, text="Marker size").grid(row=8, column=0, sticky="w", padx=(0,6))
        ttk.Scale(sf, from_=0.0, to=8.0, variable=self.marker_size, orient="horizontal",
                  command=lambda *_: self._redraw_all_figs()).grid(row=8, column=1, sticky="ew")

        # Phase vector field density
        ppf = ttk.LabelFrame(sb, text="Phase Field Density", padding=10)
        ppf.grid(row=3, column=0, columnspan=2, sticky="new", pady=(0,10))
        ttk.Label(ppf, text="P samples").grid(row=0, column=0, sticky="w", padx=(0,6))
        ttk.Spinbox(ppf, from_=6, to=200, increment=1, textvariable=self.p_samples, command=self._draw_phase)\
            .grid(row=0, column=1, sticky="ew")
        ttk.Label(ppf, text="R samples").grid(row=1, column=0, sticky="w", padx=(0,6))
        ttk.Spinbox(ppf, from_=6, to=200, increment=1, textvariable=self.r_samples, command=self._draw_phase)\
            .grid(row=1, column=1, sticky="ew")

        # Actions
        ttk.Button(sb, text="Plot", command=self._draw_all).grid(row=4, column=1, sticky="ew")
        ttk.Button(sb, text="Save PNG (Time Series)", command=self._save_png_time).grid(row=5, column=1, sticky="ew", pady=(6,0))
        ttk.Button(sb, text="Save PNG (Phase)", command=self._save_png_phase).grid(row=6, column=1, sticky="ew", pady=(6,0))
        ttk.Button(sb, text="Save PNG (Samples)", command=self._save_png_samples).grid(row=7, column=1, sticky="ew", pady=(6,0))
        ttk.Button(sb, text="Export CSV (Time+Samples)", command=self._export_csv).grid(row=8, column=1, sticky="ew", pady=(6,0))

        ttk.Label(sb, text="Tip: Effective inflow = Q/τ. Tune both to study schedules.").grid(row=9, column=0, columnspan=2, sticky="ew", pady=(10,0))

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
        if not sel: return
        for i in reversed(sel):
            del self.ICs[i]
        self._refresh_ic_listbox()
        self._draw_all()

    def _clear_ics(self):
        self.ICs.clear()
        self._refresh_ic_listbox()
        self._draw_all()

    # ----- Drawing & theming -----
    def _apply_dark_mode(self):
        dark = self.dark_mode.get()
        bg = "#0e1117" if dark else "#ffffff"
        fg = "#e5e7eb" if dark else "#111827"
        for ax, fig in [(self.ax_time, self.fig_time),
                        (self.ax_phase, self.fig_phase),
                        (self.ax_samples, self.fig_samples)]:
            ax.set_facecolor(bg); fig.patch.set_facecolor(bg)
            for s in ax.spines.values(): s.set_color(fg)
            ax.tick_params(colors=fg)
            ax.yaxis.label.set_color(fg); ax.xaxis.label.set_color(fg); ax.title.set_color(fg)
            leg = ax.get_legend()
            if leg is not None:
                leg.get_frame().set_facecolor(bg)
                for txt in leg.get_texts(): txt.set_color(fg)
        self.canvas_time.draw(); self.canvas_phase.draw(); self.canvas_samples.draw()

    def _toggle_axes_grid(self, ax):
        if self.show_axes.get():
            for s in ax.spines.values(): s.set_visible(True)
        else:
            for s in ax.spines.values(): s.set_visible(False)
        ax.grid(self.show_grid.get(), linewidth=0.5, alpha=0.3)

    def _read_params(self):
        try:
            r = float(self.r.get()); c = float(self.c.get()); k = float(self.k.get())
            Q = float(self.Q.get()); tau = float(self.tau.get())
            T = float(self.T.get()); spi = int(self.steps_per_interval.get())
            assert tau > 0 and T > 0 and spi >= 2
        except Exception:
            messagebox.showerror("Invalid parameters",
                                 "Ensure τ>0, T>0, steps/interval ≥ 2, and numeric r,c,k,Q.")
            return None
        return r, c, k, Q, tau, T, spi

    def _draw_all(self):
        self._draw_time_series()
        self._draw_phase()
        self._draw_samples()

    def _redraw_all_figs(self):
        # simple redraw to reflect style sliders without recomputing sim
        self._draw_time_series(redraw_only=True)
        self._draw_phase(redraw_only=True)
        self._draw_samples(redraw_only=True)

    def _simulate_for_all_ics(self):
        params = self._read_params()
        if params is None: return None
        r, c, k, Q, tau, T, spi = params

        sims = []
        for (P0, R0) in self.ICs:
            t, P, R, n, Pp, Rp = simulate_impulsive(
                T=T, tau=tau, steps_per_interval=spi,
                y0=np.array([P0, R0], dtype=np.float64),
                r=r, c=c, k=k, Q=Q,
                clamp_nonneg=self.lock_nonneg.get())
            sims.append((P0, R0, t, P, R, n, Pp, Rp))
        return (r, c, k, Q, tau, T, spi, sims)

    def _draw_time_series(self, redraw_only=False):
        res = getattr(self, "_cache_sim", None)
        if res is None or not redraw_only:
            res = self._simulate_for_all_ics()
            if res is None: return
            self._cache_sim = res
        r, c, k, Q, tau, T, spi, sims = res

        self.ax_time.clear()
        self.ax_time.set_title("Impulsive Dynamics: P(t) continuous, R(t) with jumps")
        self.ax_time.set_xlabel("t"); self.ax_time.set_ylabel("P(t), R(t)")
        self._toggle_axes_grid(self.ax_time)

        lw = float(self.linewidth.get())
        ms = float(self.marker_size.get())
        line_kwargs = dict(linewidth=lw)
        if ms > 0.0:
            line_kwargs["marker"] = "o"
            line_kwargs["markersize"] = ms
            # do not mark every sample to keep it clean
            line_kwargs["markevery"] = 0.04

        count = 0
        for (P0, R0, t, P, R, n, Pp, Rp) in sims:
            self.ax_time.plot(t, P, label=f"P(t) | P₀={P0:g}, R₀={R0:g}", **line_kwargs)
            # For R(t) with jumps: use same array (contains NaNs for verticals)
            self.ax_time.plot(t, R, linestyle="--", label=f"R(t) | P₀={P0:g}, R₀={R0:g}", **line_kwargs)
            count += 1

        # Delivery markers (vlines at n*tau)
        if self.show_delivery_lines.get():
            tau = float(self.tau.get()); T = float(self.T.get())
            nmax = int(np.floor(T / tau))
            for m in range(1, nmax + 1):
                tm = m * tau
                self.ax_time.axvline(tm, linestyle=":", linewidth=0.9, alpha=0.5)

        # Q/tau label
        if self.show_Q_over_tau.get():
            eff = (float(self.Q.get()) / float(self.tau.get())) if float(self.tau.get()) != 0 else np.nan
            x0, x1 = self.ax_time.get_xlim()
            y0, y1 = self.ax_time.get_ylim()
            self.ax_time.text(x0, y1, f"  Effective inflow Q/τ ≈ {eff:.3g}",
                              va="top", ha="left", fontsize=9, alpha=0.9)

        if count == 0:
            self.status.config(text="No initial conditions. Add (P₀, R₀) to plot.")
        else:
            leg = self.ax_time.legend(loc="best", frameon=True)
            if self.dark_mode.get() and leg:
                leg.get_frame().set_edgecolor("#e5e7eb")
            self.status.config(text=f"Simulated {count} trajectory set(s).")

        self._apply_dark_mode()
        self.canvas_time.draw()

    def _draw_phase(self, redraw_only=False):
        res = getattr(self, "_cache_sim", None)
        if res is None or not redraw_only:
            res = self._simulate_for_all_ics()
            if res is None: return
            self._cache_sim = res
        r, c, k, Q, tau, T, spi, sims = res

        self.ax_phase.clear()
        self.ax_phase.set_title("Phase Plane (Flow between deliveries)")
        self.ax_phase.set_xlabel("P")
        self.ax_phase.set_ylabel("R")
        self._toggle_axes_grid(self.ax_phase)

        # Determine bounds from ICs and trajectories
        Pmax = 1.0; Rmax = 1.0
        for _, _, t, P, R, *_ in sims:
            if len(P) > 0:
                Pmax = max(Pmax, np.nanmax(P))
                Rmax = max(Rmax, np.nanmax(R))
        Pmax *= 1.1; Rmax *= 1.1

        # Vector field for continuous flow (no impulses)
        if self.show_vector_field.get():
            ps = max(6, int(self.p_samples.get()))
            rs = max(6, int(self.r_samples.get()))
            P_vals = np.linspace(0.0, Pmax, ps)
            R_vals = np.linspace(0.0, Rmax, rs)
            PP, RR = np.meshgrid(P_vals, R_vals)
            dP = np.zeros_like(PP); dR = np.zeros_like(RR)
            for i in range(RR.shape[0]):
                for j in range(PP.shape[1]):
                    v = f_rhs(0.0, np.array([PP[i, j], RR[i, j]]), r, c, k)
                    dP[i, j], dR[i, j] = v[0], v[1]
            mag = np.hypot(dP, dR); mag[mag == 0] = 1.0
            U = dP / mag; V = dR / mag
            self.ax_phase.quiver(PP, RR, U, V, angles="xy", scale_units="xy", scale=22.0,
                                 width=0.0022, alpha=0.33)

        # Trajectories (with small arrows along path)
        lw = float(self.linewidth.get())
        for _, _, t, P, R, *_ in sims:
            self.ax_phase.plot(P, R, linewidth=lw)
            if len(P) > 1:
                idxs = np.linspace(0, len(P)-2, 14, dtype=int)
                for i in idxs:
                    self.ax_phase.annotate("", xy=(P[i+1], R[i+1]), xytext=(P[i], R[i]),
                                           arrowprops=dict(arrowstyle="->", lw=max(0.8, lw-0.6), alpha=0.55))

        self.ax_phase.set_xlim(0, max(1.0, Pmax))
        self.ax_phase.set_ylim(0, max(1.0, Rmax))

        self._apply_dark_mode()
        self.canvas_phase.draw()

    def _draw_samples(self, redraw_only=False):
        res = getattr(self, "_cache_sim", None)
        if res is None or not redraw_only:
            res = self._simulate_for_all_ics()
            if res is None: return
            self._cache_sim = res
        r, c, k, Q, tau, T, spi, sims = res

        self.ax_samples.clear()
        self.ax_samples.set_title("Delivery Samples (stroboscopic map): (P⁺ₙ, R⁺ₙ) at t = nτ")
        self.ax_samples.set_xlabel("Delivery index n")
        self.ax_samples.set_ylabel("Value")
        self._toggle_axes_grid(self.ax_samples)

        lw = float(self.linewidth.get())
        for (P0, R0, *_rest) in sims:
            n, Pp, Rp = _rest[3], _rest[4], _rest[5]
            if len(n) == 0:
                continue
            self.ax_samples.plot(n, Pp, marker="o", linestyle="-", linewidth=lw, label=f"P⁺ₙ | P₀={P0:g}, R₀={R0:g}")
            self.ax_samples.plot(n, Rp, marker="s", linestyle="--", linewidth=lw, label=f"R⁺ₙ | P₀={P0:g}, R₀={R0:g}")

        leg = self.ax_samples.legend(loc="best", frameon=True)
        if self.dark_mode.get() and leg:
            leg.get_frame().set_edgecolor("#e5e7eb")

        self._apply_dark_mode()
        self.canvas_samples.draw()

    # ----- Export / Save -----
    def _save_png_time(self):
        path = filedialog.asksaveasfilename(defaultextension=".png",
                                            filetypes=[("PNG image", "*.png")])
        if not path: return
        buf = io.BytesIO(); self.fig_time.savefig(buf, format="png", dpi=220, bbox_inches="tight")
        with open(path, "wb") as f: f.write(buf.getvalue())
        self.status.config(text=f"Saved Time Series PNG → {path}")

    def _save_png_phase(self):
        path = filedialog.asksaveasfilename(defaultextension=".png",
                                            filetypes=[("PNG image", "*.png")])
        if not path: return
        buf = io.BytesIO(); self.fig_phase.savefig(buf, format="png", dpi=220, bbox_inches="tight")
        with open(path, "wb") as f: f.write(buf.getvalue())
        self.status.config(text=f"Saved Phase PNG → {path}")

    def _save_png_samples(self):
        path = filedialog.asksaveasfilename(defaultextension=".png",
                                            filetypes=[("PNG image", "*.png")])
        if not path: return
        buf = io.BytesIO(); self.fig_samples.savefig(buf, format="png", dpi=220, bbox_inches="tight")
        with open(path, "wb") as f: f.write(buf.getvalue())
        self.status.config(text=f"Saved Samples PNG → {path}")

    def _export_csv(self):
        res = getattr(self, "_cache_sim", None)
        if res is None:
            res = self._simulate_for_all_ics()
            if res is None: return
            self._cache_sim = res
        r, c, k, Q, tau, T, spi, sims = res

        path = filedialog.asksaveasfilename(defaultextension=".csv",
                                            filetypes=[("CSV file", "*.csv")])
        if not path: return

        # collect widest timeline length
        # We'll export one table per IC stacked vertically with headers in between for clarity.
        with open(path, "w", encoding="utf-8") as f:
            f.write("# Impulsive model export\n")
            f.write(f"# r={r}, c={c}, k={k}, Q={Q}, tau={tau}, T={T}, steps_per_interval={spi}\n")
            f.write("# Columns: t, P(t), R(t)  |  Delivery rows: n, P_plus, R_plus\n\n")
            for (P0, R0, t, P, R, n, Pp, Rp) in sims:
                f.write(f"IC: P0={P0}, R0={R0}\n")
                f.write("t,P,R\n")
                for i in range(len(t)):
                    ti = t[i]; Pi = P[i]; Ri = R[i]
                    if np.isnan(ti):
                        # separate segments
                        f.write("nan,nan,nan\n")
                    else:
                        f.write(f"{ti:.10g},{Pi:.10g},{Ri:.10g}\n")
                f.write("DELIVERIES: n,P_plus,R_plus\n")
                for i in range(len(n)):
                    f.write(f"{int(n[i])},{Pp[i]:.10g},{Rp[i]:.10g}\n")
                f.write("\n")
        self.status.config(text=f"Exported CSV → {path}")


if __name__ == "__main__":
    app = ImpulsivePRApp()
    app.mainloop()
