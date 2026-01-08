
def count_method_calls(example):
    count = 0
    class MyClass:
        def __init__(self):
            self.myclass = example()
        def display(self):
            nonlocal count
            count += 1
            self.myclass.display()
            print(count)
    return MyClass



@count_method_calls
class Example:
    def display(self):
        print("hello world")


ss = Example()
ss.display()
ss.display()
ss.display()






