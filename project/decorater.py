#coding=utf-8


'''
	1.斐波那契函数实现
	2.爬梯子(每次只能移动一步或者两步)
'''

def decorate(func):
	cache = {}
	#可以传入多个参数，适合元组类型
	def wrap(*args):
		if args not in cache:
			cache[args] = func(*args)
		return cache[args]
	return wrap


@decorate
def fib(n):
	if n==1 or n==0:
		return 1
	else:
		#递归调用
		return fib(n-2) + fib(n-1)

print [fib(n) for n in range(10)]


@decorate
def climb(n,steps):
	count = 0
	if n <= 1:
		count = 1
	else:
		for step in steps:
			count += climb(n-step,steps)
	return count

print climb(5,(1,2))