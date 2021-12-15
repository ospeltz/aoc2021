def read_file(nm, no_newline=True):
    res = []
    with open("data/" + nm) as f:
        for line in f:
            if no_newline:
                line = line.replace('\n','')
            res.append(line)
    return res

def print_arr(ar):
    for a in ar:
        print(a)

def print_map(ma):
    for k in ma:
        print(k, ":", ma[k])

