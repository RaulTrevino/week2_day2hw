hero_health=100
monster_health=100

character=input(' attack or run or special?')
if character == 'attack':
        new_sum = monster_health - 10 
        print('monster health is', new_sum)
elif character == 'run':
        new_sum1 = hero_health - 10

        print('Monster Attacks !!! Hero health is', new_sum1)
elif character == 'special':
        print('Monster Dead You win')
character=input(' attack or run or special?')