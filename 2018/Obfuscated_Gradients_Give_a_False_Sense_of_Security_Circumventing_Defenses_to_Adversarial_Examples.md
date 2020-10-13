```
@inproceedings{pmlr-v80-athalye18a,
address = {Stockholmsm{\"{a}}ssan, Stockholm Sweden},
author = {Athalye, Anish and Carlini, Nicholas and Wagner, David},
booktitle = {Proceedings of the 35th International Conference on Machine Learning},
editor = {Dy, Jennifer and Krause, Andreas},
pages = {274--283},
publisher = {PMLR},
series = {Proceedings of Machine Learning Research},
title = {{Obfuscated Gradients Give a False Sense of Security: Circumventing Defenses to Adversarial Examples}},
url = {http://proceedings.mlr.press/v80/athalye18a.html},
volume = {80},
year = {2018}
}
```
## Summary
## Motivation
Obfuscated gradients, a term defined as a special case of gradient masking. Without a good gradient, where following the gradient does not successfully optimize the loss， iterarive optimization based methods cannot succeed.
- **shattered gradients** are caused when a defense is non- differentiable, introduces numeric instability, or otherwise causes a gradient to be nonexistent or incorrect. Defenses that cause gradient shattering can do so unintentionally, by using differentiable operations but where following the gradient does not maximize classification loss globally.
- **stochastic gradients** are caused by randomized defenses, where either the network itself is randomized or the input is randomly transformed before being fed to the classifier, causing the gradients to become randomized. This causes methods using a single sample of the randomness to incor- rectly estimate the true gradient.
- **vanishing/exploding gradients** are often caused by de- fenses that consist of multiple iterations of neural network evaluation, feeding the output of one computation as the input of the next. This type of computation, when unrolled, can be viewed as an extremely deep neural network evalua- tion, which can cause vanishing/exploding gradients.

#### Identifying obfuscated & masked gradients
- one-step attacks peform better than iterative attacks.
- black-box attacks are better than white-box attacks.
- unbounded attacks do not reach 100% success.
- random sampling finds adversarial examples.
- increasing distortion bound does not increase success.

## Method(s)
### Backward Pass Differentiaable Approximation
the main idea is to approximate the non-differentiable operations $g(x)=f^i(x)$.
then in the backward pass, use g(x) to calculate gradients.

## Evaluation
## Conclusion
## Related work