def conv(list, n):
    percent = []
    for i in list:
        percent.append(round((i / n) * 100, 1))
    return percent 


def conv_notrounded(list, n):
    percent = []
    for i in list:
        percent.append((i / n) * 100)
    return percent


def conv_lists(list1, list2):
    percent = []
    j = 0
    for i in list2:
        percent.append((i / list1[j] * 100))
        j += 1
    return percent

def conv_matrix(list, matrix):
    percent = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    i = 0
    for row in range(len(matrix)):          #number of lists/rows in matrix
        for col in range(len(matrix[0])):   #first col: matrix[0]
            a = matrix[row][col]
            percent[row][col] = round(a / list[i] * 100)
        i += 1
    return percent


def sum(list):
    sum = 0
    for i in list:
        sum += i
    return sum


def distance(list1, list2, dis):    # dis = Schwellenwert     
    x = 0
    result = []
    for i in list1:
        if i - list2[x] >= dis:
            result.append('s')
        else: 
            result.append(' ')
        x += 1 
    return result


def compare(list1, list2):    # dis = Schwellenwert     
    x = 0
    result = []
    for i in range(len(list1)):
        if list1[i] > list2[x]:
            result.append('+')
        elif list1[i] == list2[x]:
            result.append('=')
        else: 
            result.append('-')
        x += 1 
    return result


def conv2d(matrix, cols, rows, n):
    percent = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(len(matrix)):
        for _ in matrix[0]:
            percent.append(round((i / n) * 100, 1))
    return percent 


def check100(list):
    sum = 0
    for i in list:
        sum = sum + i
    return sum


n = 102810 # all participants

matrix= [[0,0,0,20,0],[5,10,70,320,10],[5,10,70,480,5],[5,5,50,240,5],
        [5,5,20,70,5],[0,5,10,40,5],[5,5,20,30,5],[5,5,5,20,0]]

hos =  [20, 420, 580, 300, 90, 50, 50, 30]