#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by toshiki on 2017/12/07.


def fizzbuzz(n):
    """Fizzbuzzの実装

    引数の整数によって以下の文字列を返す.
    ３の倍数のとき'Fizz'. ５の倍数のとき'Buzz'. 15の倍数のとき'FizzBuzz'.
    それ以外のとき、n の文字列表現.

    >>> fizzbuzz(2)
    '2'
    >>> fizzbuzz(3)
    'Fizz'
    >>> fizzbuzz(5)
    'Buzz'
    >>> fizzbuzz(14)
    '14'
    >>> fizzbuzz(15)
    'FizzBuzz'

    :param int n:
    :rtype: basestring
    :return: 'Fizz' | 'Buzz' | 'FizzBuzz' | n
    """
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    if n % 3 == 0:
        return 'Fizz'
    if n % 5 == 0:
        return 'Buzz'
    return str(n)


def main():
    pass


if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
    print(fizzbuzz(100))
