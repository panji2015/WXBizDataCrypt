#!/usr/bin/env python
# -*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: panji
# Mail: 484511231.com
# Created Time:  2019-10-21 11:25:00
#############################################


from setuptools import setup, find_packages

setup(
    name="WXBizDataCrypt",
    version="0.1.0",
    keywords=("pip", "wxdc"),
    description="wx data crypt",
    long_description="微信加密数据解密",
    license="MIT Licence",

    url="https://https://github.com/panji2015/WXBizDataCrypt",
    author="panji",
    author_email="484511231@qq.com",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=['pycryptodome']
)
