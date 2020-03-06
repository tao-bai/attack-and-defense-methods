```
@inproceedings{DBLP:conf/cvpr/Moosavi-Dezfooli17,
author = {Moosavi-Dezfooli, Seyed-Mohsen and Fawzi, Alhussein and Fawzi, Omar and Frossard, Pascal},
booktitle = {2017 {\{}IEEE{\}} Conference on Computer Vision and Pattern Recognition, {\{}CVPR{\}} 2017, Honolulu, HI, USA, July 21-26, 2017},
doi = {10.1109/CVPR.2017.17},
isbn = {978-1-5386-0457-1},
pages = {86--94},
publisher = {{\{}IEEE{\}} Computer Society},
title = {{Universal Adversarial Perturbations}},
url = {https://doi.org/10.1109/CVPR.2017.17},
year = {2017}
}
```

This paper proposed to a novel method to produce universal perturbations. Its basic idea is to generate perturbations iteratively on the training set. After calculating one perturbation on the first data, it is added to the next training data. If this perturbation fails, the algorithm tries to find another perturbation on the perturbed data. If it succeeds, the new perturbation is the sum of this two. And the new perturbation is supposed to be less than $\epsilon$ in $L_p$ norm. This process will terminate when this perturbation is able to fool the models at a certain rate, say $1-\delta$. 

Note that this universal perturbation is not unique. The order of training data will influence the generation of perturbations.

This perturbation, according to the authors, is not only transferable within training data, but also within models. And they found there is a dominant direction of perturbations. In other words, images added universal perturbations are misclassified to several classes.

This attack is non-targeted when designing, but shows some targeted features. So in my opinion, it is possible to generate targeted universal perturbations.

**update**
One paper called *Defense Against Universal Adversarial Perturbations* cited this paper.