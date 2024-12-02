# advent of code day 2

with open('2.txt','r') as file:
    matrix=[[int(num) for num in line.split()]for line in file]

count=0
for i in matrix:
    is_increasing=True
    is_decreasing=True
    is_safe=True

    for j in range(1,len(i)):
        
        diff=i[j]-i[j-1]
        
        
        if not (1<=abs(diff)<=3):
            is_safe=False
            break

        if diff>0:
            is_decreasing=False
        elif diff<0:
            is_increasing=False

    if is_safe and (is_decreasing or is_increasing):
        count+=1

print(count)
    
        
