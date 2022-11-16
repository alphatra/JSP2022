def rgb_hsv(r,g,b):
    r=r/255
    g=g/255
    b=b/255
    c_max = max(r,g,b)
    c_min = min(r,g,b)
    delta = c_max-c_min
    if c_max == c_min:
        h = 0
    elif c_max == r:
        h = (60 * ((g-b)/delta) + 360) % 360
    elif c_max == g:
        h = (60 * ((b-r)/delta) + 120) % 360
    elif c_max == b:
        h = (60 * ((r-g)/delta) + 240) % 360
    if c_max == 0:
        s = 0
    else:
        s = (delta/c_max)*100
    v = c_max*100
    return h, s, v
print(rgb_hsv(210,200,55))