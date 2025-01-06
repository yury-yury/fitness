import time
from playsound import playsound

from classes.exercise import Exercise


def read_training(name: str) -> list[Exercise]:
    """ """
    with open(f"storage/{name}.txt", "r", encoding="utf-8") as file:
        result: list = []
        for line in file:
            if line != "\n":
                ex, rep, attempts, weight = line.split(",")
                result.append(
                    Exercise(
                        name=ex, rep=rep, attempts=int(attempts), weight=weight.strip()
                    )
                )

    return result


def write_training(name: str, data: list[Exercise]) -> None:
    with open(f"storage/{name}.txt", "w", encoding="utf-8") as file:
        result = str()
        for item in data:
            w_data = ", ".join(
                [item.name, item.rep.strip(), str(item.attempts), item.weight]
            )
            result += w_data + "\n"
        file.write(result)


def write_dairy(data: str) -> None:
    """
    The write_dairy function takes as a positional argument the text of an entry in the training diary,
    in the form of a string. When called, it opens the training diary file, adds an entry to the file,
    and closes the file.
    """
    with open("storage/training_dairy.txt", "a", encoding="utf-8") as file:
        file.write(data)


def beep(t: int) -> None:
    """
    The beep function takes as a positional argument the value of the rest time between sets in seconds,
    as an integer. When a call is made after the end of the rest period, an audio signal is played.
    """
    time.sleep(t)
    playsound('static/vyistrel-pistoleta-36125.mp3')


if __name__ == "__main__":
    beep(30)
