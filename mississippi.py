#printing letters in decreasing order
string = input("please enter the string :")
new_string=(string[::-1])
print(new_string)
dic= {} 
for i in new_string: 
    if i in dic: 
        dic[i] += 1
    else: 
        dic[i] = 1 
print(str(dic)) 
