# encoding = utf-8
import multiprocessing
import os, time

def copy_file(q, file_name, old_file_path, new_file_path):
    old_file = open(old_file_path + '/' + file_name, 'rb')
    content = old_file.read()
    old_file.close()

    new_file = open(new_file_path + '/' + file_name, 'wb')
    new_file.write(content)
    new_file.close()
    q.put(file_name)

def main():
    old_file_path = input("请输入要复制的文件夹\n")

    new_file_path = old_file_path + "[复件]"
    try:
        os.mkdir(new_file_path)
    except:
        pass

    file_names = os.listdir(old_file_path)
    # print(file_names)

    po = multiprocessing.Pool(5)

    q = multiprocessing.Manager().Queue()

    for file_name in file_names:
        po.apply_async(copy_file, args=(q, file_name, old_file_path, new_file_path, ))

    po.close()
    #po.join()
    count = len(file_names)
    offset = 0
    while True:
        file = q.get()
        offset += 1
        rate = offset * 100 / count
        print("%s复制成功，进度%0.2f\n" % (file, rate))
        # print("\r%s复制成功，进度%0.2f" % (file, rate), end='')

        if offset >= count:
            break


if __name__ == "__main__":
    main()
