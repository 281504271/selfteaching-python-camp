array=[0,1,2,3,4,5,6,7,8,9]
array.reverse() #翻转
print(array)

array = [str(i) for i in array] #join不能直接拼接数字型数组，需要用for in 的函数，将列表变为含有‘’列表
array = ''.join(array) #将列表连接生成一个新的字符串
print(array)

x=array[2:8]
print(x)

y=x[::-1]
print(y)

z=int(y)
print(z)

two=bin(z) #二进制
eight=oct(z) #八进制
sixteen=hex(z) #十六进制

print(two)
print(eight)
print(sixteen)
