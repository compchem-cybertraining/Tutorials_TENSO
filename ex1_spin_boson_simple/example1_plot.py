import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

file_sb = Path("simple.dat.log")
time_units = "fs"
pop_labels = [r"$\rho_{00}$", r"$\rho_{11}$"]

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif", "font.serif": ["Times"], "font.size": 9,
    "axes.labelsize": 9, "axes.titlesize": 9, "axes.linewidth": 0.8,
    "lines.linewidth": 1.2, "lines.markersize": 4,
    "xtick.direction": "in", "ytick.direction": "in",
    "xtick.top": True, "ytick.right": True,
    "figure.dpi": 300,
})

def load_spinboson_pops(fname, convert_to_ps=False):
    arr = np.genfromtxt(fname, dtype=complex, comments="#", skip_header=1)
    t = arr[:,0].real
    if convert_to_ps:
        t *= 1e-3
    pops = np.vstack((arr[:,1].real, arr[:,4].real)).T
    return t, pops

# load data
convert = (time_units.lower() == "ps")
t_sb, p_sb = load_spinboson_pops(file_sb, convert_to_ps=convert)

# make figure
fig, ax1 = plt.subplots(figsize=(3.4, 2.0))

ax1.plot(t_sb, p_sb[:,0], label=pop_labels[0])
ax1.plot(t_sb, p_sb[:,1], label=pop_labels[1])

ax1.set_ylabel("Population", labelpad=6)
ax1.set_xlabel("Time (fs)", labelpad=3)
ax1.set_xlim(0, 1000)
ax1.legend(loc="best", fontsize=8, frameon=False)

fig.tight_layout()
plt.savefig("SpinBoson_simple.png", bbox_inches='tight', dpi=300, transparent=True)
plt.show()
