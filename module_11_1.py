from multiprocessing import Pool
import time


def read_info(name):
    all_data = []

    with open(name, "r") as f:
        for line in f:
            all_data.append(line)


filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов
# t1 = time.time()
# for f in filenames:
#     read_info(f)
# t2 = time.time()
# print(t2 - t1)

# Многопроцессный
t1 = time.time()
if __name__ == '__main__':
    with Pool() as p:
        x = (p.map(read_info, filenames))
t2 = time.time()
print(t2 - t1)