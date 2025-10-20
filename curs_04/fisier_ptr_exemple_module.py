def suma(a, b=0, *args, **kwargs):
    initial = a + b
    total = 0
    for elem in args:
        total += elem
    for key, value in kwargs.items():
        total += value
    return initial + total

model_var = 'exemplu pentru stringuri'