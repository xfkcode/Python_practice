# Union[类型,...,类型]
from typing import Union

l1: list[Union[int,str]] = [1,2,'xfk']
def func(data: Union[int,str]) -> Union[int,str]:
    pass

# 使用Union可以定义联合类型注解