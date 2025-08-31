import io
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


# --- Core math: logistic ODE closed-form ---
def logistic_solution(t, r, K, P0):
    """
    dP/dt = r P (1 - P/K)
    Closed-form: P(t) = K / (1 + A e^{-rt}), A = (K - P0)/P0 (for P0>0)
    Handles: P0=0 -> 0 identically; r=0 -> constant P0.
    """
    t = np.asarray(t, dtype=np.float64)
    if r == 0.0:
        return np.full_like(t, float(P0))
    if P0 == 0.0:
        return np.zeros_like(t)
    A = (K - P0) / P0
    return K / (1.0 + A * np.exp(-r * t))


def dP_dt(P, r, K):
    return r * P * (1.0 - P / K)


class LogisticODEApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Logistic ODE — P(t) for multiple initial conditions (Tk)")
        self.geometry("1300x900")
        self.minsize(1100, 720)

        # --- Tk variables ---
        self.dark_mode = tk.BooleanVar(value=True)
        self.show_axes = tk.BooleanVar(value=False)
        self.show_grid = tk.BooleanVar(value=False)
        self.show_K_line = tk.BooleanVar(value=True)
        self.show_levels = tk.BooleanVar(value=False)  # 50%K & 90%K
        self.show_slope_field = tk.BooleanVar(value=False)

        self.r = tk.DoubleVar(value=0.6)
        self.K = tk.DoubleVar(value=100.0)
        self.T = tk.DoubleVar(value=50.0)
        self.steps = tk.IntVar(value=600)

        self.linewidth = tk.DoubleVar(value=1.8)
        self.marker_size = tk.DoubleVar(value=0.0)  # 0 = off

        self.slope_t_samples = tk.IntVar(value=24)
        self.slope_p_samples = tk.IntVar(value=18)

        # P0 list (store as floats)
        self.P0s = [10.0, 50.0, 150.0]  # defaults; can be anything
        self.p0_new_value = tk.DoubleVar(value=20.0)

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

        # --- Tabs & figure(s) ---
        self.tabs = ttk.Notebook(self.main)
        self.tabs.grid(row=0, column=0, sticky="nsew")

        tab_sol = ttk.Frame(self.tabs); tab_sol.columnconfigure(0, weight=1); tab_sol.rowconfigure(0, weight=1)
        tab_phase = ttk.Frame(self.tabs); tab_phase.columnconfigure(0, weight=1); tab_phase.rowconfigure(0, weight=1)
        self.tabs.add(tab_sol, text="Solution P(t)")
        self.tabs.add(tab_phase, text="Phase (dP/dt vs P)")

        # Solution figure
        self.fig_sol = Figure(figsize=(8, 6), dpi=100)
        self.ax_sol = self.fig_sol.add_subplot(111)
        self.canvas_sol = FigureCanvasTkAgg(self.fig_sol, master=tab_sol)
        self.canvas_sol.get_tk_widget().grid(row=0, column=0, sticky="nsew")

        # Phase figure
        self.fig_phase = Figure(figsize=(8, 6), dpi=100)
        self.ax_phase = self.fig_phase.add_subplot(111)
        self.canvas_phase = FigureCanvasTkAgg(self.fig_phase, master=tab_phase)
        self.canvas_phase.get_tk_widget().grid(row=0, column=0, sticky="nsew")

        # status
        self.status = ttk.Label(self.main, text="Ready.", anchor="w")
        self.status.grid(row=1, column=0, sticky="ew", pady=(8, 0))

        # Build sidebar last (so callbacks can draw)
        self._build_sidebar()

        # First render
        self._apply_dark_mode()
        self._draw_all()

    # --- Sidebar ---
    def _build_sidebar(self):
        sb = self.sidebar
        for c in (0, 1):
            sb.columnconfigure(c, weight=1 if c == 1 else 0)

        # Parameters
        pf = ttk.LabelFrame(sb, text="Model Parameters", padding=10)
        pf.grid(row=0, column=0, columnspan=2, sticky="new", pady=(0, 10))
        for c in (0, 1): pf.columnconfigure(c, weight=1 if c == 1 else 0)

        def row(r, text, widget):
            ttk.Label(pf, text=text).grid(row=r, column=0, sticky="w", padx=(0, 6), pady=2)
            widget.grid(row=r, column=1, sticky="ew", pady=2)

        row(0, "Growth rate r", ttk.Spinbox(pf, from_=0.0, to=10.0, increment=0.01, textvariable=self.r,
                                            command=self._draw_all))
        row(1, "Carrying cap. K", ttk.Spinbox(pf, from_=0.001, to=1e6, increment=1.0, textvariable=self.K,
                                              command=self._draw_all))
        row(2, "Time horizon T", ttk.Spinbox(pf, from_=1.0, to=1e6, increment=1.0, textvariable=self.T,
                                             command=self._draw_all))
        row(3, "Steps (N)", ttk.Spinbox(pf, from_=50, to=200000, increment=50, textvariable=self.steps,
                                        command=self._draw_all))

        # Initial conditions list
        icf = ttk.LabelFrame(sb, text="Initial Conditions (P₀)", padding=10)
        icf.grid(row=1, column=0, columnspan=2, sticky="new", pady=(0, 10))
        for c in (0, 1): icf.columnconfigure(c, weight=1 if c == 1 else 0)

        self.p0_listbox = tk.Listbox(icf, height=7, exportselection=False)
        self.p0_listbox.grid(row=0, column=0, columnspan=2, sticky="nsew", pady=(0, 6))
        self._refresh_p0_listbox()

        ttk.Label(icf, text="Add P₀").grid(row=1, column=0, sticky="w", padx=(0, 6))
        ttk.Spinbox(icf, from_=0.0, to=1e9, increment=1.0, textvariable=self.p0_new_value)\
            .grid(row=1, column=1, sticky="ew")

        btns = ttk.Frame(icf); btns.grid(row=2, column=0, columnspan=2, sticky="ew", pady=(6, 0))
        btns.columnconfigure(0, weight=1); btns.columnconfigure(1, weight=1); btns.columnconfigure(2, weight=1)

        ttk.Button(btns, text="Add", command=self._add_p0).grid(row=0, column=0, sticky="ew")
        ttk.Button(btns, text="Remove selected", command=self._remove_selected_p0).grid(row=0, column=1, sticky="ew", padx=6)
        ttk.Button(btns, text="Clear", command=self._clear_p0s).grid(row=0, column=2, sticky="ew")

        # Quick presets relative to K
        presets = ttk.Frame(icf); presets.grid(row=3, column=0, columnspan=2, sticky="ew", pady=(8, 0))
        presets.columnconfigure((0,1,2,3), weight=1)
        ttk.Button(presets, text="Add 10%K", command=lambda: self._add_pct_of_K(0.10)).grid(row=0, column=0, sticky="ew")
        ttk.Button(presets, text="Add 50%K", command=lambda: self._add_pct_of_K(0.50)).grid(row=0, column=1, sticky="ew", padx=6)
        ttk.Button(presets, text="Add 100%K", command=lambda: self._add_pct_of_K(1.00)).grid(row=0, column=2, sticky="ew")
        ttk.Button(presets, text="Add 150%K", command=lambda: self._add_pct_of_K(1.50)).grid(row=0, column=3, sticky="ew", padx=6)

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
        ttk.Checkbutton(sf, text="Show K line", variable=self.show_K_line, command=self._draw_all)\
            .grid(row=3, column=1, sticky="w")
        ttk.Checkbutton(sf, text="Show 50%K & 90%K", variable=self.show_levels, command=self._draw_all)\
            .grid(row=4, column=1, sticky="w")
        ttk.Checkbutton(sf, text="Show slope field (on P(t) tab)", variable=self.show_slope_field, command=self._draw_all)\
            .grid(row=5, column=1, sticky="w")

        ttk.Label(sf, text="Line width").grid(row=6, column=0, sticky="w", padx=(0,6))
        ttk.Scale(sf, from_=0.5, to=4.0, variable=self.linewidth, orient="horizontal",
                  command=lambda *_: self._draw_solution()).grid(row=6, column=1, sticky="ew")
        ttk.Label(sf, text="Marker size").grid(row=7, column=0, sticky="w", padx=(0,6))
        ttk.Scale(sf, from_=0.0, to=8.0, variable=self.marker_size, orient="horizontal",
                  command=lambda *_: self._draw_solution()).grid(row=7, column=1, sticky="ew")

        # Slope field resolution
        slf = ttk.LabelFrame(sb, text="Slope Field Resolution", padding=10)
        slf.grid(row=3, column=0, columnspan=2, sticky="new", pady=(0, 10))
        ttk.Label(slf, text="t samples").grid(row=0, column=0, sticky="w", padx=(0,6))
        ttk.Spinbox(slf, from_=8, to=200, increment=1, textvariable=self.slope_t_samples,
                    command=self._draw_solution).grid(row=0, column=1, sticky="ew")
        ttk.Label(slf, text="P samples").grid(row=1, column=0, sticky="w", padx=(0,6))
        ttk.Spinbox(slf, from_=6, to=200, increment=1, textvariable=self.slope_p_samples,
                    command=self._draw_solution).grid(row=1, column=1, sticky="ew")

        # Actions
        ttk.Button(sb, text="Plot", command=self._draw_all).grid(row=4, column=1, sticky="ew")
        ttk.Button(sb, text="Save PNG (Solution)", command=self._save_png_solution).grid(row=5, column=1, sticky="ew", pady=(6,0))
        ttk.Button(sb, text="Save PNG (Phase)", command=self._save_png_phase).grid(row=6, column=1, sticky="ew", pady=(6,0))
        ttk.Button(sb, text="Export CSV (Solution)", command=self._export_csv).grid(row=7, column=1, sticky="ew", pady=(6,0))

        ttk.Label(sb, text="Tip: use presets to quickly compare different P₀ vs K.").grid(row=8, column=0, columnspan=2, sticky="ew", pady=(8,0))

    def _refresh_p0_listbox(self):
        self.p0_listbox.delete(0, tk.END)
        for p in self.P0s:
            self.p0_listbox.insert(tk.END, f"{p:g}")

    def _add_p0(self):
        try:
            p = float(self.p0_new_value.get())
            if p < 0:
                raise ValueError
        except Exception:
            messagebox.showerror("Invalid P₀", "P₀ must be a non-negative number.")
            return
        self.P0s.append(p)
        self._refresh_p0_listbox()
        self._draw_all()

    def _add_pct_of_K(self, frac):
        K = float(self.K.get())
        self.P0s.append(frac * K)
        self._refresh_p0_listbox()
        self._draw_all()

    def _remove_selected_p0(self):
        sel = list(self.p0_listbox.curselection())
        if not sel:
            return
        # remove from end to maintain indices
        for i in reversed(sel):
            del self.P0s[i]
        self._refresh_p0_listbox()
        self._draw_all()

    def _clear_p0s(self):
        self.P0s.clear()
        self._refresh_p0_listbox()
        self._draw_all()

    # --- Drawing & theming ---
    def _apply_dark_mode(self):
        dark = self.dark_mode.get()
        bg = "#0e1117" if dark else "#ffffff"
        fg = "#e5e7eb" if dark else "#111827"

        for ax, fig in [(self.ax_sol, self.fig_sol), (self.ax_phase, self.fig_phase)]:
            ax.set_facecolor(bg); fig.patch.set_facecolor(bg)
            for s in ax.spines.values(): s.set_color(fg)
            ax.tick_params(colors=fg)
            ax.yaxis.label.set_color(fg); ax.xaxis.label.set_color(fg); ax.title.set_color(fg)
            leg = ax.get_legend()
            if leg is not None:
                leg.get_frame().set_facecolor(bg)
                for txt in leg.get_texts(): txt.set_color(fg)

        # Force redraw
        self.canvas_sol.draw()
        self.canvas_phase.draw()

    def _toggle_axes_grid(self, ax):
        if self.show_axes.get():
            for s in ax.spines.values(): s.set_visible(True)
        else:
            for s in ax.spines.values(): s.set_visible(False)
        ax.grid(self.show_grid.get(), linewidth=0.5, alpha=0.3)

    def _draw_all(self):
        self._draw_solution()
        self._draw_phase()

    def _draw_solution(self):
        # Read parameters
        try:
            r = float(self.r.get()); K = float(self.K.get())
            T = float(self.T.get()); N = int(self.steps.get())
            assert K > 0 and T > 0 and N >= 2
        except Exception:
            messagebox.showerror("Invalid parameters",
                                 "Ensure K>0, T>0, steps≥2 (and r≥0).")
            return

        # Build time axis
        t = np.linspace(0.0, T, N, dtype=np.float64)

        # Clear & basic styling
        self.ax_sol.clear()
        self.ax_sol.set_title("Logistic ODE Solution: P(t)")
        self.ax_sol.set_xlabel("t")
        self.ax_sol.set_ylabel("P(t)")
        self._toggle_axes_grid(self.ax_sol)

        # Plot each P0
        lw = float(self.linewidth.get())
        ms = float(self.marker_size.get())
        line_kwargs = dict(linewidth=lw)
        if ms > 0.0:
            line_kwargs["marker"] = "o"
            line_kwargs["markersize"] = ms
            line_kwargs["markevery"] = max(1, len(t)//40)

        if len(self.P0s) == 0:
            self.status.config(text="No P₀ values. Add initial conditions to plot.")
        else:
            for P0 in self.P0s:
                y = logistic_solution(t, r, K, P0)
                label = f"P₀={P0:g}"
                self.ax_sol.plot(t, y, label=label, **line_kwargs)

        # Reference levels
        if self.show_K_line.get():
            self.ax_sol.axhline(K, linestyle="--", linewidth=1.0, alpha=0.9, color="tab:red")
            self.ax_sol.text(self.ax_sol.get_xlim()[0], K, "  K", va="center", color="tab:red")

        if self.show_levels.get():
            for frac, name in [(0.5, "0.5K"), (0.9, "0.9K")]:
                y = frac * K
                self.ax_sol.axhline(y, linestyle=":", linewidth=1.0, alpha=0.9, color="tab:green")
                self.ax_sol.text(self.ax_sol.get_xlim()[0], y, f"  {name}", va="center", color="tab:green")

        # Slope field overlay (direction field in t–P plane)
        if self.show_slope_field.get():
            ts = int(self.slope_t_samples.get())
            ps = int(self.slope_p_samples.get())
            ts = max(4, ts); ps = max(4, ps)
            tt = np.linspace(0.0, T, ts)
            PP = np.linspace(0.0, max(K * 1.6, max(self.P0s or [K])), ps)
            TT, YY = np.meshgrid(tt, PP)
            S = dP_dt(YY, r, K)
            # normalize to unit length in plot coordinates
            max_s = max(1e-9, np.max(np.abs(S)))
            U = np.ones_like(S)  # dt direction
            V = S / max_s        # scaled dP/dt
            self.ax_sol.quiver(TT, YY, U, V, angles="xy", scale_units="xy", scale=20.0,
                               width=0.002, alpha=0.35)

        # Legend & theming
        if len(self.P0s) > 0:
            leg = self.ax_sol.legend(loc="best", frameon=True)
            if self.dark_mode.get():
                leg.get_frame().set_edgecolor("#e5e7eb")

        self._apply_dark_mode()
        self.canvas_sol.draw()
        if len(self.P0s) > 0:
            self.status.config(text=f"Plotted {len(self.P0s)} initial condition(s).")

    def _draw_phase(self):
        # Phase: dP/dt vs P, with fixed points marked
        try:
            r = float(self.r.get()); K = float(self.K.get())
            assert K > 0
        except Exception:
            return

        self.ax_phase.clear()
        self.ax_phase.set_title("Phase Plot: dP/dt vs P")
        self.ax_phase.set_xlabel("P")
        self.ax_phase.set_ylabel("dP/dt")
        self._toggle_axes_grid(self.ax_phase)

        P = np.linspace(0.0, max(K*1.6, max(self.P0s or [K])), 800)
        F = dP_dt(P, r, K)
        self.ax_phase.plot(P, F, linewidth=1.8)

        # Fixed points 0 and K
        self.ax_phase.axhline(0.0, linewidth=1.0, linestyle="--", alpha=0.8)
        self.ax_phase.axvline(0.0, linewidth=0.8, linestyle=":", alpha=0.6)
        self.ax_phase.scatter([0.0, K], [0.0, 0.0], s=40, zorder=3)

        # Stability arrows on 1D line (heuristic: sign of dP/dt)
        # Draw small arrows along P-axis
        for p in np.linspace(0.0, max(K*1.6, max(self.P0s or [K])), 16):
            slope = dP_dt(p, r, K)
            dx = 0.04 * max(1.0, K) * (1 if slope > 0 else -1)
            self.ax_phase.annotate("", xy=(p + dx, 0), xytext=(p, 0),
                                   arrowprops=dict(arrowstyle="->", lw=1.0, alpha=0.6))

        self._apply_dark_mode()
        self.canvas_phase.draw()

    # --- Export / Save ---
    def _save_png_solution(self):
        path = filedialog.asksaveasfilename(defaultextension=".png",
                                            filetypes=[("PNG image", "*.png")])
        if not path:
            return
        buf = io.BytesIO(); self.fig_sol.savefig(buf, format="png", dpi=200, bbox_inches="tight")
        with open(path, "wb") as f:
            f.write(buf.getvalue())
        self.status.config(text=f"Saved Solution PNG → {path}")

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
        if not self.P0s:
            messagebox.showinfo("Nothing to export", "Add at least one P₀.")
            return

        try:
            r = float(self.r.get()); K = float(self.K.get())
            T = float(self.T.get()); N = int(self.steps.get())
            assert K > 0 and T > 0 and N >= 2
        except Exception:
            messagebox.showerror("Invalid parameters",
                                 "Ensure K>0, T>0, steps≥2.")
            return

        path = filedialog.asksaveasfilename(defaultextension=".csv",
                                            filetypes=[("CSV file", "*.csv")])
        if not path:
            return

        t = np.linspace(0.0, T, N, dtype=np.float64)
        data_cols = [t]
        headers = ["t"]
        for P0 in self.P0s:
            y = logistic_solution(t, r, K, P0)
            data_cols.append(y)
            headers.append(f"P_t_P0_{str(P0).replace('.', '_')}")

        # write CSV
        arr = np.column_stack(data_cols)
        with open(path, "w", encoding="utf-8") as f:
            f.write(",".join(headers) + "\n")
            for row in arr:
                f.write(",".join(f"{v:.10g}" for v in row) + "\n")
        self.status.config(text=f"Exported CSV → {path}")


if __name__ == "__main__":
    app = LogisticODEApp()
    app.mainloop()
