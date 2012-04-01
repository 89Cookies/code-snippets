# -*- coding: utf-8 -*-

# it works alright, but...
s = "Hello, 世界"
print s

# slicing operations do work so well
print s[:-4] + "."

# it should print just "Hello.", but it prints "Hello" + plus garbage

# BUT, this works just fine
s = u"Hello, 世界"

print s
print s[:-4] + "."
