
#默认输入视频帧的大小（1920，1080）如需修改在cnn-yolo.py中
from cnn_yolo import testmainvideo

VIDEO_PATH = 'E:\\original.avi'  # 源视频地址
EXTRACT_FOLDER = 'E:\\result.avi'  # 生成视频存放的位置
EXTRACT_FREQUENCY = 1  # 帧提取频率，每3帧提取一张分析
FPS = 25   #形成视频的每秒帧数
#建议  EXTRACT_FREQUENCY*FPS 等于源视频的每秒帧数
SIZE = (1280,720)  #输出视频大小

testmainvideo(VIDEO_PATH,EXTRACT_FOLDER,EXTRACT_FREQUENCY,FPS,SIZE)


