import colorgram


colors = colorgram.extract('hirst.jpg', 10)
rgb_list = []

index = 0
for color in colors:
    rgb = color.rgb
    red = rgb[0]
    green = rgb[1]
    blue = rgb[2]
    color_tuple = (red, green, blue)
    rgb_list.append(color_tuple)

print(rgb_list)

