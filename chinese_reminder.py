import numpy

def gcdExtended(a, b):
    # Base Case
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = gcdExtended(b % a, a)

    # Update x and y using results of recursive
    # call
    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y


# Driver code
# a, b = 35, 15
# g, x, y = gcdExtended(a, b)
# print("gcd(", a, ",", b, ") = ", g)
# print(x, '*' , a, ' + ', y, '*', b,' = ', g)

n = [2, 5, 7, 13, 17]
N_prod = numpy.prod(n)
print('N_prod=', N_prod)
N = [int(N_prod/n_i) for n_i in n]
M = []
for i in range(len(n)):
    g, M_i, m_i = gcdExtended(N[i], n[i])
    print(M_i,'*',N[i],'+', m_i,'*',n[i],'=1')
    M.append(M_i)
print('M_i =', M)
print('N_i =', N)
residues = [1, 0, 6, 5]
print('residues= ', residues)
num_of_res = len(residues)
products = [a * N_i * M_i for a, N_i, M_i in zip(residues, N[:num_of_res], M[:num_of_res])]
sum = numpy.sum(products)
print('sum =', sum)
print ('calc_new_residues =', [sum % n_i for n_i in n[:num_of_res]])
