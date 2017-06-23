from time import sleep


class FizzBuzz(object):

    def __init__(self, i=0):
        self.i = i

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        return self

    def get_number(self):
        return self.i

    def say(self):
        word = self.get_word()
        if (word == ''):
            return str(self.i)
        return word

    def get_word(self):
        if self.i == 0:
            return ''
        elif self.i % 3 == 0 and self.i % 5 == 0:
            return 'FizzBuzz'
        elif self.i % 3 == 0:
            return 'Fizz'
        elif self.i % 5 == 0:
            return 'Buzz'

        return ''


print('Hello FizzBuzz!')

fbs = FizzBuzz()
for fb in fbs:
    if fb.get_word() == '':
        append = ''
    else:
        append = '(' + str(fb.get_number()) + ')'

    print(fb.say() + append)
    sleep(.01)
