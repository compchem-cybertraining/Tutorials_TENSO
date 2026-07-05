# Exercises — Example 5: Time-propagation algorithms

Same physics, same tensor network — different *integrators*. This example compares two ways of advancing the tensor network in time:

- `'vmf'` — solves one big coupled differential equation for all tensors at once;
- `'ps1'` — "projector splitting": sweeps through the network updating one tensor at a time.

It's the same kind of choice as picking an SCF mixing scheme in DFT or an optimizer in ML: all correct choices must converge to the same answer, but they differ in speed and robustness.

Each run takes about a minute. Estimated time: ~20 min.

## 5.1 — Do they agree?

Run `example5.py` and `example5_plot.py`.

- The `ps1` and `vmf` curves should coincide. Load the two output files and print the maximum difference.
- Note the speed (it/s from the progress bar) of each. Which algorithm is faster here?

## 5.2 — A third scheme

Add `'ps2'` to the `ps_methods` list and rerun. PS2 is like PS1 but can *adaptively grow* the tensor sizes during the run (like a solver that refines its own mesh).

- Does it agree with the other two? How does its speed compare?

## 5.3 — The default strategy (optional)

Delete the `stepwise_method` and `ps_method` arguments from the `system_multibath` call and rerun. This gives TENSO's default `'mix'` strategy: it starts with the adaptive PS2 to build up the tensors from the simple initial state, then switches to VMF for production.

- Compare with your fixed-scheme runs. Defaults in good codes usually encode exactly this kind of practical experience — worth knowing what they do before overriding them.
