
###############################
# 아래 코드의 의미를 알아본다.
# list1 = [4, 5, 6]
# list1[0] = 10
###############################
list1 = [4, 5, 6]
list2 = list1
print("list1==>", "address=", id(list1), ", value=", list1)
print("list2==>", "address=", id(list2), ", value=", list2)
print("-----------------")


print("list1[0]==>", "address=", id(list1[0]), ", value=", list1[0])
print("list1[1]==>", "address=", id(list1[1]), ", value=", list1[1])
print("list1[2]==>", "address=", id(list1[2]), ", value=", list1[2])
print("-----------------")


print("list2[0]==>", "address=", id(list2[0]), ", value=", list2[0])
print("list2[1]==>", "address=", id(list2[1]), ", value=", list2[1])
print("list2[2]==>", "address=", id(list2[2]), ", value=", list2[2])
print("-----------------")

list1[0] = 10
print("list1[0] = 10")
print("list1[0]==>", "address=", id(list1[0]), ", value=", list1[0])
print("list2[0]==>", "address=", id(list2[0]), ", value=", list2[0])
print("#################")


###############################
# 아래 코드의 의미를 알아본다.
#list1 = [1, 2, 3]
#list1 = [4, 5, 6]
###############################
list1 = [1, 2, 3]
list2 = list1
print("list1==>", "address=", id(list1), ", value=", list1)
print("list2==>", "address=", id(list2), ", value=", list2)
print("-----------------")
print("list1[0]==>", "address=", id(list1[0]), ", value=", list1[0])
print("list1[1]==>", "address=", id(list1[1]), ", value=", list1[1])
print("list1[2]==>", "address=", id(list1[2]), ", value=", list1[2])
print("list2[0]==>", "address=", id(list2[0]), ", value=", list2[0])
print("list2[1]==>", "address=", id(list2[1]), ", value=", list2[1])
print("list2[2]==>", "address=", id(list2[2]), ", value=", list2[2])
print("-----------------")


list1 = [4, 5, 6]
print("list1 = [4, 5, 6]")
print("list1==>", "address=", id(list1), ", value=", list1)
print("list2==>", "address=", id(list2), ", value=", list2)
print("-----------------")
print("list1[0]==>", "address=", id(list1[0]), ", value=", list1[0])
print("list1[1]==>", "address=", id(list1[1]), ", value=", list1[1])
print("list1[2]==>", "address=", id(list1[2]), ", value=", list1[2])
print("list2[0]==>", "address=", id(list2[0]), ", value=", list2[0])
print("list2[1]==>", "address=", id(list2[1]), ", value=", list2[1])
print("list2[2]==>", "address=", id(list2[2]), ", value=", list2[2])
print("-----------------")
