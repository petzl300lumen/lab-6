def sizer(cls):
    class Sizer_class(cls):
        @property
        def size(self):
            try:
                return len(self)
            except:
                try:
                    return abs(self) 
                except:
                    return 0 
        def __abs__(self):
            return len(str(abs(self.a)))
        def __len__(self): 
            return len(self.a)
    return Sizer_class
@sizer
class MyClass:
    def __init__(self, a):
        self.a = a

x = MyClass(-11)
print(x.size)
y = MyClass([1,2,3,4,5])
print(y.size)
z = MyClass(None)
print(z.size)
