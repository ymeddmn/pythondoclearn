import decimal

a = "hello world"
b = f'I want say {a}'  # 格式化字符串，超级简单
# print(b)


fData = 12.32445441654654654465
result = decimal.Decimal(fData)
width = 10
precision = 4
print(f'fData格式化的结果是{result:{width}.{precision}}')#precision是精确后的数字的长度