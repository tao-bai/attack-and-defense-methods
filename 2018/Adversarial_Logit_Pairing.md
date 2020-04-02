```
@article{DBLP:journals/corr/abs-1803-06373,
archivePrefix = {arXiv},
arxivId = {1803.06373},
author = {Kannan, Harini and Kurakin, Alexey and Goodfellow, Ian J},
eprint = {1803.06373},
journal = {CoRR},
title = {{Adversarial Logit Pairing}},
url = {http://arxiv.org/abs/1803.06373},
volume = {abs/1803.0},
year = {2018}
}
```
- Adversarial logit pairing
- Clean logit pairing
- Clean logit squeeze

Mixup trains the model on input points that are interpolated between training examples.

The better performance of ALP than VAT may be due to the fact that the KL divergence can suffer from saturating gradients or it may be due to the fact that the KL divergence is invariant to a shift of all the logits for an individual example while the logit pairing loss is not.


Our results suggest that feature pairing (matching adversarial and clean intermediate features instead of logits) may also prove useful in the future.


[Evaluating and Understanding the Robustness of Adversarial Logit Pairing](https://arxiv.org/abs/1807.10272)