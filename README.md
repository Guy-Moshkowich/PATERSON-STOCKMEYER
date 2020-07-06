# PATERSON-STOCKMEYER
This is an implementation for evaluating a polynomial for a certain x value with nonscalar complexity of
<img src="https://latex.codecogs.com/gif.latex?\sqrt{n}&space;&plus;&space;O(log\&space;n)" title="\sqrt{n} + O(log\ n)" />
using the Paterson-Stockmeyer algorithms.

## The main idea
Let p(x) be a monic polynomails of degree k(2p-1).
We present p(x) as a sum of two monic polynomials of degree k(p-1) and use precomputed powers of x: 


Calculate q(x) and r(x) by dividing p(x) by <img src="https://latex.codecogs.com/gif.latex?x^{kp}" title="x^{kp}" />,

<img src="https://latex.codecogs.com/gif.latex?p(x)&space;=&space;q(x)&space;\cdot&space;x^{kp}&space;&plus;&space;r(x)" title="p(x) = q(x) \cdot x^{kp} + r(x)" />
, where deg(q)=k(p-1) and deg(r)<=kp-1.


Calculte c(x) and s(x) by dividing 
<img src="https://latex.codecogs.com/gif.latex?r(x)-x^{k(p-1)}" title="r(x)-x^{k(p-1)}" />,
by q(x)

<img src="https://latex.codecogs.com/gif.latex?r(x)-x^{k(p-1)}=c(x)q(x)&space;&plus;&space;s(x),&space;\\&space;\text{where}&space;\text{\&space;deg}(c)\le&space;k-1&space;\text{\&space;and&space;deg}(s)\le&space;k(p-1)-1" title="r(x)-x^{k(p-1)}=c(x)q(x) + s(x), \\ \text{where} \text{\ deg}(c)\le k-1 \text{\ and deg}(s)\le k(p-1)-1" />

Then, 

<img src="https://latex.codecogs.com/gif.latex?p(x)&space;=&space;\left&space;\{&space;\big(x^{kp}&plus;c(x)\big)q(x)\right&space;\}&space;&plus;\left&space;\{&space;x^{k(p-1)}&space;&plus;&space;s(x)\right&space;\}" title="p(x) = \left \{ \big(x^{kp}+c(x)\big)q(x)\right \} +\left \{ x^{k(p-1)} + s(x)\right \}" />


## Algorithm 


The algorithm is based on the following papers:
1) [On The Number Of Nonscalar Multiplications Necessary To Evaluate Polynomials](https://www.researchgate.net/profile/Mike_Paterson3/publication/220617048_On_the_Number_of_Nonscalar_Multiplications_Necessary_to_Evaluate_Polynomials/links/5630d22408aef3349c29f8c1.pdf)
2) [Improved Bootstrapping for Approximate Homomorphic Encryption](https://eprint.iacr.org/2018/1043.pdf)

<img src="https://latex.codecogs.com/gif.latex?x^2&plus;2x&plus;1" title="x^2+2x+1" />

Note: you need to install [SymPy](https://www.sympy.org/en/index.html) in order to run the unit tests.
