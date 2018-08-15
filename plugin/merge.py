# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import os

def updateKeyValue(line, result):
    # key = value # comm
    key = line[:line.find('=')].strip()
    if key in result:
        value = line[line.find('=')+1:line.find('#')].strip()
        result[key] = value

def getKeyValue(line, result):
    key = line[:line.find('=')].strip()
    value = line[line.find('=')+1:line.find('#')].strip()
    result[key] = value

# this is current uncrustify's defaults confiture of new version
memap = {}
with open("defaults.cfg", "r") as bkcfg:
    for line in bkcfg.readlines():
        line = line.strip()
        if ((line == '') or (line[0]=='#')):
            continue
        #  backlines.append(line)
        getKeyValue(line, memap)


# this is your last configure version
cfglines = []
with open("me.cfg", "r") as mecfg:
    for line in mecfg.readlines():
        line = line.strip()
        #  if ((line == '') or (line[0]=='#')):
        if (line == ''):
            continue

        if line[0] == '#':
            cfglines.append(line)
            continue

        # if it's not comment line, get key and value
        key = line[:line.find('=')].strip()
        value = line[line.find('=')+1:line.find('#')].strip()
        comment = line[line.find('#')-1:].strip()
        # find key in memap, and if find, replace value, or use new value
        if key in memap:
            value = memap[key]

        newline = key + "=" + value + comment
        cfglines.append(newline)

# 输出
with open("new.cfg", "w+") as newcfg:
    #  newcfg.writelines(cfglines)
    newcfg.writelines([line+'\n' for line in cfglines])

if __name__ == '__main__':
    pass
