with open('1.txt', encoding='utf8') as file_1:
    lines_1 = file_1.read()
    file_1.seek(0)
    count_1 = len(file_1.readlines())

with open('2.txt', encoding='utf8') as file_2:
    lines_2 = file_2.read()
    file_2.seek(0)
    count_2 = len(file_2.readlines())

with open('3.txt', encoding='utf8') as file_3:
    lines_3 = file_3.read()
    file_3.seek(0)
    count_3 = len(file_3.readlines())

l_1 = (f"{file_1.name} '\n' {count_1}'\n' {lines_1}'\n'")
l_2 = (f"{file_2.name} '\n' {count_3}'\n' {lines_2}'\n'")
l_3 = (f"{file_3.name} '\n' {count_3}'\n' {lines_3}'\n'")

with open('4.txt', 'w', encoding='utf8') as file_4:
    file_4.writelines(f'{l_2} {l_1} {l_3}')


