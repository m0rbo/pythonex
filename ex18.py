def print_two(*args):
    arg1, arg2 = args
    print "arg1: %s, arg2: %s" % (arg1, arg2)

def print_two_again(arg1, arg2):
    print "arg1: %s, arg2: %s" % (arg1, arg2)

def print_one(arg1):
    print "arg1: %s" % arg1

def print_none():
    print "i got nothin."


print_two("zED","Shaw")
print_two_again("Zed","Sharwer")
print_one("First!")
print_none()
