file = open('input_ch2.txt','r')
arr = file.readline().split(',')
arr2 = arr[:]
file.close()

#Так как не помню метод для разбития на подмассивы заданной размерности,
#пишу свою функцию
def chunk(list,dem):
    start = 0
    stop = dem
    arr = []
    for item in range((len(list)//dem)):
        arr.append(list[start:stop])
        start += dem
        stop += dem
    return arr
def get_opcode(arr,noun,verb):
    arr[1] = noun
    arr[2] = verb
    opcode_list = chunk(arr,4)
    #перед запуском программы значение на позиции 1 - 12, а на 2й - 2
    for key,item in enumerate(opcode_list,start=0):
        key_akk = int(item[3])
        key_op1 = int(item[1])
        key_op2 = int(item[2])
        if int(item[0]) == 99:
            # print("Конец программы")
            break
        elif int(item[0]) == 1:
            arr[key_akk] = int(arr[key_op1]) + int(arr[key_op2])
        elif int(item[0]) == 2:
            arr[key_akk] = int(arr[key_op1]) * int(arr[key_op2])
        else:
            continue
    return arr

# print(arr)
for noun in range(0,100):
    for verb in range(0,100):
        copy_arr = arr[:]
        output = get_opcode(copy_arr,noun,verb)[0]
        if(output == 19690720 ):
            print(((100 * noun) + verb))
            break
# print(get_opcode(arr,12,2)[0])