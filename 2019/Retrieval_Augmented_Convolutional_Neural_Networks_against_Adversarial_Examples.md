```
@inproceedings{cho2019retrieval,
author = {Cho, Kyunghyun and Others},
booktitle = {Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition},
pages = {11563--11571},
title = {{Retrieval-Augmented Convolutional Neural Networks Against Adversarial Examples}},
year = {2019}
}
```

## Motivation
Adversarial examples could be categorized into those off the data manifold, which is defined as a manifold on which training examples lie, and those on the data manifold[1].
They proposed to tackle both off- and on manifold adversarial examples by incorporating an off-the-shelf retrieval mechanism which indexes a large set of examples and training this combination of a deep neural network classifier and the retreval engine to behave linearly on the data manifold.

## Methods
1. define a feature convex hull as a reasonable local approximation to the data manifold.
2. learn a goal-driven projection procedure based on the attention mechanism. This trainable projection could be thought of as learning to project an off-manifold example on the locally-approximated manifold to maximize the classification accuracy.
3. constrain the final classifier to work only with a point inside a feature-space convex hull of neighboring training examples. This constraint alleviates the issue of the classifier's misbehaviors in the region outside the data manifold up to a certain degree.
4. To ensure the robustness of the proposed approach to on-manifold adversarial examples, a **local mixup**[2] is used in which a new mixed example pair is created by Kraemer Algorithm. When training, the classifier only observes a very small subset of any feature-space convex hull. 

## Experiments
Test their method in 2 scenarios: attacks to classifiers and to retrieval engine.

[1] Gilmer, J., Metz, L., Faghri, F., Schoenholz, S. S., Raghu, M., Wattenberg, M., & Goodfellow, I. (2018). Adversarial Spheres. ArXiv E-Prints, arXiv:1801.02774.
[2] Zhang, H., Cisse, M., Dauphin, Y. N., & Lopez-Paz, D. (2017). mixup: Beyond empirical risk minimization. arXiv preprint arXiv:1710.09412.