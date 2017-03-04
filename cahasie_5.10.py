#Cal Hasie
#10-1-12
#Lab 5- 5.10

num_steps = 6

for x in range(num_steps):
    for r in range(x+1):
        if r == 0:
            print('#', end='')
        else:
            print(' ',end='')
    print('#')
