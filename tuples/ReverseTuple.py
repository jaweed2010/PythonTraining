# With built-in function
tpl = (-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 2)
li_tpl = list(tpl)
li_tpl.sort(reverse=True)
tpl = tuple(li_tpl)
print(tpl)
