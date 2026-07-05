# Exercises — Example 1: A minimal open-system simulation

**The setup in one sentence:** a quantum two-level system (think: two energy levels of a molecule) is in contact with an *environment* (a "bath" — the surrounding vibrations/solvent), and we watch how the environment drags the system toward thermal equilibrium.

The whole simulation runs in under a minute, so experiment freely. Estimated time: ~20 min.

## 1.1 — Run it

Run `example1.py`, then `example1_plot.py`.

- The system starts with all population in the upper state. What happens, and roughly how long does it take to settle?
- The final populations are *not* 50/50. The energy gap between the two states (~1600 cm⁻¹) is much bigger than the thermal energy at 300 K (~208 cm⁻¹) — how does that explain what you see?

## 1.2 — Temperature

Change `temperature` in `gen_bcf` from 300 to 600 and rerun (rename the old `simple.dat.log` first so you can compare).

- How do the final populations change? Is it the direction you expected from Boltzmann statistics?

## 1.3 — Coupling strength (optional)

The parameter `re_d=[540]` sets how strongly the environment couples to the system. Try `[54]` (10× weaker) and rerun.

- With a weak environment the populations *oscillate* before settling — the system behaves almost like an isolated quantum system. Why does a strong environment kill the oscillations?
