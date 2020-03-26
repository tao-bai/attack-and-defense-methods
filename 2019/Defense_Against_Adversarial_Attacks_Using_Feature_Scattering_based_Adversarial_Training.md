```
@incollection{NIPS2019_8459,
author = {Zhang, Haichao and Wang, Jianyu},
booktitle = {Advances in Neural Information Processing Systems 32},
editor = {Wallach, H and Larochelle, H and Beygelzimer, A and d$\backslash$textquotesingle Alch{\'{e}}-Buc, F and Fox, E and Garnett, R},
pages = {1829--1839},
publisher = {Curran Associates, Inc.},
title = {{Defense Against Adversarial Attacks Using Feature Scattering-based Adversarial Training}},
url = {http://papers.nips.cc/paper/8459-defense-against-adversarial-attacks-using-feature-scattering-based-adversarial-training.pdf},
year = {2019}
}
```
## Motivation
Conventional adversarial training approaches leverage a supervised scheme in generating attacks for training, which typically suffer from issues such as label leaking.

This paper introduces optimal transport to feature matching. And based on the feature matching distance, they formulated the feature scattering method, which intuitively interpreted as maximizing the feature matching distance between the original and perturbed empirical distributions with respect to the inputs.

When generating adversarial examples, it takes the inter-sample relationships into consideration.