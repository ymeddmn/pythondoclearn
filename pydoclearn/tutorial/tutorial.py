#  除法运算符  "/" 总是返回一个float类型的结果，如果想返回一个int类型的结果要使用 "//"
#  "**"可以用来计算指数计算


a = '''asdf\
sdf\
sdf\
sdf'''

# 用 "\"打印字符串的时候不会换行
# print(a)


from collections import deque

dq = deque([1, 2, 3, 4])  # 队列

# print(dq.popleft())#队列左边弹出
# print(dq.pop())#队列右边弹出


a = []
for i in range(5):  # 创建列表的方法1
    a.append(i)
# print(a)


b = list(map(lambda x: x + 2, range(7)))  # 创建列表方式2
# print(b)


c = [i for i in range(8)]  # 创建列表的方式3
# print(c)

d = [(i, j) for x in range(1, 2, 1) for j in range(10, 13, 1)]  # 创建复杂元组列表
# print(d)#


e = [23, 54, 6, 7, 8, 6, 7, 4]
del e[4]  # 删除列表中的元素
# print(e)
del e[3: 5]  # 删除列表中部分元素
# print(e)

del e  # 删除列表中所有元素
# print(e)



f = (3, 8, 3)
g = 2, 3, 4, "d"  # 和上面一行一样都可以创建一个元组
# print(f)
# print(g)


h = {3, 4, 6, 7, 8, 9, 23}  # 创建集合方法1
i = set("dfsdfsd")  # 创建集合方法2
# print(h)
# print(i)  # 集合会自动过滤多余元素

j = {x for x in range(3)}  # 创建集合方法3
# print(j)




