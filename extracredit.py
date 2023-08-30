# For example: If the function takes [1,11,14,5,8,9] as input (representing the levels of the monsters), the function should return [1,5,8,9] as these are the monsters the player can fight.


# Use the following list - [1,11,14,5,8,9]




#exercise 1

levels=[1,11,14,5,8,9]
lower_level = []


for num in levels:
    if num < 10:
        lower_level.append(num)
print(lower_level)


#exercise2

# For example, if the function takes the lists [1, 2, 3, 4, 5, 6] and [3, 4, 5, 6, 7, 8, 10], and the maximum inventory size is 8, it should return [10, 8, 7, 6, 6, 5, 5, 4].
# Use the following lists and maximum inventory size:

list1 = 'bat', 'rock', 'sling-shot', 'bow', 'arrow', 'potion',
list2 = 'knife', 'hat', 'boots', 'gun', 'ammo', 'book', 'lighter',
inv_size =[8]

list1 += list2

list1.sort()
print(list1)


#dont understand why list doesnt sort it worked with question 1 does it not work the same when words are entered instead of numbers?