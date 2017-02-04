

a = {'name':'hello workd', 'age':29, 'phone':'010-1234-5678'}

print(a.keys())
print(a.values())
print(a.items())
print(a.get('name'))

print('name' in a)

del a['name']
print(a.keys())
print(a.values())
print(a.items())
print(a.get('name'))
print('name' in a)


