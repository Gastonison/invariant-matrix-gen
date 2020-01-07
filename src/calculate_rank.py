import os
import time
import numpy
from matrix_generator_standard_mod2 import generate_matrix
from algorithm_utils import run_spasm_rank, generate_sms, generate_sms_array, binomial, p_prod, direct_sum_combinations, primes
        
n = 5
# prime = 30
index = 0
# for k in primes(prime):
    # for j in primes(prime)[index::]:
    #     array = [(j, k, i) for i in primes(prime)[index::]]
    #     index += 1

    # for p in array:    
# for p in [(23,k) for k in primes(600)[11::]]:
for p in primes(100)[12:40]:
    print("p {}".format(p))
    timerValue = time.time()
    matrix_data, generated_dictionary, generated_array = generate_matrix(n,p)
    # print(generated_dictionary)
    # print(sorted(generated_dictionary))
    print("Generating Matrix took: {} seconds".format(time.time() % timerValue))
    
    # print(generated_dictionary)
    #     dictionary solution
    timerValue = time.time()
    # generate_sms(matrix_data, generated_dictionary)
    generate_sms_array(matrix_data, generated_array)
    print("Generating sms took: {} seconds".format(time.time() % timerValue))

    # timerValue = time.time()
    # rank = run_spasm_rank()

    # # prod = p_prod(p)

    # result = binomial(p-1+n, n)-int(rank)

    # print("Computing rank took: {} seconds".format(time.time() % timerValue))
    # print("{} {}".format(p, result))
    print("-------------------------")

