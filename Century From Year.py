def century(year):
    seculo=year//100
    if year%100==0:
        return seculo
    else:
        return seculo+1
