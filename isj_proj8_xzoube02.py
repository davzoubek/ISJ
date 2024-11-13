def first_with_given_key(iterable, key=lambda y: y):
    done=list()
    it=iter(iterable)
    while not False:
        try:
            value=next(it)
            if key(value) not in done:
                yield value
                done.insert(-1,key(value))
        except StopIteration:
            break