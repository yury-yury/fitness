from typing import Any

from classes.exercise import Exercise


def read_training(name: str) -> list[Exercise]:
    with open(f'{name}.txt', 'r', encoding='utf-8') as file:
        result = []
        for line in file:
            if line != '\n':
                ex, rep, attempts, wedth = line.split(',')
                attempts = int(attempts)
                wedth = wedth.strip()
                result.append(Exercise(name=ex,
                                       rep=rep,
                                       attempts=attempts,
                                       wedth=wedth))

    return result


def write_training(name: str, data: list[Exercise]) -> None:
    with open(f'{name}.txt', 'w', encoding='utf-8') as file:
        result = str()
        for item in data:
            w_data = ', '.join([item.name,
                                item.rep.strip(),
                                str(item.attempts),
                                item.wedth])
            result += w_data + '\n'
        file.write(result)


if __name__ == '__main__':
    print(read_training(1))

