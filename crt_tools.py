import numpy as np

def gcdExtended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcdExtended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def calc_prod_hat(chain, i):
    p = 1
    for k in range(len(chain)):
        if k != i:
            p = p * chain[k]
    return p


def inverse(element, mod):
    gcd, x, y = gcdExtended(element, mod)
    assert gcd == 1
    return x % mod


def get_int(rns, mod_chain):
    x_hat = 0
    for i in range(len(mod_chain)):
        mod = mod_chain[i]
        inverse_prod_hat = inverse(calc_prod_hat(mod_chain, i), mod)
        x_hat += rns[i] * (calc_prod_hat(mod_chain, i)) * (inverse_prod_hat % mod)
    assert [x_hat % residue for residue in mod_chain] == rns
    return x_hat % np.prod(mod_chain)


def transform_basis(rns, source_mod_chain, target_mod_chain):
    rns_results = []
    inverse_prod_hat = [[0]*len(source_mod_chain)]*len(target_mod_chain)
    prod_hat = [calc_prod_hat(source_mod_chain, i) for i in range(len(source_mod_chain))]

    for j in range(len(target_mod_chain)):
        target_mod_j = target_mod_chain[j]
        for i in range(len(source_mod_chain)):
            source_mod_i = source_mod_chain[i]
            inverse_prod_hat_i = inverse(prod_hat[i], source_mod_i)
            inverse_prod_hat[j][i] = (inverse_prod_hat_i % source_mod_i) % target_mod_j

    for j in range(len(target_mod_chain)):
        x_hat = 0
        for i in range(len(source_mod_chain)):
            x_hat += (rns[i] % target_mod_chain[j]) * (prod_hat[i] % target_mod_chain[j]) * inverse_prod_hat[j][i]
        rns_results.append(x_hat % target_mod_chain[j])
    return rns_results
