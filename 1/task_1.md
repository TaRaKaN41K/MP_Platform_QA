# Задание

Написать реализацию функции по примеру входных данных и результата

## Запуск 1
**Код вызова**
```python
my_code({
    'first': 'first_value',
    'second': 'second _value'
})
```
**Вывод консоли**
```console
first:
    first_value
second:
    second_value
```

## Запуск 2
**Код вызова**
```python
my_code({
    '1': {
        'child': '1/child/value'
    },
    '2': '2/value'
})
```
**Вывод консоли**
```console
1:
    child:
        1/child/value
2:
    2/value
```

# Решение
Функция реализована в `/1/task_1.py`

```python
def my_code(input_dict: dict, recursion_depth: int = 0):
    for dict_element in input_dict.items():
        if dict_element is not None:
            key = dict_element[0]
            value = dict_element[1]
            print(f"{recursion_depth * "\t"}{key}:")
            if type(value) == dict:
                my_code(input_dict=value, recursion_depth=recursion_depth+1)
            else:
                print(f"{(recursion_depth + 1) * "\t"}{value}")
```

## Результат работы

![Результат работы](/images/1_task_photo/result_of_work.png)