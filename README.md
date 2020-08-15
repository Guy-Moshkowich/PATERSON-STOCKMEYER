
[Summary of the paper [1]](https://docs.google.com/document/d/1r4JoMK0-2MnjHo-drYb7QsJlx5ewTTvStPfr2cZl1oM/edit?usp=sharing)


# PATERSON-STOCKMEYER
This is an implementation for evaluating a polynomial at a certain x value with nonscalar complexity of
<img src="https://latex.codecogs.com/gif.latex?\sqrt{n}&space;&plus;&space;O(log\&space;n)" title="\sqrt{n} + O(log\ n)" />
using the Paterson-Stockmeyer algorithms.

## The main idea
Let p(x) be a monic polynomials of degree k(2p-1) where p is a 2-power.

We write p(x) as a sum of two monic polynomials of degree k(p-1) and use precomputed powers: 
<img src="https://latex.codecogs.com/gif.latex?x^2,x^3,\dots,x^k&space;\text{\&space;and&space;}&space;x^{2k},x^{4k},\dots,x^{pk}" title="x^2,x^3,\dots,x^k \text{\ and } x^{2k},x^{4k},\dots,x^{2^{m-1}k}" />.

Calculate q(x) and r(x) by dividing p(x) by <img src="https://latex.codecogs.com/gif.latex?x^{kp}" title="x^{kp}" />,

<img src="https://latex.codecogs.com/gif.latex?p(x)&space;=&space;q(x)&space;\cdot&space;x^{kp}&space;&plus;&space;r(x)" title="p(x) = q(x) \cdot x^{kp} + r(x)" />
, where deg(q)=k(p-1) and deg(r)<=kp-1.


Calculate c(x) and s(x) by dividing 
<img src="https://latex.codecogs.com/gif.latex?r(x)-x^{k(p-1)}" title="r(x)-x^{k(p-1)}" />,
by q(x)

<img src="https://latex.codecogs.com/gif.latex?r(x)-x^{k(p-1)}=c(x)q(x)&space;&plus;&space;s(x),&space;\\&space;\text{where}&space;\text{\&space;deg}(c)\le&space;k-1&space;\text{\&space;and&space;deg}(s)\le&space;k(p-1)-1" title="r(x)-x^{k(p-1)}=c(x)q(x) + s(x), \\ \text{where} \text{\ deg}(c)\le k-1 \text{\ and deg}(s)\le k(p-1)-1" />

Then, 

<img src="https://latex.codecogs.com/gif.latex?p(x)&space;=&space;\left&space;\{&space;\big(x^{kp}&plus;c(x)\big)q(x)\right&space;\}&space;&plus;\left&space;\{&space;x^{k(p-1)}&space;&plus;&space;s(x)\right&space;\}" title="p(x) = \left \{ \big(x^{kp}+c(x)\big)q(x)\right \} +\left \{ x^{k(p-1)} + s(x)\right \}" />

The degree of the two polynomials in the curly brackets have degree of k(p-1) i.e.,  p(x) is presented as a sum of two monic polynomials of degree k(p-1).

Using the precomputed powers, we can evaluate  
<img src="https://latex.codecogs.com/gif.latex?x^{kp}&plus;c(x)" title="x^{kp}+c(x)" />
for specific x value with zero nonscalar multiplication and so we can compute p(x) using recursion on the two polynomials with degree k(p-1).

In order to evaluate a general polynomial f(x) at u, we calculate 
<img src="https://latex.codecogs.com/gif.latex?f^{\prime}&space;=&space;f&space;&plus;&space;x^{k(2p-1)}" title="f^{\prime} = f + x^{k(2p-1)}" />
which is has degree k(2p-1) for 
<img src="https://latex.codecogs.com/gif.latex?n=\deg(f)" title="n=\text{deg}(f)}" /> was precomputed.
<img src="https://latex.codecogs.com/gif.latex?k\approx\sqrt{n/2}" title="k\approx\sqrt{n/2}" />
and 
<img src="https://latex.codecogs.com/gif.latex?p&space;=&space;2^{\left&space;\lceil&space;\log_2\big((n/k)&space;&plus;&space;1\big)\right&space;\rceil}" title="p = 2^{\left \lceil \log_2\big(n/k) + 1\big)\right \rceil}" />

Then, calculate 
<img src="https://latex.codecogs.com/gif.latex?f^{\prime}(u)" title="f^{\prime}(u)" />
using recursion as explained above.

Finally, we have
<img src="https://latex.codecogs.com/gif.latex?f(u)&space;=f^{\prime}(u)&space;-&space;u^{k(2p-1)}" title="f(u) =f^{\prime}(u) - u^{k(2p-1)}" /> 
where 
<img src="https://latex.codecogs.com/gif.latex?u^{k(2p-1)}" title="u^{k(2p-1)}" /> was precomputed.






 
## The algorithm is based on the following papers
[1] [On The Number Of Nonscalar Multiplications Necessary To Evaluate Polynomials](https://www.researchgate.net/profile/Mike_Paterson3/publication/220617048_On_the_Number_of_Nonscalar_Multiplications_Necessary_to_Evaluate_Polynomials/links/5630d22408aef3349c29f8c1.pdf)
[2] [Improved Bootstrapping for Approximate Homomorphic Encryption](https://eprint.iacr.org/2018/1043.pdf)

Note: you need to install [SymPy](https://www.sympy.org/en/index.html) in order to run the unit tests.


