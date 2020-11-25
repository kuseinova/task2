# incapsulation
# prinsip oop
# 
# 1)

# class Phone:
#     number = '11 111 1 11 '


#     def print_number(self):
#         print(self.number)


# 2)
# class Phone:
#     username = "Bektur"  # public variable
#     _age = 21
#     __how_many_time_turned_on = 0


#     def call(self):      # public method

#         self.__turn_on()
#         print("Ring ring")


#     def __turn_on(self):    # private method
#         self.__how_many_time_turned_on += 1
#         print("Times was turned on :" , self.__how_many_time_turned_on)


# phone = Phone()
# # print(phone.username)
# # print(dir(phone))    
# # print(phone._Phone__how_many_time_turned_on)        
# phone.call()
# print(phone._age)
# print(phone._Phone__how_many_time_turned_on)


# # 3)
# class Phone:
#     username = 'Bakyt'
#     __serial_number = '11.22.33'
#     __turned_on_times = 0


#     def call(self):
#         print("ring-ring")

#     def __turned_on_times_func(self):
#         self.__how_many_time_turned_on += 1
#         print("times was turned on :", self.__how_many_time_turned_on)


# phone = Phone()


# print(phone.username)
# print(phone._Phone__serial_number)

# phone._Phone__turned_on_times_func()



# 4)
# class Sample:
#     def __init__(self,age):
#         self.set_age(age)

#     def get_age(self):
#         return self.__age


#     def set_age(self,age):
#         if age in range(1,101):
#             self.__age = age
#         else:
#             print("eto vozrast ne formalen")
        

        # if age > 0 :
        #     print("eto vozrast ne formalen")
        # else:
        #     self.__age = age




# ins = Sample(50)
# print(ins._Sample__age)    # ne est xorosho
# print(ins.get_age())          # cherez func
# ins.set_age(-30)
# print(ins.get_age())


# 5)
# class Sample:
#     def __init__(self,age):
#         self.set_age(age)

#     def get_age(self):
#         return self._age

#     def set_age(self,age):
#         if age > 0 and age < 150:
#             self.__age =  age 
#         else:
#             print("The age can not be a {age}")



# class Property:
#     def __init__(self,value):
#         self.age = value

    
#     @property
#     def age(self):
#         return self.__age

#     @age.setter
#     def age(self,value):
#         if value > 0 and value < 150:
#             self.__age =  value 
#         else:
#             print("the age can not be a {value}")


# obj = Property(23)
# obj.age = 15           
# print(obj.age)


# # 6)
# class FinalClass():
#     def __init__(self,value):
#         self.__set_age(value)

    
#     def __get_age(self):
#         return self.__age

#     def __set_age(self,value):
#         if value > 0 and value < 150:
#                 self.__age =  value 
#         else:
#             print("the age can not be a {value}")

#     age = property(__get_age,__set_age )

# obj = FinalClass(12)
# obj.age = 10
# print(obj.age)
# print(obj.age)

