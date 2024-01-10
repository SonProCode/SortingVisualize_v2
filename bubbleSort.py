import time
import keyboard

is_paused = False


def bubble_sort(data, drawData, timeTick, ascending):
    for _ in range(len(data) - 1):
        for j in range(len(data) - 1):
            if is_paused:
                time.sleep(1000)
            if (data[j] > data[j + 1] and ascending) or (data[j] < data[j + 1] and not ascending):
                data[j], data[j + 1] = data[j + 1], data[j]
                drawData(data, ['yellow' if x == j or x == j + 1 else 'red' for x in range(len(data))])
                time.sleep(timeTick)
        drawData(data, ['yellow' for x in range(len(data))])
