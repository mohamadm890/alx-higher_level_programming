#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list_v = my_list[:]
    for i in range(len(list_v)):
        if list_v[i] == search:
            list_v[i] = replace
    return list_v
