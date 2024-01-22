import pprint

cook_book_1 = {}

def cook_book_init():

        with open("cook_book.txt", "r", encoding="utf-8") as file1:

            for i in range(7):
                # считываем строку
                name_dish = file1.readline().strip()
                # прерываем цикл, если строка пустая

                if not name_dish:
                    continue

                else:
                    cook_book_1[name_dish.strip()] = []
                    count_ingridient = int(file1.readline().strip())

                    for i in range(count_ingridient):
                        name_ingridient = file1.readline().strip().split(' ')
                        name_ingridient.remove("|")
                        name_ingridient.remove("|")
                        name_ingridient_set = {}
                        if len(name_ingridient) == 4:
                            name_ingridient[0] = name_ingridient[0] + ' ' + name_ingridient[1]
                            name_ingridient.pop(1)
                        name_ingridient_set["ingridient_name"] = name_ingridient[0]
                        name_ingridient_set["quantity"] = int(name_ingridient[1])
                        name_ingridient_set["measure"] = name_ingridient[2]
                        cook_book_1[f"{name_dish}"].append(name_ingridient_set)

def get_shop_list_by_dishes(dishes, person_count):

    result = {}
    for i in dishes:
        for j in cook_book_1[i]:
            j["quantity"] *= person_count

    for i in dishes:
        for j in cook_book_1[i]:
            if j["ingridient_name"] in result:
                result[j["ingridient_name"]]["quantity"] += j["quantity"]
            else:
                result[j["ingridient_name"]] = {"measure": j["measure"], "quantity": j["quantity"]}

    return pprint.pprint(result)

cook_book_init()

get_shop_list_by_dishes(["Запеченный картофель", "Омлет"], 2)
print(cook_book_1)
