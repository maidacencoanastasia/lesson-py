from tqdm import tqdm
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
d=[]
d.append(a)
d.append(b)
d.append(c)
for i in tqdm(range(0,3)):
    for j in tqdm(range(0,3)):
        for k in tqdm(range(0,3)):
            if(i!=j&j!=k&k!=i):
                print(d[i],d[j],d[k])