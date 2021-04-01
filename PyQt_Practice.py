import sys
import shutil #파일 복사용 이름 변경 패키지 로드
import os #os 모듈 호출
import pandas as pd
from os.path import isfile
from PyQt5.QtWidgets import * #pyqt Module 호출
from PyQt5 import uic
form_class =uic.loadUiType("C:/Users/User/Desktop/App/FU_r0.ui")[0]




def replace_fnames(old_list,new_list,old,new):

    for f in old_list:
        n=f.replace(old,new)
        new_list.append(n)
    return new_list

def add_fnames(old_list,new_list,prefix,suffix): #파일경로를 받아서 파일명에 접두사 추가 후 list 새로 저장
    for f in old_list:
        o=os.path.split(f)[0]+"/"+prefix+os.path.splitext(os.path.split(f)[1])[0]+suffix+os.path.splitext(f)[1]
        new_list.append(o)
    return new_list

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self) #ui 디자인 한대로 셋업하기

        #각 요소별 기능 작성
        self.tb.setAcceptRichText(False)  # TB 텍스트 서식 미적용
        self.btn_Files_2.clicked.connect(self.btn_clicked_1) #파일 선택(복수) 버튼 클릭시 동작 메서드
        self.btn_Folder.clicked.connect(self.btn_clicked_2) #폴더 선택 버튼 클릭시 동작 메서드
        self.btn_mod1.clicked.connect(self.btn_clicked_3)#파일명 변경단어 버튼 클릭
        self.btn_Cancle.clicked.connect(self.btn_clicked_cancle) #변경결과 적용
        self.btn_Add.clicked.connect(self.btn_clicked_Add) #접두사/접미사 추가
        self.flist_original = [] #원래 파일명 저장할 List
        self.flist_new = [] #변경된 파일명 저장할 List
        self.flist_final=[] # 저장할 List
        self.lbl_status.setText("   File 관리 Utility v0.0")
        self.btn_ApplyLast_Rename.clicked.connect(self.btn_clicked_Rename)
    # 파일직접 선택하는 창 선택
    def btn_clicked_1(self):
        #text browser 일괄 삭제 (기존 List는 삭제, 추후 Program에는 리스트 추가 수정 가능하도록 할 것)

        self.tb.clear()
        self.tb_2.clear()
        if len(self.flist_original)!=0:
            print("리스트 초기화")
            self.flist_original=[]
        fnames=QFileDialog.getOpenFileNames(self,"파일 직접 선택",) #값을 Tuple로 반환함
        # Tuple에서 List만 Indexing
        flist=fnames[:-1][0]
        self.flist_original=flist
        Num_flist=str(len(self.flist_original)) #파일 개수 확인

        if fnames != ([],""):
            for f in self.flist_original:
                self.tb.append(os.path.basename(f))
            QMessageBox.information(self,"Message",Num_flist+"개 파일 추가",QMessageBox.Ok)


        else:
            QMessageBox.warning(self,"Warning","파일을 선택하지 않았습니다.",QMessageBox.Ok)


        print(len(self.flist_original))
    def btn_clicked_2(self):
        #text browser 일괄 삭제 (기존 List는 삭제, 추후 Program에는 리스트 추가 수정 가능하도록 할 것)
        if len(self.flist_original)!=0:
            print("리스트 초기화")
            self.flist_original=[]
        print(len(self.flist_original))
        self.tb.clear()
        self.tb_2.clear()
        #폴더 선택창 출력함
        fdir=QFileDialog.getExistingDirectory(self,"폴더 선택(하위 폴더 미포함)")
        print(fdir)
        if fdir!="":
            flist=os.listdir(fdir)

            print(flist)
            for f in flist:
                if os.path.isfile(fdir+"/"+f):
                    print(f)
                    self.flist_original.append(fdir+"/"+f)
                    self.tb.append(f)
            Num = len(self.flist_original)
            print(self.flist_original)
            if Num==0:
                QMessageBox.warning(self, "Warning", "파일이 존재하지 않습니다", QMessageBox.Ok)
            else:
                QMessageBox.information(self, "Message", str(Num) + "개 파일 추가", QMessageBox.Ok)
        elif fdir=="":
            QMessageBox.warning(self, "Warning", "폴더를 선택하지 않았습니다.", QMessageBox.Ok)
    def btn_clicked_3(self): # 파일명 수정_1:파일명내 단어 수정 /변경
        self.tb_2.clear()
        flist_change=[] #변수 선언
        if self.flist_new==[]:
            print("original Insert")
            flist_change=self.flist_original
        else:
            msg_q2 = QMessageBox.question(self, "변경 사항 발생", "수정사항을 적용하시겠습니까?", QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.No)
            if msg_q2==QMessageBox.Yes: #수정 두번 이상 할 경우 list_new 초기화
                print("change Insert")
                flist_change=self.flist_new
                self.flist_new = []

        txt_old=self.le_old.text() # Text Edit창에서 검색할 단어 저장
        print("변경할 단어: "+txt_old)
        txt_new=self.le_new.text() # Text Edit창에서 변경 단어 저장
        print("변경할 단어: " + txt_new)
        if len(self.flist_original)==0:
            QMessageBox.information(self, "Message", "수정할 파일이 없습니다.", QMessageBox.Ok)

        # 텍스트 브라우저에 변경된 파일명 표시

        replace_fnames(flist_change,self.flist_new,txt_old,txt_new)
        print(self.flist_new)
        for f in self.flist_new:
            self.tb_2.append(os.path.basename(f)) # 텍스트 브라우저에 표시
    def btn_clicked_cancle(self):
        print(self.flist_original)
        if len(self.flist_original)==0:
            QMessageBox.information(self, "Message", "수정할 파일이 없습니다.", QMessageBox.Ok)



        #메시지박스 : 수정사항 적용 여부 문의

        msg_q=QMessageBox.question(self,"수정 취소","수정사항을 취소하시겠습니까?",QMessageBox.Yes|QMessageBox.No,
                                   QMessageBox.No)
        if msg_q==QMessageBox.Yes:
            self.tb_2.clear() #수정본 브라우서 삭제
            for f in self.flist_original:
                self.tb_2.append(os.path.basename(f))  # 텍스트 브라우저에 표시

            QMessageBox.information(self, "적용완료", "적용되었습니다.", QMessageBox.Ok)
            self.flist_new=self.flist_original
    def btn_clicked_Add(self):
        if len(self.flist_original)==0:
            QMessageBox.information(self, "Message", "수정할 파일이 없습니다.", QMessageBox.Ok)
        txt_prefix=self.le_prefix.text()
        print("prefix : "+txt_prefix)
        txt_suffix = self.le_suffix.text()
        print("suffix: "+txt_suffix)
        flist_change=[] #변수 선언
        if self.flist_new==[]:
            print("original Insert")
            flist_change=self.flist_original
        else:
            msg_q2 = QMessageBox.question(self, "변경 사항 발생", "수정사항을 적용하시겠습니까?", QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.No)
            if msg_q2==QMessageBox.Yes: #수정 두번 이상 할 경우 list_new 초기화
                print("change Insert")
                flist_change=self.flist_new
                self.flist_new = []
        add_fnames(flist_change,self.flist_new,txt_prefix,txt_suffix)
        print(self.flist_new)
        for f in self.flist_new:
            self.tb_2.append(os.path.basename(f)) # 텍스트 브라우저에 표시
    def btn_clicked_Rename(self): #원본에 변경된 파일명 그대로 적용
        self.flist_final=self.flist_new #리스트에 있는 자료 복사
        n1=len(self.flist_original)
        n2=len(self.flist_final)
        print(n1)
        print(n2)
        for i in range(0,n1):
            os.rename(self.flist_original[i],self.flist_final[i])




if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
