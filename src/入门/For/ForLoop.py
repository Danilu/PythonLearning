# for用于完成指定次数的循环
# 基本语法 for 变量 in 集合

# range(start,end) end取不到
# for i in range(0,10):
#     print(i)

rabbit = 3
print("请输入N的值")
N = int(input()) #获取键盘输入的N的值
for i in range(0, N):
    rabbit = rabbit*2
print("%d年后，兔子数量为%d" % (N, rabbit))
