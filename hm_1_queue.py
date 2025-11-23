from queue import Queue


# Створити чергу заявок
queue = Queue()


# Функція generate_request():
def generate_request():
    generate_request.counter += 1 # Лічильник заявок
    new_request = f"Заявка №{generate_request.counter}"
    queue.put(new_request)
    print(f"Створено: {new_request}")

generate_request.counter = 0

# Функція process_request():
def process_request():
    if not queue.empty():
        request = queue.get()
        print(f"Оброблено: {request}")
    else:
        print("Черга пуста, немає заявок для обробки.")

while True:
    user_input = input("Введіть 'g' для створення заявки, 'p' для обробки заявки, 'q' для виходу: ")
    if user_input == 'q':
        break
    elif user_input == 'g':
        generate_request()
    elif user_input == 'p':
        process_request()  
    else:
        print("Невірна команда. Спробуйте ще раз.")
    





