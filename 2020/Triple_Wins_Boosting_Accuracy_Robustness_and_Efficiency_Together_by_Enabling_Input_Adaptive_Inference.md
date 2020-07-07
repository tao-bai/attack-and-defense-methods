```
@inproceedings{huang2018multiscale,
author = {Huang, Gao and Chen, Danlu and Li, Tianhong and Wu, Felix and van der Maaten, Laurens and Weinberger, Kilian},
booktitle = {International Conference on Learning Representations},
title = {{Multi-Scale Dense Networks for Resource Efficient Image Classification}},
url = {https://openreview.net/forum?id=Hk2aImxAb},
year = {2018}
}
```
- We assume that the final prediction will be one chosen (NOT fused) from [ ˆy1, ..., yˆN ] via some deterministic strategy. (**Is it better than fused?**. I found answers in latter paper: The goal of this paper is to keep efficiency, so fused prediction can be better than chosen one.)

I wanted to propose a similar method like this, but I don't care about efficiency. 