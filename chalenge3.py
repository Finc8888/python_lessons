file = open('input_ch3.txt','r')
wires_list_str = file.readlines()
file.close()
wires_list_arr = [ item.split(',') for item in wires_list_str]

#здесь будет храниться пути все проводников исходящих из главного порта
wire_path_list = []

for wire in wires_list_str:
   wire_path = []
   current_x = 0
   current_y = 0
   for path in wire:
       pass

#функция для парсинга пути
def parse_path(path,start_x = 0,start_y = 0):
    #определим направление по первой букве
    direction = path[0:1]
    distance = int(path[1:])
    arr = []
    if direction == 'R':
        for item in range(start_x,(distance + 1)):
            arr.append((item,start_y))
    elif direction == 'L':
        for item in range(start_x,(-distance - 1),-1):
            arr.append((item,start_y))
    elif direction == 'U':
        for item in range(start_y,(distance + 1)):
            arr.append((start_x,item))
    elif direction == 'D':
        for item in range(start_y,(-distance - 1),-1):
            arr.append((start_x,item))
    else:
        pass
    return arr



print(parse_path('R9'))
# print(wires_list_arr[0])
# print(wires_list_arr[1])