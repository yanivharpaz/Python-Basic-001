
#%% 
print('hello')

x = 50
print(type(x))

x = "utilization"
print(type(x))

x = "123"
print(int(x))
print(type(123.0))

xxx = "hello"
xxx = None 

yyy = 230 ** 100
print(yyy)


zzz = "my string"
xxx = 'my "string"'
yyy = '''
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
print(yyy)

ttt = r"my\\file"
print(ttt)

my_list01 = list([1,2,3,4])

# dict 



# %%
my_list02 = [1,
  2,
  3,
  4,
  5,
  6,
  7,
  ]
print(len(my_list02))
# print(my_list02[89])
# print(my_list02[::-1])
print(my_list02[-2])

my_2d_list = [
    [1,2,3,4,5,6],
    [11,12,13,14,15,16],
]

my_strange_list = [1, "dog", True]
print(my_strange_list.pop())


# %%
my_list02[2:3] = [777, 888]

print(my_list02)
# my_list02.append([777, 888])
my_list02.extend([777, 888])
print(my_list02)


# %%
# my_list02.remove(888)
print('777' in my_list02)
print(444 in my_list02)

print([1,2,3] + [4,5,6])
print([1,2,3] * 4)






# %%
print("Dexter")
print(list("Dexter"))
print(list(["Dog","Cat"]))
print("Dexter"[:-1])
print("Dexter"[1:3])


# %%

# print(["Dexter"][0:1][0:1][0:1])
my_list      = [1,2,3,4,5]
# my_list1     = my_list.copy()
my_list1     = my_list[:]
my_list[2:3] = [22,33]
print(my_list1)

print("*" * 12)


# %%
for counter in [1,2,3,4,5]:
    print(counter)
    print('hi')

# print('no more hi')
# for counter in range(5):
#     print(counter)

# print(list(range(5)))

if counter == 5:
    print('this is 5')
else:
    print('this is NOT 5')


counter = 7

if counter == 5:
    print('this is 5')
elif counter == 6:
    print('this is 6')
elif counter == 7:
    print('this is 7')

else:
    print('I gave up')




# %%
a = 23
b = 56
a, b = b, a
print(a,b)


# %%
aa = tuple([1,2,3])
bb = (1,2,3)
print(aa == bb)

print(bb[1])
# bb[1] = 8

a, b = my_func()
print(a,b )

# %%
def my_func():
    return 1,2
# %%
for item in bb:
    print(item)


my_dict = {
    'key1': 'my_value1',
    'key2': 'my_value2',
}    

print(my_dict)
my_dict['key1']

for x in my_dict:
    print(type(x), x)
    print(my_dict[x])

for x in my_dict.values():
    print(type(x), x)
    # print(my_dict[x])

for k, v in my_dict.items():
    print(k, v)
    # print(my_dict[x])






# %%
print(my_dict.get('key1','default'))
print(my_dict.get('key8','default'))
print('key8' in my_dict)

print(0 < b < 2000)

c = a if b >= 2 else 5
# %%
for counter in range(20):
    if counter % 2 == 0:
        print(counter)