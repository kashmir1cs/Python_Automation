import pyautogui as pya
import time as t

pya.FAILSAFE=True
#초기화

n=1 #Data Set No. 지정
k=133
#KY Pipe 활성화


#딜레이 함수 선언

def delay(d):
    t.sleep(d)
#Icon Click



def appchange(x,y):
    delay(0.3)
    pya.click(x,y)
    delay(0.3)
#원위치 하기
def origin():

    pya.keyDown('ctrl')
    pya.press('home')
    pya.keyUp('ctrl')

def operate(kx,ky):

    if pya.pixelMatchesColor(1240,10,(204, 238, 255)):

        print("KYPIPE 활성화 되어 있음")

    else:
        print("KYPIPE 비활성화")
        pya.click(kx,ky)
        print("KYPIPE 창 전환")






def Kyactivate(kx,ky):
    # KYPIPE Data 입력 창 활성화
    #KY PIPE 비활성창이면 활성화 시킨다
    operate(kx,ky)
    print("입력창모드로 전환")

    pya.click(950,0);t.sleep(0.5);pya.click(592, 35);t.sleep(0.5);pya.click(98, 105);t.sleep(0.5)

    pya.click(923,581);t.sleep(0.5)

    pya.click(170,1011)
    if pya.pixelMatchesColor(194,1005,(255, 255, 255)):
        print("Node Demand 입력창활성화")
    else:
        print("Node Demand 비활성화 ")
        pya.click(170, 1011)
        print("Node Deman 활성화 완료")



def InputClose():

    pya.click(1891,4)



#Data입력할 위치로 커서 이동
def Inputinitiate(r,l):
    print("일괄입력:")
    print("Cell 이동")
    pya.click(49,29)
    pya.click(99, 390)
    celladdr=r+str(l)

    pya.typewrite(celladdr)
    pya.press('enter')

    print("복사할 위치 이동동")










# Excel Data 복사하기
def ExcelCopy(n,Ex,Ey):
    print("엑셀창 활성화 확인")

    if pya.pixelMatchesColor(44,29,(54,135,46)):
        print("활성화")
    else:
        print("비활성화 되어 있음")
        pya.click(Ex,Ey)
        if pya.pixelMatchesColor(44,29,(54,135,46)):
            print("활성화")
    #해당 칼럼선택
    c= n+1
    col= "R1"+"C" + str(c)

    print(col)

    pya.click(1203,0)
    delay(0.3)
    pya.keyDown('ctrl')
    pya.press('g')
    pya.keyUp('ctrl')

    delay(0.3)
    pya.typewrite(col,0)

    delay(0.2)
    pya.press('enter')

    pya.hotkey('ctrl','space')
    t.sleep(0.2)
    pya.hotkey('ctrl', 'c')
    t.sleep(0.2)
    print("복사 완료")






def saveNODE(Loop_name,num):
    #Data 불러오기(NODE)
    pya.click(622,35)
    t.sleep(3)
    print("노드결과 저장시작")
    pya.click(40,170); delay(0.2)
    pya.click(260,70);delay(0.2)
    pya.press('up')
    pya.press('up')
    pya.press('up')
    pya.press('up')
    pya.press('up')
    pya.press('up')
    pya.press('enter')
    pya.click(295, 52)
    pya.click(297, 101)
    delay(0.4)




    #엑셀 저장 버튼 입력
    pya.click(145,268);delay(0.35)
    pya.doubleClick(1230,242)
    pya.press('delete')
    t.sleep(0.35)
    prefix1 = "RESULT_NODE-"
    if  num<10:
        fix1 = "000"

    elif   num>=10 and num<100:
        fix1= "00"

    elif   num>=100 and num<1000:
        fix1= "0"

    elif    num>1000:
        fix1 = ""
    fname = prefix1 + Loop_name +"-"+ fix1+str(num)


    pya.typewrite(fname)


    pya.click(661,780)
    delay(0.4)
    pya.click(920,570)

    pya.click(1907,11)
    #화면닫기



def solve():
    pxl = (128, 191, 255)
    p=[]
    if pya.pixelMatchesColor(1240, 10, (204, 238, 255)):

        print("해석모드")
        pya.click(260,10)
        delay(0.2)
        pya.click(712, 80)
        delay(0.5)
        pya.click(250,60)
        delay(0.3)
        pya.click(130, 170)
        delay(7)



    print("해석완료")







def savePIPE(Loop_name,num):
    #Data 불러오기
    print("배관 해석 결과 저장시작")
    pya.click(622,35)
    t.sleep(2)
    pya.click(265, 73)
    pya.press('up')
    pya.press('up')
    pya.press('down')
    pya.press('enter')
    delay(0.3)
    pya.click(38, 170)
    #항목 선택
    pya.click(297, 54)
    delay(0.3)
    pya.click(1869,83)
    pya.dragRel(0,140)
    pya.click(295, 189)
    pya.click(295, 208)
    pya.click(1865,200)
    pya.dragRel(0, -180)
    pya.click(295, 69)

    #엑셀 저장 버튼 입력
    pya.click(145,268);delay(0.3)
    pya.doubleClick(1230,242)
    pya.press('delete')
    t.sleep(0.3)
    prefix = "RESULT_PIPE-"
    if  num<10:
        fix = "000"

    elif   num>=10 and num<100:
        fix= "00"

    elif   num>=100 and num<1000:
        fix= "0"

    elif    num>1000:
        fix = ""
    fname = prefix + Loop_name +"-"+ fix+str(num)


    pya.typewrite(fname)
    pya.click(661,780)
    delay(0.35)
    pya.click(920,570)

    pya.click(1907,11)
    #화면닫기

    #화면닫기





