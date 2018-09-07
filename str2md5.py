# -*- coding: utf-8 -*-
import hashlib

name = input('Please input the name:')
nm = hashlib.md5()
nm_str = name + 'the-salt'
nm.update(name.encode('utf-8'))
print(nm.hexdigest())