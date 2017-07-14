def product_list(list_of_numbers):
    greatest_num = 0
    for value  in list_of_numbers:
        if  greatest_num < value:
            greatest_num = value
    print greatest_num

print product_list([4, 200, 201, 4, 5])
