def fn(function):
    """ funkce pro zjištění jména funkce """
    return function.__name__

def log_and_count(*args2, **kwargs2):
    """ továrna dekorátorů """
    def decorator(function):
        """ dekorátor """
        def function_inside(*args, **kwargs):
            if "key" in kwargs2:
                kwargs2["counts"][kwargs2["key"]] += 1
            elif args2:
                kwargs2["counts"][list(args2)[0]] += 1
            else:
                kwargs2["counts"][fn(function)] += 1
            """ funkce tiskne formátovaný řetězec s informacemi o funkci
                a o jejích agrumentech """
            print("called {2} with {0} and {1}".format(args,kwargs,fn(function)));
            return function(*args, **kwargs)
        return function_inside
    return decorator
