#Cal Hasie
#11/12/12
#Lab 13- 13.4



number = [1,2,5,8,9,6]
def main():
    print(number)
    group(number)

def group(num):
    if num[0] > num[1]:
        maxi = num[0]
    else:
        maxi = num[1]
    if len(num) == 2:
        print("The maximum number in the list is:", maxi)
    else:
        num[1] = maxi
        num_list = num[1:]
        group(num_list)
    

main()
    
