### 1.Definition

>Also known as a "belief network," it uses a Directed Acyclic Graph (DAG) to represent dependencies among attributes and uses Conditional Probability Tables (CPTs) to describe the joint probability distribution

### 2.Structure and Inference

**Structure**: A Bayesian network effectively expresses conditional independence among attributes. Given its parent nodes, each attribute is conditionally independent of its non-descendant attributes

**Inference**: Using observed variable values to infer the values of other variables is called inference. Exact inference is NP-hard. Approximate inference methods, like Gibbs sampling, are commonly used