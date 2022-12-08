x = int(input())
y = int(input())

if y >= x:
    
    for n in range(x, y+1, 5,):
        
        print(n, end=' ')
        
    print()
    
else:
    
    print('Second integer can\'t be less than the first.')
    