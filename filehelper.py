#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author toby
'''
import json
class FileHelper:
    file_path = None
    file_content = None

    def __init__(self, file_path=""):
        self.file_path = file_path
    def setFilePath(self, file_path):
        self.file_path = file_path
    def readFile(self):
        file_handle = open(self.file_path, 'r')
        file_text = file_handle.read()
        self.file_content = file_text
        file_handle.close()
        return file_text
    def textToJSOn(self):
        return json.loads(self.file_content)
    def createFileByText(self, new_file_path, new_file_content):
        f = open(new_file_path, "w")
        f.write(new_file_content)
        f.close()
