```
@inproceedings{tramèr2018ensemble,
author = {Tram{\`{e}}r, Florian and Kurakin, Alexey and Papernot, Nicolas and Goodfellow, Ian and Boneh, Dan and McDaniel, Patrick},
booktitle = {International Conference on Learning Representations},
title = {{Ensemble Adversarial Training: Attacks and Defenses}},
url = {https://openreview.net/forum?id=rkZvSe-RZ},
year = {2018}
}
```
When adversarial training is first proposed, perturbations are crafted using fast single-step methods that maximize a linear approximation of the model's loss. This form of adversarial training converges to a degenerate global minimum, wherein small curvature artefacts near the data points obfuscate a linear approximation of the loss. Adversarially trained models using single-step methods remain vulnerable to simple attacks. For black-box adversaries, we find that perturbations crafted on an undefended model often transfer to an adversarially trained one.

**Ensemble adversarial training** augments training data with perturbations transferred from other models. It decouples adversarial example generation from the parameters of the trained model, and increases the diversity of the perturbations seen during training.