import splitfolders

# 데이터 경로
data = "original_dataset"
# output 경로
output_folder = 'split_dataset'

splitfolders.ratio(data, output=output_folder, seed=77, ratio=(0.8,0.2), group_prefix=2)