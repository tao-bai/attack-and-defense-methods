```
@article{engstrom2018evaluating,
author = {Engstrom, Logan and Ilyas, Andrew and Athalye, Anish},
journal = {arXiv preprint arXiv:1807.10272},
title = {{Evaluating and understanding the robustness of adversarial logit pairing}},
year = {2018}
}
```
Adversarial training
$$\min _{\theta} \mathbb{E}_{(x, y) \sim \mathcal{D}}\left[\max _{\delta \in S} L(\theta, x+\delta, y)\right]$$

Adversarial Logit pairing
$$\begin{array}{c}
\min _{\theta} \mathbb{E}_{(x, y) \sim \mathcal{D}}\left[L(\theta, x, y)+\lambda D\left(f(\theta, x), f\left(\theta, x+\delta^{*}\right)\right)\right] \\
\text { where } \delta^{*}=\underset{\delta \in \mathcal{S}}{\arg \max } L(\theta, x+\delta, y)
\end{array}$$

## Analyzing the defense objective
### Training on natural vs. adversarial images.
In adversarial training, the minimization with respect to $\theta$ is done over the inputs that have been crafted by the max player; $\theta$ is not minimized with respect to any natural data $x \sim \mathcal{D}$. 

In the ALP, regularization is applyied to the loss on clean data.

### Generating targeted adversarial examples.
ALP generates targeted adversarial examples during the training process. This again deviates from the robust optimization-inspired saddle point formulation for adversarial training, as the inner maximization player no longer maximizes $L(\theta, x+\delta, y)$, but rather minimizes $L\left(\theta, x+\delta, y_{a d v}\right)$ for another class $y_{adv}$.

## Analyzing empirical robustness
Overall, the attack on ALP-trained  network required more steps of gradient descent to converge, but robustness had not increased. The optimization landscape of the ALP-trained network is less amenable to gradient descent.  