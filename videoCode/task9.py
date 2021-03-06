#coding=utf-8


'''
题目一： 写一个网页数据操作类。完成下面的功能：

提示：需要用到urllib模块

get_httpcode()获取网页的状态码，返回结果例如：200,301,404等 类型为int 

get_htmlcontent() 获取网页的内容。返回类型:str

get_linknum()计算网页的链接数目。
'''
import urllib
import time

class WebPage:

    def __init__(self,url):
        self.url = url

    def get_httpcode(self):
        d = urllib.urlopen(self.url)
        return d.code

    def get_htmlcontent(self):
        d = urllib.urlopen(self.url)
        content = d.read()
        start = time.time()
        f = open('/Users/marxia/Desktop/interCode/videoCode/web/test.txt','w')
        f.write(content)
        f.close()
        end = time.time()
        return end - start

    def get_linknum(self):
        d = urllib.urlopen(self.url)
        content = d.read()
        return len(content.split('<link'))-1

wp = WebPage("https://github.com/MarsTT")
print wp.get_httpcode()
print wp.get_htmlcontent()
print wp.get_linknum()


'''
    继承，并且重写父类方法
'''

class SchoolMember:
    '''Represents any school member.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print '(Initialized SchoolMember: %s)' % self.name

    def tell(self):
        '''Tell my details.'''
        print 'Name:"%s" Age:"%s"' % (self.name, self.age),

class Teacher(SchoolMember):
    '''Represents a teacher.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print '(Initialized Teacher: %s)' % self.name

    def tell(self):
        print 'Salary: "%d"' % self.salary

class Student(SchoolMember):
    '''Represents a student.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print '(Initialized Student: %s)' % self.name

    def tell(self):
        print 'Marks: "%d"' % self.marks

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 22, 75)

members = [t, s]
print members
for member in members:
    member.tell()


