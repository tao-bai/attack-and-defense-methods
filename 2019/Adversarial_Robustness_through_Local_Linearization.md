```
@incollection{NIPS2019_8821,
author = {Tramer, Florian and Boneh, Dan},
booktitle = {Advances in Neural Information Processing Systems 32},
editor = {Wallach, H and Larochelle, H and Beygelzimer, A and d$\backslash$textquotesingle Alch{\'{e}}-Buc, F and Fox, E and Garnett, R},
pages = {5858--5868},
publisher = {Curran Associates, Inc.},
title = {{Adversarial Training and Robustness for Multiple Perturbations}},
url = {http://papers.nips.cc/paper/8821-adversarial-training-and-robustness-for-multiple-perturbations.pdf},
year = {2019}
}
```
## Motivation
the computational cost of adversarial training grows prohibitively as the size of the model and number of input dimensions increase.

training against less expensive and therefore weaker adversaries produces models that are robust against weak attacks but break down under attacks that are stronger.

One approach which can alleviate the cost of adversar- ial training is training against weaker adversaries that are cheaper to compute. For example, by taking fewer gradi- ent steps to compute adversarial examples during training.
However, this can produce models which are robust against weak attacks, but break down under strong attacks – often due to **gradient obfuscation**.

If the loss surface was linear in the vicinity of the training examples, which is to say well-predicted by local gradient information, gradient obfuscation cannot occur.

find the subplementary to learn about the algorithms.