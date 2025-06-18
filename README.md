# Fundamental Research in Machine and Deep Learning : Contol Dataset

## Problem Statement
Convolutional Neural Networks (CNNs) are widely used for image recognition tasks due to their ability to detect patterns regardless of their position in the image. This property is known as translation equivariance.

To generalize equivariance beyond translations, Cohen and Welling introduced Group Convolutional Neural Networks (Group CNNs), which incorporate transformations such as rotations directly into convolutional layers. These models aim to achieve equivariance to a broader set of transformations, leading to better generalization.

Standard Group CNNs treat all transformations equally, regardless of their relevance to the task. Romero et al. propose extending Group CNNs with an attention mechanism over the transformation group. By weighting transformations based on importance, these models better capture which transformations matter.

The target property this controlled experiment aims to verify is the equivariance of Attentive Group CNNs. The model should learn to respond differently to transformations that affect the class label, while ignoring those that do not.
