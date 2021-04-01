from IsoSort1 import *

#폴더 생성
#폴더 경로 List 선언
copyfolder=[]
print("Iso정리2단계")
#Folder 생성
for f in Folder:
    targetdir= iso_dir + f

    copyfolder.append(targetdir)
    os.makedirs(targetdir)
print(copyfolder)
for g in copyfolder:
    print(g[len(g)-2:])
for f in  filelist:
    print(Serial_FAB(f))

#파일 복사하기









