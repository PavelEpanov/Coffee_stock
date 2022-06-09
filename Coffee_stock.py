import os


def main():
    line_1 = int(
        input("'1' - Get info, '2' - Search info, '3' - Change info, '4' - delete brand: "))

    if line_1 == 1:
        get_info_of_coffee()
        show_info_of_coffe()
    elif line_1 == 2:
        search_info_of_coffee()
    elif line_1 == 3:
        change_funt_of_coffee()
    elif line_1 == 4:
        delete_info_of_coffee()


def show_info_of_coffe():
    coffee_info = open("coffee_stock.txt", "r")

    brand = coffee_info.readline()

    while brand != "":
        funt = coffee_info.readline()

        brand = brand.strip("\n")
        funt = funt.rstrip("\n")

        print("--------------")
        print(f"Brand is {brand}")
        print(f"Funt are {funt}")

        brand = coffee_info.readline()

    coffee_info.close()


def get_info_of_coffee():
    coffe_info = open("coffee_stock.txt", "a")

    print("If youw want add a Brand Coffee - take - '1' if youn want quit take - '2'")

    x = int(input("'1' or '2': "))

    while x != 2 and x == 1:

        name_of_brand = input("Brand is: ")
        funt_of_this_brand = float(input("Funt this brand is: "))

        name_of_brand = name_of_brand.rstrip("\n")
        funt_of_this_brand = str(funt_of_this_brand)
        funt_of_this_brand = funt_of_this_brand.rstrip("\n")

        coffe_info.write(name_of_brand + "\n")
        coffe_info.write(str(funt_of_this_brand) + "\n")

        x = int(input("'1' or '2': "))

    coffe_info.close()
    print("Data have been written")


def search_info_of_coffee():
    found = False

    search = input("Your detail is: ")

    coffe_file = open("coffee_stock.txt", "r")

    descr = coffe_file.readline()

    while descr != "":
        qty = coffe_file.readline()

        descr = descr.rstrip("\n")

        if descr == search:
            print(f"Details are : {descr}")
            print(f"Funt are : {qty} ")
            print()
            found = True

        descr = coffe_file.readline()

    coffe_file.close()

    if found == False:
        print("I dont know what is it")


def change_funt_of_coffee():

    main_file = open("coffee_stock.txt", "r")
    new_file = open("new_coffee_stock.txt", "w")

    found = False

    detail = input("Detail is: ")
    new_funt = float(input("New funt is: "))

    detail_file_main = main_file.readline()
    while detail_file_main != "":
        detail_file_main = detail_file_main.rstrip("\n")

        funt_file_main = main_file.readline()
        if detail_file_main == detail:
            new_file.write(detail_file_main + "\n")
            new_file.write(str(new_funt) + "\n")
            found = True
        else:
            new_file.write(detail_file_main + "\n")
            new_file.write(str(funt_file_main) + "\n")
        detail_file_main = main_file.readline()

    if found == False:
        print("I dont see it")
    else:
        print("Data has been changed")

    main_file.close()
    new_file.close()

    os.remove("coffee_stock.txt")
    os.rename("new_coffee_stock.txt", "coffee_stock.txt")


def delete_info_of_coffee():

    detail_user = input("Detail is: ")

    main_file = open("coffee_stock.txt", "r")
    new_coffe_file = open("new_coffe_stock.txt", "w")

    found = False

    detail = main_file.readline()

    while detail != "":
        detail = detail.rstrip("\n")

        funt = main_file.readline()

        if detail != detail_user:
            new_coffe_file.write(detail + "\n")
            new_coffe_file.write(str(funt) + "\n")
            found = True
        detail = main_file.readline()

    if found == True:
        print("Data nas been changed")
    else:
        print("I dont see this brand")

    main_file.close()
    new_coffe_file.close()

    os.remove("coffee_stock.txt")
    os.rename("new_coffe_stock.txt", "coffee_stock.txt")


main()
