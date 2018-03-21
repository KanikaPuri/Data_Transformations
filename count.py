import read
from collections import Counter

df = read.load_data()


s = ""
for i in df['headline']:
    s+=str(i)+' '

print(Counter(s.lower().split()).most_common(100))