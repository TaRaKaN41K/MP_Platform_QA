# Задание

Даны две таблицы в виде списков:

`events: list[list] = [id, timedate, name, .., asset_id], ...]`

Id - PK, asset_id - FK (Null) 

`assets: listlist] = [id, name, …..], ...]`

Id - PK

Необходимо вывести результат работы запроса: 

```sql
SELECT event.id, event.name, asset.id, asset.name
FROM events as event LEFT JOIN assets as asset ON event.asset_id = asset.id
ORDER BY event.id
LIMIT 100
```

Реализовать функцию query

```python
def query(events: list, assets: list) -> list:
    pass
```

**Код вызова**
```python
events = [
    [4, '2024-03-28', 'Event 4', 1],
    [1, '2024-03-26', 'Event 1', 1], 
    [6, '2024-03-29', 'Event 6', 3], 
    [3, '2024-03-28', 'Event 3', 2],
    [5, '2024-03-29', 'Event 5', None],
    [2, '2024-03-27', 'Event 2', None],
    # Дополнительные события...
]

assets = [
    [4, 'Asset 4'], 
    [1, 'Asset 1'], 
    [3, 'Asset 3'], 
    [2, 'Asset 2'],
    # Дополнительные активы...
]

result = query(events, assets)

for row in result:
    print(row)
```
**Вывод консоли**
```console
[1, 'Event 1', 1, 'Asset 1']
[2, 'Event 2', None, None]
[3, 'Event 3', 2, 'Asset 2']
[4, 'Event 4', 1, 'Asset 1']
[5, 'Event 5', None, None]
[6, 'Event 6', 3, 'Asset 3']
```

# Решение
Функция реализована в `/3/task_3.py`

```python
def query(events: list, assets: list) -> list:
    
    result: list[list] = []

    for event in events:
        if not event[3]:
            result.append([event[0], event[2], None, None])
        else:
            for asset in assets:
                if event[3] == asset[0]:
                    result.append([event[0], event[2], asset[0], asset[1]])

    return sorted(result)[:100]
```

## Результат работы
![Результат работы](/images/3_task_photo/result_of_work.png)