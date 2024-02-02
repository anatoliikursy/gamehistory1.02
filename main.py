from random import randint
import time
import os

game_logs = "game_logs"
if not os.path.exists(game_logs):
    os.mkdir(game_logs)

log_file_path = os.path.join(game_logs, "game_history.txt")

if not os.path.exists(log_file_path):
    open(log_file_path, "w") 

with open(log_file_path, "w") as file:
    current_timestamp = time.time()
    file.write(f"Time: {current_timestamp}, Game Started\n")

print("           Загадка!!! \n         Вгадай число.")
time.sleep(2)

def vgad_num():
    num_ran = randint(1, 100)
    start_time = time.time()

    while True:
        i = int(input("Введіть число: "))
        
        current_time = time.time()
        elapsed_time = current_time - start_time

        if i > num_ran:
            print("Загадане число менше")
            log_entry = f"Time: {current_time}, Guess: {i}, random_integer: {num_ran}. Too high\n"
        
        if i < num_ran:
            print("Загадане число більше")
            log_entry = f"Time: {current_time}, Guess: {i}, random_integer: {num_ran}. Too low\n"
        
        if i == num_ran:
            print(f"Ви відгадали число! Це {i}")
            log_entry = f"Time: {current_time}, Guess: {i}, random_integer: {num_ran}. You guessed it!\n"
            break

        with open(log_file_path, "a") as file:
            file.write(log_entry)
    
    return num_ran

vgad_num()