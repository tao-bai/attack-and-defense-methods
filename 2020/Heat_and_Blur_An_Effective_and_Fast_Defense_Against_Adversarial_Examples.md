```
@article{2020arXiv200307573B,
archivePrefix = {arXiv},
arxivId = {cs.CV/2003.07573},
author = {Brama, Haya and Grinshpoun, Tal},
eprint = {2003.07573},
journal = {arXiv e-prints},
keywords = {Computer Science - Computer Vision and Pattern Rec,Computer Science - Machine Learning,Computer Science - Neural and Evolutionary Computi},
month = {mar},
pages = {arXiv:2003.07573},
primaryClass = {cs.CV},
title = {{Heat and Blur: An Effective and Fast Defense Against Adversarial Examples}},
year = {2020}
}
```

## Motivation
Some existing methods can increase NNs' robustness, but they often require special architecture or training procedures and are irrelevant to already trained models.

## Methods
It claims that the NN preservers the same info of correct labels for benign and adversarial images, illustrated as a heatmap.

Basicly, it produces a heatmap to identify the primary object. It looks like a kind of attention.