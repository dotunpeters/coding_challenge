


def decorator_function(original_function):
    print("Decorator_function runs")
    def wrapper_function(*args, **kwargs):
        print(f"{wrapper_function.__name__} runs")
        return original_function()
    return wrapper_function


@decorator_function
def original_function():
    print(f"{original_function.__name__} runs")

print(original_function())