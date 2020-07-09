"""
>>> import numberutil
>>> numberutil.aswords(0)
'zero'
>>> numberutil.aswords(1)
'one'
>>> numberutil.aswords(30)
'thirty'
>>> numberutil.aswords(31)
'thirty one'
>>> numberutil.aswords(100)
'one hundred'
>>> numberutil.aswords(101)
'one hundred and one'
>>> numberutil.aswords(130)
'one hundred and thirty'
>>> numberutil.aswords(131)
'one hundred and thirty one'

"""
import doctest
doctest.testmod(verbose=True)


