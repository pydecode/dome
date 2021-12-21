# 覆盖父类的方法
# 在子类中定义一个与父类同名的方法，再改写即可
class Dog(object):
    
    def dos(self):
        print('旺旺……')
        
class Cat(Dog):
    
    def cat(self):
        print('喵喵……')

    def dos(self):
        print('哼哼……')
        
        super().dos()
        Dog.dos(self)

pig = Cat()
pig.dos()
pig.cat()
