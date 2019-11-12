import os
import time
from matrix_generator_direct_sum_mod import generate_matrix
from algorithm_utils import run_spasm_rank, generate_sms, binomial, p_prod, direct_sum_combinations
        
n = 5
array = [(5, i) for i in range(1, 200)]

for p in array:    
    timerValue = time.time()
    matrix_data, generated_dictionary = generate_matrix(n,p)
    # print("Generating Matrix took: {} seconds".format(time.time() % timerValue))

    # print(generated_dictionary)
    #     dictionary solution
    timerValue = time.time()
    generate_sms(matrix_data, generated_dictionary)
    rank = run_spasm_rank()

    prod = p_prod(p)

    result = binomial(prod-1+n, n)-int(rank)

    # print("Computing rank took: {} seconds".format(time.time() % timerValue))
    print("{} {}".format(p, result))
    # print("-------------------------")

