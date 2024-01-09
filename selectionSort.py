import time


def selectionSort(data, drawData, timeTick, ascending):
    for i in range(len(data)):

        min_index = i
        drawData(data, ['pink' if x == min_index else 'red' for x in range(len(data))])
        time.sleep(timeTick)

        for j in range(i + 1, len(data)):
            drawData(data, ['blue'if x == j else 'red' for x in range(len(data))])
            time.sleep(timeTick)
            if (data[j] < data[min_index] and ascending) or (data[j] > data[min_index] and not ascending):
                drawData(data, ['yellow' if x == j else 'red' for x in range(len(data))])
                time.sleep(timeTick)
                min_index = j

        drawData(data, ['yellow' if x == i or x == min_index else 'red' for x in range(len(data))])
        time.sleep(timeTick)
        data[min_index], data[i] = data[i], data[min_index]

    drawData(data, ['yellow' for x in range(len(data))])
