# import library
import pythagoras as p

# -----------------------------------------------------
# calculate the hypotenuse of a right triangle
# -----------------------------------------------------
# instantiate class object
leg1 = 3
leg2 = 4
obj = p.Triangle(leg1, leg2)

# use the class defined function to find the hypotenuse
hyp = obj.get_hypotenuse()
print( 'The hypotenuse is {}'.format(hyp) )

# create another triangle object using the original object
# make the legs twice the size and calculate the new hypotenuse

