num_list=[1,11,14,5,8,9]
num_list2=[]
for num in num_list: #the numbers in numlist
    if num < 10:      #if any of the numbers in list are less than 10
        num_list2.append(num)  #add the numbers to num_list2   .append=add   (num)==number found less than 10
print(num_list2)     #print num_list2 with numbers that are less than 10
