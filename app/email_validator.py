# Reference: https://stackabuse.com/python-validate-email-address-with-regular-expressions-regex/

import re

regex = re.compile(
    r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")


def isValidEmail(email):
    if re.fullmatch(regex, email):
        return True
    return False
