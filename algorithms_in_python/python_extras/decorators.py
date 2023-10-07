def function_decorator():

    def my_decorator(func):
        def this_can_be_any_name():
            print("Called before the function is called.")
            func()
            print("Called after the function is called.")
        return this_can_be_any_name

    @my_decorator
    def say_whee():
        print("Whee!")

    say_whee()

##############################
# static
def static_method():
    class Math:
        @staticmethod
        def add(i, j):
            return i + j

    sum = Math.add(2,3)
    print(sum)

    m = Math()
    # No! j = m.add(4.5)
    #print(j)

def class_method():

    class C:
        @classmethod
        def go(cls):
            print("go")

    # either intantiate the class
    c = C()
    c.go()
    # statically calleed
    C.go()

if __name__ == "__main__":
    static_method()
    #class_method()