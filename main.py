import os
import pprint


def book_recipes(path_):
    recipe = {}
    with open(path_, encoding='utf-8') as file:
        str_ = file.readlines()
        item = 0
        while item <= len(str_):
            recipe[str_[item].strip()] = []
            itr = item + 1
            step = int(str_[itr].strip())
            prod_list = []
            for i in range(1, step+1):
                product = str_[item+i+1].strip().split("|")
                prod_dict = dict()
                prod_dict['ingredient_name'] = product[0]
                prod_dict['quantity'] = int(product[1])
                prod_dict['measure'] = product[2]
                prod_list.append(prod_dict)
            recipe[str_[item].strip()] = prod_list
            cook_book.update(recipe)
            item = itr + step + 2
    return cook_book


def get_shop_list_by_dishes(dishes_, count):
    for item in dishes_:
        prod_list = cook_book[item]
        for prod in prod_list:
            dict_quantity = dict()
            dict_measure = dict()
            measure = prod['measure']
            quantity = int(prod['quantity']) * count
            dict_quantity['quantity'] = quantity
            dict_measure['measure'] = measure
            dict_measure.update(dict_quantity)
            if prod['ingredient_name'] in shop_dict:
                shop_dict[prod['ingredient_name']]['quantity'] = shop_dict[prod['ingredient_name']]['quantity']\
                                                                 + quantity
            else:
                shop_dict[prod['ingredient_name']] = dict_measure
    return shop_dict


def len_file_dict(path_):
    with open(path_, encoding='utf-8') as file:
        str_ = int(len(file.readlines()))
        len_f_dict[file.name] = str_
    return len_f_dict


def merging_files(dict_):
    open(os.path.join(os.getcwd(), "result.txt"), 'w').close()
    for key, value in dict_.items():
        with open(key, encoding="utf-8") as file_r:
            with open(os.path.join(os.getcwd(), "result.txt"), "a") as file_w:
                file_w.write(os.path.basename(key))
                file_w.write('\n')
                file_w.write(str(value))
                file_w.write('\n')
                for i in range(value):
                    str_temp = file_r.readline()
                    file_w.write(str_temp)
                file_w.write('\n')
    return print("Запись в файл завершена")


if __name__ == '__main__':
    cook_book = {}
    shop_dict = dict()
    len_f_dict = dict()
    file_path = os.path.join(os.getcwd(), "recipes.txt")
    book_recipes(file_path)
    pprint.pprint(cook_book)
    dishes = list(cook_book.keys())
    person_count = int(input('Введите количество гостей: '))
    get_shop_list_by_dishes(dishes, person_count)
    pprint.pprint(shop_dict)
    file_path = os.path.join(os.getcwd(), "1.txt")
    len_file_dict(file_path)
    file_path = os.path.join(os.getcwd(), "2.txt")
    len_file_dict(file_path)
    file_path = os.path.join(os.getcwd(), "3.txt")
    len_file_dict(file_path)
    len_f_dict = dict(sorted(len_f_dict.items(), key=lambda x: x[1]))
    merging_files(len_f_dict)
