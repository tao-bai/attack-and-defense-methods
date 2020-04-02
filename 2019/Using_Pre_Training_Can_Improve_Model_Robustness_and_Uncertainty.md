```
@inproceedings{DBLP:conf/icml/HendrycksLM19,
author = {Hendrycks, Dan and Lee, Kimin and Mazeika, Mantas},
booktitle = {Proceedings of the 36th International Conference on Machine Learning, {\{}ICML{\}} 2019, 9-15 June 2019, Long Beach, California, {\{}USA{\}}},
editor = {Chaudhuri, Kamalika and Salakhutdinov, Ruslan},
pages = {2712--2721},
publisher = {PMLR},
series = {Proceedings of Machine Learning Research},
title = {{Using Pre-Training Can Improve Model Robustness and Uncertainty}},
url = {http://proceedings.mlr.press/v97/hendrycks19a.html},
volume = {97},
year = {2019}
}
```
- Pre-training tremendously improve the model's adversarial robustness.
- To reduce this gap, we introduce **adversarial pre-training**, where we make representations transfer across data distributions robustly.
- Choosing to use targeted adversaries or no adversaries during pre-training does not provide substantial robustness. Instead, we choose to adversarially pre- train a Downsampled ImageNet model against an untargeted adversary, contra Kurakin et al. (2017); Kannan et al. (2018); Xie et al. (2018)