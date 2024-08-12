from time import sleep

def write_words(word_count, file_name):
    with open(file_name, 'w') as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i}\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")
    
import time

start_time = time.time()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_time = time.time()
print(f"Время выполнения функций: {end_time - start_time} секунд")

import threading

threads = []

for i in range(4):
    thread = threading.Thread(target=write_words, args=(10, f'example5_{i+1}.txt'))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Все потоки завершены.")

start_time_threads = time.time()

end_time_threads = time.time()
print(f"Время выполнения потоков: {end_time_threads - start_time_threads} секунд")