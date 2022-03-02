import os
import sys

#하나로 합칠 파일들이 저장된 폴더 이름을 시스템으로부터 입력
directory = sys.argv[1]

# 하나로 합쳐진 파일의 이름을 정의
outfile_name = "merge_file.csv"

# 결과물 파일을 생성 
output_file = open(outfile_name, "w")

# 폴더의 내용물을 열람해서 목록을 생성
input_files = os.listdir(directory)

# 헤더를 분리하기 위한 변수를 정의
outfile_header = False

for filename in input_files:
    #csv 파일이 아닌 것은 걸러줌
    if ".csv" not in filename:
        continue
    
    #csv 파일이 맞다면, 파일을 읽어옴
    file = open(directory + "/" + filename)
    
    # 첫 번째 줄 헤더를 정의
    header = file.readline()
    
    # 첫 번째 줄 헤더를 최초 1회 파일에 입력
    if not outfile_header:
        output_file.write(header.strip()) #strip으로 공백없애기
        outfile_header = True
        
    #결과물 파일에 내용물을 입력
    output_file.write('\n'+ file.read())

    #읽어온 파일들을 종료
    file.close()

#결과물 파일을 쓰기를 종료
output_file.close()