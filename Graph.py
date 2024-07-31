import os
import Sort
import matplotlib.pyplot as plt

if __name__ == '__main__':
    orientations = ['increasing', 'decreasing', 'random']
    arr_size = ['10000', '20000', '30000', '40000', '50000']
    for o in orientations:
        is_result = []
        ss_result = []
        for x in arr_size:
            os.system('python -m trace --count -C . Sort.py ' + str(x) + ' ' + o)
            with open('Sort.cover', 'r') as fp:
                is_linenum = [4, 5, 6, 7, 9, 10, 11]
                ss_linenum = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
                is_sum, ss_sum, is_line, ss_line = 0, 0, [], []
                for i, line in enumerate(fp):
                    if i in is_linenum:
                        is_line.append(line.strip())
                    if i == 8:
                        is_sum += int(line.strip().split()[0][:-1])*2
                    if i in ss_linenum:
                        ss_line.append(line.strip())
                for line in is_line:
                    try:
                        is_sum += int(line.split()[0][:-1])
                    except:
                        pass
                for line in ss_line:
                    try:
                        ss_sum += int(line.split()[0][:-1])
                    except:
                        pass
                is_result.append(is_sum)
                ss_result.append(ss_sum)
                print(o,x,is_sum, ss_sum)
        plt.clf()
        plt.plot(arr_size, is_result, label = 'Insertion Sort')
        plt.plot(arr_size, ss_result, '-.', label = 'Selection Sort')

        plt.xlabel("Array Sizes")
        plt.ylabel("Instruction Counts")
        plt.legend()
        plt.title(o)
        plt.savefig(o + '.png')