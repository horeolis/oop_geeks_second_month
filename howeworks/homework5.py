import time

class User():
    def __init__(self,name,role):
        self.name = name
        self.role = role
    
def is_admin(func):
    def wrapper(user, *args, **kwargs):
        if user.role == "admin":
            func(*args, **kwargs)
        else:
            print("У вас нет доступа к этой функции")
    return wrapper


@is_admin
def delete_video():
    print("Видео удалено")

admin = User("Ardager", "admin")
user = User("Bek", "user")
print("-------------------------------------------------------------")
delete_video(admin)
print("-------------------------------------------------------------")
delete_video(user)
print("-------------------------------------------------------------")

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"Время выполнения функции: {end_time - start_time} секунд")
    return wrapper

@timer
def download_video():
    print("Загрузка видео...")
    time.sleep(2)
    print("Видео загружено")    

download_video()

