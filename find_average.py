def find_average(units):
    units_count = 0
    units.sort(reverse=True)
    for val in range(100) :
        curr_count = 0
        for i in units :
            if val>=i :
                count = int(val/i)
                curr_count += count
                val -= i*count
        units_count += curr_count
    return units_count/100

units = list(map(int,input().split()))
print("AVG of units =",find_average(units))
