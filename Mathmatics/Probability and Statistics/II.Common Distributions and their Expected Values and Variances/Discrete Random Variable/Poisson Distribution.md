### I.Definition

>The Poisson distribution is a discrete probability distribution that expresses the probability of a **given number of events occurring in a fixed interval of time or space** if these events occur with a known constant mean rate and independently of the time since the last event.
>
><font color="red">In simpler terms, it's used to model the number of times an event happens over a specified period</font>


### II.Key Characteristics and Assumptions

**Events are independent**

>The occurrence of one event does not affect the probability of another event occurring.

**Constant Mean Rate (λ)**

>Events occur at a known constant mean rate. This rate, denoted by λ (lambda), is the average number of events in the given interval.

**Events are rare**

>The probability of an event occurring in a very small interval is proportional to the length of the interval and is very small. Two events cannot occur at the exact same instant.


### III.The Formula

$$P(X=k)=\frac{\lambda^{k}e^{-\lambda}}{k!}$$
where:
- k is the number of occurances of the event
- Lambda（λ）is the average number of events per interval
- e is Euler's number ≈ 2.71828
- k! is the factorial of k

### IV.Mean and Variance

Expected Value (Mean): $$E(X)=\lambda$$
Variance:
$$D(X)=\lambda$$

### V.Properties

**Additive Property**

>If you have two independent random variables that both follow a Poisson distribution, their sum also follows a Poisson distribution.

### VI.Relationship to Poisson Process

>The **count** of events in a fixed interval.
>
>**How many** events in an interval?
