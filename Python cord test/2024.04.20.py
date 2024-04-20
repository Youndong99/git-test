'''
text='abc'

print(text[-3])
print(text[-2])
print(text[-1])
'''

text='abcde fgh ijk'
'''
print(text[2:5])
print(text[1:8])
print(text[-5:-1])
print(text[-5:-0])

print(text[5:])
print(text[:5])
print(text[:])  
'''
'''
print(text[0:9:2])
print(text[9:0:-1])
print(text[::-1])
'''
'''
text='abced {} {}'
print(text.format('ABC', 123))
'''
'''
text ='abced ABC ABC'
print(text.replace('A','K'))
'''
'''
text='abcde A/B/C A.B.C'
a,b,c=text.split('.')
print(a)
print(b)
print(c)
'''

'''
print('/'.join(text))
'''
'''
text='abce ABC ABC'
print(text.count('a'))
print(text.count('b'))
print(text.count('1'))
'''
'''
text='*** abce ***'
print(text.strip('*'))
print(text.lstrip('*'))
print(text.rstrip('*'))
'''
'''
text='ABC ABC'
print(text.find('A'))
print(text.rfind('A'))
print(text.index('A'))
print(text.rindex('A'))
'''
'''
text1='ABCabc123'
text2='123'
text3='ABC'
text4='abc'

print(text3.isalpha())
print(text3.isdigit())
print(text3.isalnum())
print(text3.isupper())
print(text3.islower())
'''
'''
text='ABCabc'
print(text.upper())
print(text.lower())
'''

y='2024'
m='4'
d='16'
print(y.zfill(4))
print(m.zfill(2))
print(d.zfill(2))
