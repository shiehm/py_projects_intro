my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

def find_even(my_list):
    evens = []
    
    i = 0 
    while i < len(my_list):
        
        # print('printing i: ', i)
        # print('my_list[i]: ', my_list[i])
        
        k = 0
        while k < len(my_list[i]):
            
            # print('printing k: ', k)
            # print('my_list[i][k] ', my_list[i][k])
            
            if my_list[i][k] % 2 == 0:
                evens.append(my_list[i][k])
            k += 1
        i += 1
        
    # print('printing evens: ', evens)
    return evens
    
print(find_even(my_list))