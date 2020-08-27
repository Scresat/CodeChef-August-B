
def subsets_binary_way(array):
    for i in range(1, pow(2,len(array)), 1):

        binary_array = [int(j) for j in bin(i)[2:]]

        zero_array = [0]*(len(array) - len(binary_array))

        binary_array_full = zero_array + binary_array
        sub_array = [array[k]*binary_array_full[k] for k in range(len(binary_array_full))]

        print([i for i in sub_array if i !=0])

if __name__ == "__main__":
    a = [1, 2, 2,  3, 4, 5, 8, 9, 10, 11, 12, 13, 14, 15] 
    subsets_binary_way(a)