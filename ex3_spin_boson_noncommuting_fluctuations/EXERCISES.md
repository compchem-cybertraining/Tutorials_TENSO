# Exercises — Example 3: Two competing environments

Here the two-level system is coupled to **two independent environments** through two different operators — one shakes the energy *levels* (diagonal coupling), the other shakes the *coupling between* the levels (off-diagonal). The two "noises" are incompatible (the operators don't commute), a situation many approximate methods can't handle but TENSO can.

⚠️ As written the script runs 10,000 time steps — long. **Set `end_time = 200` before starting**; that's enough for everything below. Estimated time: ~25 min.

## 3.1 — Run it

Run `example3.py` (with the shortened `end_time`).

- Describe the population dynamics. The system starts in the *upper* state.
- In the `system_multibath` call, `sys_ops` has two entries and `bath_correlations` has two entries — each pair defines one independent environment. Find them in the code.

## 3.2 — One environment at a time

Make two modified runs (change `out` each time so the outputs don't overwrite):

- (a) keep only the first coupling: `sys_ops=[bath_op1]`, `bath_correlations=[bath_simulation]`
- (b) keep only the second: `sys_ops=[bath_op2]`, `bath_correlations=[bath_simulation]`

Compare all three cases. `bath_op2` directly connects the two levels while `bath_op1` does not — which environment is better at moving population between the states?

## 3.3 — Time step (optional)

Rerun the two-bath case with `dt = 1.0` instead of `0.1`.

- Does the result change? The system oscillates with a period of about 20 fs — a good rule of thumb anywhere in numerics: your time step must resolve the fastest motion in the problem.
