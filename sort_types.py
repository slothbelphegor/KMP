




def BubbleSort(args):
    for x in range(len(args)-1):
        if args[x] > args[x + 1]:
            args[x],args[x+1] = args[x+1],args[x]
    return args

def SelectionSort(args):
    for i in range(len(args)):
        min = args[i]
        for x in range(i,len(args)-1):
            if min > args[x]:
                min = args[x]
                args[x] = args[i]
                args[i] = min
    return args

def InsertionSort(args):
    for i in range(1,len(args)):
        if (args[i]<args[i-1]):
            key = args[i]
            for j in range(i,-1,-1):
                args[j] = args[j-1]
            args[0] = key
            print(args)
    return args

def MergeSort(args):
    if len(args)>1:
        #Chia mảng thành 2 nửa
        mid = len(args)//2
        left = args[:mid]
        right = args[mid:]

        #Đệ quy cho mỗi bên (chỉ thực hiện khi mảng nhiều hơn 1 phần tử)
        MergeSort(left)
        MergeSort(right)

        #Biến đếm cho left, right, và kết quả trả về
        i = j = k = 0

        '''So sánh 2 bên: bên nào bé hơn thì gán vào vị trí k của kết quả 
        sau đó i (hoặc j) và k tiến thêm 1 bước'''
        while i< len(left) and j<len(right):
            if left[i]<right[j]:
                args[k] = left[i]
                k += 1
                i += 1
            elif left[i]>right[j]:
                args[k] = right[j]
                j += 1
                k += 1

        '''Trong trường hợp 1 bên đã gán hết mà bên kia còn dư, 
        cứ tự nhiên đưa bên còn dư vào kết quả (đã được sắp xếp từ 
        trước do đệ quy)'''
        while i < len(left):
            args[k] = left[i]
            i += 1
            k +=1
        while j < len(right):
            args[k] = right[j]
            j+=1
            k+=1
    return args


def HeapSort(arr):
    #Hàm sắp xếp 1 mảng theo cấu trúc cây nhị phân
    def Heapify(arr, i, size):
        #Largest là vị trí phần tử mẹ, theo sau đó là 2 phần tử con theo nó
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        #print(i, left, right)

        #Xác nhận rằng mọi phần tử mẹ đều lớn hơn phần tử con, cũng như left,right không quá giới hạn
        if arr[left] > arr[largest] and left <= size-1:
            largest = left
        if right <= size-1:
            if arr[right] > arr[largest]:
                largest = right
        arr[i], arr[largest] = arr[largest], arr[i]

    #Thực hiện cấu trúc cây nhị phân
    def MaxHeap(arr,size):
        #Từ start về 0 là vị trí các phần tử mẹ, sau start là các phần tử con
        start = int(size / 2) - 1
        #Đi ngược từ start về 0 để đảm bảo phần tử lớn nhất ở trên cùng
        for i in range(start, -1, -1):
            Heapify(arr, i,size)
            #print(arr)

    size = len(arr)
    while size>0:
        MaxHeap(arr,size)
        #Swap phần tử trên cùng (lớn nhất) về cuối, sau đó loại nó ra khỏi cây nhị phân
        arr[0],arr[size-1] = arr[size-1],arr[0]
        size -= 1
        # Cứ vậy cho đến khi hết cây nhị phân
    return arr


def QuickSort(arr,low,high):

    def Partition(arr, low, high):
        """This function takes last element as pivot, places
       the pivot element at its correct position in sorted
        array, and places all smaller (smaller than pivot)
       to left of pivot and all greater elements to right
       of pivot"""
        pivot = arr[high]
        i = low -1
        #Biến j đi từ đầu đến cuối mảng
        for j in range(low,high):
            print(f'i = {i}, j = {j}')
            '''Biến i chỉ tiến khi j chỉ đến 1 phần tử nhỏ hơn pivot
            --> Có thể không tiến, dẫn đến swap giữa 2 phần tử'''
            #Swap để đảm bảo rằng những cái nhỏ hơn pivot nằm bên trái, lớn hơn thì nằm bên phải
            if arr[j] < pivot:
                #Nếu i và j từ đẩu chỉ cùng tăng thì sẽ ko có swap (do i==j),trừ khi i dừng lại ở 1 lúc nào đó
                i += 1
                arr[i],arr[j] = arr[j],arr[i]
                print(f'swap {i} and {j}\n', arr[low:high])
        #Khi này đưa phần tử ở i+1 về cuối mảng
        arr[i+1],arr[high] = arr[high],arr[i+1]
        print(f'final swap {i + 1} and {high}\n', arr[low:high])
        #Vị trí i+1 thành pivot sau khi swap với phần tử cuối (ban đầu vị trí cuối là pivot)
        return i+1

    if low<high:
        pi = Partition(arr,low,high)
        print('pi =',pi,arr[low:high])
        QuickSort(arr,low,pi-1) # Trước pivot
        QuickSort(arr,pi+1,high) # Sau pivot
    return arr

def CountingSort(arr):
    print(arr)
    count = []

    for i in range(max(arr)+1):
        #Lập mảng với mỗi phần tử là số lần xuất hiện của 1 số index trong arr
        #VD: count[2] = 3 --> Số 2 xuất hiện 3 lần trong arr
        count.append(arr.count(i))
        if i == 0:
            continue
        #Lấy phần tử sau cộng dồn cho phần tử trước, cứ thế đến hết count
        count[i] += count[i-1]
    result = arr.copy()
    print(count)
    for i in arr:
        '''Tham chiếu arr, với mỗi i trong arr thì gán i vào vị trí tương ứng với
        số lần nó xuất hiện trong arr (trừ 1) rồi lấy chính số lần xuất hiện đó
        (trong mảng count)trừ đi 1'''
        result[count[i]-1] = i
        count[i] -= 1
    print('result:',result)




def RadixSort(arr):
    '''Sắp xếp theo hàng đơn vị của các phần tử, sau đó là hàng chục, hàng tràm,
    cứ thé đến hết (áp dụng Count Sort)'''

    def CountSort(arr,exp):
        '''Vẫn là CountingSort nhưng có thêm biến exp chỉ xem cần đếm số ở
        hàng đơn vị, hàng chục, hay hàng trăm...'''
        n = len(arr)

        #Mảng lưu số lần xuất hiện của các chữ số từ 0-9
        count = [0 for i in range(10)]

        #Mảng kết quả (dài bắng arr)
        result = [0 for i in range(n)]

        for i in range(0,n):
            #Mỗi index % 10 là chữ số cần xét trong số được tham chiếu (hàng chục, dơn vi...)
            #VD: 126 // 10 == 12 % 10 == 2
            index = arr[i] // exp
            count[index % 10] += 1
        for i in range(1,10):
            #Cộng dồn phần tử trước vào phần tử sau
            count[i] += count[i-1]

        #Xây dụng mảng đã sắp xếp
        i = n - 1
        while i >= 0:
            index = arr[i] // exp
            result[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
            i -= 1

        #Copy mảng đã xếp vào mảng ban đầu
        for i in range(0, len(arr)):
            arr[i] = result[i]

    #Bắt đầu RadixSort
    #Thực hiện CountSort cho mọi số trong mảng
    exp = 1
    while max(arr) / exp > 1:
        CountSort(arr,exp)
        exp*=10







import math


list = [23,12,36,600,79,55]
# BubbleSort(list)
# SelectionSort(list)
#InsertionSort(list)
#MergeSort(list)
#print(QuickSort(list,0,len(list)-1))
#CountingSort(list)
RadixSort(list)
print(list)



