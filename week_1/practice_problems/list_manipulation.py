def list_manipulation(L):
    even_numbers = [i for i in L if i%2 == 0]
    doubled_list = [2*i for i in even_numbers]
    Sum = sum(doubled_list)
    return Sum

print(list_manipulation([1,2,3,4,5]))