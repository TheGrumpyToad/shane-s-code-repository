def find_names(current_name, idx, names, m):
    if len(current_name) == m:
        print(current_name)
    for i in range(idx, len(names)):
        find_names(current_name + [names[i]], i + 1, names , m)

names = ['Megatron', 'Fallen', 'Shockwave', 'Starscream']

find_names([], 0 , names, 2)