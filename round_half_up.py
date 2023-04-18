from decimal import Decimal

def round_half_up(num, d):
    multiplier = 10 ** (d)
    num = Decimal(str(num)) * multiplier
    if num>0:  
        new_num = Decimal(num) + Decimal('0.5')
    else:
        new_num = Decimal(num) + Decimal('1.0')
    final_num = int(new_num)/multiplier
    return final_num

print(round_half_up(17.445, 2))