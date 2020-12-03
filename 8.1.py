cook_book = {}
with open('recipes.txt', encoding='utf8') as file_recipes:
    all_lines = file_recipes.readlines()
    zero = len([l for l in all_lines if l == '\n']) + 1

with open('recipes.txt', encoding='utf8') as file_recipes:
    for a in range(zero):
        while True:
            line = file_recipes.readline().rstrip('\n')
            if not line:
                break
            cook_book[line] = []
            n = int(file_recipes.readline().rstrip('\n'))
            ingredients = [file_recipes.readline().rstrip('\n').split('|') for i in range(n)]
            for ingredient in ingredients:
                new_values = [ingredient[0].rstrip(' '), int(ingredient[1]), ingredient[2].replace(' ', '')]
                new_key = ['ingredient_name', 'quantity', 'measure']
                cook_book[line].append(dict(zip(new_key, new_values)))

with open('new_recipes.txt', 'w', encoding='utf8') as new_file_recipes:
    for k, v in cook_book.items():
        new_file_recipes.write(f"{k}:'\n' {v}'\n'")


def get_shop_list_by_dishes(cook_book):
    name_dishes = input('Введите список блюд (через запятую): ').capitalize()
    person_count = int(input('Введите количество персон: '))
    # shop_list = {}
    for dishes, ingredients in cook_book.items():
        if name_dishes in dishes:
            for ingredient in ingredients:
                new_shop_list = dict(ingredient)
                ingredient['quantity'] *= person_count
                # if new_shop_list['ingredient_name'] not in shop_list:
                #     shop_list[new_shop_list['ingredient_name']] = new_shop_list
                # else:
                #     shop_list[new_shop_list['ingredient_name']]['quantity'] += new_shop_list['quantity']
                print(new_shop_list)
        # else:
        #     print("Данное блюдо не существует")

            # ingredients_shop =
            #     print(l)
get_shop_list_by_dishes(cook_book)



