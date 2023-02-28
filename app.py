#!/usr/bin/env python3
 
# -*- coding: utf-8 -*-

import os
import opencc

# 设置简繁体转换器
# s2t: 简体转繁体
# t2s: 繁体转简体
# 也可添加其他转换器，如：s2tw, tw2s, s2hk, hk2s, s2twp, tw2sp, t2tw, tw2t, t2hk, hk2t, t2jp, jp2t

converter = opencc.OpenCC('s2t')

# 设置文件目录 如果是windows系统，路径中的\需要转义  如 '.\\demo'
directory = './demo'

# 遍历文件目录中的所有文件
for root, dirs, files in os.walk(directory):
    for file in files:
        # 读取文件内容
        with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
            content = f.readlines()
        # 将文件内容中的简体转换为繁体
        converted_content = [converter.convert(line) for line in content]

        # 将转换后的内容写入文件
        with open(os.path.join(root, file), 'w', encoding='utf-8') as f:
            f.write("".join(converted_content))