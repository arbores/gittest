#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by toshiki on 2017/12/16.

from collections import namedtuple

Circle = namedtuple('Circle', "x, y, r")
Position = namedtuple('Position', "x, y")


def is_in_circle(circle: Circle, pos: Position) -> bool:
    """pos が circle の線上か内部のとき true """
    return (pos.x - circle.x) ** 2 + (pos.y - circle.y) ** 2 - circle.r ** 2 <= 0


def in_circle_num(x: int, y: int, r: int) -> int:
    """中心 (x,y) 半径 r の内部か線上にある格子点を返す

    >>> in_circle_num(0, 0, 0)
    1
    >>> in_circle_num(1, 2, 3)
    29
    >>> in_circle_num(4, 5, 6)
    113
    """
    xs = range(x - r, x + r + 1)
    ys = range(y - r, y + r + 1)
    posls = [Position(i, j) for i in xs for j in ys]
    return sum(map(lambda pos: is_in_circle(Circle(x, y, r), pos), posls))


def in_two_circle_num(c1: Circle, c2: Circle) -> int:
    """2つの円 c1, c2 に共通する線上か内部にある格子点

    >>> in_two_circle_num(Circle(1, 2, 3), Circle(4, 5, 4))
    10
    >>> in_two_circle_num(Circle(0, 1, 5), Circle(4, 8, 6))
    16
    >>> in_two_circle_num(Circle(0, 1, 6), Circle(3, 2, 3))
    28
    """
    xs = range(max(c1.x - c1.r, c2.x - c2.r), min(c1.x + c1.r, c2.x + c2.r) + 1)
    ys = range(max(c1.y - c1.r, c2.y - c2.r), min(c1.y + c1.r, c2.y + c2.r) + 1)
    pos_seq = (Position(i, j) for i in xs for j in ys)
    return sum(map(lambda pos: is_in_circle(c1, pos) and is_in_circle(c2, pos), pos_seq))


def main():
    s = input()
    ls = [Circle(*map(int, x.split(","))) for x in s.split()]
    print(in_two_circle_num(*ls))


main()

if __name__ == '__main__':
    main()
