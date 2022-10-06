from turtle import delay
from modul import *
import time

# assume value is a decimal
def transform_to_rupiah_format(value):
    str_value = str(value)
    separate_decimal = str_value.split(".")
    after_decimal = separate_decimal[0]
    before_decimal = separate_decimal[1]

    reverse = after_decimal[::-1]
    temp_reverse_value = ""

    for index, val in enumerate(reverse):
        if (index + 1) % 3 == 0 and index + 1 != len(reverse):
            temp_reverse_value = temp_reverse_value + val + "."
        else:
            temp_reverse_value = temp_reverse_value + val

    temp_result = temp_reverse_value[::-1]

    return "Rp " + temp_result + ",0" + before_decimal


def formatrupiah(uang):
    y = str(uang)
    if len(y) <= 3:
        return 'Rp ' + y 
    else:
        p = y[-3:]
        q = y[:-3]
        return formatrupiah(q) + '.' + p 
      

# default budgeting percentage (single)
living = 0.30
playing = 0.20
saving = 0.50

# # default budgeting percentage (married)
# living = 0.30
# playing = 0.15
# saving = 0.55

budget = int(input('Masukkan pemasukan anda: '))


# tiap tiap kategorinya
percent_living = living * 100
percent_playing = playing * 100
percent_saving = saving * 100
percentage = [percent_playing, percent_living, percent_saving]
sum = 00.0
percent_budget = (living + playing + saving)*100

budget_living = budget * living
budget_playing = budget * playing
budgett_saving = budget * saving

print('========================================================')
for x in percentage:
    print('Checking Persen Budgeting '+'{}'.format(sum)+' %'+' (Checking)')
    time.sleep(2)
    sum += x

print('Checking Persen Budgeting '+'{}'.format(percent_budget)+'%'+' (Done)')
time.sleep(2)
print('Budgeting anda adalah sebesar {}'.format(formatrupiah(budget))+',00')
print('Pemasukan anda untuk kebutuhan hidup adalah\t: {}'.format(
    transform_to_rupiah_format(budget_living)))

print('Pemasukan anda untuk kegiatan adalah\t\t: {}'.format(
    transform_to_rupiah_format(budget_playing)))
print('Pemasukan anda untuk tabungan adalah\t\t: {}'.format(
    transform_to_rupiah_format(budgett_saving)))
print('========================================================')
