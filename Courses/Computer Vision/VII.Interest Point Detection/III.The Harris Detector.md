### 1.Mathematical Formulation

>The Harris detector measures the change in intensity that results from shifting a window in different directions

1. The change of intensity for a shift [u,v] is given by the Sum of Squared Differences (SSD)

$$E(u,v)=\sum_{x,y\in W}(I(x+u,y+v)-I(x,y))^{2}$$

2. Using a Taylor expansion, this can be approximated and expressed in matrix form

$$E(u,v)≈[u,v]M\left[\begin{matrix}u\\v\end{matrix}\right]$$

3. Where M is a 2x2 matrix computed from image derivatives

$$M=\sum_{x,y\in W}
\left[
\begin{matrix} 
I_{x}^{2} & I_{x}I_{y} \\ I_{x}I_{y} & I_{y}^{2}
\end{matrix}
\right]$$

**M is a real symmetric matrix, so M can be decomposed as:**

$$M=PΛP^{T}$$

where,
* P : each column is an eigenvector
* Λ: diagonal matrix with eigenvalues
* PT: each row is an eigenvector
### 2.Interpreting the Eigenvalues of M

**Uniform Region**: Both λ1 and λ2 are small
**Edge**: One eigenvalue is large, and the other is small
**Cornor**: Both λ1 and λ2 are large

### 3.Harria Response Function

$$R=det(M)-k(trace(M))^{2}$$

where 
* det(M)=λ1λ2
* trace(M)=λ1+λ2
* $k\in[0.04,0,06]$ 
