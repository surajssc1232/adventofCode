import os

def part1():

    with open(os.path.join(os.path.dirname(__file__), '1.txt'), 'r') as f:
        lines = f.readlines()

    left=[]
    right=[]
    
    for line in lines:
        l,r=line.strip().split()
        left.append(int(l))
        right.append(int(r))
    
    left.sort()
    right.sort()
    
    total = 0
    for i in range(len(left)):
        total += abs(left[i]-right[i])
    
    print(total)


def part2():
    with open(os.path.join(os.path.dirname(__file__), '1.txt'), 'r') as f:
        lines = f.readlines()
    
    left=[]
    right=[]
    for line in lines:
        l,r=line.strip().split()
        left.append(int(l))
        right.append(int(r))
    
    res=0

    for i in left:
        count=0
        for j in right:
            if j==i:
                count+=1
        res+=i*count
    
    print(res)

if __name__ == "__main__":
    part1()
    part2()

    