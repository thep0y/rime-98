#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author:    thepoy
# @Email:     thepoy@163.com
# @File Name: convert.py
# @Created:   2022-02-12 09:03:09
# @Modified:  2022-02-12 09:24:14


def main():
    with open("src/98-single-gbk.txt") as fr:
        with open("dist/wubi_98_single_gbk.dict.yaml", "w") as fw:
            for line in fr:
                temp = line[:-1].split("\t")
                new_line = f"{temp[1]}\t{temp[0]}\n"
                fw.write(new_line)


if __name__ == "__main__":
    main()
