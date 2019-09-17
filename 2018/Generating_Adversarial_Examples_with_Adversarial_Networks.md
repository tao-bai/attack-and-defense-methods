```
@inproceedings{DBLP:conf/ijcai/XiaoLZHLS18,
author = {Xiao, Chaowei and Li, Bo and Zhu, Jun-Yan and He, Warren and Liu, Mingyan and Song, Dawn},
booktitle = {Proceedings of the Twenty-Seventh International Joint Conference on Artificial Intelligence, {\{}IJCAI{\}} 2018, July 13-19, 2018, Stockholm, Sweden.},
doi = {10.24963/ijcai.2018/543},
editor = {Lang, J{\'{e}}r{\^{o}}me},
isbn = {978-0-9992411-2-7},
pages = {3905--3911},
publisher = {ijcai.org},
title = {{Generating Adversarial Examples with Adversarial Networks}},
url = {https://doi.org/10.24963/ijcai.2018/543},
year = {2018}
}
```
This paper proposed to use GAN to generate adversarial examples. To my best knowledge, this is the first paper which generated adversarial examples with GAN. But there are a few shortbacks of their method:
1. Their method takes the label in the loss when training, which means once the model is trained, it is only be able to generate one class images.
2. The quality of generated images are not satisfying. In MNIST, for example, the adversarial examples look like unnatural, where shadows are easy to recognize.