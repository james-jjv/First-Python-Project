# Q1: Cipher via functional programming (15 marks)

---

## Description

In this question, you are asked to solve the PS9 Q3b again, but this time it is solved via the functional programming approach.

---

## Instructions

Using the same encryption and decryption mechanism as PS9 Q3b cipher, do the following:

1. In [src/crypto.py](src/crypto.py), write the function definition for the function `encode()`, for which it takes 2 arguments: a message to encrypt (type: `str`, length > 0) and a key (type: `str`, length > 0). It returns the encrypted message (type: `str`, length > 0) based on the given key

2. In [src/crypto.py](src/crypto.py), write the function definition for the function `decode()`, for which it takes 2 arguments: a encrypted message to decrypt (type: `str`, length > 0) and a key (type: `str`, length > 0). It returns the decrypted message (type: `str`, length > 0) based on the given key

3. In [src/report.ipynb](src/report.ipynb), demonstrate the use of the two functions

---

## Example use

Example use of the functions:

```
>>> encode("ProgrammingforDataScience", 'passcode123')
'ATc[VQRSz!z7Qf8EdF9t{x_EY'

>>> decode("ATc[VQRSz!z7Qf8EdF9t{x_EY", 'passcode123')
'ProgrammingforDataScience'
```

---

## Things to show in the report

* As mentioned in `Instructions`, part 3 needs to be shown in the report

---

## Note

* Please treat `cypto.py` as a _module_
* Only the following built-in functions / functions from the Python standard library can be used:
  * built-in function `ord()`
  * built-in function `chr()`
  * built-in function `len()`
  * built-in function `map()`
  * `reduce()` from `functools`
* No loops should be used
* Any function written must be pure function
* No change in variable value or modification of objects
* You can reuse the function definitions you have written in Q3a PS9, _given they fulfil the requirements above_
