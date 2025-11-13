# class A:        
#     x=89     #class attribute-can be used in both fun and fun1 
#     def fun(self,a,b):
#         p="hdcjswkd"      #instance attribute-can't be used in fun1
#         print("hello world")
#         print(a+b)
#         print(self.x)
#     def fun1(self):
#         print(self.x)
# obj=A()
# obj.fun(3,4)

##normal method

# class A:
#     x="devika"
#     def fun(self):     #duty of fun is to print self.x
#         print(self.x)
# obj=A()
# obj.fun()

##class method

# class A:
#     x="devika"
#     @classmethod       #decorator
#     def fun(self):     
#         print(self.x)
# A.fun()

##static method

# class A:
#     x="devika"
#     @staticmethod
#     def fun(a,b):     
#         print("sum is:",a+b)
# A.fun(2,3)

##INHERITANCE
    #single inheritance

# class A:
#     def fun1(self):
#         print("i am method from class A")
# class B(A):
#     def fun2(self):
#         print("i am method from class B")
# b=B()
# b.fun1()
# b.fun2()

    #multiple inheritance
# class A:
#     def fun1(self):
#         print("i am method from class A")
# class B:
#     def fun2(self):
#         print("i am method from class B")   
# class C(A,B):
#     def fun3(self):
#         print("i am method from class C")
# c=C()
# c.fun1()
# c.fun2()
# c.fun3() 

    #multilevel inheritance
# class A:
#     def fun1(self):
#         print("i am method from class A")
# class B(A):
#     def fun2(self):
#         print("i am method from class B")   
# class C(B):
#     def fun3(self):
#         print("i am method from class C")
# c=C()
# b=B()
# c.fun1()
# c.fun2()
# c.fun3()
# b.fun1()
# b.fun2()

    #hirarchical inheritance
# class A:
#     def fun1(self):
#         print("i am method from class A")
# class B(A):
#     def fun2(self):
#         print("i am method from class B")   
# class C(A):
#     def fun3(self):
#         print("i am method from class C")
# c=C()
# b=B()
# c.fun1()
# c.fun3()
# b.fun1()
# b.fun2()

    #hybrid inheritance
# class A:
#     def fun1(self):
#         print("i am method from class A")
# class B(A):
#     def fun2(self):
#         print("i am method from class B")  
# class C(B):
#     def fun3(self):
#         print("i am method from class C")
# class D(B):
#     def fun4(self):
#         print("i am method from class D") 
# class E(C,D):
#     def fun5(self):
#         print("i am method from class E")
# b=B()
# c=C()
# d=D()
# e=E()
# b.fun1()
# b.fun2()
# c.fun2()
# c.fun1()
# c.fun3()
# d.fun2()
# d.fun1()
# d.fun4()
# e.fun1()
# e.fun2()
# e.fun3()
# e.fun4()
# e.fun5()

# class A:
#     def fun1(self):
#         print("i am method from class A")
# class B(A):
#     def fun2(self):
#         print("i am method from class B")
# class C(B):
#     def fun3(self):
#         print("i am method from class C")  
# class D(C):
#     def fun4(self):
#         print("i am method from class D")
# class E(C):
#     def fun5(self):
#         print("i am method from class E") 
# b=B()
# c=C()
# d=D()
# e=E()

##POLYMORPHISM
    #method overloading

# def fun1(a):
#     print("one parameter")
# def fun1():
#     print("no parameter")
# def fun1(a,b,c):
#     print("three parameter")
# def fun1(a,b,c,d,e):
#     print("five parameter")
# fun1(2,3,4,5,6)

    #method overriding
# class A:
#     def fun1(self):
#         print("parent class")
# class B(A):
#     def fun1(self):
#         print("child class")
# b=B()
# b.fun1()

# class A:
#     def fun1(self):
#         print("parent class")
# class B(A):
#     def fun1(self):
#         super().fun1()
#         print("child class")
# b=B()
# b.fun1()

##ENCAPSULATION
    #public access modifier

# class A:
#     x=10
#     def fun1(self):
#         print(self.x)
# class B(A):
#     def fun2(self):
#         print(self.x)
# b=B()
# b.fun1()
# b.fun2()
# print(b.x)

    #protected access modifier
# class A:
#     _x=10
#     def fun1(self):
#         print(self._x)
# class B(A):
#     def fun2(self):
#         print(self._x)
# b=B()
# b.fun1()
# b.fun2()
# print(b._x)

    #private access modifier
# class A:
#     __x=10
#     def fun1(self):
#         print(self.__x)
# class B(A):
#     def fun2(self):
#         print()
# b=B()
# b.fun1()
# b.fun2()

##ABSTRACTION

# from abc import ABC, abstractmethod
# class A(ABC):
#     @abstractmethod
#     def fun(self):
#         pass
# a=A()            #varilla

# from abc import ABC, abstractmethod
# class A(ABC):
#     @abstractmethod
#     def fun1(self):
#         pass
# class B(A):              #concrete class
#     def fun1(self):
#         print("hello")
# #a=A()
# b=B()
# b.fun1()

##ITERATOR

# lst=[1,2,3,4,5]
# i=iter(lst)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

##GENERATOR

# def fun():
#     yield 1
#     yield 2
#     yield 3
# i=fun()
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

# def fun():
#     for i in range(1,6):
#         yield 1
# for i in fun():
#     print(i)

##CONSTRUCTOR

# class A:
#     def __init__(self):
#         print("constructor")
# obj=A()

