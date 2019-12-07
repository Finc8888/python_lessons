file = open('input_ch3.txt','r')
wires_list_str = file.readlines()
file.close()
wires_list_arr = [ item.split(',') for item in wires_list_str]
print(wires_list_arr[0])
print(wires_list_arr[1])