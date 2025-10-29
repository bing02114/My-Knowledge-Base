### 1.Purpose

>The EKF is an extension of the Kalman filter for **non-linear** system or measurement models, which are common in real-world vision applications.

### 2.Method

>It approximates the non-linear behavior by performing a **local linearization** of the system and measurement functions around the last state estimate. This is done using **Jacobian matrices**

### 3.Model

>The models are now non-linear functions:

### 4.Cycle

>The Prediction-Correction cycle is the same as the standard KF, but it uses the non-linear functions `f` and `h` and their Jacobians for the updates