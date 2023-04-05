'''Program to generate a random password.'''


import sys
import secrets

c_level = {'alphabet': """
    abcdefghijklm
    nopqrstuvwxyz
    ABCDEFGHIJKLM
    NOPQRSTUVWXYZ
""",
    'alphanumerical': """
    abcdefghijklm
    nopqrstuvwxyz
    ABCDEFGHIJKLM
    NOPQRSTUVWXYZ
    0123456789
""",
    'complete': """
    abcdefghijklm
    nopqrstuvwxyz
    ABCDEFGHIJKLM
    NOPQRSTUVWXYZ
    0123456789
    !#$%&*+?@^
"""}


def passwd(n: int, c: dict) -> str:
    '''
    Main function which generate a random password using hardware.

    Args:
        n (int) : The length of the password that is generated.
        c (list) : The level of complexity of the password.
            3 options of complexity : alphabet, alphanumerical, or complete.
    '''
    password = ''
    for i in range(n):
        password += secrets.choice(c[sys.argv[2]])
    return password


assert len(sys.argv) == 3

print(passwd(int(sys.argv[1]), c_level))
