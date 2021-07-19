def closest_higher_mod_5(x):
    remainder = x % 5
    if remainder == 0:
        return x
    x += (5 - remainder)
    return x
