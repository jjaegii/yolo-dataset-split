import os
import shutil
import time

def read_all_file(path):
    output = os.listdir(path)
    file_list = []

    for i in output:
        if os.path.isdir(path+"/"+i):
            file_list.extend(read_all_file(path+"/"+i))
        elif os.path.isfile(path+"/"+i):
            file_list.append(path+"/"+i)

    return file_list

def copy_all_file(file_list, new_path):
    for src_path in file_list:
        file = src_path.split("/")[-1]
        shutil.copyfile(src_path, new_path+"/"+file)
        print("파일 {} 작업 완료".format(file)) # 작업한 파일명 출력
        
        
start_time = time.time() # 작업 시작 시간 

# 경로 설정
train_src_path = "./split_dataset/train" # 기존 폴더 경로
train_new_path = "./merged_dataset/train" # 옮길 폴더 경로

file_list = read_all_file(train_src_path)
copy_all_file(file_list, train_new_path)

print("=" * 40)
print("train 합치는데 걸린 시간 : {}".format(time.time() - start_time)) # 총 소요시간 계산

start_time = time.time() # 작업 시작 시간 

# 경로 설정
val_src_path = "./split_dataset/val" # 기존 폴더 경로
val_new_path = "./merged_dataset/val" # 옮길 폴더 경로

file_list = read_all_file(val_src_path)
copy_all_file(file_list, val_new_path)

print("=" * 40)
print("val 합치는데 걸린 시간 : {}".format(time.time() - start_time)) # 총 소요시간 계산