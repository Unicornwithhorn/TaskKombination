# Задача:
# На вход подается натуральное число N и символьная строка S длины N.
# На выходе программа должна сгенерировать все различные (то есть несовпадающие !)
# символьные строки всех длин от 1 до N,
# причем каждая строка должна состоять из символов, составляющих подмножество строки S.
# Например, вход «3, ‘МАА’» генерирует на выходе строки ‘M’, ‘A’, ‘MA’, ‘AM’, ‘AA’, ‘MAA’, ‘AMA’, ‘AAM’.
# (Считаем, что N≤20, память 100М). Требуется  программа на удобном языке…
#
import random
N = int(input('Введите натуральное число'))
S = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
end_list = []
my_list =list(random.choice(S) for i in range(N))
print(f'исходная комбинация = {my_list}')

def shift(my_list: list):
    temp = my_list[0]
    for i in range(len(my_list)-1):
        my_list[i]=my_list[i+1]
    my_list[-1] = temp

def shift_one_weel(my_list: list, level: int):
    shift(my_list[level])

matrix = []

for j in range(N):
    counter = 0
    matrix.append(my_list[:])
    list_of_shifts = [0 for level in matrix]
    for i in range(N**len(matrix)):
        if len(set(list_of_shifts)) == j+1:
            word = ''.join(list(zip(*matrix))[0])
            end_list.append(word)
        counter += 1
        check_counter = counter
        deep = 0
        while check_counter % N == 0:
            deep += 1
            check_counter /= N
        if j >= deep:
            shift_one_weel(matrix, j - deep)
            list_of_shifts[deep] += 1
            list_of_shifts[deep]%=N
    shift(matrix[0])

for element in end_list:
    print(element)




