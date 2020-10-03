```
@incollection{NIPS2019_9388,
author = {Alayrac, Jean-Baptiste and Uesato, Jonathan and Huang, Po-Sen and Fawzi, Alhussein and Stanforth, Robert and Kohli, Pushmeet},
booktitle = {Advances in Neural Information Processing Systems 32},
editor = {Wallach, H and Larochelle, H and Beygelzimer, A and d$\backslash$textquotesingle Alch{\'{e}}-Buc, F and Fox, E and Garnett, R},
pages = {12192--12202},
publisher = {Curran Associates, Inc.},
title = {{Are Labels Required for Improving Adversarial Robustness?}},
url = {http://papers.nips.cc/paper/9388-are-labels-required-for-improving-adversarial-robustness.pdf},
year = {2019}
}
```

## Summary
This paper demonstrates that with training on unlabelled data, adversarial robustness can be improved. They proposed two unsupervised training loss. One of the key points is that controlling the smoothness loss is the key to adversarial generalization as it is observed that the smoothness loss dominates the classification loss on the test set.

## Motivation
Central hypothesis is that additional unlabeled wxamples may suffice for adversarial robustness.
- adversarial robustness depends on the smoothness of the classifier around natural images, which can be estimated from unlabeled data.
- only a realtively small amount of labeled data is needed for standard generalization.

Unsupervised adversarial training (UAT) to use unlabeled data for adversarial training.
## Method(s)
## Evaluation
## Conclusion
## Related work