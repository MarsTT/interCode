#coding=utf-8
'''
有10个刷卡机，代表建立10个线程，
每个刷卡机每次扣除用户一块钱进入总账中，
每个刷卡机每天一共被刷100次。账户原有500块。所以当天最后的总账应该为1500

用多线程的方式来解决，提示需要用到这节课的内容
'''

import threading

money = 500
mlock = threading.Lock()

def pos(id):
	global money
	#mlock.acquire()
	money += 1
	#mlock.release()

	print money

i = 0
while i < 100:

	for j in xrange(10):
		th = threading.Thread(target=pos,args=[j])
		th.start()

	i += 1


