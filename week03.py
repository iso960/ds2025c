import array

def move_zeros(a_list):
    zero_index = 0;
    for index, n in enumerate(a_list):
        if n != 0:
            a_list[zero_index] = n
            if zero_index != index:
                a_list[index] = 0
            zero_index += 1
    return(a_list)

arr = array.array('i', [99, 0, -7, 0, 16])
move_zeros(arr)
for i in range(len(arr)):
    print(f"{arr[i]:5} {id(arr[i])}")

l = [9, 9]
print(id(0), id(1))