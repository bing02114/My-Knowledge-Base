### 1.Separating Hyperplane

>In a sample space, a separating hyperplane can be described by the linear equation $w^{T}x+b=0$, where w is the normal vector that determins the directions of the hyperplane, and b is the displacement term that determines its distance

For any point x in the sample sapce, the distance to hyperplane (w,b) is:

$$r=\frac{|w^{T}x+b|}{||w||}$$
### 2.Margin

>Intuitively, the separating hyperplane should be the one in the "middle" of the two classes, because this hyperplane has the best "tolerance" for local perturbations of the training data. The distance between the separating planes for the two different classes is called the margin

$$\gamma = \frac{2}{||w||}$$
### 3.Support Vectors

>The training samples closest to the separating hyperplane are called "support vectors". These are the samples that make the equality hold in the constraint $y_{i}(w^{T}x_{i}+b)\geq 1$ 

### 4.Basic Form of SVM

>The goal is to find the separating hyperplane with the "maximum margin". This is equivalent to minimizing $\frac{1}{2}||w||^{2}$ subject to the constraint $y_{i}(w^{T}x_{i}+b) \geq 1$. This is the basic model of a Support Vector Machine (SVM)


