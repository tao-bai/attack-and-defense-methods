```
@incollection{NIPS2019_8441,
author = {Hu, Shengyuan and Yu, Tao and Guo, Chuan and Chao, Wei-Lun and Weinberger, Kilian Q},
booktitle = {Advances in Neural Information Processing Systems 32},
editor = {Wallach, H and Larochelle, H and Beygelzimer, A and d$\backslash$textquotesingle Alch{\'{e}}-Buc, F and Fox, E and Garnett, R},
pages = {1633--1644},
publisher = {Curran Associates, Inc.},
title = {{A New Defense Against Adversarial Images: Turning a Weakness into a Strength}},
url = {http://papers.nips.cc/paper/8441-a-new-defense-against-adversarial-images-turning-a-weakness-into-a-strength.pdf},
year = {2019}
}
```
## Motivation
Recent studies[1][2] show the existence of adversarial perturbations may be an inherent property of natural data distributions in high dimensinal spaces.
The authors use this inherent property as a signature to attest that if a natural image is unperturbed.

On one hand, natural images lie with high probability near the decision boundary to any given label [1][2]. on the other hand, natural images are robust to random noise [49], which means these small “pockets” of spaces where the input is misclassified have low density and are unlikely to be found through random perturbations.

## Methods
**Existing methods**: 
- feature squeezing *W. Xu, D. Evans, and Y. Qi. Feature Squeezing: Detecting Adversarial Examples in Deep Neural Networks. Network and Distributed Systems Security Symposium (NDSS), 2018.*
- Artifacts *R. Feinman, R. R. Curtin, S. Shintre, and A. B. Gardner. Detecting Adversarial Samples from Artifacts.*

**Criterion 1: Robustness to random noise.** Sample $\epsilon \sim N\left(0, \sigma^{2} I\right)$ and compute $\Delta=\|h(\mathbf{x})-h(\mathbf{x}+\epsilon)\|_{1}$. The input is rejected as asversarial if $\Delta$ is sufficiently large. 

This is beacuse adversarial perturbations push the benign image near the boundary to the incorrect class. With gaussian noise, the image may move to the original class.

However, C1 is not enough if the image is pushed into deep area of incorrect class.

**Criterion 2: Susceptibility to adversarial noise.** For a chosen first-order iterative attack algorithm A, evaluate A on the input x and record the minimum number of steps K required to adversarially perturb x. The input is rejected as adversarial if K is sufficiently large.

The tuition is that real images requires very few steps to reach the dicision boundary of any random target class.





## References
[1] Fawzi, A., Fawzi, H., & Fawzi, O. (2018). Adversarial vulnerability for any classifier. In S. Bengio, H. M. Wallach, H. Larochelle, K. Grauman, N. Cesa-Bianchi, & R. Garnett (Eds.), Advances in Neural Information Processing Systems 31: Annual Conference on Neural Information Processing Systems 2018, NeurIPS 2018, 3-8 December 2018, Montréal, Canada. (pp. 1186–1195). Retrieved from http://papers.nips.cc/paper/7394-adversarial-vulnerability-for-any-classifier
[2] Shafahi, A., Huang, W. R., Studer, C., Feizi, S., & Goldstein, T. (2019). Are adversarial examples inevitable? 7th International Conference on Learning Representations, {ICLR} 2019, New Orleans, LA, USA, May 6-9, 2019. Retrieved from https://openreview.net/forum?id=r1lWUoA9FQ