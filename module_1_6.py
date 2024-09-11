may_dick = {'Piter': 1997,'stepan': 2001 }
print (may_dick)
print(may_dick['Piter'])
print(may_dick.get ('Martin','значение отсутствует в списке'))
may_dick.update({'Petr': 1995,
                'Kirill': 1994})
print(may_dick)
a=may_dick.pop('Petr')
print(a)
may_set = {1,1,3,4,16,16,14,15,15,13,14,14,18,'string','no string','no string',True ,False,False}
print(may_set.add(11))
print(may_set.add(21))
may_set.remove(16)
print(may_set)
