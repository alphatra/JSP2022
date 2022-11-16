def rgb_hsv(r,g,b):
    c_max = max(list(r,g,b))
    c_min = min(list(r,g,b))
    return c_max,c_min
print(rgb_hsv(210,200,55))