# Exercises — Example 6: Energy transfer in photosynthesis (FMO)

The FMO complex is a pigment-protein complex in photosynthetic bacteria that funnels absorbed light energy toward the reaction center. Here it's modeled as 3 sites (molecules), each with its own vibrational environment, and we watch the excitation hop from site 1 to the lowest-energy site 3 — a real biological energy-transport problem solved with the same machinery as the previous toy models.

⚠️ The script defines six configurations; the "structured" ones are **very** expensive. **Only run the two `"drude"` entries** (comment the other four out of `configs`) and set `end_time = 500`. Each Drude run then takes several minutes. Estimated time: ~30 min.

## 6.1 — Follow the energy

Run the two Drude configurations (300 K and 77 K) and plot the three site populations (`example6_plot.py`, or a quick matplotlib script of your own — the output columns are the 3×3 density matrix, with populations at columns 1, 5, 9).

- The excitation starts on site 1. Where does it end up, and roughly how fast?
- Compare 300 K vs 77 K: at which temperature do you see clearer oscillations (quantum coherence between sites) at early times, and at which is the final population more concentrated on the lowest site? Both observations have the same thermal explanation — what is it?

## 6.2 — Change the starting point

In real photosynthesis, where the excitation enters depends on the antenna geometry. Change `psi0` so the excitation starts on site 2 (`psi0[1] = 1.0` instead of `psi0[0]`), and rerun one Drude configuration.

- Is the transfer to site 3 faster or slower than from site 1? Look at the Hamiltonian `H`: site 2 has the highest energy and is coupled to both other sites.

## 6.3 — Does the environment's structure matter? (optional, long)

If you have time (this run is noticeably heavier), run one `"three_peak"` configuration at 300 K — an environment with actual vibrational peaks instead of the smooth Drude model — and compare the site-3 population against the Drude run.

- The two bath models have similar overall coupling strength but different frequency content. Does that change the transfer? This is why "how you model the environment" is a headline question in this field.
