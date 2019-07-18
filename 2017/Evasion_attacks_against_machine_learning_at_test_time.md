```
@inproceedings{biggio2013evasion,
  title={Evasion attacks against machine learning at test time},
  author={Biggio, Battista and Corona, Igino and Maiorca, Davide and Nelson, Blaine and {\v{S}}rndi{\'c}, Nedim and Laskov, Pavel and Giacinto, Giorgio and Roli, Fabio},
  booktitle={Joint European conference on machine learning and knowledge discovery in databases},
  pages={387--402},
  year={2013},
  organization={Springer}
}
```
## Summary
The authors presented a gradient-decent based appproach to attack the target model. The attack strategy is 
$$
\begin{aligned} \mathbf{x}^{*}=\underset{\mathbf{x}}{\arg \min } & \hat{g}(\mathbf{x}) \\ \text { s.t. } & d\left(\mathbf{x}, \mathbf{x}^{0}\right) \leq d_{\max } \end{aligned}
\tag{1}
$$
$\hat{g}(x)$ is the estimated targeted model and $x^0$ is the targeted example.

This strategy is particularly susceptible to failure because $\hat{g}(x)$ may be non-convex and descent appproaches may not achieve a global optima. As shown in Figure 1(1st row), not all points switched to blue area.

The discriminant function does not incorporate the evidence we have about the data distribution, p(x), and thus, using gradient descent to optimize Eq. $1$ may lead into unsupported regions $(p(x) ≈ 0)$.

Then an additional component is introduced, the objective is below:
$$
\begin{array}{c}{\arg \min _{x} F(\mathbf{x})=\hat{g}(\mathbf{x})-\frac{\lambda}{n} \sum_{i | y_{i}^{c}=-1} k\left(\frac{\mathbf{x}-\mathbf{x}_{i}}{h}\right)} \\ {\text { s.t. } d\left(\mathbf{x}, \mathbf{x}^{0}\right) \leq d_{\max }}\end{array}
$$
where h is a bandwidth parameter for a kernel density estimator (KDE), and n is the number of benign samples (yc = −1) available to the adversary.

The added component estimates $p(x|y^c = −1)$ using a density estimator. This term acts as a penalizer for x in low density regions and is weighted by a parameter λ ≥ 0.
In doing so, it reshapes the objective function and thereby biases the resulting gradient descent towards regions where the negative class is concentrated.

_I do not understand the relationship between the component and $p(x|y^c = −1)$._

