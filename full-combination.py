

def find_m_people(cur_name, name, indx, m):
    if len(cur_name) == m:
        print(cur_name)
    for i in range(indx, len(name)):
        find_m_people(cur_name + [name[i]], name, i + 1, m)

name = ['a', 'b', 'c']

find_m_people([], name, 0 ,)