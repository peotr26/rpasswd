# rpasswd
This program will generate a random password using three levels of complexity using the random number generator from your computer. You can choose the length of the password.

## Instructions

The program takes 2 arguments after the file name. The first one correspond to the length of the password, and the second one to the level of complexity.  
Here is how to run the program on a *NIX system:

```bash
python rpasswd.py n complexity_level

# Example

python rpasswd.py 8 alphabet
```

## Different level of complexity:

- Alphabet : the password that will be generated will only contain ASCII letters, both capitalize and minimize.
- Alphanumerical : the password that will be generated will only contain ASCII letters and numbers.
- Complete : the password that will be generated will contain ASCII letters and numbers, as well as the following symbols :
  - `!`
  - `#`
  - `$`
  - `%`
  - `&`
  - `*`
  - `+`
  - `?`
  - `@`
  - `^`
