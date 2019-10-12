```
@inproceedings{xiao2018spatially,
author = {Xiao, Chaowei and Zhu, Jun-Yan and Li, Bo and He, Warren and Liu, Mingyan and Song, Dawn},
booktitle = {International Conference on Learning Representations},
title = {{Spatially Transformed Adversarial Examples}},
url = {https://openreview.net/forum?id=HyydRMZC-},
year = {2018}
}
```
[OpenReview](https://openreview.net/forum?id=HyydRMZC-)

To my best knowledge, this is the first paper to generate adversarial examples by modifying the geometry of images. It is a new type of adversarial examples.

In this paper, they defined a new loss called $\mathcal{L}_{flow}$ to evaluate the distortion.
$$
\mathcal{L}_{f l o w}(f)=\sum_{p}^{\text {all pixels}} \sum_{q \in \mathcal{N}(p)} \sqrt{\left\|\Delta u^{(p)}-\Delta u^{(q)}\right\|_{2}^{2}+\left\|\Delta v^{(p)}-\Delta v^{(q)}\right\|_{2}^{2}}
$$