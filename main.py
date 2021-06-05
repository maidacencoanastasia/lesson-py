from tqdm import tqdm
a = []
for i in tqdm(range(100000000)):
    if(i%2 == 0):
        a.append(i)
