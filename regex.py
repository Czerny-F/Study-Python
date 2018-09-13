import re

pattern = r"c[a|b]"
text = "bcaabsacbsca"

p = re.compile(pattern)

m = p.match(text)
s = p.search(text)
a: list = p.findall(text)
g: iter = p.finditer(text)


print('pattern:', pattern)
print('target:', text)
print('compiled:', p, '\n')
print('split:', p.split(text))
print('substitude:', p.sub(lambda m: '*%s*' % m.group(), text))

print('match:')
if m:
    print(m)

print('search:')
if s:
    print(s)

print('findall:', a)

print('finditer:')
for _m in g:
    print(_m)
