```
@inproceedings{DBLP:conf/cvpr/PoursaeedKGB18,
author = {Poursaeed, Omid and Katsman, Isay and Gao, Bicheng and Belongie, Serge J},
booktitle = {2018 {\{}IEEE{\}} Conference on Computer Vision and Pattern Recognition, {\{}CVPR{\}} 2018, Salt Lake City, UT, USA, June 18-22, 2018},
doi = {10.1109/CVPR.2018.00465},
publisher = {{\{}IEEE{\}} Computer Society},
title = {{Generative Adversarial Perturbations}},
url = {http://openaccess.thecvf.com/content{\_}cvpr{\_}2018/html/Poursaeed{\_}Generative{\_}Adversarial{\_}Perturbations{\_}CVPR{\_}2018{\_}paper.html},
year = {2018}
}
```
This paper investigated methods to generate adversarial perturbations. They classified the perturbations with universal/iamge-dependent, and targeted/untargeted.

Something interesting is that the perturbations converted to a bird-like perturbation when generating universal perturbations. And the targeted universal perturbations contains patterns resembling the target class. **This is the first paper to generate targeted universal perturbations**.

And according to the experiments, teh Resnet Generator introduced in [1] outperforms the U-net.

[1] Johnson, J., Alahi, A., & Fei-Fei, L. (2016). Perceptual losses for real-time style transfer and super-resolution. European Conference on Computer Vision, 694–711.