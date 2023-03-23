'''
A module used to encode and decode a message based on an encryption mechanism
'''

import functools


def ch_to_num(ch):
    '''
    Converts a unicode character to its corresponding integer shifted by a fixed amount based on an ecvryption mechanism

    Parameters
    ----------
    ch : str
        a single character string of length 1

    Returns
    -------
    index : int (0 <= int <= 94)
        corresponding position in set of permissible characters
    
    '''
    index = ord(ch) - 32  # shifted down by 32 to ensure first character ' ' has the index 0
    
    return index


def num_to_ch(num):
    '''
    Converts an integer to its corresponding unicode character shifted by a fixed amount based on an ecvryption mechanism

    Parameters
    ----------
    num : int
        position of character in a set of extended permissible characters

    Returns
    -------
    ch : str
        corresponding unicode character

    '''
    ch = chr(num%95 + 32)  # modulo ensures chr() argument is always within our desired range of integers from 32 to 126, corresponding to the respective unicode code of a character we are dealing with
    
    return ch


# add() and substract() functions are defined below to prevent labmda functions from being defined multiple times, encouraging code reuse and increasing readability

def add(x, y):
    '''
    Adds or concatenates two values, depending on default behaviour of type
    
    '''
    return x + y


def subtract(x, y):
    '''
    Subtracts or splits two values, depending on default behaviour of type
    
    '''
    return x - y


def encode(message, key):
    '''
    Encodes a given message based on the key and an encryption mechanism

    Parameters
    ----------
    message : str
        a message to be encrypted
    key : str
        a key used to encrypt a given message based on character reassignment rules

    Returns
    -------
    ciphertext : str
        an encrypted unreadable string of characters

    '''
    extended_key = key * ((len(message) // len(key)) + 1)  # string multiplication of the key, the number of times the key should be repeated to be the same length as the message, rounded up
    cut_key = extended_key[:len(message)]  # ensuring the altered key and the message are the exact same length
    key_indexes = map(ch_to_num, cut_key)  # coverting altered key string to integer representation of shifted unicode characters
    message_indexes = map(ch_to_num, message)  # converting message to integer representation of chifted unicode characters
    combined_indexes = map(add, key_indexes, message_indexes)  
    ciphertext = functools.reduce(add, map(num_to_ch, combined_indexes))  # converting combined integer representation back to a string of scrambled characters 
    
    return ciphertext


def decode(ciphertext, key):
    '''
    Decodes a given message based on the key and an encryption mechanism

    Parameters
    ----------
    ciphertext : str
        an encrypted unreadable string of characters
    key : str
        a key used to decrypt a given message based on character reassignment rules

    Returns
    -------
    message : str
        the original unencrypted message which is decoded using the key

    '''
    extended_key = key * ((len(ciphertext) // len(key)) + 1)  # string multiplication of the key, the number of times the key should be repeated to be the same length as the ciphertext, rounded up
    cut_key = extended_key[:len(ciphertext)]  # ensuring the altered key and the message are the exact same length
    key_indexes = map(ch_to_num, cut_key)  # coverting altered key string to integer representation of shifted unicode characters
    ciphertext_indexes = map(ch_to_num, ciphertext)  # converting message to integer representation of chifted unicode characters
    combined_indexes = map(subtract, ciphertext_indexes, key_indexes) 
    message = functools.reduce(add, map(num_to_ch, combined_indexes))  # converting combined integer representation back to the original comprehensible string
    
    return message