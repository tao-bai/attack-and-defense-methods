```
@inproceedings{DBLP:journals/corr/SzegedyZSBEGF13,
  author    = {Christian Szegedy and
               Wojciech Zaremba and
               Ilya Sutskever and
               Joan Bruna and
               Dumitru Erhan and
               Ian J. Goodfellow and
               Rob Fergus},
  title     = {Intriguing properties of neural networks},
  booktitle = {2nd International Conference on Learning Representations, {ICLR} 2014,
               Banff, AB, Canada, April 14-16, 2014, Conference Track Proceedings},
  year      = {2014},
  crossref  = {DBLP:conf/iclr/2014},
  url       = {http://arxiv.org/abs/1312.6199},
  timestamp = {Thu, 04 Apr 2019 13:20:07 +0200},
  biburl    = {https://dblp.org/rec/bib/journals/corr/SzegedyZSBEGF13},
  bibsource = {dblp computer science bibliography, https://dblp.org} 
}
```
## Summary
This paper presented two counter-intuitive properties of deep neural networks.

#### 1. Semantic meaning of individual units.

Previous works interpret an activation of a hidden unit as a meaningful feature. They found images satisfying the following equation and concluded that these images have same semantic meaning. 
$$
x^{\prime}=\underset{x \in \mathcal{I}}{\arg \max }\left\langle\phi(x), e_{i}\right\rangle
$$
where $e_{i}$ is the natural basis vector associated with the i-th hidden unit.

The authors, however, replaced $e_{i}$ with a random vector and got similar results. It means the space actually has semantic meaning but the coordinates(units).

#### 2. Stability of neural networks wrt small purturbations. 
**This property that networks are vulnerable to inperceptible tiny purturbations is what we should focus on.** This paper proposed a method to generate adversarial examples. Finding adversarial examples is formulated as a optimization problem as:
$$
\begin{array}{c}{\cdot \text { Minimize }\|r\|_{2} \text { subject to: }} \\ {\text { 1. } f(x+r)=l} \\ {\text { 2. } x+r \in[0,1]^{m}}\end{array}
\tag{1}
$$
where $l$ is the targeted label, $r$ is the noise added, and $x$ is the original image. Usually $x$ is normalized.

It is hard to solve this optimization, so they approximated it by using a box-constrained L-BFGS.Concretely, they found an approximation of equation $(1)$ by performing line-search to find the minimum c > 0 for which
the minimizer $r$ of the following problem satisfies $f(x + r) = l$.
$$
\bullet \text { Minimize } c|r|+\operatorname{loss}_{f}(x+r, l) \text { subject to } x+r \in[0,1]^{m}
$$


### My questions
1. Have no idea of L-BFGS and how to do the transformation?
2. Check the [code](https://github.com/akshaychawla/Adversarial-Examples-in-PyTorch) though it does not use L-BFGS.  
