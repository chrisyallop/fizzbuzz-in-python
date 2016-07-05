class FizzBuzz:
  def generate(self):
     fb = range(1, 101)
     for i in range(2,101,3):
         fb[i] = 'Fizz'

     for i in range(4,101,5):
         fb[i] = 'Buzz'

     return fb
