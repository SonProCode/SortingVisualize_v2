import time


def partition(data, head, tail, drawData, timeTick, ascending):
    border = head
    pivot = data[tail]
    drawData(data, getColorArray(len(data), head, tail, border, border))
    time.sleep(timeTick)
    for j in range(head, tail):
        if (data[j] < pivot and ascending) or (data[j] > pivot and not ascending):
            drawData(data, getColorArray(len(data), head, tail, border, j, True))
            time.sleep(timeTick)

            data[border], data[j] = data[j], data[border]
            border += 1

            drawData(data, getColorArray(len(data), head, tail, border, border, j))
            time.sleep(timeTick)

    drawData(data, getColorArray(len(data), head, tail, border, tail, True))
    time.sleep(timeTick)

    data[border], data[tail] = data[tail], data[border]

    return border


def quick_sort(data, head, tail, drawData, timeTick, ascending):
    if head < tail:
        partitionIdx = partition(data, head, tail, drawData, timeTick, ascending)
        # LEFT
        quick_sort(data, head, partitionIdx - 1, drawData, timeTick, ascending)

        # RIGHT
        quick_sort(data, partitionIdx + 1, tail, drawData, timeTick, ascending)


def getColorArray(dataLen, head, tail, border, currIdx, isSwapping=False):
    colorArray = []
    for i in range(dataLen):
        # base_coloring
        if head <= i <= tail:
            colorArray.append('gray')
        else:
            colorArray.append('white')

        if i == tail:
            colorArray[i] = 'blue'
        elif i == border:
            colorArray[i] = 'red'
        elif i == currIdx:
            colorArray[i] = 'yellow'

        if isSwapping:
            if i == border or i == currIdx:
                colorArray[i] = 'green'

    return colorArray

