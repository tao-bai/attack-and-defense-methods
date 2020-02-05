```
@inproceedings{jia2020fooling,
author = {Jia, Yunhan and Lu, Yantao and Shen, Junjie and Chen, Qi Alfred and Chen, Hao},
booktitle = {International Conference on Learning Representations},
title = {{Fooling Detection Alone is Not Enough: Adversarial Attack against Multiple Object Tracking}},
url = {https://openreview.net/forum?id=rJl31TNYPr},
year = {2020}
}
```

## Motivation
Multiple Object Tracking (MOT) is designed to be robust against errors in object detection. 
They find that a success rate of over 98% is needed for existing attack methods to actually affect the tracking results. No existing attack technique can satisfy.

They claim they are the first to study adversarial machine learning attacks considering the **complete visual perception pipeline** in autonomous driving.
## Methods
- Focus on track-by-detection pipeline.
- Generate a patch to fool the object detector with **two adversarial goals**: 
  - Erase the bounding box of target object from detection result
  - fabricate a bounding box with similar shape that is shifted a little bit towards an attacker-specified direction.
- The interesting part is the fabricated bounding box is associated with the original tracker of target object in the tracking result, which is called *hijacking of the tracker*. **The tracker hijacking gives a fake velocity towards the attacker-desired direction to the tracker and lasts for only one frame. But its adversarial effects can last tens of frames, depending on the MOT parameters $R, H$.**
- In practice, hijacking achieves a nearly 100% success rate when 3 consecutive frames are successfully attacked.
- Two critical steps
  - **Finding optimal position for adversarial bounding box.**
  - **Generating adversarial patch against object detection.**

## Insights
- Our key insight is that although it is highly difficult to directly create a tracker for fake objects or delete a tracker for existing objects, we can carefully design AEs to attack the tracking error reduction process in MOT to deviate the tracking results of existing objects a tracker for fake objects or delete a tracker for existing objects, we can carefully design AEs to attack the tracking error reduction process in MOT to deviate the tracking results of existing objects towards an attacker-desired moving direction. Such process is designed for increasing the robustness attack the tracking error reduction process in MOT to deviate the tracking results of existing objects towards an attacker-desired moving direction. 
