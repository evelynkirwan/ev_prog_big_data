words = open("spell.words").readlines()
words = map(lambda x: x.strip(), words)

# if 'zygotic' in words:
    # print True


for i in range(1000): 
    a = 'zygotic' in words
    
    # print a

hash = {}
for word in words:
    hash[word] = True

# print a

for i in range(100000):
    a = hash.has_key('zygotic')
    
print a    

import bitmap
b = bitmap.Bitmap(2**20)
print b
len(b.map)