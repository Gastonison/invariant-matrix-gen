from itertools import chain, combinations, product
import commands
from scipy.special import binom
import operator 

def binomial(a,b):
    return int(binom(a,b))

def subsets(length, size):
    s = range(1, length+1)
    return list(combinations(s, size))

def map_subset(subset):
    alist=list(subset)
    alist.sort()
    a=[alist[i]-i-1 for i in range(len(alist))]
    return a

def direct_sum_combinations(p):
    return tuple(product(*[range(i) for i in p])) 

def vector_mod_sum(a, b, p):
    vector = map(sum, zip(a, b))
    for i in range(len(vector)):
        vector[i] = vector[i]%p[i]
    return tuple(vector)

def vector_mod_subtract(a, b, p):
    vector = map(operator.sub, a, b)
    for i in range(len(vector)):
        vector[i] = vector[i]%p[i]
    return tuple(vector)

def p_prod(p):
    total = 1
    for var in p:
        total *= var
    return total

def primes(n):
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

print(primes(200))
def generate_sms(matrix_data, dic):
    items = sorted(dic.items())
    result_string = ""
    for key, val in items:
        if val != 0:
            result_string += "{} {} {}\n".format(key[0]+1, key[1]+1, val)
    result_string += "0 0 0\n"
    create_sms_file(matrix_data, result_string)

def create_sms_file(matrix_data, result_string):
    sms_file= open("../spasm/bench/bivariant_matrix1.sms","w+")
    sms_file.write('{} {} M\n'.format(matrix_data["rows"], matrix_data["cols"]))
    sms_file.write(result_string)
    return sms_file

def run_spasm_rank():
    spasm_script = 'cat ../spasm/bench/bivariant_matrix1.sms | ../spasm/bench/rank_hybrid'
    response = commands.getstatusoutput(spasm_script)
    rank = response[1].split("s rank = ",1)[1]
    return rank