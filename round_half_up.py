from decimal import Decimal

def round_half_up(num, d):
    if type(num)==float or type(num)==str:
        multiplier = 10 ** (d)
        num=Decimal(str(num))
        if num>0:
            num = Decimal(str(num)) * multiplier
            new_num = Decimal(num) + Decimal('0.5')
            return int(new_num)/multiplier
        else:
            new_num=round_half_up(str(Decimal(num) *-1), d)*-1
            if new_num!=int(num*multiplier)/multiplier:
                new_num=Decimal(str(new_num))+Decimal(str(2/multiplier))
            return float(new_num)
    else:
        return float(num)