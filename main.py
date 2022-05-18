import shutil
import os
import re

# path = "D:\\Asher's Documents\\Computer Programming\\Python Practice\\From zero to hero\\Advanced Python Module Assignment\\Assignment Files\\one\\HDOHZHFSTTK.txt"
# # path = ""
# if os.path.isdir(path):
#     print("\nIt is a directory")
# elif os.path.isfile(path):
#     print("\nIt is a normal file")
# else:
#     print("It is a special file (socket, FIFO, device file)")

# for x in os.walk(path):
#     print (x)
path = "D:\\Asher's Documents\\Computer Programming\\Python Practice\\From zero to hero\\Advanced Python Module Assignment\\Assignment Files\\"
final_results = []
for (root, dirs, files) in os.walk(path, topdown=True):
        print("The root is: ")
        print(root)
        print("The directories are: ")
        print(dirs)
        print("The files are: ")
        print(files)
        print('--------------------------------')

# for x in files:
#     print (f'\n{x}')

# for (root, dirs, files) in os.walk(path, topdown=True):
        # print("The root is: ")
        # print(root)
        # print("The directories are: ")
        # print(dirs)
        # print("The files are: ")
        # print(files)
        # print('--------------------------------')
        # print(files)
        #
        # for current_dir in dirs:
        for current_file in files:
            try:
                file_in_use = open(root+'\\'+current_file,'r+')
                text = file_in_use.read()
                # phone_pattern = re.compile(r'\d{3}-\d{3-\}-d{4}')
                # phone = re.search(phone_pattern,text)
                result = re.findall(r"[\d]{3}-[\d]{3}-[\d]{4}", text)
                try:
                    if len(result[0]) > 6:
                        final_results.append(current_file)
                        final_results.append(result)
                except IndexError:
                    pass

                # result = group(phone)
                print(result)
                file_in_use.close()
            except FileNotFoundError:
                print(f"File {current_file} not found")
            print(final_results)



