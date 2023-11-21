def full_parmutation(current_name, name, m):
    if len(current_name) == m:
        print(current_name)
    for i in range(0, len(name)):
        if not name[i] in current_name:
            full_parmutation(current_name + [name[i]], name, m)


names = ['Megatron', 'Fallen', 'Shockwave', 'Starscream']
full_parmutation([], names, 2)