import time
from concurrent.futures import thread
from tkinter import *
from tkinter import ttk
import random
# from bubbleSort import bubble_sort
# from quickSort import quick_sort
# from merge_sort import merge_sort
# from insertionSort import insertionSort
# from selectionSort import selectionSort
import threading

# Khai báo cửa sổ
root = Tk()
# tiêu đề
root.title('Sorting Algorithm Visualisation')
# kích cỡ cửa sổ
root.maxsize(900, 600)
root.config(bg='black')
# variables
selected_alg = StringVar()
selected_seq = StringVar()
data = []
is_paused = False
is_stop = False


# hàm pause chương trình
def pause():
    global is_paused
    is_paused = True


# hàm tắt pause chương trình
def resume():
    global is_paused
    is_paused = False


# hàm dừng chương trình
def stop():
    global is_stop
    is_stop = True


def drawData(data, colorArray, kind=0, leftIndex=0, rightIndex=10, leaderboard=[], border=0):
    # xóa hết mọi thứ trong canvas và note
    canvas.delete("all")
    note.delete("all")
    dataToDraw = data
    # vẽ phần giải thích cho bubble_sort
    if kind == 1:
        note.create_rectangle(5, 10, 15, 20, fill='blue')
        note.create_text(32, 30, text='Swapping')
        note.create_rectangle(5, 50, 15, 60, fill='red')
        note.create_text(42, 70, text='Color of array')
        note.create_rectangle(5, 90, 15, 100, fill='yellow')
        note.create_text(30, 110, text='Finished')
    # vẽ phần giải thích cho merge_sort
    if kind == 2:
        note.create_text(17, 20, text='Left:')
        note.create_text(20, 35, text=str(leftIndex))
        note.create_text(50, 20, text='Mid:')
        note.create_text(50, 35, text=str((leftIndex + rightIndex) // 2))
        note.create_text(20, 45, text='Right:')
        note.create_text(20, 60, text=str(rightIndex))
        note.create_rectangle(5, 70, 15, 80, fill='blue')
        note.create_text(45, 90, text='Left before sort')
        note.create_rectangle(5, 100, 15, 110, fill='red')
        note.create_text(49, 120, text='Right before sort')
        note.create_rectangle(5, 130, 15, 140, fill='black')
        note.create_text(40, 150, text='Before merge')
        note.create_rectangle(5, 160, 15, 170, fill='green')
        note.create_text(43, 180, text='Sorted left part')
        note.create_rectangle(5, 190, 15, 200, fill='pink')
        note.create_text(46, 210, text='Sorted right part')
        note.create_rectangle(5, 220, 15, 230, fill='yellow')
        note.create_text(37, 240, text='After merge')
        note.create_rectangle(5, 250, 15, 260, fill='cyan')
        note.create_text(48, 270, text='Pre sorting right')
    # vẽ phần giải thích cho quick_sort
    if kind == 3:
        note.create_text(17, 20, text='Head:')
        note.create_text(20, 35, text=str(leftIndex))
        note.create_text(55, 20, text='Border:')
        note.create_text(50, 35, text=str(border))
        note.create_text(15, 47, text='Tail:')
        note.create_text(15, 60, text=str(rightIndex))
        note.create_rectangle(5, 70, 15, 80, fill='grey')
        note.create_text(45, 90, text='Doan dang xet')
        note.create_rectangle(5, 100, 15, 110, fill='white')
        note.create_text(49, 120, text='Doan khong xet')
        note.create_rectangle(5, 130, 15, 140, fill='blue')
        note.create_text(20, 150, text='Pivot')
        note.create_rectangle(5, 160, 15, 170, fill='red')
        note.create_text(23, 180, text='Border')
        note.create_rectangle(5, 190, 15, 200, fill='black')
        note.create_text(22, 210, text='Swap')
        note.create_rectangle(5, 220, 15, 230, fill='yellow')
        note.create_text(37, 240, text='Completed')
        note.create_rectangle(5, 250, 15, 260, fill='pink')
        note.create_text(45, 270, text='Current Index')
    # vẽ phần giải thích cho insert_sort
    if kind == 4:
        note.create_text(17, 20, text='j:')
        note.create_text(25, 20, text=str(leftIndex))
        note.create_text(55, 20, text='i:')
        note.create_text(64, 20, text=str(rightIndex))
        note.create_rectangle(5, 70, 15, 80, fill='green')
        note.create_text(30, 90, text='Swapping')
        note.create_rectangle(5, 100, 15, 110, fill='yellow')
        note.create_text(32, 120, text='Completed')
        note.create_rectangle(5, 130, 15, 140, fill='red')
        note.create_text(40, 150, text='Color of array')
    # vẽ phần giải thích cho selection_sort
    if kind == 5:
        note.create_text(17, 20, text='i:')
        note.create_text(25, 20, text=str(leftIndex))
        note.create_text(55, 20, text='j:')
        note.create_text(64, 20, text=str(rightIndex))
        note.create_text(34, 47, text='Min_index:')
        note.create_text(69, 47, text=str(border))
        note.create_rectangle(5, 70, 15, 80, fill='pink')
        note.create_text(19, 74, text='i')
        note.create_rectangle(5, 100, 15, 110, fill='Blue')
        note.create_text(20, 103, text='j')
        note.create_rectangle(5, 130, 15, 140, fill='Black')
        note.create_text(52, 150, text='Update min_index')
        note.create_rectangle(5, 160, 15, 170, fill='red')
        note.create_text(40, 180, text='Color of array')
        note.create_rectangle(5, 190, 15, 200, fill='yellow')
        note.create_text(34, 210, text='Completed')
        note.create_rectangle(5, 220, 15, 230, fill='green')
        note.create_text(34, 240, text='Swapping')

    # chuẩn bị các thông số để vẽ các cột
    c_height = 380
    c_width = 600
    x_width = c_width / (len(dataToDraw) + 1)
    offset = 30
    spacing = 10
    normalizedData = [i / max(dataToDraw) for i in dataToDraw]
    tmp = 0
    # bắt đầu vẽ các cột
    for i, height in enumerate(normalizedData):
        # top_left của cột
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        # bottom right của cột
        x1 = (i + 1) * x_width + offset
        y1 = c_height
        # vẽ cột với các thông số
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0 + 2, y0, anchor=SW, text=str(dataToDraw[i]))
        # vẽ thứ tự của các cột khi merge nếu thuật toán là merge_sort
        if (kind == 2) and (len(leaderboard) != 0) and (leftIndex <= i <= rightIndex):
            canvas.create_text(x0 + 2, y0 - 14, anchor=SW, text=str(leaderboard[tmp]), fill="blue")
            tmp = tmp + 1
    # gọi các tác vụ
    root.update_idletasks()


def Generate():
    global data, is_stop
    is_stop = False
    # xử lí đầu vào
    if dataEntry.get() != "":
        lst = dataEntry.get().split()
        data = []
        data = [int(i) for i in lst]
    else:
        # sinh ra xâu ngẫu nhiên
        if minEntry.get() != "":
            minVal = int(minEntry.get())
        else:
            minVal = 1
        if maxEntry.get() != "":
            maxVal = int(maxEntry.get())
        else:
            maxVal = 50
        if sizeEntry.get() != "":
            size = int(sizeEntry.get())
        else:
            size = 10
        data = []
        for _ in range(size):
            data.append(random.randrange(minVal, maxVal + 1))
    # vẽ dãy số
    drawData(data, ['red' for x in range(len(data))])

    root.after(0, lambda: root.mainloop())


# bat dau thuat toan merge sort
def merge_sort(data, drawData, timeTrick, ascending):
    merge_sort_alg(data, 0, len(data) - 1, drawData, timeTrick, ascending)


def merge_sort_alg(data, left, right, drawData, timeTrick, ascending):
    if left < right:
        middle = (left + right) // 2
        # pause hoặc dừng chương trình
        while is_paused:
            time.sleep(1)
        if is_stop:
            return
        # vẽ dãy trước khi bắt đầu sắp xếp
        drawData(data, getColorArray_mergeSort(len(data), left, middle, right, kind=1), kind=2, leftIndex=left,
                 rightIndex=right)
        time.sleep(timeTrick)
        # sắp xếp phần bên trái
        merge_sort_alg(data, left, middle, drawData, timeTrick, ascending)
        while is_paused:
            time.sleep(1)
        if is_stop:
            return
        # vẽ dãy số với phần bên trái đã được sắp xếp
        drawData(data, getColorArray_mergeSort(len(data), left, middle, right, kind=2), kind=2, leftIndex=left,
                 rightIndex=right)
        time.sleep(timeTrick)
        # sắp xếp phần bên phải
        merge_sort_alg(data, middle + 1, right, drawData, timeTrick, ascending)
        while is_paused:
            time.sleep(1)
        if is_stop:
            return
        # vẽ dãy số với phần bên trái và bên phải đã được sắp xếp
        drawData(data, getColorArray_mergeSort(len(data), left, middle, right, kind=3), kind=2, leftIndex=left,
                 rightIndex=right)
        time.sleep(timeTrick)
        # merge phần trái với phần phải với nhau
        merge(data, left, middle, right, drawData, timeTrick, ascending)


def merge(data, left, middle, right, drawData, timeTick, ascending):
    # pause hoặc dừng chương trình
    while is_paused:
        time.sleep(1)
    if is_stop:
        return
    time.sleep(timeTick)

    leftPart = data[left:middle + 1]
    rightPart = data[middle + 1: right + 1]
    # bảng stt khi merge 2 phần trái phải lại với nhau
    left_leaderboard = []
    right_leaderboard = []
    stt = 0
    old_data = data.copy()
    leftIdx = 0
    rightIdx = 0
    # bắt đầu merge
    if ascending:
        for dataIdx in range(left, right + 1):
            if is_stop:
                return
            stt = stt + 1
            if leftIdx < len(leftPart) and rightIdx < len(rightPart):
                # kiểm tra 2 đầu của phần bên trái và bên phải
                if leftPart[leftIdx] <= rightPart[rightIdx]:
                    data[dataIdx] = leftPart[leftIdx]
                    leftIdx += 1
                    left_leaderboard.append(stt)
                else:
                    data[dataIdx] = rightPart[rightIdx]
                    rightIdx += 1
                    right_leaderboard.append(stt)
            # thêm phần thừa còn lại
            elif leftIdx < len(leftPart):
                data[dataIdx] = leftPart[leftIdx]
                leftIdx += 1
                left_leaderboard.append(stt)
            else:
                data[dataIdx] = rightPart[rightIdx]
                rightIdx += 1
                right_leaderboard.append(stt)
    else:
        for dataIdx in range(left, right + 1):
            if is_stop:
                return
            if leftIdx < len(leftPart) and rightIdx < len(rightPart):
                # kiểm tra 2 đầu của phần bên trái và bên phải
                if leftPart[leftIdx] >= rightPart[rightIdx]:
                    data[dataIdx] = leftPart[leftIdx]
                    leftIdx += 1
                    left_leaderboard.append(stt)
                else:
                    data[dataIdx] = rightPart[rightIdx]
                    rightIdx += 1
                    right_leaderboard.append(stt)
            # thêm phần thừa còn lại
            elif leftIdx < len(leftPart):
                data[dataIdx] = leftPart[leftIdx]
                leftIdx += 1
                left_leaderboard.append(stt)
            else:
                data[dataIdx] = rightPart[rightIdx]
                rightIdx += 1
                right_leaderboard.append(stt)
    while is_paused:
        time.sleep(1)
    while is_paused:
        time.sleep(1)
    if is_stop:
        return
    # vẽ dãy trước khi merge với số thứ tự merge
    drawData(old_data, getColorArray_mergeSort(len(data), left, middle, right, kind=4), kind=2, leftIndex=left,
             rightIndex=right,
             leaderboard=left_leaderboard + right_leaderboard)
    time.sleep(timeTick)
    while is_paused:
        time.sleep(1)
    if is_stop:
        return
    # vẽ dãy sau khi merge
    drawData(data, getColorArray_mergeSort(len(data), left, middle, right, kind=5), kind=2, leftIndex=left,
             rightIndex=right)
    time.sleep(timeTick)


# hàm trả lại dãy màu của các cột
def getColorArray_mergeSort(length, left, middle, right, kind):
    colorArray = []

    for i in range(length):
        if kind == 1:
            if left <= i <= right:
                if i <= middle:
                    colorArray.append("red")
                else:
                    colorArray.append("blue")
            else:
                colorArray.append("white")
        if kind == 2:
            if left <= i <= right:
                if i <= middle:
                    colorArray.append("green")
                else:
                    colorArray.append("cyan")
            else:
                colorArray.append("white")
        if kind == 3:
            if left <= i <= right:
                if i <= middle:
                    colorArray.append("green")
                else:
                    colorArray.append("pink")
            else:
                colorArray.append("white")
        if kind == 4:
            if left <= i <= right:
                colorArray.append("black")
            else:
                colorArray.append("white")
        if kind == 5:
            if left <= i <= right:
                colorArray.append("yellow")
            else:
                colorArray.append("white")

    return colorArray


# ket thuc thuat toan mergesort

# bat dau thuat toan bubblesort
def bubble_sort(data, drawData, timeTick, ascending):
    for _ in range(len(data) - 1):
        for j in range(len(data) - 1):
            while is_paused:
                time.sleep(1)
            if is_stop:
                return
            # doi vi tri cua phan tu vi tri j va j + 1 neu thoa man dieu kien
            if (data[j] > data[j + 1] and ascending) or (data[j] < data[j + 1] and not ascending):
                data[j], data[j + 1] = data[j + 1], data[j]
                # vẽ dãy với sự thay đổi ở phần tử ở vị trí j và j + 1
                if is_stop:
                    return
                drawData(data, ['blue' if x == j or x == j + 1 else 'red' for x in range(len(data))], kind=1)
                time.sleep(timeTick)

    # vẽ dãy sau khi sort xong
    if is_stop:
        return
    drawData(data, ['yellow' for x in range(len(data))], kind=1)


# ket thuc thuat toan bubble sort
# bat dau thuat toan quick sort

# tìm vị trí border với pivot là phần tử cuối
def partition(data, head, tail, drawData, timeTick, ascending):
    # khởi tạo border luôn ở đầu
    border = head
    # khởi tạo pivot luôn ở cuối
    pivot = data[tail]
    while is_paused:
        time.sleep(1)
    if is_stop:
        return -1
    # vẽ dãy trước khi tìm border
    drawData(data, getColorArray(len(data), head, tail, border, border), leftIndex=head, rightIndex=tail, kind=3,
             border=border)
    time.sleep(timeTick)
    for j in range(head, tail):
        if is_stop:
            return -1
        if (data[j] < pivot and ascending) or (data[j] > pivot and not ascending):
            while is_paused:
                time.sleep(1)
            if is_stop:
                return -1
            # vẽ dãy khi data[j] < pivot
            drawData(data, getColorArray(len(data), head, tail, border, j, True), leftIndex=head, rightIndex=tail,
                     kind=3, border=border)
            time.sleep(timeTick)
            # đổi giá trị ở vị trí hiện tại với borders
            data[border], data[j] = data[j], data[border]
            # cập nhật lại border khi giá trị tại ví trị hiện tại nhỏ (lớn) hơn pivot
            border += 1

            while is_paused:
                time.sleep(1)
            if is_stop:
                return -1
            # vẽ lại dãy khi cập nhật lại border
            drawData(data, getColorArray(len(data), head, tail, border, j), leftIndex=head, rightIndex=tail, kind=3,
                     border=border)
            time.sleep(timeTick)

    # Đổi pivot với giá trị ở border
    while is_paused:
        time.sleep(1)
    if is_stop:
        return -1
    # vẽ lại dãy sau khi đổi pivot với giá trị ở border
    drawData(data, getColorArray(len(data), head, tail, border, tail, True), leftIndex=head, rightIndex=tail,
             border=border, kind=3)
    time.sleep(timeTick)
    data[border], data[tail] = data[tail], data[border]

    return border


def quick_sort(data, head, tail, drawData, timeTick, ascending):
    if head < tail:
        # tìm vị trí đề chia dãy thành 2 phần
        partitionIdx = partition(data, head, tail, drawData, timeTick, ascending)
        # dừng chương trình
        if is_stop or partitionIdx == -1:
            return
        # LEFT
        quick_sort(data, head, partitionIdx - 1, drawData, timeTick, ascending)

        # RIGHT
        quick_sort(data, partitionIdx + 1, tail, drawData, timeTick, ascending)

        while is_paused:
            time.sleep(1)
        # dừng chương trình
        if is_stop or partitionIdx == -1:
            return
        # vẽ dãy sau khi sort
        drawData(data, ['yellow' if head <= x <= tail else 'white' for x in range(len(data))], kind=3, leftIndex=head,
                 rightIndex=tail, border=partitionIdx)
        time.sleep(timeTick)


# hàm trả lại dãy màu của các cột
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
            colorArray[i] = 'pink'

        if isSwapping:
            if i == border or i == currIdx:
                colorArray[i] = 'black'

    return colorArray


# ket thuc thuat toan quick sort

# bat dau thuat toan insertion sort
def insertionSort(data, drawData, timeTick, ascending):
    for i in range(len(data)):
        j = i
        # tạm dừng hoặc dừng chương trình
        while is_paused:
            time.sleep(1)
        if is_stop:
            return
        # vòng lặp chèn
        while j > 0 and ((data[j - 1] > data[j] and ascending) or (data[j - 1] < data[j] and not ascending)):
            while is_paused:
                time.sleep(1)
            if is_stop:
                return
            # hoán đổi giá trị
            data[j - 1], data[j] = data[j], data[j - 1]
            j -= 1
            # vẽ dãy khi hoán đổi giá trị
            drawData(data, ['green' if j == x or x == j + 1 else 'red' for x in range(len(data))],
                     leftIndex=j, rightIndex=i, kind=4)
            time.sleep(timeTick)
    # vẽ dãy sau khi hoàn thành
    drawData(data, ['yellow' for x in range(len(data))], kind=4)


# ket thuc thuat toan insertion sort

# bat dau thuat toan selection sort
def selectionSort(data, drawData, timeTick, ascending):
    # Di chuyển ranh giới của mảng đã sắp xếp và chưa sắp xếp
    for i in range(len(data)):
        # Tìm phần tử nhỏ nhất trong mảng chưa sắp xếp
        min_index = i
        while is_paused:
            time.sleep(1)
        if is_stop:
            return
        drawData(data, ['pink' if x == i else 'red' for x in range(len(data))], kind=5, leftIndex=i, rightIndex=i,
                 border=i)
        time.sleep(timeTick)
        for j in range(i + 1, len(data)):
            while is_paused:
                time.sleep(1)
            if is_stop:
                return
            # vẽ quá trình xét qua các phần tử của dãy
            drawData(data, ['blue' if x == j else 'red' for x in range(len(data))], kind=5, leftIndex=i, rightIndex=j,
                     border=min_index)
            time.sleep(timeTick)
            if (data[j] < data[min_index] and ascending) or (data[j] > data[min_index] and not ascending):
                while is_paused:
                    time.sleep(1)
                if is_stop:
                    return
                # cập nhật ví trí phần tử nhỏ nhất
                min_index = j
                # vẽ dãy khi cập nhật ví trí phần tử nhỏ nhất
                drawData(data, ['black' if x == j else 'red' for x in range(len(data))], kind=5, leftIndex=i,
                         rightIndex=j, border=min_index)
                time.sleep(timeTick)

        while is_paused:
            time.sleep(1)
        if is_stop:
            return
        # vẽ dãy khi đổi chỗ phần tử nhỏ nhất với phần tử đầu tiên
        drawData(data, ['green' if x == i or x == min_index else 'red' for x in range(len(data))], kind=5, leftIndex=i,
                 rightIndex=i, border=min_index)
        time.sleep(timeTick)
        # Đổi chỗ phần tử nhỏ nhất với phần tử đầu tiên
        data[min_index], data[i] = data[i], data[min_index]
    # vẽ dãy sau khi hoàn thành sort
    drawData(data, ['yellow' for x in range(len(data))], kind=5, leftIndex=len(data) - 1, rightIndex=len(data) - 1,
             border=len(data) - 1)


# ket thuc thuat toan selection sort

def StartAlgorithm():
    global data
    global thread
    global is_paused
    if not data:
        return
    # kiểm tra xem sắp xếp theo giảm dần hay tăng dần
    ascending = True
    if seq.get() == 'descending':
        ascending = False
    # bắt đầu luồng thuật toán với các kiểu sắp xếp
    if algMenu.get() == 'Bubble sort':
        thread = threading.Thread(target=bubble_sort, args=(data, drawData, speedScale.get(), ascending))
        thread.start()
        # bubble_sort(data, drawData, speedScale.get(), ascending)
    if algMenu.get() == 'Quick sort':
        thread = threading.Thread(target=quick_sort,
                                  args=(data, 0, len(data) - 1, drawData, speedScale.get(), ascending))
        thread.start()
        # quick_sort(data, 0, len(data) - 1, drawData, speedScale.get(), ascending)
        # drawData(data, ['yellow' for x in range(len(data))])
    if algMenu.get() == 'Merge sort':
        thread = threading.Thread(target=merge_sort, args=(data, drawData, speedScale.get(), ascending))
        thread.start()
        # merge_sort(data, drawData, speedScale.get(), ascending)
    if algMenu.get() == 'Insertion sort':
        thread = threading.Thread(target=insertionSort, args=(data, drawData, speedScale.get(), ascending))
        thread.start()
        # insertionSort(data, drawData, speedScale.get(), ascending)
    if algMenu.get() == 'Selection sort':
        thread = threading.Thread(target=selectionSort, args=(data, drawData, speedScale.get(), ascending))
        thread.start()
        # selectionSort(data, drawData, speedScale.get(), ascending)


# frame / base layout
UI_frame = Frame(root, width=600, height=200, bg='grey')
UI_frame.grid(row=0, column=0, padx=10, pady=5)
canvas = Canvas(root, width=660, height=380, bg='white')
note = Canvas(root, width=100, height=300, bg='grey')
canvas.grid(row=1, column=0, padx=10, pady=5)
note.grid(row=1, column=0, padx=10, pady=5, sticky=E)

# UI area
# Row[0]
# thanh chọn thuật toán
Label(UI_frame, text="Algorithm: ", bg='grey').grid(row=0, column=0, padx=5, pady=5, sticky=W)
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Bubble sort', 'Merge sort', 'Quick sort',
                                                                    'Insertion sort', 'Selection sort'])
algMenu.grid(row=0, column=1, padx=5, pady=10)
algMenu.current(0)

# thanh chọn thứ tự sắp xếp
Label(UI_frame, text="Order: ", bg='grey').grid(row=0, column=2, padx=5, pady=5, sticky=W)
seq = ttk.Combobox(UI_frame, textvariable=selected_seq, values=['ascending', 'descending'])
seq.grid(row=0, column=3, padx=5, pady=10)
seq.current(0)

# thanh chỉnh tốc độ
speedScale = Scale(UI_frame, from_=0.1, to=5.0, length=180, digits=2, resolution=0.1, orient=HORIZONTAL,
                   label="Select Speed [s]")
speedScale.grid(row=0, column=7, padx=5, pady=5)

# nút Start
Button(UI_frame, text="Start", command=StartAlgorithm, bg='cyan').grid(row=0, column=7, padx=10, pady=10, sticky=NE)

# Input nhập xâu của người dùng
Label(UI_frame, text="Your array: ", bg='grey').grid(row=0, column=4, padx=5, pady=5, sticky=W)
dataEntry = Entry(UI_frame, width=15)
dataEntry.grid(row=0, column=5, padx=5, pady=5, sticky=W)

# Button(UI_frame, text="Pause", command=pause, bg='red').grid(row=0, column=4, padx=5, pady=5)

# Button(UI_frame, text="Resume", command=resume, bg='red').grid(row=0, column=5, padx=5, pady=5)


# Row[1]
# Nhập size của xâu ngẫu nhiên
Label(UI_frame, text="Size: ", bg='grey').grid(row=1, column=0, padx=5, pady=5, sticky=W)
sizeEntry = Entry(UI_frame, width=10)
sizeEntry.grid(row=1, column=1, padx=5, pady=5, sticky=W)
# Nhập giá trị nhỏ nhất
Label(UI_frame, text="Min Value: ", bg='grey').grid(row=1, column=2, padx=5, pady=5, sticky=W)
minEntry = Entry(UI_frame, width=15)
minEntry.grid(row=1, column=3, padx=5, pady=5, sticky=W)
# Nhập giá trị lớn nhất
Label(UI_frame, text="Max Value: ", bg='grey').grid(row=1, column=4, padx=5, pady=5, sticky=W)
maxEntry = Entry(UI_frame, width=15)
maxEntry.grid(row=1, column=5, padx=5, pady=5, sticky=W)
# Nút tạo dãy
Button(UI_frame, text="Generate", command=Generate, bg='white').grid(row=1, column=7, padx=5, pady=5, sticky=W)
# Nút tạm dừng
Button(UI_frame, text="Pause", command=pause, bg='red').grid(row=1, column=7, padx=5, pady=5, sticky=S)
# Nút tiếp tục
Button(UI_frame, text="Resume", command=resume, bg='red').grid(row=1, column=7, padx=5, pady=5, sticky=E)
# Nút dừng chương trình
Button(UI_frame, text="Stop", command=stop, bg='red').grid(row=1, column=9, padx=5, pady=5, sticky=E)

root.mainloop()
