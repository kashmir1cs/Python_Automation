#ISO 폴더 정리
import os

import shutil

'''ISO 들어있는 폴더 확인'''
iso_dir="C:/Users/User/Desktop/ISO_SORT/"
print("ISO Line No.별 정리")
print(iso_dir)
# Print file list
if os.path.exists(iso_dir):
    print("File 목록:\n")
    filelist=os.listdir(iso_dir)

for f in filelist:
    print(f)
#파일명 출력후 총 개수 표시

num_files = len(filelist)
print("\n파일 개수: 총 %d개\n" % num_files)


#Splicing 실시
Dwg_Name = []
Dwg_Size=[]
Dwg_Fluid=[]
Dwg_Serial=[]
Dwg_Spec=[]

def Serial_FAB(file):
    s= file.split("-")
    w=s[4].replace(".dwg",""))
    z=w.split("_")


#해당 List에 파일 저장

if prefix == 1 :
    print("\nFAB ISO DWG\n")
    for f in filelist:
        n = f.split("-")
        n[4].replace(".dwg","")
        Dwg_Name.append(n[4].replace(".dwg","")) #Dwg_name에 List 저장
    for s in Dwg_Name:
        a = s.split("_")
        print(a[2])
        Dwg_Serial.append(a[2])
elif prefix == 2:
    print("\n기계실 DWG\n")
    for f in filelist:
        n = f.split("-")
        print(n[4].replace(".dwg",""))
        Dwg_Name.append(n[4].replace(".dwg","")) #Dwg_name에 List 저장
    for s in Dwg_Name:
        a = s.split("_")
        print(a[2])
        Dwg_Serial.append(a[2])

Folder_Name=[]
for s in Dwg_Serial:
    a=s[0:2]
    Folder_Name.append(a)

Folder=list(set(Folder_Name)) #중복된 문자 제거

#파일 개수 출력

