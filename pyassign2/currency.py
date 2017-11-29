# use string-manipulation methods to read the
# web page and extract the exact information we need

from urllib import urlopen

def exchange(currency_from, currency_to, amount_from):
    """Returns: amount of currency received in the given exchange.
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    if the input is unlawful, you will get an error:
        "Source currency code is invalid."
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    In this exchange, the user is changing amount_from money in
    currency currency_from to the currency currency_to. The value
    returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code

    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""
    doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=%s&to=%s&amt=%s'%(currency_from, currency_to, amount_from))
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    jstr = jstr.split(' : ')
    error = jstr[4].split('"')[1]
    if error != '':
        return error
    else:
        num = (jstr[2].split(', ')[0]).replace('"','').split(' ')[0]
        num = float(num)
        return num

def testAll():
    """Unit test for module currency

    When run as a script, this module invokes several procedures that
    test the various functions in the module currency."""
    assert('Source currency code is invalid.' == exchange('a','b','c'))
    assert(3.35238 == exchange('USD','EUR','4'))
    print("All tests passed")

if __name__ == '__main__':
    currency_from=input('the currency on hand e.g. USD >>>')
    currency_to=input('the currency to convert to e.g. EUR >>>')
    amount_from=input('amount of currency to convert >>>')
    num = exchange(currency_from, currency_to, amount_from)
    print(num)
