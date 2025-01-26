import inspect
from inspect import getmodule
from module_10 import module_10_4
from time import sleep
from pprint import pprint



def introspection_info(obj):

    # insp_ = (inspect.getmembers(obj))
    # for at_r in insp_:
    #     print(at_r, type(at_r))
    attr_ = []
    mod_ = []
    meth_  = []
    cls_ = []
    funk_ = []
    for at_r in dir(obj):

        attr = getattr(obj, at_r)
        if inspect.ismodule(attr):
            # print('Модуль: ', at_r, type(attr))
            mod_.append(at_r)
        elif inspect.ismethod(attr):
            # print('Метод: ', at_r, type(attr))
            meth_.append(at_r)
        elif inspect. isclass(attr):
            # print('Класс: ', at_r, type(attr))
            cls_.append(at_r)
        elif inspect. isfunction(attr):
            # print('Функция: ', at_r, type(attr))
            funk_.append(at_r)
        else:
            # print('Атрибут: ', at_r, type(attr))
            attr_.append(at_r)

    print('Тип:', type(obj))
    print('Атрибуты: ')
    pprint(attr_)
    print('Функции: ')
    pprint(funk_)
    print('Классы: ')
    pprint(cls_)
    print('Методы: ')
    pprint(meth_)
    print('Модули: ')
    pprint(mod_)
    print(inspect.getmodule(obj))




# obj_ = [1,2,3,4,5,6]
# obj_ = 795
#obj_ = "Обычная строка"
# obj_ = sleep
#obj_ = module_10_4.Cafe
obj_ = module_10_4.Cafe.guest_arrival
inf_ = introspection_info(obj_)
