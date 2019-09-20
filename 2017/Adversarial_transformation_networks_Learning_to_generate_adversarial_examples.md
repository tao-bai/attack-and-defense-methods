```
@article{baluja2017adversarial,
author = {Baluja, Shumeet and Fischer, Ian},
journal = {arXiv preprint arXiv:1703.09387},
title = {{Adversarial transformation networks: Learning to generate adversarial examples}},
year = {2017}
}
```
This paper proposed Adversarial Transformation Network(ATN) generate adversarial examples, including Perturbation ATN and Adversarial Autoencoding(AAE). Their method aimed at white-box targeted attacks. AAE could generate adversarial examples directly rather than generate purturbations, this is the reason that it is called transformation. **And they added $tanh()$ as the last operation to make sure the values of images are valid, which I think is better than clipping arbitrarily.**

There are two losses in their objective function: one is the input-space loss function to make the adversarial examples similar to original images; the other is the adversarial loss function. 

This adversarial loss function is interesting. See the paper for details.
$$
L_{\mathcal{Y}, t}\left(\mathbf{y}^{\prime}, \mathbf{y}\right)=L_{2}\left(\mathbf{y}^{\prime}, r(\mathbf{y}, t)\right)
$$

$$
r_{\alpha}(\mathbf{y}, t)=\operatorname{norm}\left(\left\{\begin{array}{cc}{\alpha * \max \mathbf{y}} & {\text { if } k=t} \\ {} & {y_{k} \quad \text { otherwise }}\end{array}\right\}_{k \in \mathbf{y}}\right)
$$

$\alpha$ equals to 1.5 in the experiments.