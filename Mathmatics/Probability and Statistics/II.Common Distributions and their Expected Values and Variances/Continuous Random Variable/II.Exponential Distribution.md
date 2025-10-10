### I.Definition

>The Exponential distribution is a continuous probability distribution that is used to model the time we must wait until a certain event occurs. It is closely related to the Poisson process, where it describes the time for the next event to occur.
>
><font color="red">In simple terms, it answers the question: "How long do I have to wait for sth to happen"</font>


### II.Key Characteristics and the Formula

**Parameter**

>Rate parameter: **λ** This is the average number of events that occur per unit of time. A higher λ means events happen more frequently, and the waiting time is shorter.

**Probability Density Function (PDF)**

>$$f(t;\lambda)=\lambda e^{-\lambda t}$$

**Cumulative Distribution Funciton (CDF)**

>$$F(t;\lambda)=P(T ≤ t)=1-e^{-\lambda t}$$

### III.Mean and Variance

**Mean**

$$E(T)=\frac{1}{\lambda}$$

**Variance**

$$D(T)=\frac{1}{\lambda^2}$$

### IV.Properties

**The Memoryless Property**

>The **memoryless property** states that the probability of an event occurring in the future is independent of how much time has already passed. In other words, the process "forgets" what has happened in the past.


### V.Relationship to Poisson Process

>The time between consecutive events
>
>How long until the next event