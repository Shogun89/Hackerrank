def is_leap(year):
    leap = False
    cond1 = year % 4 ==0
    cond2 = year % 100 ==0
    cond3 = year % 400 == 0
    if cond1 and not cond2:
        leap =True
    elif cond1 and cond2 and cond3:
        leap =True
        
        

    
    return leap

year = int(input())