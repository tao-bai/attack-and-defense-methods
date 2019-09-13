```
@article{Bose2019,
archivePrefix = {arXiv},
arxivId = {1905.10864},
author = {Bose, Avishek Joey and Cianflone, Andre and Hamilton, William L},
eprint = {1905.10864},
month = {may},
title = {{Generalizable Adversarial Attacks Using Generative Models}},
url = {http://arxiv.org/abs/1905.10864},
year = {2019}
}
```
This paper proposed a general framework for attacks. The main idea is using a encoder to get the latent vector of input data, then a decoder to generate the perturbations, which I think it is just VAE. Then combine the perturbations and images together to get adversarial examples.

The overall loss function have 3 parts:
- One loss funciton is max-margin misclassification loss provided by a pretrained classifier. 
- One is to constrain the magnitude of the perturbation.
- One is to make the distribution of latent vector similar to normal distribution.