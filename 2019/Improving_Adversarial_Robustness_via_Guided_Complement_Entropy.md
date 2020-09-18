```
@inproceedings{Chen_2019_ICCV,
author = {Chen, Hao-Yun and Liang, Jhao-Hong and Chang, Shih-Chieh and Pan, Jia-Yu and Chen, Yu-Ting and Wei, Wei and Juan, Da-Cheng},
booktitle = {The IEEE International Conference on Computer Vision (ICCV)},
month = {oct},
title = {{Improving Adversarial Robustness via Guided Complement Entropy}},
year = {2019}
}
```
## Summary
This paper proposed a new loss function to produce adversarially robust models without training on adversarial examples. However, it did not compare with PGD adversarial training, and did not evaluate on PGD attacks.
## Motivation
1. Adversarial training is computational intensive, and not flexible.
2. Existing methods achieves adversarial robustness at a cost of model performance.

## Method(s)
### Complement Entropy
$$-\frac{1}{N} \sum_{i=1}^{N} \sum_{j=1, j \neq g}^{K}\left(\frac{\hat{y}_{i j}}{1-\hat{y}_{i g}}\right) \log \left(\frac{\hat{y}_{i j}}{1-\hat{y}_{i g}}\right)$$

The idea behind complement entropy is to flatten the weight distribution among the incorrect classes. Mathematically, a distribution is flattened when its entropy is maximized, so Complement Entropy incorporates a negative sign to make it a loss function to be minimized.

### Guided Complement Entropy
$$-\frac{1}{N} \sum_{i=1}^{N} \hat{y}_{i g}^{\alpha} \sum_{j=1, j \neq g}^{K}\left(\frac{\hat{y}_{i j}}{1-\hat{y}_{i g}}\right) \log \left(\frac{\hat{y}_{i j}}{1-\hat{y}_{i g}}\right)$$

The main difference is that GCE also introduces a guiding factor of $\hat{y}_{i g}$ to modulate the effect of the complement loss factor, according to the model’s prediction quality during the training iterations

## Evaluation

## Conclusion
1. robust against several kinds of "white-box" adversarial attacks.
2. in adversarial training, substituting the GCE loss gives more robust models.
## Related work