import sys

# Ваши импорты

if __name__ == '__main__':
    filename = sys.argv[1]

    # Ваш код

def main(file):
    """
    Функция по открытию говно файлов в читаемом виде
    """
    open_file(file)


def open_file(file):
        try:
            somefile = open(file, "r")
        except FileNotFoundError:
            print("Файл не валиден")
        except Exception:
            print("Формат не валиден")

def read_file():
фыавыаыа
фвфыаыа
фыывфыфыа