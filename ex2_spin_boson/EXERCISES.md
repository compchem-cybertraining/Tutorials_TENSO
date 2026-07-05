# Exercises — Example 2: Tensor-network structures

TENSO represents the simulation state as a *tensor network* — a big tensor factorized into small connected pieces. This example runs the **same physics twice**, changing only the network layout: a binary tree (`tree2`) and a chain (`train`). Think of it like choosing a basis set or a mesh: a numerical representation choice that must not change the answer.

Each run takes a few minutes. Estimated time: ~20 min.

## 2.1 — Same physics, same answer?

Run `example2.py` and `example2_plot.py`.

- The tree and train curves should lie on top of each other. Do they?
- Load both output files (`tree2.dat.log`, `train.dat.log`) with numpy and print the maximum absolute difference between the two population curves. How big is it, and why should a converged result not depend on the network structure at all?

## 2.2 — Which is faster?

The tqdm progress bar prints the speed (it/s) of each run.

- Which structure is faster for this problem? The difference is small here because the environment is simple (few "bath modes"); for larger problems the layout choice can decide whether a simulation is feasible at all.

## 2.3 — A third structure (optional)

Add `'naive': 'naive'` to the `outs` dictionary and rerun. This uses one big unfactorized tensor — the "brute force" layout.

- Does it agree with the other two? For this small problem it works fine; it's the option that becomes exponentially expensive as the environment grows.
