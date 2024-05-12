# Этот модуль содержит функции для обработки данных о коммитах.
def read_commits(path):
    """
        Читает данные о коммитах из файла commits.txt.

        Аргументы:
        path (str): Путь к файлу с данными о коммитах.

        Возвращает:
        dict: Словарь с количеством коммитов для каждого пользователя.
        """
    # Создаем пустой словарь для хранения количества коммитов каждого пользователя
    commits = dict()
    # Читаем данные из файла построчно
    with open(path) as f:
        for line in f:
            # Разбиваем строку на части по пробелам
            parts = line.strip().split()
            # Извлекаем имя пользователя из строки
            username = parts[0]
            # Если имя пользователя уже присутствует в словаре, увеличием значение(счетчик коммитов), иначе - добавляем пользователя в словарь
            if username in commits:
                commits[username] += 1
            else:
                commits[username] = 1
    # Сортируем словарь по количеству коммитов в обратном порядке и оставляем только три самых активных пользователя
    sorted_commits = dict(sorted(commits.items(), key=lambda item: item[1], reverse=True)[:3])
    # Возвращаем отсортированный словарь
    return sorted_commits
def result(destination, sorted_commits):
    """
        Записывает результаты анализа коммитов в файл result.txt.

        Аргументы:
        destination (str): Путь к файлу, в который будут записаны результаты.
        sorted_commits (dict): Словарь с количеством коммитов для каждого пользователя.
        """
    # Открываем файл для записи результатов
    with open(destination, 'w') as file:
        # Записываем результаты в файл при помощи f-строки
        for key, value in sorted_commits.items():
            file.write(f'Username: {key}. Amount of commits: {value}\n')



