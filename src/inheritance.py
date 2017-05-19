class SuperClass(object):

    def say_hello(self):
        print("Hello")

    def do_nothing(self):
        pass


class SubClass(SuperClass):

    def do_nothing(self):
        # super(SubClass, self).say_hello()
        super().say_hello()


su_obj = SuperClass()
su_obj.do_nothing

obj = SubClass()
obj.do_nothing()
