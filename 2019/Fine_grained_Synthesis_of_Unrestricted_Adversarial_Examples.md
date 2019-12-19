```
@article{2019arXiv191109058P,
archivePrefix = {arXiv},
arxivId = {cs.CV/1911.09058},
author = {Poursaeed, Omid and Jiang, Tianxing and Yang, Harry and Belongie, Serge and Lim, Ser-Nam},
eprint = {1911.09058},
keywords = {Computer Science - Computer Vision and Pattern Rec,Computer Science - Cryptography and Security,Computer Science - Machine Learning,Statistics - Machine Learning},
month = {nov},
pages = {arXiv:1911.09058},
primaryClass = {cs.CV},
title = {{Fine-grained Synthesis of Unrestricted Adversarial Examples}},
year = {2019}
}

```
## Motivation
There are several different methods generating **unrestricted adversarial methods**[1-3]. These methods are not controllable.

## Methods
They leverage disentangled latent representations of images for unrestricted adversarial examples. Style-GAN is a SOTA generative model which learns to disentangle high-level attributes and stochastic variations in an unsupervised manner. More specifically, stylistic variations are represented by style variables and stochastic details are captured by noise variables. Changing the noise only affects low-level details, leaving the over composition and high-level aspects such as identity intact. This makes it possible to manipulate the noise variables such that variations are barely noticeable by the human eye, yet the synthesized image can fool a pre-trained classifier.

This approach is able to break the SOTA certified defense but adversarial training makes the target models more robust. Also doing adversarial training based on this approach does not affect the accuracy of the models.



[1] Xiao, C., Zhu, J.-Y., Li, B., He, W., Liu, M., & Song, D. (2018). Spatially Transformed Adversarial Examples. 6th International Conference on Learning Representations, {ICLR} 2018, Vancouver, BC, Canada, April 30 - May 3, 2018, Conference Track Proceedings. 
[2] Song, Y., Shu, R., Kushman, N., & Ermon, S. (2018). Constructing Unrestricted Adversarial Examples with Generative Models. In S. Bengio, H. Wallach, H. Larochelle, K. Grauman, N. Cesa-Bianchi, & R. Garnett (Eds.), Advances in Neural Information Processing Systems 31 (pp. 8312–8323). 
[3] Liu, A., Liu, X., Fan, J., Ma, Y., Zhang, A., Xie, H., & Tao, D. (2019). Perceptual-Sensitive {GAN} for Generating Adversarial Patches. The Thirty-Third {AAAI} Conference on Artificial Intelligence, {AAAI} 2019, The Thirty-First Innovative Applications of Artificial Intelligence Conference, {IAAI} 2019, The Ninth {AAAI} Symposium on Educational Advances in Artificial Intelligence, {EAAI}, 1028–1035.
