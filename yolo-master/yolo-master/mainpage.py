from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QWidget,QFileDialog,QLabel
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import QUrl
import sys
from cnn_yolo import testmainpicture
from cnn_yolo import testmainvideo
from network import picnetwork

#全局变量——文件名
FILE_NAME = ''
IN_FILE = ''
OUT_FILE = ''

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        #视图参数
        self.title = "基于多目标检测模型的车辆检测系统【检测端】"
        self.top = 100
        self.left = 100
        self.width = 1500
        self.height = 800

        self.InitWindow()

    def InitWindow(self):
        #初始化视图
        self.setWindowTitle(self.title)
        self.setGeometry(self.top,self.left,self.width,self.height)
        #self.show()

        #初始化背景图片
        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(),QtGui.QBrush(QtGui.QPixmap("./layout_pic/background.png")))
        self.setPalette(window_pale)

        #初始化“车辆检测”按钮
        button_pic = QPushButton("车辆检测",self)
        button_pic.setMinimumSize(220,100)
        button_pic.move(200,340)
        font = QtGui.QFont()
        font.setPointSize(34)
        button_pic.setFont(font)
        button_pic.clicked.connect(self.pic_on_click)

        #初始化“车辆跟踪”按钮
        button_video = QPushButton("车辆跟踪",self)
        button_video.setMinimumSize(220,100)
        button_video.move(200,520)
        font = QtGui.QFont()
        font.setPointSize(34)
        button_video.setFont(font)
        button_video.clicked.connect(self.vedio_on_click)

    def pic_on_click(self):
        picwindow.show()
        mainwindow.close()
        vediowindow.close()

    def vedio_on_click(self):
        vediowindow.show()
        mainwindow.close()
        picwindow.close()

class PicWindow(QWidget):

    def __init__(self):
        super().__init__()

        #视图参数
        self.title = "【检测端】车辆检测"
        self.top = 100
        self.left = 100
        self.width = 1500
        self.height = 800

        self.input_pic = QLabel(self)
        self.pix_input = QtGui.QPixmap("./layout_pic/cqupt_icon.jpg")

        self.output_pic = QLabel(self)
        self.pix_output = QtGui.QPixmap("./layout_pic/cqupt_icon.jpg")

        self.InitWindow()

    def InitWindow(self):
        #初始化视图
        self.setWindowTitle(self.title)
        self.setGeometry(self.top,self.left,self.width,self.height)

        #初始化背景图片
        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(),QtGui.QBrush(QtGui.QPixmap("./layout_pic/black_background.png")))
        self.setPalette(window_pale)

        #初始化两个图像框
        self.input_pic.move(50,50)
        self.input_pic.setMinimumSize(800,600)
        self.input_pic.setMaximumSize(800,600)

        self.input_pic.setPixmap(self.pix_input)


        self.output_pic.move(800,50)
        self.output_pic.setMinimumSize(800,600)
        self.output_pic.setMaximumSize(800,600)

        self.output_pic.setPixmap(self.pix_output)

        #初始化“返回上级”按钮
        pic_back = QPushButton("返回上级",self)
        pic_back.setMinimumSize(160,80)
        pic_back.move(300,660)
        font = QtGui.QFont()
        font.setPointSize(34)
        pic_back.setFont(font)
        pic_back.clicked.connect(self.pic_back_click)

        #初始化“选择图片”按钮
        pic_choose = QPushButton("选择图片",self)
        pic_choose.setMinimumSize(160,80)
        pic_choose.move(560,660)
        font = QtGui.QFont()
        font.setPointSize(34)
        pic_choose.setFont(font)
        pic_choose.clicked.connect(self.pic_choose_click)

        #初始化“开始检测”按钮
        pic_detection = QPushButton("开始检测",self)
        pic_detection.setMinimumSize(160,80)
        pic_detection.move(820,660)
        font = QtGui.QFont()
        font.setPointSize(34)
        pic_detection.setFont(font)
        pic_detection.clicked.connect(self.pic_detection_click)

        #初始化“上传结果”按钮
        pic_upload = QPushButton("上传结果",self)
        pic_upload.setMinimumSize(160,80)
        pic_upload.move(1080,660)
        font = QtGui.QFont()
        font.setPointSize(34)
        pic_upload.setFont(font)
        pic_upload.clicked.connect(self.pic_upload_click)

    #"返回上级"按钮触发事件
    def pic_back_click(self):
        mainwindow.show()
        picwindow.close()
        FILE_NAME = "./layout_pic/cqupt_icon.jpg"
        self.pix_input = QtGui.QPixmap(FILE_NAME)
        self.input_pic.setPixmap(self.pix_input)

    #"选择图片"按钮触发事件
    def pic_choose_click(self):
        filename = QFileDialog.getOpenFileName(self,"open file",'./images/')
        global FILE_NAME
        FILE_NAME = '.' + filename[0][54:]
        print(FILE_NAME)
        self.pix_input = QtGui.QPixmap(FILE_NAME)
        self.input_pic.setPixmap(self.pix_input)

    def pic_detection_click(self):
        global FILE_NAME,IN_FILE,OUT_FILE
        IN_FILE = FILE_NAME
        OUT_FILE = "./out"+FILE_NAME[8:]
        print(IN_FILE)
        print(OUT_FILE)
        testmainpicture(IN_FILE, OUT_FILE)

        self.pix_output = QtGui.QPixmap(OUT_FILE)
        self.output_pic.setPixmap(self.pix_output)

    def pic_upload_click(self):
        global OUT_FILE
        print(OUT_FILE)
        picnetwork.uploadResult(["test.jpg","number.txt"],[OUT_FILE,"./number.txt"])
        return None

class VedioWindow(QWidget):
    def __init__(self):
        super().__init__()

        #视图参数
        self.title = "【检测端】车辆跟踪"
        self.top = 100
        self.left = 100
        self.width = 1500
        self.height = 800

        self.InitWindow()

    def InitWindow(self):
        #初始化视图
        self.setWindowTitle(self.title)
        self.setGeometry(self.top,self.left,self.width,self.height)

        #初始化背景图片
        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(),QtGui.QBrush(QtGui.QPixmap("./layout_pic/black_background.png")))
        self.setPalette(window_pale)

        #初始化输入和输视频加载框
        self.input_player = QMediaPlayer(self)
        self.input_vedio = QVideoWidget(self)
        self.input_vedio.move(0,50)
        self.input_vedio.setMinimumSize(800,600)
        self.input_vedio.setMaximumSize(800,600)
        self.input_vedio.show()
        self.input_player.setVideoOutput(self.input_vedio)

        self.output_player = QMediaPlayer(self)
        self.output_vedio = QVideoWidget(self)
        self.output_vedio.move(780,50)
        self.output_vedio.setMinimumSize(800,600)
        self.output_vedio.setMaximumSize(800,600)
        self.output_vedio.show()
        self.output_player.setVideoOutput(self.output_vedio)

        #初始化“返回上级”按钮
        vedio_back = QPushButton("返回上级",self)
        vedio_back.setMinimumSize(160,80)
        vedio_back.move(300,660)
        font = QtGui.QFont()
        font.setPointSize(34)
        vedio_back.setFont(font)
        vedio_back.clicked.connect(self.vedio_back_click)

        #初始化“选择视频”按钮
        vedio_choose = QPushButton("选择视频",self)
        vedio_choose.setMinimumSize(160,80)
        vedio_choose.move(560,660)
        font = QtGui.QFont()
        font.setPointSize(34)
        vedio_choose.setFont(font)
        vedio_choose.clicked.connect(self.vedio_choose_click)

        #初始化“开始跟踪”按钮
        vedio_detection = QPushButton("开始跟踪",self)
        vedio_detection.setMinimumSize(160,80)
        vedio_detection.move(820,660)
        font = QtGui.QFont()
        font.setPointSize(34)
        vedio_detection.setFont(font)
        vedio_detection.clicked.connect(self.vedio_detection_click)

        #初始化“上传结果”按钮
        vedio_upload = QPushButton("上传结果",self)
        vedio_upload.setMinimumSize(160,80)
        vedio_upload.move(1080,660)
        font = QtGui.QFont()
        font.setPointSize(34)
        vedio_upload.setFont(font)
        vedio_upload.clicked.connect(self.vedio_upload_click)

    def vedio_back_click(self):
        mainwindow.show()
        vediowindow.close()

    def vedio_choose_click(self):
        tempFile = QFileDialog.getOpenFileUrl()[0]
        self.input_player.setMedia(QMediaContent(tempFile))
        self.input_player.play()
        tempFile = tempFile.toString()[62:]
        global IN_FILE,OUT_FILE
        IN_FILE = "."+tempFile
        OUT_FILE = "./out/"+tempFile[7:]
        #self.input_player.pause()

    def vedio_detection_click(self):
        EXTRACT_FREQUENCY = 5
        FPS = 5
        SIZE = (600, 400)
        global IN_FILE,OUT_FILE
        testmainvideo(IN_FILE,OUT_FILE,EXTRACT_FREQUENCY,FPS,SIZE)
        self.output_player.setMedia(QMediaContent(QUrl.fromLocalFile(OUT_FILE)))
        self.output_player.play()
        #print(IN_FILE,OUT_FILE)

    def vedio_upload_click(self):
        global OUT_FILE
        picnetwork.uploadVedio("vediotest.avi",OUT_FILE)
        return None

App = QApplication(sys.argv)
mainwindow = Window()
picwindow = PicWindow()
vediowindow = VedioWindow()
mainwindow.show()
sys.exit(App.exec())