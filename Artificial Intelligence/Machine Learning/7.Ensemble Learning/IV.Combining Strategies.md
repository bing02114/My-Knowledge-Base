### 1.Average

* Simple Averaging
* Weighted Averaging

### 2.Voting

* **Plurality Voting:**  Predicts the class that receives the most votes.
* **Majority Voting:** Predicts the class only if it receives more than half of the votes; otherwise, it rejects the prediction
* **Weighted Voting:** Each vote is weighted by the individual learner's weight.
* **Hard vs. Soft Voting:** Hard voting" is based on class labels. "Soft voting" is based on class probabilities, which often performs better.

### 3.Stacking

>A more powerful strategy where another learner, called a "meta-learner" or "secondary learner," is used to combine the outputs of the "primary learners"

* Process

>The outputs of the primary learners on a dataset are used as the input features to train the meta-learner. The original labels are used as the labels for this new dataset. To prevent overfitting, cross-validation is typically used to generate the training data for the meta-learner.