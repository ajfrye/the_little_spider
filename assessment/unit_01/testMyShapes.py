
import shapes

# instantiate my object
s = shapes.Square('spongeBob', 2)

squareName = s.get_name()
print(squareName)

newName = 'my Little Square'
s.set_name(newName)

print(s.get_name())
print('my area is {}'.format(s.get_area()))

t = shapes.Triangle('Mr T.', 4, 3)
print(t.get_area())
