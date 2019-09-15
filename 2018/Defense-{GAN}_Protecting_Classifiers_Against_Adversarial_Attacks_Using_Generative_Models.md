```
@inproceedings{samangouei2018defensegan,
author = {Samangouei, Pouya and Kabkab, Maya and Chellappa, Rama},
booktitle = {International Conference on Learning Representations},
title = {{Defense-{\{}GAN{\}}: Protecting Classifiers Against Adversarial Attacks Using Generative Models}},
url = {https://openreview.net/forum?id=BkJ3ibb0-},
year = {2018}
}
```
This paper proposed a method called Defense-GAN as a pre-processing technique before feeding the input to a classifier. Specifically, they trained a WGAN to learn the distribution in latent space. Then they sampled the points in the latent space and used pretrained WGAN to reconstruct the images. Computing the L2 distance between the original images and the reconstructed images, the reconstructed image which has least distance with the original image is selected and fed to the classifier. The classifier could be trained on the original datasets or the reconstructed, which leads to little difference to accuracy. 
