### 1.**Confusion Matrix:** The foundation for most classification metrics.

|                  | Predicted: Positive | Predicted: Negative |
| ---------------- | ------------------- | ------------------- |
| Actual: Positive | TP                  | FN                  |
| Actual: Negative | FP                  | TN                  |

### 2.Error Rate & Accuracy

**Accuracy**

>Accuracy is the most intuitive metric. It measures the proportion of total predictions that were correct
>
>$$Accuracy = \frac{(TP+TN)}{(TP+TN+FP+FN)}$$
>**Note**: <font color="Red">Accuracy can be very misleading on imbalanced datasets. For example, if 99% of samples are negative, a model that always predicts "negative" will have 99% accuracy but is completely useless.</font>

**Error Rate**

>**Error Rate** is the opposite of accuracy. It measures the proportion of total predictions that were incorrect.
>
>$$ErrorRate = \frac{(FP+FN)}{(TP+TN+FP+FN)}$$


### 3.Precision, Recall & F1-Score

**Precision**

>Precision, also known as Positive Predictive Value.
>
>**Of all the samples we predicted as positive, how many were actually positive**
>
>$$Precision=\frac{TP}{TP+FP}$$

**Recall**

>**Of all the actual positive samples, how many did we correctly identify**
>
>$$Recall=\frac{TP}{TP+FN}$$

**F1-Score**

>**F1-Score** is the harmonic mean of Precision and Recall. It provides a single metric that balances both. It is particularly useful when you need a balance between finding all positives (recall) and not making too many false alarms (precision).
>
>$$F1=\frac{Precision*Recall}{Precision+Recall}$$


### 4.ROC & AUC

**ROC**

>The **ROC (Receiver Operating Characteristic) Curve** is a graph that shows the performance of a classification model at all classification thresholds. It plots the **True Positive Rate (TPR)** against the **False Positive Rate (FPR)**.
>
>$$TPR=\frac{TP}{TP+FN}$$
>
>$$FPR=\frac{FP}{TN+FP}$$
>
>Note: <font color="red">An ideal ROC curve hugs the top-left corner, which represents a high TPR and a low FPR. A curve along the diagonal line (y=x) represents a model with no discriminative power (equivalent to random guessing).</font>

**AUC**

>The **AUC (Area Under the Curve)** represents the area under the ROC curve. It provides a single number to summarize the model's performance across all thresholds.
>
><font color="red">The AUC value ranges from 0 to 1. An AUC of 1.0 represents a perfect classifier, while an AUC of 0.5 represents a model that is no better than random guessing.</font>

