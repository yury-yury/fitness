from typing import Any


def read_training(name: str) -> list[list[Any]]:
    with open(f'{name}.txt', 'r', encoding='utf-8') as file:
        result = []
        for line in file:
            ex, rep, attempts, wedth = line.split(', ')
            attempts = int(attempts)
            result.append([ex, rep, attempts, wedth])

    return result


def write_training(name: str, data: list[list[Any]]) -> None:
    with open(f'{name}.txt', 'w', encoding='utf-8') as file:
        result = str()
        for line in data:
            line[2] = str(line[2])
            w_data = ', '.join(line)
            result += w_data + '\n'
        file.write(result)

