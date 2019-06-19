from bond import make_bond

def interface():
    return make_bond("javascript")

def run_function(function_name):
    return interface().call(function_name)

def evaluate(code):
    return interface().eval(code)
