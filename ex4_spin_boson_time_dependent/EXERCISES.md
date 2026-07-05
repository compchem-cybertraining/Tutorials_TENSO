# Exercises — Example 4: Driving the system with a laser pulse

This example adds a time-dependent field: a short laser pulse designed to flip the system from its ground state to its excited state (a "π pulse" — for an ideal isolated system it would work perfectly). The environment is watching, though, and degrades the flip. This is the basic physics behind quantum control and qubit gate errors.

The run takes a few minutes. Estimated time: ~25 min.

## 4.1 — How good is the flip?

Run `example4.py` and `example4_plot.py`.

- The system starts in the ground state, the pulse hits at t ≈ 6 fs. What fraction of the population ends up in the excited state?
- For an isolated system the answer would be 1. The missing part is the error caused by the environment acting *during* the operation — the same reason real quantum-computer gates aren't perfect.

## 4.2 — Half and full rotations

The variable `target_area` sets the pulse strength. Textbook result for an ideal two-level system: final excited-state population = sin²(area/2), so `np.pi` → 1, `np.pi/2` → 0.5, `2*np.pi` → 0.

- Run with `target_area = np.pi/2` and `2*np.pi`. Predict the outcomes first, then compare. Which case shows the environment's effect most clearly? (Hint: for the 2π pulse, the ideal answer is exactly zero — anything you see is pure error.)

## 4.3 — A noisier environment (optional)

Double the system-environment coupling: `re_d = [1080]`. Rerun the π pulse.

- How much worse does the flip get? If you were designing a control pulse for a real device, would you rather make the pulse shorter or the environment weaker?
