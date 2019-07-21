"""
FGSM

resource: https://pytorch.org/tutorials/beginner/fgsm_tutorial.html

INPUTS:
- epsilons - List of epsilon values to use for the run. It is important to keep 0 in the list because it represents the model performance on the original test set. Also, intuitively we would expect the larger the epsilon, the more noticeable the perturbations but the more effective the attack in terms of degrading model accuracy. Since the data range here is [0,1], no epsilon value should exceed 1.
- pretrained_model - path to the pretrained MNIST model which was trained with pytorch/examples/mnist. For simplicity, download the pretrained model here.
- USE_CUDA - boolean flag to use CUDA if desired and available. Note, a GPU with CUDA is not critical for this tutorial as a CPU will not take much time.
"""
from __future__ import print_function
import torch 
import torch.nn as nn
import torch.nn.functional as F 
import torch.optim as optim
from torchvision import datasets, transforms            
import numpy as np 
import matplotlib.pyplot as plt 

epsilons = [0, .05, .1, .15, .2, .25, .3]
pretrained_model = "./pretrained/lenet_mnist_model.pth"
USE_CUDA=True

# model under attack
## LeNet Model definition
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5)
        self.conv2_drop = nn.Dropout2d()
        self.fc1 = nn.Linear(320, 50)
        self.fc2 = nn.Linear(50, 10)

    def forward(self, x):
        x = F.relu(F.max_pool2d(self.conv1(x), 2))
        x = F.relu(F.max_pool2d(self.conv2_drop(self.conv2(x)), 2))
        x = x.view(-1, 320)
        x = F.relu(self.fc1(x))
        x = F.dropout(x, training=self.training)
        x = self.fc2(x)
        return F.log_softmax(x, dim=1)

# MNIST Test dataset and dataloader declaration
test_loader = torch.utils.data.DataLoader(
    datasets.MNIST('../data', train=False, download=True, transform=transforms.Compose([
            transforms.ToTensor(),
            ])),
        batch_size=1, shuffle=True)

# Define what device we are using
print('CUDA available:', torch.cuda.is_available())
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

# initialize the network
model = Net().to(device)

# load the pretrained model
model.load_state_dict(torch.load(pretrained_model, map_location='cpu'))

# set the model in evaluation mode. In this case this for the dropout layers
model.eval()

# FGSM attack code
def fgsm_attack(image, epsilon, data_grad):
    # collect the element-wise sign of the data gradient
    sign_data_grad = data_grad.sign()
    # create teh perturbed image by adjusting each pixel of the input image
    perturbed_image = image +  epsilon*sign_data_grad
    # adding clipping to maintain [0,1] range
    perturbed_image = torch.clamp(perturbed_image, 0, 1)
    # return the perturbed image
    return perturbed_image


def test(model, device, test_loader, epsilon):
    # accuracy counter
    correct = 0
    adv_examples = []

    # loop over all examples in test set
    for data, target in test_loader:
        # Send the data and label to the device
        data, target = data.to(device), target.to(device)

        # set requires_grad attribute of tensor. Important for attack.
        data.requires_grad = True

        # Forwardd pass the data through the model
        output = model(data)
        init_pred = output.max(1, keepdim=True)[1] # get the index of the max log-probability
        
        # if the initial prediction is wrong, dont bother attacking just move on
        if init_pred.item() != target.item():
            continue
        
        # calculate the loss
        loss = F.nll_loss(output, target)

        # zero all existing gradients
        model.zero_grad()

        # calcualte gradients of the model in backword pass
        loss.backward()

        # collect datagrad
        data_grad = data.grad.data

        # call FGSM attack
        perturbed_data = fgsm_attack(data, epsilon, data_grad)

        # re-classify the perturbed image
        output = model(perturbed_data)

        # check for success
        final_pred = output.max(1, keepdim=True)[1]
        if final_pred.item() == target.item():
            correct += 1
            # special case for saving 0 epsilon examples
            if (epsilon==0) and (len(adv_examples)<5):
                adv_ex = perturbed_data.squeeze().detach().cpu().numpy()
                adv_examples.append((init_pred.item(), final_pred.item(), adv_ex))

        else:
            # save some adv examples for visualization  later
            if len(adv_examples) < 5:
                adv_ex = perturbed_data.squeeze().detach().cpu().numpy()
                adv_examples.append( (init_pred.item(), final_pred.item(), adv_ex))

    # Calculate final accuracy for this epsilon
    final_acc = correct/float(len(test_loader))
    print("Epsilon: {}\tTest Accuracy = {} / {} = {}".format(epsilon, correct, len(test_loader), final_acc))

    # Return the accuracy and an adversarial example
    return final_acc, adv_examples

accuracies = []
examples = []

# Run test for each epsilon
for eps in epsilons:
    acc, ex = test(model, device, test_loader, eps)
    accuracies.append(acc)
    examples.append(ex)

plt.figure(figsize=(5,5))
plt.plot(epsilons, accuracies, "*-")
plt.yticks(np.arange(0, 1.1, step=0.1))
plt.xticks(np.arange(0, .35, step=0.05))
plt.title("Accuracy vs Epsilon")
plt.xlabel("Epsilon")
plt.ylabel("Accuracy")
plt.show()