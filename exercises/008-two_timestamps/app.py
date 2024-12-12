def two_timestamp(hr1, min1, sec1, hr2, min2, sec2): 
    return abs((hr1-hr2)*3600 + (min1-min2)*60 + sec1-sec2)


# Invoke the function and pass two timestamps(6 intergers) as its arguments
print(two_timestamp(1,1,1,2,2,2))
