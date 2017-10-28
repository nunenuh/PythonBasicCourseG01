

class Foo:
    
    fooValue = 0.0

    bar = ""

    def setBar(self, bar):
        self.bar = bar

    def getBar(self):
        return self.bar

    def tampil(self):
        print("Ini adalah class Foo")



class Bar:
    barValue = 0.0

    foo = ""

    def setFoo(self, foo):
        self.foo = foo
    
    def getFoo(self):
        return self.foo

    def tampil(self):
        print("Ini adalah class Bar")
    


foo = Foo()
bar = Bar()

foo.setBar(bar)
bar.setFoo(foo)

print(bar.barValue)
print(foo.fooValue)

foo.getBar().barValue = 20
print(bar.barValue)

bar.getFoo().fooValue = 25
print(foo.fooValue)





