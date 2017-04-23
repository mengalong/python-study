# 列表解析，增加if else 判断
# parser list with if... else... condition
list_data = [2,3,4,5,6,7,8]

list_data_new = [ x+1 if x>4 else x-1 for x in list_data ]
print list_data_new
