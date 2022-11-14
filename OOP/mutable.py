"""
MUTABLE OBJECTS
once created in the 
id function returns a unique id for an specific object
Cpython returns the memory address
Names are attached to the memory address

Alias are different variables names dfor values
The change of the internla values are considered to be mutable object
innmutable are string and int
mutable classes are list, dict, set , bytearray

IMMUTABLE OBJECTS
ONce created in the memory it can not be changed
Built in are --> int, float, bool, complex, tuple, frozenset, unicode

the value is stored in the memory and if there are another variables with the same value it will be directed to the same memory location

if the location has no link can be removed from the memory

IDENTITY OPEARTOR
THE IS/ IS NOT 
IS (Checks if the memory location is the SAME) vs. ==  (Compares the value)
Avoid using is with immutable objects

DEL is the command for deleting the reference in the memory location
UnboundLocalError means that the value is set but not attached to the memory
"""
