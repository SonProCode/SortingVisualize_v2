import time


def insertionSort(data, drawData, timeTick, ascending):
    for i in range(len(data)):
        j = i
        while j > 0 and ((data[j - 1] > data[j] and ascending) or (data[j - 1] < data[j] and not ascending)):

            data[j - 1], data[j] = data[j], data[j - 1]
            j -= 1
            drawData(data, ['yellow' if j == x or x == j + 1 else 'red' for x in range(len(data))])
            time.sleep(timeTick)

    drawData(data, ['yellow' for x in range(len(data))])
