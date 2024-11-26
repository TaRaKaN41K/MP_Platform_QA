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