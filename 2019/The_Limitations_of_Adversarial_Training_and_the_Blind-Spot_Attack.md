```
@inproceedings{zhang2018the,
author = {Zhang, Huan and Chen, Hongge and Song, Zhao and Boning, Duane and Inderjit dhillon and Hsieh, Cho-Jui},
booktitle = {7th International Conference on Learning Representations, {\{}ICLR{\}} 2019, New Orleans, LA, USA, May 6-9, 2019},
title = {{The Limitations of Adversarial Training and the Blind-Spot Attack}},
url = {https://openreview.net/forum?id=HylTBhA5tQ},
year = {2019}
}
```
This paper proposed a simple method to attack models with adversarial training. 

The authors claimed that there are blind spots that adversarial training could not cover. The distance between the test points and training data contributes to the attack. The attack success rate increases when the distance gets large. And the attack just be conducted by this formula:
$$
x^{\prime}=\alpha x+\beta, \text { s.t. } x^{\prime} \in[-0.5,0.5]^{d}
$$