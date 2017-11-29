#!/usr/bin/env python
# -*- coding:utf-8
import string

#本函数未涉及base36的四舍五入机制，如需四舍五入，请自行添加。
def base36encode(number):
    temp_value = str(number)
    temp_value = temp_value.split('.') if '.' in temp_value else [temp_value,'0']
    integer_part,decimal_part = temp_value
    result_int,result_dec = '',''
    dec = len(decimal_part)+ 10 if decimal_part != '0' else 0
    for digit in getb36Dint(int(integer_part)):
        result_int= digit + result_int
    for digit in getb36Ddec(decimal_part,dec):
        result_dec+=digit
    return result_int if result_dec == '0' else result_int+'.'+result_dec 


def getb36Dint(number):
    ALPHABET = string.digits+string.ascii_lowercase
    if number ==0:
        yield '0'
    while number !=0:
        result,reminder = divmod(number,36)
        yield ALPHABET[reminder]
        number = result


def getb36Ddec(number,dec=20):
    ALPHABET = string.digits+string.ascii_lowercase
    number = float('0.{}'.format(number))
    if number ==0:
        yield '0'
    while number !=0 and dec>0:
        result =int(number*36)
        reminder = number*36 - result
        yield ALPHABET[result]
        dec -=1
        number = reminder

print(base36encode(0.1,12))


