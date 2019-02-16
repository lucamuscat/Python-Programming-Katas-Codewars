soldiers = [1,5,6,8,9,10]
k = 2


def winner(soldiers, k, sword_pointer = 0):
    sword_pointer+= k % len(soldiers)
    
print(winner(soldiers,3))

        


