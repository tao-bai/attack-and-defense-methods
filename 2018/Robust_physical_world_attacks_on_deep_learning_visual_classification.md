```
@inproceedings{eykholt2018robust,
author = {Eykholt, Kevin and Evtimov, Ivan and Fernandes, Earlence and Li, Bo and Rahmati, Amir and Xiao, Chaowei and Prakash, Atul and Kohno, Tadayoshi and Song, Dawn},
booktitle = {Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition},
pages = {1625--1634},
title = {{Robust physical-world attacks on deep learning visual classification}},
year = {2018}
}
```
## Motivation
For physical-world attacks
- Environmental conditions. The distance and angle.
- Spatial Constraints. For a physical road sign, the attacker cannot manipulate background imagery. The road sign will change depending on the distance and angle of the viewing camera.
- Physical limits on Imperceptibility. We need to ensure that a camera could perceive the perturbations.
- Fabrication Error. All perturbation values must be valid colours that can be reproduced in the real world.

## Methods
### Overview
1. start with the optimization method that generates a perturbation for a single image, without considering other physical conditions.
2. update the algorithm taking the physical challenges above into account.

### Details
- For **Environmental conditions**, model the distribution of images containing object under both physical and digital transformations $X^V$. Sample instances from $X^V$ by both generating experimental data that contains actual physical condition variability as well as synthetic transformations. 
- For **spatial constraints** and **physical limits on imperceptibility**, introduce a mask to project the computed perturbations to a physical region on the surface of the object. This mask also helps generate perturbations that are visible but inconspicuous to human observers.
- For **fabrication error**, add an additional term to objective function that models printer color reproduction errors. This term is based upon the Non-Printability Score(NPS).
## Thoughts
1. Use L1 metric to find the most vulnerable positions, and then use L2 metric to reproduce the perturbation.

