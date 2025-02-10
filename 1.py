import time

start_time = time.time()
print(start_time)
time.sleep(10)
finish_time = time.time()
print(finish_time)
d_time = int(finish_time - start_time)
print(d_time)
print(f'{d_time // 3600}:{(d_time % 3600 // 60) if (d_time % 3600 // 60) > 9 else "0" + str(d_time % 3600 // 60)}:{(d_time % 60) if (d_time % 60) > 9 else "0" + str(d_time % 60)}')