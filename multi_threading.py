import threading
import os, fnmatch

# obj = '*.py'
# path_ob = [r"D:\програмування\Python\Класи. Декоратори та консольні менеджери\topic_2", r"D:\програмування\Python\Класи. Декоратори та консольні менеджери\topic_1"]



obj = '*.' + input("type file: ")
path_ob = input("directory or path: ").split(",")


def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    print('\n'.join(result))


if __name__ == "__main__":
    for index in path_ob:
        x = threading.Thread(target=find, args=(str(obj), index,))
        x.start()



