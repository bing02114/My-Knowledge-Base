### 1.The Need for Temporal Information

>Simple tracking methods like LK can fail due to:

* Changes in apperance (noise, illumination, deformation)
* Occlusion
* Cluttered backgrounds

>The kalman filter improves tracking robustness by incorporating a dynamic model that predicts the object's state in the next frame, combining this prediction with the actual image measurement.

### 2.Core Concepts

* It is a recrusive algorithm for optimally estimating the state of a linear dynamic system with Gaussian noise
* It models uncertainty using Gaussian distribution. It fuses two uncertain estimates (prediction and measurement) to produce a new, more certain estimate
* It uses two main models:
	* System Dynamic (State) Model: Describes how the state evolves over time
	* $$x_k=Ax_{k-1}+Bu_{k-1}+noise$$
	* Measurement (Observation) : Describes how the measurement relates to the state 
	* $$z_k=Hx_k+noise$$

### 3.The Algorithm Cycle

* **Prediction**: Predict the next state and its uncertainty based on the dynamic model
* **Correction**: Use the current measurement to correct the predicted state, resulting in an updated, more accurate state estimate and uncertainty. This step uses the Kalman Gain to weight the prediction againt the measurement
