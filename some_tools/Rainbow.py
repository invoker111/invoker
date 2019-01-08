def rainbow(color, speed=1):
    """
    制造彩虹颜色变化的R,G,B

    传入RGB数值返回变化后的RGB
    """
    (r, g, b) = color
    # R
    if b == 255 and g == 0:
        if r < 255:
            R = r + speed
        else:
            R = 255
    elif b == 0 and g == 255:
        if r > 0:
            R = r - speed
        else:
            R = 0
    else:
        R = r
    # G
    if r == 255 and b == 0:
        if g < 255:
            G = g + speed
        else:
            G = 255
    elif r == 0 and b == 255:
        if g > 0:
            G = g - speed
        else:
            G = 0
    else:
        G = g
    # B
    if r == 0 and g == 255:
        if b < 255:
            B = b + speed
        else:
            B = 255
    elif r == 255 and g == 0:
        if b > 0:
            B = b - speed
        else:
            B = 0
    else:
        B = b
    
    return (R,G,B)

