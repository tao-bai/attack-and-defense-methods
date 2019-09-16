```
@article{DBLP:journals/corr/abs-1906-07927,
archivePrefix = {arXiv},
arxivId = {1906.07927},
author = {Qiu, Haonan and Xiao, Chaowei and Yang, Lei and Yan, Xinchen and Lee, Honglak and Li, Bo},
eprint = {1906.07927},
journal = {CoRR},
title = {{SemanticAdv: Generating Adversarial Examples via Attribute-conditional Image Editing}},
url = {http://arxiv.org/abs/1906.07927},
volume = {abs/1906.0},
year = {2019}
}
```
Honestly, I do not think this is a good paper. It proposed to utilize the conditional GAN to generate adversarial examples by modifying the images' attributes. To put it simple, the main idea is interpolating the latent vectors of two images and feeding the modified vector into a Generator to reconstruct the images. There are two loss functions(Section 3.2): one is the loss for adversarial examples, the other is interpolation smoothness.

The experiments are sufficient and the results are pretty. 