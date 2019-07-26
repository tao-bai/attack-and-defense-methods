```
@inproceedings{carlini2017towards,
author = {Carlini, Nicholas and Wagner, David},
booktitle = {2017 IEEE Symposium on Security and Privacy (SP)},
organization = {IEEE},
pages = {39--57},
title = {{Towards evaluating the robustness of neural networks}},
year = {2017}
}
```

## Summary
C&W could be the benchmark of adversarial attacks. In this paper, their targeted model is distilled model, which was the SOTA defense at that time.

In this paper, they proposed three metrics to evaluate the distance between adversarial examples and original images.

This is optimization based method the problem is formulated as:
$$
\begin{array}{cl}{{\operatorname{minimize}}} & {\mathcal{D}(x, x+\delta)} \\ {\text { such that }} & {C(x+\delta)=t} \\ {} & {x+\delta \in[0,1]^{n}}\end{array}
$$

But it is difficult to solve it directly, the objective function $f$ is defined such that $C(x+\delta)=t$ iff $f(x+\delta) \leq 0$. The possible choices of f:
$$
\begin{aligned} f_{1}\left(x^{\prime}\right) &=-\operatorname{loss}_{F, t}\left(x^{\prime}\right)+1 \\ f_{2}\left(x^{\prime}\right) &=\left(\max _{i \neq t}\left(F\left(x^{\prime}\right)_{i}\right)-F\left(x^{\prime}\right)_{t}\right)^{+} \\ f_{3}\left(x^{\prime}\right) &=\operatorname{softplus}\left(\max _{i \neq t}\left(F\left(x^{\prime}\right)_{i}\right)-F\left(x^{\prime}\right)_{t}\right)-\log (2) \\ f_{4}\left(x^{\prime}\right) &=\left(0.5-F\left(x^{\prime}\right)_{t}\right)^{+} \\ f_{5}\left(x^{\prime}\right) &=-\log \left(2 F\left(x^{\prime}\right)_{t}-2\right) \\ f_{6}\left(x^{\prime}\right) &=\left(\max _{i \neq t}\left(Z\left(x^{\prime}\right)_{t}\right)-Z\left(x^{\prime}\right)_{t}\right)^{+} \\ f_{7}\left(x^{\prime}\right) &=\operatorname{softplus}\left(\max _{i \neq t}\left(Z\left(x^{\prime}\right)_{i}\right)-Z\left(x^{\prime}\right)_{t}\right)-\log (2) \end{aligned}
$$
where $s$ is the correct classification, $(e)^+ = \max(e,0)$, $\operatorname{softplus}(x)=\log (1+\exp (x))$ and $loss_{F,s}(x)$ is the cross entropy loss for $x$.

Then the new objective function is 
$$
\begin{array}{ll}{\text { minimize }} & {\mathcal{D}(x, x+\delta)} \\ {\text { such that }} & {f(x+\delta) \leq 0} \\ {} & {x+\delta \in[0,1]^{n}}\end{array}
$$
and rewritten as 
$$
\begin{array}{ll}{\operatorname{minimize}} & {\mathcal{D}(x, x+\delta)+c \cdot f(x+\delta)} \\ {\text { such that }} & {x+\delta \in[0,1]^{n}}\end{array}
$$

$c$ is a constant and often the best way to choose
$c$ is to use the smallest value of c for which the resulting solution $x∗$ has $f(x∗) ≤ 0$. This causes gradient descent to minimize both of the terms simultaneously instead of picking only one to optimize over first.

To ensure the modification yields a valid image, there is a box constraints on $\epsilon$.
$$
0 \leq x_{i}+\delta_{i} \leq 1
$$
Projected gradient descent and Clipped gradient descent have different drawbacks. So they adapted another way: **Change of variables**.
$$
\delta_{i}=\frac{1}{2}\left(\tanh \left(w_{i}\right)+1\right)-x_{i}
$$
Since $-1 \leq \tanh \left(w_{i}\right) \leq 1$, it follows that $0 \leq x_{i}+\delta_{i} \leq 1$.

The authors also disscussed the problems of how to choose $f$ and discretization.

The $L_2$ Attack:
$$
\left\|\frac{1}{2}(\tanh (w)+1)-x\right\|_{2}^{2}+c \cdot f\left(\frac{1}{2}(\tanh (w)+1)\right).
$$
$$
f\left(x^{\prime}\right)=\max \left(\max \left\{Z\left(x^{\prime}\right)_{i} : i \neq t\right\}-Z\left(x^{\prime}\right)_{t},-\kappa\right)
$$