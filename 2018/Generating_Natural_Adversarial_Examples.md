```
@inproceedings{zhao2018generating,
author = {Zhao, Zhengli and Dua, Dheeru and Singh, Sameer},
booktitle = {6th International Conference on Learning Representations, {\{}ICLR{\}} 2018, Vancouver, BC, Canada, April 30 - May 3, 2018, Conference Track Proceedings},
title = {{Generating Natural Adversarial Examples}},
url = {https://openreview.net/forum?id=H1BLjgZCb},
year = {2018}
}
```

This paper proposed to generate adversarial examples more naturally. This method first trained a WGAN to generate examples with a vector $z$ from a gaussian distribution, then trained a Inverter, which transformed the images to a vector $\tilde{z}$ with same length of $z$. The loss function is to make $\tilde{z}$ close to $z$. In other words, the aim is to find $\tilde{z}$ in gaussian distribution. Next is adding purturbations to $\tilde{z}$ and find the optimal noise. But the search process could be time-consuming.

This method could generate adversarial examples with images and texts.