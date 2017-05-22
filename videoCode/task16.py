#coding=utf-8

'''
习题一：

定义一个生成器函数，函数里只能用yield，要求输出结果：

step 1
step 2 x=haha
step 3 y=haha

提示步骤：建立生成器对象，并且用对象的next()和send()方法来输出结果。
send()方法传入的参数是"haha"
'''

def generate():
	
	x = yield "step 1"

	x = yield "step 2 %s"%x

	x = yield "step 3 %s"%x

g = generate()

print g.next()
print g.send("x=haha")
print g.send("y=haha")



'''
习题二：用生成器yield实现斐波拉切数列。
'''

def fib(input_data):
	n,a,b = 0,0,1
	while n < input_data:
		print b
		#yield b
		a,b = b,a+b
		n += 1

	return "ending"

print fib(10)
