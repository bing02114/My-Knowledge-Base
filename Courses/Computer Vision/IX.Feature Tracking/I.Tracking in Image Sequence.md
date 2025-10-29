### 1.Key Assumptions

>Feature tracking algorithms are built on several key assumptions about the video sequence

* **Brightness Constancy** : The intensity of a specific point on ann object remains the same across consecutive frames. This is the most fundamental assumption

$$I(x+\Delta x,y+\Delta y,t+\Delta t)=I(x,y,t)$$

* **Temporal Persistence** : The motion of features between consecutive frames is small, and the camera's position changes slowly
* **Spatial Coherence** : Neighboring points on the same physical surface belong to the same object and thus have similar motion


### 2.The Brightness Constancy Constraint

>Using a Taylor series expansion on the brightness constancy equation, we get the optical flow constraint equation


$$I_x u+I_y v + I_t=0$$

where

* Ix, Iy: Gradient of the image intensity in the x and y directions
* Iit: Gradient of the image intensity with respect to time (the difference between frames)
* (u,v): The displacement vector (optical flow) we want to find

>This equation has one equation with two unknowns, so it cannot be solved for a single pixel

