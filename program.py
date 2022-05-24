from typing import List, Union


def series_sum(incoming: List[Union[int, float]]) -> str:
    """Принимает на вход список из строк и чисел с плавающей точкой, приводит его элементы к строкам и конкатенирует их.
    """
    result = ''
    for i in incoming:
        result += str(i)
    return result

series_sum([1, 1.5])