# @Time : 2020/4/7 0007 15:00 

# @Author : ztrxRestful

# @File : qsharesshow.py 

# @Software: PyCharm

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtGui
# import time,datetime
# from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from getshares import getshares

class window(QWidget):
    def __init__(self,parent=None):
        super(window, self).__init__(parent)
        self.title = '股票看板'
        self.left = 500
        self.top = 200
        self.width = 516
        self.height = 120
        self.iconName = "image/icon.png"
        self.InitWindow()
        self.setLayout(self.fqvbox)
        #设置透明度
        self.setWindowOpacity(0.7)

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet("background-color: rgb(255,255, 255)")

        #加入main_layout
        self.fqvbox = QVBoxLayout()
        self.createMainLayout()

        self.show()

    def createMainLayout(self):
        #self.autoCreateBox()
        msg = getshares()#.git_gupiao(getshares)
        msg_list = msg.git_gupiao()
        print(msg_list)
        self.showLabel(msg_list)

        self.share_thead = shares_thead()
        self.share_thead.start()
        self.share_thead.share_signal.connect(self.showLabel_1)


    def showLabel_1(self,list):

        for i in range(len(list)):
            msg_1 = list[i]
            str_i = str(i+1)
            print(str_i)
            #self.group_box_1 = QGroupBox(msg_1[0]+'['+msg_1[1]+']')
            #exec("self.group_box_{} = QGroupBox(msg_1[0]+'['+msg_1[1]+']')".format(str_i))
            #self.fqvbox.addWidget(self.group_box_1)
            exec("self.fqvbox.addWidget(self.group_box_{})".format(str_i))
            #self.h_main_layout_1 = QHBoxLayout()
            #exec("self.h_main_layout_{} = QHBoxLayout()".format(str_i))
            #self.group_box_1.setLayout(self.h_main_layout_1)
            exec("self.group_box_{}.setLayout(self.h_main_layout_{})".format(str_i,str_i))
            #self.v_layout_1_1 = QVBoxLayout()
            #exec("self.v_layout_{}_1 = QVBoxLayout()".format(str_i))
            #self.h_main_layout_1.addLayout(self.v_layout_1_1)
            exec("self.h_main_layout_{}.addLayout(self.v_layout_{}_1)".format(str_i,str_i))
            #self.label_1_1_1 = QLabel()
            #exec("self.label_{}_1_1 = QLabel()".format(str_i))
            if msg_1[11] == 'green':
                exec("self.label_{}_1_1.setStyleSheet('color:green')".format(str_i))
                exec("self.label_{}_1_2.setStyleSheet('color:green')".format(str_i))
            elif msg_1[11] == 'red':
                exec("self.label_{}_1_1.setStyleSheet('color:red')".format(str_i))
                exec("self.label_{}_1_2.setStyleSheet('color:red')".format(str_i))

            #self.label_1_1_1.setText(str(msg_1[2]))
            exec("self.label_{}_1_1.setText(self.number_format(msg_1[2]))".format(str_i))
            #self.v_layout_1_1.addWidget(self.label_1_1_1)
            exec("self.v_layout_{}_1.addWidget(self.label_{}_1_1)".format(str_i,str_i))
            #self.label_1_1_2 = QLabel()
            #exec("self.label_{}_1_2 = QLabel()".format(str_i))
            #self.label_1_1_2.setText(str(msg_1[9])+'  '+str(msg_1[10]))
            exec("self.label_{}_1_2.setText(self.number_format(msg_1[9])+' '+self.number_format(msg_1[10])+'%')".format(str_i))
            #self.v_layout_1_1.addWidget(self.label_1_1_2)
            exec('self.v_layout_{}_1.addWidget(self.label_{}_1_2)'.format(str_i,str_i))


            '''
            开始1
            '''
            max_temp = self.number_format(msg_1[4]) #round(msg_1[4],2)
            over_amt = self.number_format(msg_1[6]) #round(msg_1[6],2)
            min_temp = self.number_format(msg_1[5]) #round(msg_1[5],2)
            open_amt = self.number_format(msg_1[3]) #round(msg_1[3],2)
            if max_temp > over_amt:
                exec('self.label_{}_2_1.setText("<font color=black>  最高:</font><font color=red>"+str(max_temp)+"</font>")'.format(str_i))
            elif max_temp < over_amt:
                exec('self.label_{}_2_1.setText("<font color=black>  最高:</font><font color=green>"+str(max_temp)+"</font>")'.format(str_i))
            #self.label_1_2_1.setText("<font color=black size=4>最高:</font><font color=green size=4>"+str(max_temp)+"</font>")

            if min_temp > over_amt:
                exec(
                    'self.label_{}_2_2.setText("<font color=black>  最低:</font><font color=red>"+str(min_temp)+"</font>")'.format(
                        str_i))
            elif min_temp < over_amt:
                exec(
                    'self.label_{}_2_2.setText("<font color=black>  最低:</font><font color=green>"+str(min_temp)+"</font>")'.format(
                        str_i))

            '''
            2
            '''
            if open_amt > over_amt:
                exec('self.label_{}_3_1.setText("<font color=black>今开:</font><font color=red>"+str(open_amt)+"</font>")'.format(str_i))
            elif open_amt < over_amt:
                exec('self.label_{}_3_1.setText("<font color=black>今开:</font><font color=green>"+str(open_amt)+"</font>")'.format(str_i))

            exec(
                'self.label_{}_3_2.setText("<font color=black>昨收:</font><font color=black>"+str(over_amt)+"</font>")'.format(
                    str_i))

            '''
            3
            '''
            liang = self.number_change(msg_1[7])
            exchange = self.number_change(msg_1[8])

            exec(
                'self.label_{}_4_1.setText("<font color=black>成交量:</font><font color=black>"+liang+"</font>")'.format(
                    str_i))

            exec(
                'self.label_{}_4_2.setText("<font color=black>成交额:</font><font color=black>"+exchange+"</font>")'.format(
                    str_i))
            '''
                结束
            '''

    def showLabel(self,list):

        for i in range(len(list)):
            msg_1 = list[i]
            str_i = str(i+1)
            print(str_i)
            #self.group_box_1 = QGroupBox(msg_1[0]+'['+msg_1[1]+']')
            exec("self.group_box_{} = QGroupBox(msg_1[0]+'['+msg_1[1]+']')".format(str_i))
            #self.fqvbox.addWidget(self.group_box_1)
            exec("self.fqvbox.addWidget(self.group_box_{})".format(str_i))
            #self.h_main_layout_1 = QHBoxLayout()
            exec("self.h_main_layout_{} = QHBoxLayout()".format(str_i))
            #self.group_box_1.setLayout(self.h_main_layout_1)
            exec("self.group_box_{}.setLayout(self.h_main_layout_{})".format(str_i,str_i))





            #self.v_layout_1_1 = QVBoxLayout()
            exec("self.v_layout_{}_1 = QVBoxLayout()".format(str_i))
            #self.h_main_layout_1.addLayout(self.v_layout_1_1)
            exec("self.h_main_layout_{}.addLayout(self.v_layout_{}_1)".format(str_i,str_i))
            #self.label_1_1_1 = QLabel()
            exec("self.label_{}_1_1 = QLabel()".format(str_i))
            exec("self.label_{}_1_2 = QLabel()".format(str_i))
            #self.label_1_1_1.setText(str(msg_1[2]))
            if msg_1[11] == 'green':
                exec("self.label_{}_1_1.setStyleSheet('color:green')".format(str_i))
                exec("self.label_{}_1_2.setStyleSheet('color:green')".format(str_i))
            elif msg_1[11] == 'red':
                exec("self.label_{}_1_1.setStyleSheet('color:red')".format(str_i))
                exec("self.label_{}_1_2.setStyleSheet('color:red')".format(str_i))

            exec("self.label_{}_1_1.setFont(QFont('time', 28, QFont.Bold))".format(str_i))
            exec("self.label_{}_1_2.setFont(QFont('time', 12, QFont.Bold))".format(str_i))

            exec("self.label_{}_1_1.setText(self.number_format(msg_1[2]))".format(str_i))
            #self.v_layout_1_1.addWidget(self.label_1_1_1)
            exec("self.v_layout_{}_1.addWidget(self.label_{}_1_1)".format(str_i,str_i))
            #self.label_1_1_2 = QLabel()

            #self.label_1_1_2.setText(str(msg_1[9])+'  '+str(msg_1[10]))
            exec("self.label_{}_1_2.setText(self.number_format(msg_1[9])+' '+self.number_format(msg_1[10])+'%')".format(str_i))
            #self.v_layout_1_1.addWidget(self.label_1_1_2)
            exec('self.v_layout_{}_1.addWidget(self.label_{}_1_2)'.format(str_i,str_i))

            #self.v_layout_1_2 = QVBoxLayout()
            exec("self.v_layout_{}_2 = QVBoxLayout()".format(str_i))
            # self.h_main_layout_1.addLayout(self.v_layout_1_1)
            exec("self.h_main_layout_{}.addLayout(self.v_layout_{}_2)".format(str_i, str_i))
            #self.label_1_2_1 = QLabel()
            exec("self.label_{}_2_1 = QLabel()".format(str_i))
            #self.label_1_2_2 = QLabel()
            exec("self.label_{}_2_2 = QLabel()".format(str_i))
            exec("self.v_layout_{}_2.addWidget(self.label_{}_2_1)".format(str_i, str_i))
            exec("self.v_layout_{}_2.addWidget(self.label_{}_2_2)".format(str_i, str_i))
            exec("self.label_{}_2_1.setFont(QFont('time', 8, QFont.Bold))".format(str_i))
            exec("self.label_{}_2_2.setFont(QFont('time', 8, QFont.Bold))".format(str_i))
            max_temp = self.number_format(msg_1[4]) #round(msg_1[4],2)
            over_amt = self.number_format(msg_1[6]) #round(msg_1[6],2)
            min_temp = self.number_format(msg_1[5]) #round(msg_1[5],2)
            open_amt = self.number_format(msg_1[3]) #round(msg_1[3],2)
            if max_temp > over_amt:
                exec('self.label_{}_2_1.setText("<font color=black>  最高:</font><font color=red>"+str(max_temp)+"</font>")'.format(str_i))
            elif max_temp < over_amt:
                exec('self.label_{}_2_1.setText("<font color=black>  最高:</font><font color=green>"+str(max_temp)+"</font>")'.format(str_i))
            #self.label_1_2_1.setText("<font color=black size=4>最高:</font><font color=green size=4>"+str(max_temp)+"</font>")
            else:
                exec(
                    'self.label_{}_2_1.setText("<font color=black>  最高:</font><font color=black>"+str(max_temp)+"</font>")'.format(
                        str_i))

            if min_temp > over_amt:
                exec(
                    'self.label_{}_2_2.setText("<font color=black>  最低:</font><font color=red>"+str(min_temp)+"</font>")'.format(
                        str_i))
            elif min_temp < over_amt:
                exec(
                    'self.label_{}_2_2.setText("<font color=black>  最低:</font><font color=green>"+str(min_temp)+"</font>")'.format(
                        str_i))

            #self.v_layout_1_2 = QVBoxLayout()
            exec("self.v_layout_{}_3 = QVBoxLayout()".format(str_i))
            # self.h_main_layout_1.addLayout(self.v_layout_1_1)
            exec("self.h_main_layout_{}.addLayout(self.v_layout_{}_3)".format(str_i, str_i))
            #self.label_1_2_1 = QLabel()
            exec("self.label_{}_3_1 = QLabel()".format(str_i))
            #self.label_1_2_2 = QLabel()
            exec("self.label_{}_3_2 = QLabel()".format(str_i))
            exec("self.v_layout_{}_3.addWidget(self.label_{}_3_1)".format(str_i, str_i))
            exec("self.v_layout_{}_3.addWidget(self.label_{}_3_2)".format(str_i, str_i))
            exec("self.label_{}_3_1.setFont(QFont('time', 8, QFont.Bold))".format(str_i))
            exec("self.label_{}_3_2.setFont(QFont('time', 8, QFont.Bold))".format(str_i))

            if open_amt > over_amt:
                exec('self.label_{}_3_1.setText("<font color=black>今开:</font><font color=red>"+str(open_amt)+"</font>")'.format(str_i))
            elif open_amt < over_amt:
                exec('self.label_{}_3_1.setText("<font color=black>今开:</font><font color=green>"+str(open_amt)+"</font>")'.format(str_i))
            else:
                exec(
                    'self.label_{}_3_1.setText("<font color=black>今开:</font><font color=black>"+str(open_amt)+"</font>")'.format(
                        str_i))

            exec(
                'self.label_{}_3_2.setText("<font color=black>昨收:</font><font color=black>"+str(over_amt)+"</font>")'.format(
                    str_i))

            #self.v_layout_1_2 = QVBoxLayout()
            exec("self.v_layout_{}_4 = QVBoxLayout()".format(str_i))
            # self.h_main_layout_1.addLayout(self.v_layout_1_1)
            exec("self.h_main_layout_{}.addLayout(self.v_layout_{}_4)".format(str_i, str_i))
            #self.label_1_2_1 = QLabel()
            exec("self.label_{}_4_1 = QLabel()".format(str_i))
            #self.label_1_2_2 = QLabel()
            exec("self.label_{}_4_2 = QLabel()".format(str_i))
            exec("self.v_layout_{}_4.addWidget(self.label_{}_4_1)".format(str_i, str_i))
            exec("self.v_layout_{}_4.addWidget(self.label_{}_4_2)".format(str_i, str_i))
            exec("self.label_{}_4_1.setFont(QFont('time', 8, QFont.Bold))".format(str_i))
            exec("self.label_{}_4_2.setFont(QFont('time', 8, QFont.Bold))".format(str_i))
            liang = self.number_change(msg_1[7])
            exchange = self.number_change(msg_1[8])
            print(type(liang))
            print(liang)
            exec(
                'self.label_{}_4_1.setText("<font color=black>成交量:</font><font color=black>"+liang+"</font>")'.format(
                    str_i))

            exec(
                'self.label_{}_4_2.setText("<font color=black>成交额:</font><font color=black>"+exchange+"</font>")'.format(
                    str_i))


    def number_format(self,number):
        temp = str(number)
        nlist = temp.split('.')
        if len(nlist) == 1:
            return temp+'.00'
        elif len(nlist) == 2:
            if len(nlist[1]) == 1:
                return temp+'0'
            else:
                return temp

    def number_change(self,temp):
        if temp > 100000000:
            temp = str(round(temp / 100000000, 2)) + '亿'
        elif temp > 10000000:
            temp = str(round(temp / 10000000, 2)) + '千万'
        elif temp > 10000:
            temp = str(round(temp / 10000, 2)) + '万'
        elif temp > 1000:
            temp = str(round(temp / 1000, 2)) + '千'
        else:
            temp = str(round(temp/1000),2)+'千'
        return temp


class shares_thead(QThread):
    share_signal = pyqtSignal(list)
    def __init__(self,parent=None):
        super(shares_thead,self).__init__(parent)
        self.working = True

    def __del__(self):
        self.working = False
        self.wait()

    def tick(self):
        msg = getshares()  # .git_gupiao(getshares)
        msg_list = msg.git_gupiao()
        print(msg_list)
        self.share_signal.emit(msg_list)

    def run(self):
        scheduler = BlockingScheduler()
        scheduler.add_job(self.tick, 'cron', day_of_week='mon-fri',hour='9-14' ,second='*/5')
        #scheduler.add_job(self.tick, 'cron', second='*/5')
        scheduler.start()



# def run():
#     sched = BlockingScheduler()
#     sched.add_job(my_job,'cron',day_of_week='mon-fri',hour='9-15' ,second='*/5')
#     sched.start()
#
# def my_job():
#     location = time.strftime("%H:%M:%S" ,  time.localtime() )
#    # current = current
#     print('demo'+'->'+location)

if __name__ == '__main__':
    #nongli.nongli()
    App = QApplication(sys.argv)
    win = window()
    sys.exit(App.exec())

