#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author toby
'''
import filehelper
import json

f_h = filehelper.FileHelper()
f_h.setFilePath("source.txt")
f_h.readFile()
json_content = f_h.textToJSOn()
for controller, info in enumerate(json_content):
    info_body = ""
    for info_body_key in json_content[info]:
        info_body = "%s\n%s%s%s%s%s%s"%(info_body, "function ", info_body_key, " ", "()", " {", "}")
    info_body = "%s\n%s%s%s\n%s\n%s\n%s"%("<?php", "class ", info+"Controller "+"extends "+"Eye", " {", info_body, "}", "?>")
    f_h.createFileByText(info+"Controller.php", info_body)