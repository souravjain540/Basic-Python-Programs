# Buy 9 Get 1 Free

def buy_nine_get_one_free(my_quantity, my_product_price):
    my_price_to_pay = 0
    for my_q in range(1,my_quantity+1):
        if my_q % 10 == 0:
            my_price_to_pay = my_price_to_pay
        else:
            my_price_to_pay += my_product_price
    return my_price_to_pay


# Asserts
assert buy_nine_get_one_free(8, 2.50) == 20
assert buy_nine_get_one_free(9, 2.50) == 22.50
assert buy_nine_get_one_free(10, 2.50) == 22.50
assert buy_nine_get_one_free(11, 2.50) == 25