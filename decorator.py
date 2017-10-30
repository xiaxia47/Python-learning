import functools

def count():
          fs= []
          fs.append(map(lambda i:i*i,range(1,4)))
          return fs
def log(func  ):
          @functools.wraps(func)
          def wrapper(*args,**kw):
                print('call %s():' % func.__name__)
                func(*args,**kw)
                print('End call %s():' % func.__name__)
          return wrapper
def log1(text):
          def decorator(func):
                    @functools.wraps(func)
                    def wrapper(*args,**kw):
                              print('%s %s():' % (text,func.__name__))
                              return func(*args,**kw)
                    return wrapper
          return decorator


@log
def now():
      print('2015-03-25')


now()
