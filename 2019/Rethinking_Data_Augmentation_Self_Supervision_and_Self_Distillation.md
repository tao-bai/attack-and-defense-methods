```
@article{lee2019rethinking,
  title={Rethinking Data Augmentation: Self-Supervision and Self-Distillation},
  author={Lee, Hankook and Hwang, Sung Ju and Shin, Jinwoo},
  journal={arXiv preprint arXiv:1910.05872},
  year={2019}
}
```
## Motivation
In the supervised setting, a common practice for data augmentation is to assign
the same label to all augmented samples of the same source. However, if the
augmentation results in large distributional discrepancy among them (e.g., rotations), forcing their label invariance may be too difficult to solve and often hurts
the performance.

## Methods
The key idea is to remove teh unnecessary invariant property of the classifier. To this end, they use a joint softmax classifier which represents the joint probability.

- aggregated inference. Since the transformation is known, they predict a lable using the conditional probability.
- self-distillation from aggregation. 