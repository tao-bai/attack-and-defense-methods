```
@inproceedings{8424631,
author = {Hayes, J and Danezis, G},
booktitle = {2018 IEEE Security and Privacy Workshops (SPW)},
doi = {10.1109/SPW.2018.00015},
keywords = {Atmospheric modeling,Error analysis,Machine learning,Measurement,Perturbation methods,Security,Training,adversarial examples,adversarial training,deep learning,generative models,generative network,known universal adversarial attacks,learning (artificial intelligence),misclassification,neural nets,neural networks,pattern classification,single perturbation,source input,universal adversarial networks,universal adversarial perturbations learning,universal perturbations},
month = {may},
pages = {43--49},
title = {{Learning Universal Adversarial Perturbations with Generative Models}},
year = {2018}
}
```
This paper proposed to generate universal adversarial perturbations using generative models. The loss function are 
$$
L_{n t}=\underbrace{\log \left[f\left(\delta^{\prime}+x\right)\right]_{c_{0}}-\max _{i \neq c_{0}} \log \left[f\left(\delta^{\prime}+x\right)\right]_{i}}_{L_{f s}}+\underbrace{\alpha \cdot\left\|\delta^{\prime}\right\|_{p}}_{L_{d i s t}}
$$
for untargeted attacks, which is adapted from C&W attack and ZOO.

$$
\min _{w} \frac{1}{N_{\mathrm{tr}}} \sum_{i=1}^{N_{\mathrm{tr}}}\left[\ell\left(f\left(x_{i} ; w\right), y_{i}\right)+\lambda \cdot\left\|\frac{\partial}{\partial x_{i}} \ell\left(f\left(x_{i} ; w\right), y_{i}\right)\right\|_{2}\right]
$$

According to the experiments, it outperforms the two former work [Universal Adversarial Perturbations](../2017/Universal_Adversarial_Perturbations.md) and [Deep Fool](../2016/DeepFool.md).