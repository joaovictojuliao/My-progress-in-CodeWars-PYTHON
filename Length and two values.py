def alternate(n, first_value, second_value):
    v=0    
    list=[]
    while v<n:
        if v<n:
            list.append(first_value)
            v=v+1
            if v<n:
                list.append(second_value)
                v=v+1
                
    return (list)
