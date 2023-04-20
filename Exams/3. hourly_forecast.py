def forecast(*args):
    key_order = ["Sunny", "Cloudy", "Rainy"]

    sorted_data = sorted(args, key=lambda x: (key_order.index(x[1]), x[0]))

    output = '\n'.join(f"{location} - {weather}" for location, weather in sorted_data)
    return output


print(forecast(

    ("Beijing", "Sunny"),

    ("Hong Kong", "Rainy"),

    ("Tokyo", "Sunny"),

    ("Sofia", "Cloudy"),

    ("Peru", "Sunny"),

    ("Florence", "Cloudy"),

    ("Bourgas", "Sunny")))