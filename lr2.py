import functools


def once(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        if inner.called >= 0:
            print("Запускаем foo")
            # func.called = () # Сравнить работу once в случае
            # сохранения внутри func и внутри inner
            res = (func(*args, **kwargs))
            inner.called += 1
            print(inner.called)
        return res

    print('init')
    inner.called = 0  # ?
    return inner


@once
# def foo(prev_el, prev_prev_el):
def foo(prev_el=0, prev_prev_el=1):
    """
    docs for foo
    """
    # предпред эл-т, пред эл-т
    # args[0], args[1]
    # [0, 1, 1, 2, 3, 5, 8, 13]
    # то, что у вас должно возвращать очередной
    # элемент ряда Фибоначчи
    cur_el = 0
    # если foo - вызывается впервые, то возвращаем 0
    # а если во второй раз, то 1
    # обычная ситуация
    cur_el = prev_el + prev_prev_el

    return cur_el


print("Очередное число ряда Ф.", foo())
print("Очередное число ряда Ф.", foo())
print("Очередное число ряда Ф.", foo())
# print("Очередное число ряда Ф.", foo())





def gen_foo():
    yield 0

    yield 1


fib_lst = gen_foo()

i = 0
while True:
    el = next(fib_lst)
    if i == 100:
        break
    i+=1


assert el == 354224848179261915075, "Number #100 of fib seq. "
