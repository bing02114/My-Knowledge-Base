### 1.Motivation

>Since the attribute conditional independence assumption is often too strong for real-world tasks, semi-naïve Bayes classifiers relax this assumption by considering dependencies among some attributes

### 2.One-Dependent Estimator (ODE)

>A common strategy that assumes each attribute depends on at most one other attribute besides the class

### 3.Examples of ODEs

**SPODE (Super-Parent ODE)**: Assumes all attributes depend on a single common "super-parent" attribute.

**TAN (Tree-Augmented Naïve Bayes)**: Uses a maximum weighted spanning tree to model dependencies, effectively retaining only the dependencies between strongly correlated attributes.

**AODE (Averaged One-Dependent Estimator)**: An ensemble method that averages all valid SPODEs, where each attribute acts as the super-parent

