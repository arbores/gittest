#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by toshiki on 2017/12/14.

import pytest
from prime import is_prime


@pytest.mark.parametrize('num', [3, 4, 5])
def test_is_prime(num):
    assert is_prime(num)


def main():
    pass

if __name__ == '__main__':
    main()
