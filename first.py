#!/usr/bin/python3
"""
# @filename           :  first.py
# @author             :  Copyright (C) Church.Zhong
# @date               :  Fri Sep 16 02:02:34 PM HKT 2022
# @function           :
# @see                :  https://docs.python.org/3/library/datetime.html
# @require            :  Python 3.10.4 works well.
# @style              :  https://google.github.io/styleguide/pyguide.html
"""

# import os
# import sys
import time

# import re
# from datetime import datetime
# from datetime import timedelta
# import argparse

from problems.easy import DATA00001


def work():
    """
    Description : main
    """
    print('hello world')
    print(DATA00001["title"])
    print(DATA00001["url"])
    print(DATA00001["entry"])


def main():
    """
    Description : main
    """
    start = time.time()
    work()
    print(f'# running time:{time.time() - start}')


if __name__ == "__main__":
    main()

# t=first.py;flake8 --max-line-length 128 --indent-size 4 ${t};pylint --max-line-length=128 --indent-after-paren=4 ${t};
