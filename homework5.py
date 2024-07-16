immutable_var = 1, 4.5, 'Aaa', [3, 8, 10]
print(immutable_var, ',', type(immutable_var))
# immutable_var[0] = 10 не даёт сменить, ругается что неизменяемое что правильно закомменчено чтоб работало
immutable_var[3][2] = 35  # а тут даёт, потому что списки внутри кортежа менять можно
print(immutable_var[3])
mutable_list = [1, 12, 'AaaA', True]
print(mutable_list, ',', type(mutable_list))
mutable_list[2] = 'Modified'
print(mutable_list)  # ну тут и так ясно что всё ясно PS ой не дай бог в больших проектах такие комменты

