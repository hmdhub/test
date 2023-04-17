## numpy  202115050105

```
import numpy as np
# 查看版本
print(np.__version__)
```

## 一.1， 2， 3维数组

#### 1.一维基本方法

```
查看数据类型  type()
最大值  max()
最小值  min()
切片   [-1]  取最后一个值
倒叙   [::-1]
```

#### 2.二维

```python
b = np.array([[1, 2, 3, 9], [3, 4, 5, 8], [4, 5, 6, 8]])
# 行要[]分隔开，外面在加个[]
print(b)
print(b.shape)
# 最大值，最小值  要是有相同的最大值会报错吗？不会报错
print(b.min(), b.max())
# 索引取值
print(b[0][0])   # 第一个0是索引的第一行第二个是第一行的第一个
# 切片
print(b[1][:])
print(b[:][0])   # :的意思是选全部中的第一行
print(b[0])    # print(b[:][0])  print(b[0])没有区别
# print(b[0:][:-1])
print(b[:])
print(a.shape)   # (4,) 4代表4行

print(b[1][:])   # 打印索引为1的全部
print(b[1][:-1])   # 后面的:表示打印的东西是b索引为1的那一行除去这里[3, 4, 5, 8]的最后一个数8，相当于8是索引的最后一个值

# 注意
print(b[:][0])   # :的意思是选全部中的第一行
print(b[0])    # print(b[:][0])  print(b[0])没有区别
```

#### 3.三维

```python
shape 形状
c = np.array([[[1, 2, 3], [2, 3, 4], [4, 5, 6], [6, 7, 8]]])
print(c)
print(c.shape)   # (1, 4, 3)1行4列3宽
```

```python
# 创建数组 arange()等同于python中的range()
ran = np.arange(20)
print(ran)
"""reshape():传入一个元组可以定制多维度的额形状 （2， 10）是一个二维的两行十列"""
ran1 = np.arange(20).reshape((2, 10))
print(ran1)
```

## 二.参数

##### 1.参数 元组 shape

创建数组0填充形状的多维数组 zeros()
    默认类型：float
    dtype可以设置元素类型np.uint8 整数
    astype 重置数组类型
创建数组1填充形状的多维数组 ones()

```python
z = np.zeros((3, 3), dtype=np.uint8)
f = z.astype(np.float64)  # 类型是浮点型
one = np.ones((3, 3), dtype=np.uint8)
```

##### 2.repeat() 重复元素 1，元素，2. 重复次数

```python
f = np.repeat((3, 4, 5), 4)
print(f)
```

##### 3.广播():

​    广播是一种强大的机制，它允许numpy在执行算数运行时使用不同形状的数组
​    s.shape = b.shape  形状相同

```python
# 形状相同
d = np.array([1, 2, 3, 4])
e = np.array([10, 20, 30, 40])
g = d * e
print(g)
# 形状不同
num1 = np.array([[1, 2, 3], [10, 10, 10], [20, 20, 20], [30, 30, 30]])
num2 = np.array([1, 2, 3])
num3 = num1 + num2
print(num3)
```

##### 4.数学函数   三角函数  反三角函数

```python
l = np.array([30, 45, 60])
print(l)
# 弧度 = np.pi / 180
sin_num = np.sin(l * np.pi/180)    # 正弦
cos_num = np.cos(l * np.pi/180)    # 余弦
tan_num = np.tan(l * np.pi/180)    # 正切
print("正弦", sin_num)
print("余弦", cos_num)
print("正切", tan_num)
sin_arg = np.arcsin(sin_num)   # 反正弦
cos_arg = np.arccos(cos_num)   # 反余弦
tan_arg = np.arctan(tan_num)   # 反正切
print("反正弦", sin_arg)
print("反余弦", cos_arg)
print("反正切", tan_arg)

print("反转正弦角度", np.degrees(sin_arg))
print("反转余弦角度", np.degrees(cos_arg))
print("反转正切角度", np.degrees(tan_arg))
```

##### 5.舍入函数

around函数 四舍五入值  1.数组  2.舍入的小树位数 ：默认为0
floor函数  向下取整数
ceil函数   向上取整数

```python
a1 = np.around([20.3, 30.63, 40.234, 34.3245])    # 四舍五入
print(a1)
b1 = np.floor([20.3, 30.63, 40.234, 34.3245])     # 向下取整数
print(b1)
c1 = np.ceil([20.3, 30.63, 40.234, 34.3245])      # 向上取整数
print(c1)
```

##### 6.算法函数  

数组的加减乘除，数组必须具有相同的形状add() +加

subtract()-减

muItipIy0*乘

divide()/除

reciprocal() 倒数，元素的倒数 1/4倒数4/1

power() 1.底数2.幂次方

mod()两数组余数

```python
t = np.arange(9, dtype=np.float64).reshape(3, 3)
y = np.array([10, 10, 10])
print("加法", np.add(t, y))
# print("减法", np.subtract(t, y))
# print("乘法", np.multiply(t, y))
# print("除法", np.divide(t, y))
# 幂次方
c2 = np.array([10, 100, 1000])
print(np.power(c, 2))    # 幂次方
d2 = np.array([1, 2, 3])
print(np.power(c2, d2))
# 倒数
e2 = np.array([0.25, 1.23, 1, 1000])
print(np.reciprocal(e2))
# 两数组余数
num = np.array([10, 20, 30])
num5 = np.array([3, 45, 67])
print('余数', np.mod(num, num5))
```

##### 7.统计函数从数组中快速查询最小、最大、百分位标准差、方差等

```
amin()参数： axis 1行、0列
amax()
ptp()最大值-最小值的差
percentile() 度量，百分比1.数组2.半分比 0-100  3.axis
medianO 计算数组的(中位数)中值
mean()算数平均值
std() 标准差
sqrt(mean(x-x.mean()**2)    
	标准差是一组数组的平均值分散成都的一种度量
var() 方差 mean((x-x. mean())**2)    
	平均数之差的平方的平均数
加权平均数 average()各个数组乘以相对应的权重，然后总求和得到总体值，再除于总数    
	参数：weights:权重系数（可选参数， 默认为1
```

```python
a2 = np.array([[3, 4, 5], [8, 4, 3], [2, 3, 4]])
print(a2)
print('行最大值', np.amax(a2, axis=1))
print('列最大值', np.amax(a2, axis=0))
print('默认最大值', np.amax(a2))
print('行最小值', np.amin(a2, axis=1))
print('列最小值', np.amin(a2, axis=0))
# 百分值  50%的分位数，a排序后的中位数
print('百分值', np.percentile(a2, 50))
print('行百分值', np.percentile(a2, 50, axis=1))
print('列百分值', np.percentile(a2, 50, axis=0))
print('百分值 维持数组形状保持不变', np.percentile(a2, 50, axis=0, keepdims=True))
# 中位数
a3 = np.array([[30, 40, 50], [34, 54, 65], [40, 50, 60]])
print('百分值', np.median(a3))
print('行中位数', np.median(a3, axis=1))
print('列中位数', np.median(a3, axis=0))
# 平均数
# a3 = np.array([[30, 40, 50], [34, 54, 65], [40, 50, 60]])
print('平均数', np.mean(a3))
print('行平均数', np.mean(a3, axis=1))
print('列平均数', np.mean(a3, axis=0))
```

##### 8.权重

```python
a4 = np.array([80, 90, 85])
i = np.array([0.2, 0.3, 0.5])
print(np.average(a4, weights=i))
```

##### 9.vdot 向量点积

```python
二维，计算两个数组所有对应下标元素乘积的和    公式：1*11 + 2*12 + 3*13 + 4*14
a5 = np.array([[1, 2], [3, 4]])
b5 = np.array([[11, 12], [13, 14]])
print('向量点积', np.vdot(a5, b5))
```

##### 10.dot

```python
一维  计算两个数组对应下标位置元素的乘积和
    二维  计算数组的矩阵乘积，交叉元素相乘和
    公式: 1*11 + 2*13    1*12 + 2*14
           3*11 + 4 *13  3*12 + 4*14
"""
a4 = np.array([[1, 2], [3, 4]])
b4 = np.array([[11, 12], [13, 14]])
print(a4)
print(b4)
print('数组点积', np.dot(a4, b4))
```

