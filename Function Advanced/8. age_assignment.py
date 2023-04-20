def age_assignment(*args, **kwargs):
    names = []
    result = []

    for arg in args:
        if isinstance(arg, str):
            names.append(arg)

    names.sort()

    for name in names:
        first_letter = name[0].lower()
        age = kwargs.get(first_letter)
        if age is None:
            age = kwargs.get(first_letter.upper())
        result.append(f"{name} is {age} years old.")

    return '\n'.join(result)



