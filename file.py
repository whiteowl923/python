import os
print("THIS PROGRAM IS JUST FOR SANGGONLEE <3")
folder_name = input("파일명을 무엇으로 할까요?:")
folder_num1 = int(input("시작 번호를 입력해주세요:"))
folder_num2 = int(input("마지막 번호를 입력해주세요:"))
i = folder_num1

while folder_num2 >= i:
    if i < 10:
        os.mkdir(folder_name + "0"+str(i))
        i += 1
    else:
        os.mkdir(folder_name + str(i))
        i += 1