import os
# 파이썬 기본 모듈 Import
# 경로 입력시 \ -> /로 변경 필요
path_root="디렉토리경로1"
path_import="디렉토리경로2"
# print(path_root+path_import)
# os 모듈 메소드 이용 
file_list=os.listdir(path_root+path_import) 
# 해당 경로의 Directory의 File명 List로 저장
# 파일명만 반환
# 전체 경로 (절대 경로)를 알기위해선 다른 메소드 사용 필요

print(file_list)
text_list=[]
for f in file_list:
    if f.endswith("확장자명 입력"): # 문자열 검사 : endswith
        text_list.append(f) #특정 확장자 파일만 추가
# print(text_list)

# 반복문 시작
for f in export_pcf:
    data_of_txt=[]
    # search_str="검색할 문자열 입력"
    # new_str= "변경할 문자열 입력"
    with open(path_root+path_import+f,"rt",encoding="euc-kr") as fr: #인코딩 지정, 읽기 모드
        read_line=fr.readlines() # txt파일 전체 내용을 Line별로 list형식으로 반환
        for line in read_line:
            line=line.rstrip()
            if line.rfind("찾을 문자열"): # rfind : 문자열 오른쪽부터 검색
                new_str=line.replace("찾을 문자열","바꿀 문자열")
                data_of_txt.append(new_str)
            else:
                data_of_txt.append(line)
    with open(path_root+path_import+f,"w",encoding="euc-kr") as fw: # 인코딩 지정, 쓰기모드
        for line in data_of_pcf:
            fw.writelines("%s\n" % line) # \n : 줄바꿈

print("작업완료")
