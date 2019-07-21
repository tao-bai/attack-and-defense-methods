```
@inproceedings{DBLP:journals/corr/GoodfellowSS14,
author = {Goodfellow, Ian J and Shlens, Jonathon and Szegedy, Christian},
booktitle = {3rd International Conference on Learning Representations, {\{}ICLR{\}} 2015, San Diego, CA, USA, May 7-9, 2015, Conference Track Proceedings},
editor = {Bengio, Yoshua and LeCun, Yann},
title = {{Explaining and Harnessing Adversarial Examples}},
url = {http://arxiv.org/abs/1412.6572},
year = {2015}
}
```
## Summary
**Reading through this paper even hundreds times is not enough.**

#### FSGM
In this paper, Goodfellow *et~al.* first proposed the linearity of neural networks in high dimentions. Based on this linearity, they designed a method *FGSM* to generate adversarial examples efficiently. The noise in max-norm could be formulated as below:
$$
\boldsymbol{\eta}=\epsilon \operatorname{sign}\left(\nabla_{\boldsymbol{x}} J(\boldsymbol{\theta}, \boldsymbol{x}, y)\right)
$$
where $\epsilon$ is the maximal noise in max-norm.

Then the adversarial examples are obtained as $\tilde{\boldsymbol{x}} = \boldsymbol{x} + \boldsymbol{\eta}$. Note here the loss function is seen as a function of $\boldsymbol{x}$ rather than $\theta$. So $\tilde{\boldsymbol{x}}$ is modified to make the loss function move in a gradient-ascending direction.

#### Adversarial training
*"Obviously, standard supervised training does not specify that the chosen function be resistant to adversarial examples. This must be encoded in the training procedure somehow.supervised training does not specify that the chosen function be resistant to adversarial examples. This must be encoded in the training procedure somehow."*

$$
\tilde{J}(\boldsymbol{\theta}, \boldsymbol{x}, y)=\alpha J(\boldsymbol{\theta}, \boldsymbol{x}, y)+(1-\alpha) J\left(\boldsymbol{\theta}, \boldsymbol{x}+\epsilon \operatorname{sign}\left(\nabla_{\boldsymbol{x}} J(\boldsymbol{\theta}, \boldsymbol{x}, y)\right)\right.
$$

The second term on the right means that we could continue updating the adversarial examples based on the current model in the training process.

**Chapter 10 summarizes the main ideas of this paper! Go and have a look.**
### My questions
Find the [code](../codes/fgsm).