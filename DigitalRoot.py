# Author: Andrew Osborne
# GitHub username: 16ozcoldbru Link: https://github.com/16ozcoldbru
# Date: 02/16/2022
# Description: A recursive program exploring the digital root problem. Given a non-negative integer n, the digital
# root is the recursive sum of all the digits of n.

def split_integer(integer, digits=None):
    """A function which takes an integer and splits it into it's separate digits and returns this as an unordered list.
    942 would return as [2, 4, 9] for example."""
    if digits is None:
        digits = []
    if integer < 10:
        digits.append(integer)
        return digits
    else:
        digits.append(integer % 10)  # add the remainder of the divide operation to the return list
        integer = integer // 10  # run the recursion again using the quotient of the divide operation
        return split_integer(integer, digits)


def digital_root(integer):
    """A function which recursively sums the digits of an integer"""
    if integer < 10:
        return integer
    else:
        integer = sum(split_integer(integer))
        return digital_root(integer)


my_number = 942
print(digital_root(my_number))
