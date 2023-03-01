#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author:      thepoy
# @Email:       thepoy@163.com
# @File Name:   convert.py
# @Created At:  2022-02-12 09:03:09
# @Modified At: 2023-03-01 11:12:23
# @Modified By: thepoy

HEADER = """# Rime dictionary: wubi-98-single-gbk
# encoding: utf-8

name: wubi-98-single-gbk
version: "0.1"
sort: by_weight
columns:
  - text
  - code
  - weight
  - stem
encoder:
  exclude_patterns:
    - "^z.*$"
  rules:
    - length_equal: 2
      formula: "AaAbBaBb"
    - length_equal: 3
      formula: "AaBaCaCb"
    - length_in_range: [4, 10]
      formula: "AaBaCaZa"

...
"""


def main():
    with open("src/98-single-gbk.txt", encoding="utf-8") as fr:
        with open("dist/wubi-98-single-gbk.dict.yaml", "w", encoding="utf-8") as fw:
            fw.write(HEADER)

            for line in fr:
                temp = line[:-1].split("\t")
                new_line = f"{temp[1]}\t{temp[0]}\n"
                fw.write(new_line)


if __name__ == "__main__":
    main()
