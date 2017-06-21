my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

# print "Let's talk about %s." % my_name
# print "He's %d inches tall." % my_height
# print "He's %d pounds heavy." % my_weight
# print "Actually that's not too heavy."
# print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
# print "His teeth are usually %s depending on the coffee." % my_teeth
# 
# # this line is tricky, try to get it exactly right
# print "If I add %d, %d, and %d I get %d." % (
#     my_age, my_height, my_weight, my_age + my_height + my_weight)
    
def inches_to_cm(inches):
    return inches * 2.54
    
print "%s inches is %s cm tall." % (my_height, inches_to_cm(my_height))

height2 = inches_to_cm(my_height)
print "Or its also: %s inches is %s cm tall." % (my_height, height2)
