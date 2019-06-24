
#firstclass function
def func(tag):
    def callee(msg):
        print(f"<{tag}>{msg}</{tag}>")
    return callee


calc = func("p")
calc("Dotun")