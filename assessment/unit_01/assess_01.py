# import library
import pythagoras as p

# -----------------------------------------------------
# calculate the hypotenuse of a right triangle
# -----------------------------------------------------
# instantiate class object
leg1 = 3
leg2 = 4
t = p.Triangle(leg1, leg2)

# use the class defined function to find the hypotenuse
hyp = t.get_hypotenuse()
print( 'The hypotenuse is {}'.format(hyp) )

# create another triangle object using the original object




# make the legs twice the size and calculate the new hypotenuse
new_leg1= t.get_leg1()
new_leg2= t.get_leg2()
t2 = p.Triangle(new_leg1*2, new_leg2*2)

hyp = t2.get_hypotenuse()
print( 'The hypotenuse is {}'.format(hyp) )
