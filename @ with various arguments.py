def my_decorator(func):
    print("Hi!")
    def wrapper():
        print("I'm decorator function, hi!")
        func()
    return wrapper





# decorated_function = my_decorator(lazy_function)
# print(decorated_function())


@my_decorator
def lazy_function():
    print("zzzzzzzzz")


lazy_function()

def decorator_maker():
    print("Я создаю декораторы! Я буду вызван только раз: "+\
          "когда ты попросишь меня создать тебе декоратор.")

    def my_decorator(func):
        print("Я - декоратор! Я буду вызван только раз: в момент декорирования функции.")

        def wrapped():
            print("Я - обёртка вокруг декорируемой функции. "
                  "Я буду вызвана каждый раз когда ты вызываешь декорируемую функцию. "
                  "Я возвращаю результат работы декорируемой функции.")
            return func

        print("Я возвращаю обёрнутую функцию.")
        return wrapped


    print("Я возвращаю декоратор.")
    return my_decorator

# New decorator. Call of function


new_decorator = decorator_maker()

# Now we decorate the function

def decorated_function():
    print("Я - декорируемая функция.")


decorated_function()


decorated_function = new_decorator(decorated_function)


"""Аргументы декораторов"""

def decorator_maker_with_arguments(dec_arg1, dec_arg2):
    # Вверху переданы аргументы декоратора
    print(f"Я создаю декораторы! И я получил следующие аргументы: {dec_arg1}, {dec_arg2}")

    def my_decorator(func):
        print(f"Я - декоратор. И ты всё же смог передать мне эти аргументы: {dec_arg1},{dec_arg2}")

        # Здесь переданы аргументы функции
        def wrapped(function_argument_1, function_argument_2):
            print("Я - обёртка вокруг декорируемой функции.\n"
                  "И я имею доступ ко всем аргументам: \n"
                  "\t- и декоратора: {0} {1}\n"
                  "\t- и функции: {2} {3}\n"
                  "Теперь я могу передать нужные аргументы дальше".format(dec_arg1, dec_arg2, function_argument_1, function_argument_2 ))
            return func(function_argument_1, function_argument_2)

        return wrapped
    return my_decorator


print()



@decorator_maker_with_arguments("Леонард", "Шелдон")
def decorated_function_with_arguments(function_arg1, function_arg2):
    print("Я - декорируемая функция и я знаю только о своих аргументах: {0}, {1}".format(function_arg1, function_arg2))


print()
decorated_function_with_arguments("Реджеш", "Говард")


print("More arguments")

c1 = "Penny"
c2 = "Lesley"

@decorator_maker_with_arguments ("Leonard", c1)
def dec_func_with_args(func_arg1, func_arg2):
    print(f"I'm a decorated function and I know only about my arguments: {func_arg1}, {func_arg2}")


dec_func_with_args(c2, "Howard")


# Декораторы для декораторов

def decorator_with_args(decorator_to_enhance):
    """
        Эта функция задумывается КАК декоратор и ДЛЯ декораторов.
        Она должна декорировать другую функцию, которая должна быть декоратором.
        Лучше выпейте чашку кофе.
        Она даёт возможность любому декоратору принимать произвольные аргументы,
        избавляя Вас от головной боли о том, как же это делается, каждый раз, когда этот функционал необходим.
    """
    # Мы используем тот же трюк, который мы использовали для передачи аргументов:
    def decorator_maker(*args, **kwargs):
        def decorator_wrapper(func):
         # Мы возвращаем то, что вернёт нам изначальный декоратор, который, в свою очередь
         # ПРОСТО ФУНКЦИЯ (возвращающая функцию).
         # Единственная ловушка в том, что этот декоратор должен быть именно такого
         # decorator(func, *args, **kwargs)
         # вида, иначе ничего не сработает
            return decorator_to_enhance(func, *args, **kwargs)
        return decorator_wrapper
    return decorator_maker

print()
@decorator_with_args
def decorated_decorated(func, *args, **kwargs):
    def wrapper(function_arg1, function_arg2):
        print("Мне тут передали...:{0} и {1}".format(args, kwargs))
        return func(function_arg1, function_arg2)
    return wrapper
print()
@decorated_decorated(42, 404, 1024)
def decorated_function(func1, func2):
    print("HI!", func1, func2)
decorated_function("Universe and ", "everything else")

# examples of use
def benchmark(func):
    """
        Декоратор, выводящий время, которое заняло
        выполнение декорируемой функции.
    """
    import time
    def wrapper(*args, **kwargs):
        t = time.clock()
        res = func(*args, **kwargs)
        print(func.__name__, time.clock())
        return res
    return wrapper


def logging(func):
        """
        Декоратор, логирующий работу кода.
        (хорошо, он просто выводит вызовы, но тут могло быть и логирование!)
        """
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            print(func.__name__, args, kwargs)
            return res
        return wrapper


def counter(func):
        """
        Декоратор, считающий и выводящий количество вызовов
        декорируемой функции.
        """
        def wrapper(*args, **kwargs):
            wrapper.count += 1
            res = func(*args, **kwargs)
            print(f"{func.__name__} была вызвана: {wrapper.count}x")
            return res
        wrapper.count = 0
        return wrapper


print()


@benchmark
@logging
@counter
def reverse_string(string):
    return str(reversed(string))


print(reverse_string("We can give and receive reason"))
print(reverse_string("Only Europe knows..."))








