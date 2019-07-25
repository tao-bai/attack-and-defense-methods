```
@inproceedings{papernot2016limitations,
author = {Papernot, Nicolas and McDaniel, Patrick and Jha, Somesh and Fredrikson, Matt and Celik, Z Berkay and Swami, Ananthram},
booktitle = {2016 IEEE European Symposium on Security and Privacy (EuroS{\&}P)},
file = {:F$\backslash$:/Google Drive/{\#}BAI TAO{\#} Adversarial ML/Mendeley/2016 - The limitations of deep learning in adversarial settings.pdf:pdf},
organization = {IEEE},
pages = {372--387},
title = {{The limitations of deep learning in adversarial settings}},
year = {2016}
}
```
## Summary
This paper proposed a method to craft adversarial examples by constructing a mapping from input perturbations to output variation, which is different from other methods that using output variations to find corresponding input perturbations. Their method needs the architechture, activation function and parameters of DNNs. And the problem is formulated as
$$
\arg \min _{\delta_{\mathbf{X}}}\left\|\delta_{\mathbf{X}}\right\| \text { s.t. } \mathbf{F}(\mathbf{X}+\delta \mathbf{x})=\mathbf{Y}^{*}
$$
$\mathbf{X},\mathbf{Y}, \mathbf{Y}^{*}, \delta_{\mathbf{X}}, \mathbf{F}$ are input, label, target label, purturbations and the NN respectively.

The authors defined the Jacobian matrix of the function $\mathbf{F}$ as *forward derivative*, which is shown as follows:
$$
\nabla \mathbf{F}(\mathbf{X})=\frac{\partial \mathbf{F}(\mathbf{X})}{\partial \mathbf{X}}=\left[\frac{\partial \mathbf{F}_{j}(\mathbf{X})}{\partial x_{i}}\right]_{i \in 1 \ldots M, j \in 1 \ldots N}
$$
This forward derivative is similar to that in backpropagation, but forward derivative is the derivative of the networks rather than cost functions and it is w.r.t. the input features rather than the networks parameters.

With the chain rule, forward derivative is rewritten as 
$$
\begin{aligned} \frac{\partial \mathbf{F}_{j}(\mathbf{X})}{\partial x_{i}}=&\left(\mathbf{W}_{n+1, j} \cdot \frac{\partial \mathbf{H}_{n}}{\partial x_{i}}\right) \times \\ & \frac{\partial f_{n+1, j}}{\partial x_{i}}\left(\mathbf{W}_{n+1, j} \cdot \mathbf{H}_{n}+b_{n+1, j}\right) \end{aligned}
$$
$$
\frac{\partial \mathbf{H}_{k}(\mathbf{X})}{\partial x_{i}}=\left[\frac{\partial f_{k, p}\left(\mathbf{W}_{k, p} \cdot \mathbf{H}_{k-1}+b_{k, p}\right)}{\partial x_{i}}\right]_{p \in 1 \ldots m_{k}}
$$
where $\mathbf{H}_{k}$ is the output vector of hidden layer $k$ and $f_{k,j}$ is the activation function of output neuron $j$ in layer $k$.

The $adversarial saliency map$ is constructed with 
$$
S(\mathbf{X}, t)[i]=\left\{\begin{array}{l}{0 \text { if } \frac{\partial \mathbf{F}_{t}(\mathbf{X})}{\partial \mathbf{X}_{i}}<0 \text { or } \sum_{j \neq t} \frac{\partial \mathbf{F}_{j}(\mathbf{X})}{\partial \mathbf{X}_{i}}>0} \\ {\left(\frac{\partial \mathbf{F}_{t}(\mathbf{X})}{\partial \mathbf{X}_{i}}\right)\left|\sum_{j \neq t} \frac{\partial \mathbf{F}_{j}(\mathbf{X})}{\partial \mathbf{X}_{i}}\right| \text { otherwise }}\end{array}\right.
$$
where $t$ is the target class.

**Large absolute values correspond to features with a significant impact on the output when perturbed.**

**The authors said their method is appliable to unsupervised-trained DNNs too, but it is a future work.**