import splitfolders

# 경로 설정
splitfolders.ratio("./top_five/actions/", output="./top_five", seed=77, ratio=(0.8,0.2), group_prefix=2)