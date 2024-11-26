# Задание

Реализовать функцию my_code, которая, используя информацию о смежности узлов графа, распечатывает достижимые вершины, начиная с переданной

## Запуск 1
**Код вызова**
```python
data = {
    1: [2, 3],
    2: [4]
}

my_code(data, 1)
```
**Вывод консоли**
```console
1
2
4
3
```

## Запуск 2
**Код вызова**
```python
data = {
    1: [2, 3],
    2: [3, 4],
    4: 1
}

my_code(data, 1)
```
**Вывод консоли**
```console
1
2
3
4
```

# Решение
Функция реализована в `/2/task_2.py`

```python
def my_code(adjacency_graph_nodes: dict, initial_vertex: int, visited_peaks: list = []):

    if not visited_peaks:
        visited_peaks = []

    if initial_vertex not in visited_peaks:
        visited_peaks.append(initial_vertex)
        print(initial_vertex)

    adjacency_graph_nodes[initial_vertex] = [adjacency_graph_nodes[initial_vertex]] if type(adjacency_graph_nodes[initial_vertex]) == int else adjacency_graph_nodes[initial_vertex]

    for adjacent_vertex in adjacency_graph_nodes[initial_vertex]:
        if adjacent_vertex in adjacency_graph_nodes.keys():
            del adjacency_graph_nodes[initial_vertex]
            my_code(
                adjacency_graph_nodes=adjacency_graph_nodes, 
                initial_vertex=int(adjacent_vertex),
                visited_peaks=visited_peaks 
            )
        else:
            if adjacent_vertex not in visited_peaks:
                visited_peaks.append(adjacent_vertex)
                print(adjacent_vertex)
```

## Результат работы
![Результат работы](/images/2_task_photo/result_of_work.png)