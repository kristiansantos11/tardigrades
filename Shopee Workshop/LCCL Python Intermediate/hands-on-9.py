# Write a function to convert RGB values to hexadecimal representation.
# Valid decimal values for RGB are 0-255. Values that fall out of that range must
# be rounded to the closest valid value.

def correct(n):
    return min(255, max(n, 0))

def rgb(r, g, b):
    r, g, b = correct(r), correct(g), correct(b)
    return f'#{r:0>2x}{g:0>2x}{b:0>2x}'.upper()

print(rgb(255, 128, 255))