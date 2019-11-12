from algorithm_utils import *
import time

n = 0
p = 0
matrix_data = {"rows": 0, "cols": 0}
enumeration_dictionary = {}
result_dictionary = {}
result_array = []
eqn_row = 0

# Returns matrix / dictionary generated by relations
def generate_matrix(n_val, p_val):
    #sets global variables
    global n, p, result_matrix, result_dictionary, eqn_row
    n = n_val
    p = p_val
    eqn_row = 0
    generate_enumerated_permutation()
    matrix_data = generate_initial_matrix()
    result_dictionary = generate_initial_dictionary()
    
    populate_matrix()
    return matrix_data, result_dictionary

def generate_enumerated_permutation():
    timerValue = time.time()

    global enumeration_dictionary
    count = 0
    for aset in subsets(p-1+n,n):
        a = map_subset(aset)
        enumeration_dictionary[tuple(a)] = count
        count += 1
    print("Populating enumerated list took {} seconds".format(time.time() % timerValue))
        
def enumerate_permutation(perm):
    return enumeration_dictionary[tuple(sorted(perm))]


# MARK - This is where the matrix is changed to any other data structure
# Generates initial values for the Matrix
def generate_initial_matrix():
    nvars=binomial(p-1+n,n)
    neqs=1+sum(binomial(p-1+k,k)*binomial(p-1+n-k,n-k) for k in [2])
    return {"rows": int(neqs),"cols": int(nvars)}

# Generates initial values for the Dictionary
def generate_initial_dictionary():
    return {(0,0):1}

# Sets column values
def calculate_column_values(a, b, k):
    for i in range(k):
        a_generated = [(a[i1]-a[i])%p for i1 in range(k)]
        a_generated[i] = a[i]
        j= enumerate_permutation(a_generated+b)
        
        if (eqn_row, j) in result_dictionary:
            result_dictionary[(eqn_row,j)] = result_dictionary[(eqn_row, j)]-1/a.count(a[i])
        else:
            result_dictionary[(eqn_row,j)] = -1/a.count(a[i])
            
# # Iterates through all permutations of a, b
def iterate_permutations(k, handle_permutation):
    global eqn_row
    for aset in subsets(p-1+k,k):
        a = map_subset(aset)
        # print(a)
        # print("~~~~~~~~")
        for bset in subsets(p-1+n-k,n-k):
            eqn_row=eqn_row+1
            b = map_subset(bset)
            # print(b)
            # print("-----")
            handle_permutation(a, b, k)
            
# Handles what to do with each iterated permutation
def evaluate_permutation(a, b, k):
    print(a+b)
    print(sorted(a+b))
    j=enumerate_permutation(a+b)
    result_dictionary[(eqn_row, j)] = 1
    calculate_column_values(a, b, k)

# Starts process of populating matrix / dictionary
def populate_matrix():
    # for k in [2]:
        iterate_permutations(2, evaluate_permutation)