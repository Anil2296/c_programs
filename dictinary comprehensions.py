dic={65:'A',66:'B',67:'C'}
for key,value in dic.items():
    print (key,value)
dict={n:chr(n) for n in range(65,68)}
print(dict)
ascii_values=[65,66,67]
alph=['A','B','C']
dictinary=dict(zip(ascii_values,alph))
print(dictinary)
v={65:'A',66:'B',67:'C'}
value=v.get(68,'68 is not a dictionary key')
print(value)
