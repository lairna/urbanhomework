import time
import hashlib


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = int(hashlib.sha256(password.encode()).hexdigest(), 16)  # Хэширование пароля
        self.age = age

    def __str__(self):
        return f"User: {self.nickname}"

    def __repr__(self):
        return f"User(nickname='{self.nickname}', age={self.age})"


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __str__(self):
        return f"Video: {self.title}"

    def __repr__(self):
        return f"Video(title='{self.title}', duration={self.duration}, adult_mode={self.adult_mode})"


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):

        password_hash = int(hashlib.sha256(password.encode()).hexdigest(), 16)
        for user in self.users:
            if user.nickname == nickname and user.password == password_hash:
                self.current_user = user
                print(f"Вход выполнен: {user.nickname}")
                return
        print("Неверный логин или пароль.")

    def register(self, nickname, password, age):

        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует.")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.log_in(nickname, password)

    def log_out(self):

        self.current_user = None
        print("Вы вышли из аккаунта.")

    def add(self, *videos):

        for video in videos:
            if not any(v.title.lower() == video.title.lower() for v in self.videos):
                self.videos.append(video)
                print(f"Видео '{video.title}' добавлено.")

    def get_videos(self, search_term):

        return [v.title for v in self.videos if search_term.lower() in v.title.lower()]

    def watch_video(self, title):

        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        video = next((v for v in self.videos if v.title.lower() == title.lower()), None)
        if video is None:
            print("Видео не найдено.")
            return
        if video.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return

        while video.time_now < video.duration:
            print(f"Просмотр: {video.time_now + 1} секунда")
            video.time_now += 1
            time.sleep(1)
        video.time_now = 0
        print("Конец видео")

    def __str__(self):
        return f"UrTube(users={self.users}, videos={self.videos}, current_user={self.current_user})"

    def __repr__(self):
        return f"UrTube(users={self.users}, videos={self.videos}, current_user={self.current_user})"


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

ur.add(v1, v2)

print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

ur.watch_video('Лучший язык программирования 2024 года!')

print(ur)
