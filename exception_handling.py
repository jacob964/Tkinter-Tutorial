
import exceptions

class Dog:
    __secret = 2

def main():
    
#     ## Shows all types of exceptions
#     for i in dir(exceptions):
#         print i
    

#     ## Raise a customizable exception
#     raise Exception('JustDisagreeable')
    
    try:
        zeroDivision = 1.0/0
    except (NameError, ZeroDivisionError), e:
        print "You can't divide with those numbers"
        print e
    else:
        print zeroDivision
    finally:
        print "Everything is ok"

if __name__ == '__main__': main()