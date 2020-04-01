```
@inproceedings{YAN2020On,
author = {YAN, Hanshu and DU, Jiawei and TAN, Vincent and FENG, Jiashi},
booktitle = {International Conference on Learning Representations},
title = {{On Robustness of Neural Ordinary Differential Equations}},
url = {https://openreview.net/forum?id=B1e9Y2NYvS},
year = {2020}
}
```
## Motivation
The robustness of neural ODE is unclear.

In contrast to conventional convolutional neural networks (CNNs), we find that the ODENets are more robust against both randomGaussian perturbations and adversarial attack examples.

Our work suggests that, due to their intrinsic robustness, it is promising to use neural ODEs as a basic block for building robust deep network models.

The non-intersecting property indicates that an integral curve starting from some point is constrained by the integral curves starting from that point's neighbourhood. Thus, in an ODENet, if a correctly classified datum is slightly perturbed, the integral curve associated to its perturbed version would not change too much from the original one. Thus, there exists intrinsic robustness regularization in ODENets, which is absent from CNNs.

Motivated by this property of the neural ODE flow, we attempt to explore a more robust neural ODE architecture by introducing stronger regularization on the flow. 

We thus propose a Time-Invariant Steady neural ODE (TisODE). The TisODE removes the time dependence of the dynamics in an ODE and imposes a steady-state constraint on the integral curves.