```
@inproceedings{DBLP:conf/aaai/BalujaF18,
author = {Baluja, Shumeet and Fischer, Ian},
booktitle = {Proceedings of the Thirty-Second {\{}AAAI{\}} Conference on Artificial Intelligence, (AAAI-18), the 30th innovative Applications of Artificial Intelligence (IAAI-18), and the 8th {\{}AAAI{\}} Symposium on Educational Advances in Artificial Intelligence (EAAI-18), New},
editor = {McIlraith, Sheila A and Weinberger, Kilian Q},
pages = {2687--2695},
publisher = {{\{}AAAI{\}} Press},
title = {{Learning to Attack: Adversarial Transformation Networks}},
url = {https://www.aaai.org/ocs/index.php/AAAI/AAAI18/paper/view/16529},
year = {2018}
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

And generated images seems better than that in [1].

## References
[1] Xiao, C., Li, B., Zhu, J.-Y., He, W., Liu, M., & Song, D. (2018). Generating Adversarial Examples with Adversarial Networks. In J. Lang (Ed.), Proceedings of the Twenty-Seventh International Joint Conference on Artificial Intelligence, {IJCAI} 2018, July 13-19, 2018, Stockholm, Sweden. (pp. 3905–3911). https://doi.org/10.24963/ijcai.2018/543