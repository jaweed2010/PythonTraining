def print_map(**cntry_map):
    print(cntry_map)
    li = cntry_map.keys()
    for i in li:
        print(cntry_map[i])


print_map(USA="+1", IND="+91", ESP="+81", ITA="+71")
