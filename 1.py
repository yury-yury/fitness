import time

start_time = time.time() - 26000
print(start_time)
time.sleep(3)
finish_time = time.time()
print(finish_time)
d_time = int(finish_time - start_time)
print(d_time)
print(f'{d_time // 3600}:{d_time % 3600 // 60}:{d_time % 60}')