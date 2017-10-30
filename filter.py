
def is_odd(n):
          return n % 2 == 1

def not_empty(s):
          print(s and s.strip() == True)
          return s and s.strip()

def _odd_iter():
          n = 1
          while True:
                    n += 2
                    yield n
def _not_divisible(n):
          return lambda x:x % n > 0

def primes():
          yield 2
          it = _odd_iter()
          while True:
                    n = next(it)
                    yield n
                    it = filter(lambda x:x % n > 0,it)
def is_palindrome(n):
          var = str(n)
          idx = len(var) - 1
          if idx == 0:
                    return True
          start= 0
          for i in var:
                    if i != var[idx:idx+1]:
                              return False
                    if idx == start + 1:
                              break
                    else:
                              idx-= 1
                              start += 1
          return True

def is_palindrome1(n):
          return int(str(n)[::-1])==n
                    
output = filter(is_palindrome1,range(1,1000))
print(list(output))

#b = list(filter(not_empty,['A','','B',None,'C',' ']))
#print(b)
#a =list(filter(is_odd,[2,1,3,4,5,6,7,8,9,0,10,15]))
#print(a)

#for i in primes():
#          if i < 10:
#                    print(i)
#          else:
#                    break
