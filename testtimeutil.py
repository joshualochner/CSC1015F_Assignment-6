"""
>>> import timeutil
>>> timeutil.validate('apple')
False
>>> timeutil.validate('111:01 p.m.')
False
>>> timeutil.validate('01:1 a.m.')
False
>>> timeutil.validate('12:61 am')
False
>>> timeutil.validate('1:1 p.m.')
False
>>> timeutil.validate('1:15 p.m.')
True

"""
import doctest
doctest.testmod(verbose=True)