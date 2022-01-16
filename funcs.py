from os import remove


def read_file(nm, no_newline=True, remove_blanks=False):
    res = []
    with open("data/" + nm) as f:
        for line in f:
            if no_newline:
                line = line.replace('\n','')
            if not remove_blanks or (line != "" and line != "\n"): 
                res.append(line)
    return res

def print_arr(ar):
    for a in ar:
        print(a)

def print_map(ma):
    for k in ma:
        print(k, ":", ma[k])

