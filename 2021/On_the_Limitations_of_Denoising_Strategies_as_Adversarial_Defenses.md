```
@article{niu2020limitations,
author = {Niu, Zhonghan and Chen, Zhaoxi and Li, Linyi and Yang, Yubin and Li, Bo and Yi, Jinfeng},
journal = {arXiv preprint arXiv:2012.09384},
title = {{On the Limitations of Denoising Strategies as Adversarial Defenses}},
year = {2020}
}
```

## Denoising in the spatial domain
For most defense methods, it is very difficult to remove all perturbations precisely without sacrifice benign accuracy, especially for complex images like ImageNet.
## Denoising in the frequency domain
As many works purify their adversarial examples only by filtering out high-frequency components, we suggest that to achieve an approving defense efficiency, the defense should be carried out simultaneously on multiple frequency bands.
## Denoising in latent space
The main idea is to deal with the vulnerability of individual convolutional filters in DNNs, which reveals the significant impact of adversarial noise in the latent space.

## Questions
1. Section 2.2 states that denoising on multiple frequecy bands is useful. However, the experiments are done in spatial domain, rather feature space. Is it equivalent?
2. Cannot understand Fig. 11.
3. Will double denosing work?