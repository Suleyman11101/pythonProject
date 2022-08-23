# class Test:
#     def InstanceMethod(self):
#         pass
#     @classmethod
#     def ClassMethod(cls):
#         pass
#     @staticmethod
#     def StaticMeyhod():
#         pass
#
# class Time():
#     def __init__(self,hour,minute,seconds):
#         self.__hour = hour
#         self.__minute = minute
#         self.__seconds = seconds
#     @classmethod
#     def from_string(cls,time_as_string):
#         cls.__hour,cls.__minute,cls.__seconds = map(int,time_as_string.split(":"))
#         time = cls(cls.__hour,cls.__minute,cls.__seconds)
#         return time
#
#     @staticmethod
#     def is_time_valid(time_as_string):
#         if time_as_string.count(":") == 2:
#             hour,minute,seconds = map(int,time_as_string.split(":"))
#             return 0 < hour < 24 and 0 < minute < 60  and 0<seconds < 60
#
#     def string_to_time(self):
#         return f"{self.__hour}:{self.__minute}:{self.__seconds}"
#
# times = [
#     "23:44:44",
#     "25:13:34",
#     "11:10:40",
#     "-1:32:12"
# ]
#
# for i in times:
#     if Time.is_time_valid(i):
#         time = Time.from_string(i)
#         string_to_times = time.string_to_time()
#         print(string_to_times)
#     else:
#         print("Error!")
# #=======================================================================
# class Shape:
#     def __init__(self,name,sides):
#         self.__name =  name
#         self.__sides = sides
#     def area(self):
#         pass
#     @property
#     def sides(self):
#         pass
#
#     @property
#     def name(self):
#         return self.__name
#
# class Sguare(Shape):
#     def __init__(self,len):
#         self.__len = len
#
#     def area(self):
#         return self.__len ** 2
#
# from math import pi
# class Circle(Shape):
#     def __init__(self,radius):
#         self.__radius = radius
#
#     def area(self):
#         return pi * self.__radius ** 2
#
# sg = Sguare(20)
# cir = Circle(10)
# print(sg.area())
# print(cir.area())
#=========================================================================
# class Strings:
#     def __init__(self,string):
#         self.__string = string
#
#     def __repr__(self):
#         return f"{self.__string}"
#
#     def __add__(self, other):
#         return self.__string + other
# str1 = Strings("Hello")
# print(str1 + " World")
#==============================
# class Vehicle:
#     def __init__(self, price):
#         self.__capacity = 50
#         self.__price = price
#
#     @property
#     def price(self):
#         return self.__price
#     @price.setter
#     def price(self, price):
#         self.__price = price
#
#
#
# class Bus(Vehicle):
#
#     def fare_price(self):
#         return self.price * 0.1
#========================================================================================
# class Nods:
#       def __init__(self,nods=None,value=None):
#             self.nods = nods
#             self.value = value
#
# class Linked_list:
#       def __init__(self):
#             self.__head = None
#             self.__tall = None
#       def insert(self,value):
#             if self.__head is None and  self.__tall is None:
#                   self.__head = Nods(value=value)
#                   self.__tall = self.__head
#                   return

#             new_node =Nods(value=value)
#             self.__tall.next = new_node
#             self.__tall = new_node
# my_list = Linked_list()
# my_list.insert(0)
#+====================
# steck =[1,2,3]
# print(steck.)
#=============================================================

class Queue:
    def __init__(self,list_qu):
        self.list_qu = list_qu
    def IsEmpty(self):
        return (True if len(self.list_qu) == 0 else False)
list_qu = Queue([])
print(list_qu.IsEmpty())

