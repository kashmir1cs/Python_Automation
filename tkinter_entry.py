# LTE 프로그래밍 (Log file To Excel Spreadsheet)
# 내장 라이브러리 import

import tkinter as tk
import tkinter.filedialog as fd
import tkinter.messagebox as tm
# form 관련 정보 설정 크기/위치 설정 
global log
log=[]
# Event 함수모음
def btn_func_info(event):
    global job
    global req
    global mod
    job=tk.Entry.get(entry_jobno)
    req=tk.Entry.get(entry_req)
    mod=tk.Entry.get(entry_model)
    print(job,req,mod)
    print('파일경로 열기')
    window.destroy()
    

def btn_func_clear(event):
    entry_jobno.delete(0,'end')
    entry_req.delete(0,'end')
    entry_model.delete(0,'end')
    print('입력된 사항 삭제 완료')
    
global filename

def getfilename():
    
    text_msg='log file 불러오기 완료'
    filename=fd.askopenfilename(initialdir='C:/Users/User/Desktop',title="select a file : Log Report to Excel")
    if bool(filename) and filename.endswith('.log'):
        file = open(file=filename,mode='rt',encoding='utf-8')
        for line in file:
            log.append(line) # append log file line to list
        
        
    else:
        tm.showerror("Error 발생",'파일을 선택하지 않았거나 \n잘못된 파일 양식 입니다.')

def domenu():
    print("OK")
# 변수 설정 모음 
form_geo='330x180-900+200' # form 위치 및 크기 
form_title="LTE - Log To Excel" # form Title 설정 


# lable text 설정 
txt_job="job no." # job no lable
txt_req="requested by" # request lable 
txt_model="modeled by" # modeled lable 
txt_log='log file select' # log file select

# button text 설정
txt_btn_ok = "OK"
txt_btn_clear="CLEAR"

# window 생성 및 설정 반영
window = tk.Tk()

# Menu bar 생성 

menubar = tk.Menu(window)
filemenu = tk.Menu(menubar,tearoff=0)

# Menu bar item add

menubar.add_cascade(label="File", menu=filemenu) # Cascade 추가 : File
filemenu.add_command(label="Load", command=domenu) # File 하위 메뉴 추가 : Load
filemenu.add_command(label="Help", command=domenu) # File 하위 메뉴 추가 : Help
filemenu.add_separator() # Cascade 구분 선 추가
filemenu.add_command(label="Exit", command=domenu) # File 하위 메뉴 추가 : Exit

# window 설정
window.geometry(form_geo) # window 크기/위치 설정
window.title(form_title) # window title
window.config(menu=menubar) # menubar 추가
window.resizable(False, False)
# text 입력 entry 설정 

# 1-1. job no 입력창 lable 설정
lb_job = tk.Label(window,text=txt_job,fg='gray0',width=10, height=1) # lable text 설정 
lb_job.place(x=10,y=5) # lable 위치 설정 

# 1-2. job no 입력창 entry 설정 
entry_jobno = tk.Entry(fg="gray19", bg="snow", width=40)  # entry 설정
entry_jobno.place(x=20,y=25) # entry 위치 설정 

# 2-1. 요청자 입력창 lable 설정 
lb_req = tk.Label(window, text=txt_req, fg='gray0',width=10, height=1) # lable text 설정
lb_req.place(x=20,y=45) # lable 위치 설정 

# 2-2. 요청자 입력창 entry 설정 
entry_req = tk.Entry(fg="gray19", bg="snow", width=40) # entry 설정
entry_req.place(x=20,y=65) # entry 위치 설정 

# 3-1. modeler 입력창 lable 설정
lb_model = tk.Label(window, text=txt_model, fg='gray0',width=10, height=1) # lable text 설정
lb_model.place(x=20,y=85) # lable 위치 설정 

# 3-2. modeler 입력창 entry 설정 
entry_model = tk.Entry(fg="gray19", bg="snow", width=40) # entry 설정
entry_model.place(x=20,y=105) # entry 위치 설정 

job=tk.Entry.get(entry_jobno)
req=tk.Entry.get(entry_req)
mod=tk.Entry.get(entry_model)

# button set - OK
btn_ok=tk.Button(window, text=txt_btn_ok, fg='gray0', width=10)
btn_ok.place(x=45,y=140)
btn_ok.bind('<Button-1>',btn_func_info)

# button set - CLEAR
btn_clear=tk.Button(window, text=txt_btn_clear, fg='gray0', width=10)
btn_clear.place(x=195,y=140)
btn_clear.bind('<Button-1>',btn_func_clear)
window.mainloop()


print('jara : ',job,'req: ',req,'model: ',mod)