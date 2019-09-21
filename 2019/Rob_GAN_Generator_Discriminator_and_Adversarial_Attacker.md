```
@inproceedings{Liu_2019_CVPR,
author = {Liu, Xuanqing and Hsieh, Cho-Jui},
booktitle = {The IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
month = {jun},
title = {{Rob-GAN: Generator, Discriminator, and Adversarial Attacker}},
year = {2019}
}
```
This paper combined adversarial training and GAN together. They gave two insights:
1. The generalization gap is large under adversarial attacks. Enforcing a small local Lipschitz value(LLV) on the underlining data distribution is desirable. But it helps little. Then the authors proposed to use GAN to learn $\mathcal(P_{data})$ and perform the adversarial training process on the learned distribution.

The loss funciton is
$$
\begin{array}{l}{\min _{w} \mathcal{L}_{\text {real }}\left(w, \delta_{\max }\right)+\lambda \cdot \mathcal{L}_{\text {fake }}\left(w, \delta_{\max }\right)} \\ {\mathcal{L}_{\text {real }}\left(w, \delta_{\max }\right) \triangleq \frac{1}{N_{\text {tr }}} \sum_{i=1}^{N_{t r}} \max _{\left\|\delta_{i}\right\| \leq \delta_{\text {max }}} \ell\left(f\left(x_{i}+\delta_{i} ; w\right) ; y_{i}\right)} \\ {\mathcal{L}_{\text {fake }}\left(w, \delta_{\text {max }}\right) \triangleq \operatorname{E}_{(x, y) \sim \mathcal{P}_{\text {fake }}\|\delta\| \leq \delta_{\text {max }}} \ell(f(x+\delta ; w) ; y)}\end{array}
$$

Intuitively, it is a composite robust optimization on both original training data and GAN synthesized data.

2. Getting a robust discriminator will accelerate the training process. They required a small local Lipschitz value on the image manifold rather than a trict one-Lipschitz funciton globally. This can be done through adversarial training to teh discriminator.

As for the architectures, they chose the discriminator with auxiliary classifier of AC-GAN and the Generator is normal one, I guess.

Another thing mentioned in the original paper is that they fine-tuned the discriminator to conduct a pure multi-class classification task.

The code is [here](https://github.com/xuanqing94/RobGAN)

I think the idea of this paper simple, but why it can be accepted by a top conference is they did a good mathematical analysis, which I think  is a key point.