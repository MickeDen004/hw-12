def my_new_shiny_decorator(function_to_decorate):
    def the_wrapper_for_original_function():
        print("I'm a code which works before the call of function")
        function_to_decorate()
        print("I'm the code which works after the call of function")
    return the_wrapper_for_original_function()





@my_new_shiny_decorator
def standalone_func():
    print("Я простая одинокая функция, ты ведь не посмеешь меня изменять")

def getTalk (type="shout"):
    def shout(word="yeah"):
        return word.capitalize()+"!"
    def whisper(word="yeah"):
        return word.lower()+"..."

    if type == shout:
        return shout
    else:
        return whisper


talk = getTalk()
print(talk("whisper"))


def a_decorator_passing_arguments(func_to_decorate):
    def a_wrapper_accepting_arguments(arg1, arg2):
        print(f"Look what I've got: {arg1}, {arg2}")
        func_to_decorate(arg1, arg2)
    return a_wrapper_accepting_arguments


@a_decorator_passing_arguments
def my_full_name(first_name, second_name):
    return print(f"My name is {first_name} {second_name}")


print(my_full_name("Micke", "Denisov"))


# Remember args and kwargs

def test_var_args(farg, *args):
    print("formal argument: ", farg)
    for arg in args:
        print("another arg: ", arg)


test_var_args(1, "two", 3)


def poet(n, *poems):
    print(f"Poets name: {n}")
    for p in poems:
        print("Poem on the website: ", p)


poet("Hobert", "Seven", "Penguin", "Soul")


def arbitrary_arguments(function_to_decorate):
    def accepting_arguments(*args, **kwargs):
        print("Chto peredac?")
        print(args)
        print(kwargs)
        function_to_decorate(args, kwargs)
    return accepting_arguments()

@arbitrary_arguments
def function_with_no_argument():
    print("Python is cool, no argument here.")

function_with_no_argument()

@arbitrary_arguments
def function_with_arg(a, b, c):
    print(a, b, c)


function_with_arg(1, 2, 3)





