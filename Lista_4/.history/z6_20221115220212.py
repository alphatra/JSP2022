def rgb_hsv(r,g,b):
    r,g,b/255
    c_max = max(r,g,b)
    c_min = min(r,g,b)
    delta = c_max-c_min
    return c_max,c_min
print(rgb_hsv(210,200,55))