import os
import time
import numpy
from matrix_generator_direct_sum_mod import generate_matrix
from algorithm_utils import run_spasm_rank, generate_sms, generate_sms_array, binomial, p_prod, direct_sum_combinations, primes
        
n = 2
# prime = 30
index = 0
# for k in primes(prime):
    # for j in primes(prime)[index::]:
    #     array = [(j, k, i) for i in primes(prime)[index::]]
    #     index += 1

    # for p in array:    
for p in [(k,k) for k in primes(5)[1::]]:
# for p in primes(100)[1:40]:
    print("p {}".format(p))
    timerValue = time.time()
    matrix_data, generated_dictionary, generated_array = generate_matrix(n,p)
    # print(len(generated_array))
    # print(generated_dictionary)
    # print(sorted(generated_dictionary))pip
    print("Generating Matrix took: {} seconds".format(time.time() % timerValue))
    
    # print(generated_dictionary)
    #     dictionary solution
    timerValue = time.time()
    # generate_sms(matrix_data, generated_dictionary)
    generate_sms_array(matrix_data, generated_array)
    print("Generating sms took: {} seconds".format(time.time() % timerValue))

    timerValue = time.time()
    rank = run_spasm_rank()
    print(matrix_data)
    print("found rank: {}", rank)
    prod = p_prod(p)

    result = binomial(prod-1+n, n)-int(rank)

    # print("Computing rank took: {} seconds".format(time.time() % timerValue))
    # print("{} {}".format(p, result))
    print("-------------------------")

