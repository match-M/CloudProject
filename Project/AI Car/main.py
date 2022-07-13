#UTF-8
import time
import _XiaoRGEEK_GPIO_ as XR
import _XiaoRGEEK_GLOBAL_variable_ as G_val
from _XiaoRGEEK_MOTOR_ import Robot_Direction
go = Robot_Direction()
import cv2
import numpy as np
from _XiaoRGEEK_SOCKET_ import XR_SOCKET
soc = XR_SOCKET()
import RPi.GPIO as GPIO
import _XiaoRGEEK_GLOBAL_variable_ as glo
from socket import *
import binascii
import threading
from _XiaoRGEEK_SERVO_ import XR_Servo
Servo = XR_Servo()
from _XiaoRGEEK_LED_ import Robot_Led
XRLED = Robot_Led()
import bluetooth
from subprocess import call
import os
####################################################
##�������� Path_Dect()
##�������� ������ͷѲ�ߵ�����ƺ���
##��ڲ��� ��FF130800FF������ͷ���ԣ�FF130801FF��ʼ����ͷѭ��
##���ڲ��� 
#int Path_Dect_px 	ƽ����������
#int Path_Dect_on	1:��ʼѭ����0ֹͣѭ��
####################################################
def	Path_Dect():
	while (G_val.Path_Dect_on):
		print 'Path_Dect_px %d '%G_val.Path_Dect_px	 #��ӡѲ�����ĵ�����ֵ
		if (G_val.Path_Dect_px < 260)&(G_val.Path_Dect_px > 0):	#���Ѳ�����ĵ�ƫ�󣬾���Ҫ��ת��У����
			print("turn left")
			go.left()
		elif G_val.Path_Dect_px> 420:
			print("turn right")
			go.right()
		else :
			go.forward()
			print("go stright")
		time.sleep(0.007)
		go.stop()
		time.sleep(0.006)
####################################################
##�������� Path_Dect_img_processing()
##�������� ������ͷѲ��ͼ������
##��ڲ��� ��FF130800FF������ͷ���ԣ�FF130801FF��ʼ����ͷѭ��
##���ڲ��� 
#int Path_Dect_px 	ƽ����������
#int Path_Dect_on	1:��ʼѭ����0����ģʽ/ֹͣѭ��
####################################################
def	Path_Dect_img_processing():
	Path_Dect_fre_count = 1
	Path_Dect_px_sum = 0
	Path_Dect_cap = 0
	print("into theads Path_Dect_img_processing")
	while True:
		if(G_val.Path_Dect_on):
			if(Path_Dect_cap == 0):
				cap = cv2.VideoCapture(0)
				Path_Dect_cap = 1
			else:
				ret,frame = cap.read()	#capture frame_by_frame
				gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #get gray img
				if (G_val.Path_Dect_Flag == 0):
					ret,thresh1=cv2.threshold(gray,70,255,cv2.THRESH_BINARY)		#Ѳ��ɫ��
				else :
					ret,thresh1=cv2.threshold(gray,70,255,cv2.THRESH_BINARY_INV)	#Ѳ��ɫ��
				for j in range(0,640,5):
					if thresh1[240,j] == 0:
						Path_Dect_px_sum = Path_Dect_px_sum + j
						Path_Dect_fre_count = Path_Dect_fre_count + 1 
				G_val.Path_Dect_px =  (Path_Dect_px_sum)/ (Path_Dect_fre_count)
				Path_Dect_px_sum = 0
				Path_Dect_fre_count = 1
		elif(Path_Dect_cap):
			go.stop()
			time.sleep(0.001)
			Path_Dect_cap = 0
			cap.release()
		time.sleep(0.1)
####################################################
##�������� 
##�������� Route() ·���滮
##��ڲ��� ����
##���ڲ��� ����
####################################################
def Route():
	while G_val.RevStatus !=0 :
		print 'RevStatus==== %d ' %G_val.RevStatus
		TurnA=float(G_val.TurnAngle*6)/1000
		Golen=float(G_val.Golength*10)/1000
		print 'TurnAngle====== %f ' %TurnA
		print 'Golength======= %f ' %Golen
		if G_val.RevStatus==1:
			go.left()
			time.sleep(TurnA)
			go.stop()
			go.forward()
			time.sleep(Golen)
			go.stop()
			G_val.RevStatus = 0
			buf  = ['\xFF','\xA8','\x00','\x00','\xFF']
			soc.Sendbuf(buf)
			time.sleep(0.01)
		elif G_val.RevStatus==2:
			go.right()
			time.sleep(TurnA)
			go.stop()
			go.forward()
			time.sleep(Golen)
			go.stop()
			G_val.RevStatus = 0
			buf  = ['\xFF','\xA8','\x00','\x00','\xFF']
			soc.Sendbuf(buf)
			time.sleep(0.01)
####################################################
##�������� ��Avoiding()
##�������� ��������Ϻ���
##��ڲ��� ����
##���ڲ��� ����
####################################################
def	_Avoiding_(): #������Ϻ���
	if XR.DigitalRead(XR.IR_M) == False:
		go.forward()
	else:
		go.stop()
		time.sleep(0.1)
####################################################
##�������� TrackLine()
##�������� Ѳ����ģʽ
##��ڲ��� ����
##���ڲ��� ����
####################################################
def _TrackLine_():
	if (XR.DigitalRead(XR.IR_L) == False)&(XR.DigitalRead(XR.IR_R) == False): #����Ϊ�ߣ�����Ϊ��
		go.forward()
		#return
	elif (XR.DigitalRead(XR.IR_L) == False)&(XR.DigitalRead(XR.IR_R) == True):
		go.right()
		#return
	elif (XR.DigitalRead(XR.IR_L) == True)&(XR.DigitalRead(XR.IR_R) == False):
		go.left()
		#return
	elif (XR.DigitalRead(XR.IR_L) == True)&(XR.DigitalRead(XR.IR_R) == True): #���඼��������
		go.stop()
		#return
####################################################
##�������� Follow()
##�������� ����ģʽ
##��ڲ��� ����
##���ڲ��� ����
####################################################
def _Follow_(): 
	if(XR.DigitalRead(XR.IR_M) == True): #�м䴫����OK
		if(XR.DigitalRead(XR.IRF_L) == False)&(XR.DigitalRead(XR.IRF_R) == False):	#����ͬʱ̽�⵽�ϰ���
			go.stop()			#ֹͣ 
		if(XR.DigitalRead(XR.IRF_L) == False)&(XR.DigitalRead(XR.IRF_R) == True):		#����ϰ���
			go.right()		#��ת 
		if(XR.DigitalRead(XR.IRF_L) == True)& (XR.DigitalRead(XR.IRF_R) == False):		#�Ҳ��ϰ���
			go.left()		#��ת
		if(XR.DigitalRead(XR.IRF_L) == True)& (XR.DigitalRead(XR.IRF_R) == True):		#���κ��ϰ���
			go.forward()			#ֱ�� 
	else:
		go.stop()
####################################################
##�������� ��Get_Distence()
##�������� ��������࣬���ؾ��루��λ�����ף�
##��ڲ��� ����
##���ڲ��� ����
####################################################
def	_Get_Distence_():
	time_count = 0
	time.sleep(0.01)
	XR.GPIOSet(XR.TRIG)
	time.sleep(0.000015)
	XR.GPIOClr(XR.TRIG)
	while not XR.DigitalRead(XR.ECHO):
		pass
	t1 = time.time()
	while XR.DigitalRead(XR.ECHO):
		if(time_count < 0xfff):
			time_count = time_count + 1
			time.sleep(0.000001)
			pass
		else :
			print 'NO ECHO receive! Please check connection '
			break
	t2 = time.time()
	Distence = (t2-t1)*340/2*100
	print 'Distence is %d'%Distence
	if (Distence < 500):
		print 'Distence is %d'%Distence
		return Distence
	else :
		print 'Distence is 0'
		return 0 
####################################################
##�������� Avoid_wave()
##�������� ���������Ϻ���
##��ڲ��� ����
##���ڲ��� ����
####################################################
def	_AvoidByRadar_():
	dis = _Get_Distence_()
	#print 'Distence is %d'%dis
	if 300>dis>G_val.Radar_distence:
        go.forward()
	else:
        do:
            go.stop()
            go.left()
        while 300>dis>G_val.Radar_distence
####################################################
##�������� Send_Distance()
##�������� ������������PC����ʾ
##��ڲ��� ����
##���ڲ��� ����
####################################################
def	_Send_Distance_():
	dis_send = int(_Get_Distence_())
	send_buf=[]
	send_flag = False
	if 2<dis_send < 255:
		send_buf=['\xff','\x03','\x00',chr(dis_send),'\xff']
		#send_flag = True
		soc.Sendbuf(send_buf)
	else:
		send_buf=[]
	#time.sleep(0.05)

	
		

class XR_Function_Default:
	def __init__(self):
		pass
	def	Avoiding(self):
		_Avoiding_()
	def TrackLine(self):
		_TrackLine_()
	def Follow(self): 
		_Follow_()
	def Get_Distence(self):
		return _Get_Distence_()
	def AvoidByRadar(self):
		_AvoidByRadar_()
	def Send_Distance(self):
		 _Send_Distance_()

#######################################
#############�ź����Ŷ���##############
#######################################
########LED�ڶ���#################
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
LED0 = 10
LED1 = 9
LED2 = 25
########��������ӿڶ���#################
ENA = 13	#//L298ʹ��A
ENB = 20	#//L298ʹ��B
IN1 = 19	#//����ӿ�1
IN2 = 16	#//����ӿ�2
IN3 = 21	#//����ӿ�3
IN4 = 26	#//����ӿ�4
########����ӿڶ���#################
########�������ӿڶ���#################
ECHO = 4	#���������ս�λ  
TRIG = 17	#�����������λ
########���⴫�����ӿڶ���#################
IR_R = 18	#С���Ҳ�Ѳ�ߺ���
IR_L = 27	#С�����Ѳ�ߺ���
IR_M = 22	#С���м���Ϻ���
IRF_R = 23	#С�������Ҳ����
IRF_L = 24	#С������������



#########led��ʼ��Ϊ000##########
GPIO.setup(LED0,GPIO.OUT,initial=GPIO.HIGH)
GPIO.setup(LED1,GPIO.OUT,initial=GPIO.HIGH)
GPIO.setup(LED2,GPIO.OUT,initial=GPIO.HIGH)
#########�����ʼ��ΪLOW##########
GPIO.setup(ENA,GPIO.OUT,initial=GPIO.LOW)
ENA_pwm=GPIO.PWM(ENA,1000)
ENA_pwm.start(0)
ENA_pwm.ChangeDutyCycle(100)
GPIO.setup(IN1,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(IN2,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(ENB,GPIO.OUT,initial=GPIO.LOW)
ENB_pwm=GPIO.PWM(ENB,1000)
ENB_pwm.start(0)
ENB_pwm.ChangeDutyCycle(100)
GPIO.setup(IN3,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(IN4,GPIO.OUT,initial=GPIO.LOW)
#########�����ʼ��Ϊ���룬���ڲ�����#########
GPIO.setup(IR_R,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(IR_L,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(IR_M,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(IRF_R,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(IRF_L,GPIO.IN,pull_up_down=GPIO.PUD_UP)
##########������ģ��ܽ���������#########
GPIO.setup(TRIG,GPIO.OUT,initial=GPIO.LOW)#������ģ�鷢��˹ܽ�����trig
GPIO.setup(ECHO,GPIO.IN,pull_up_down=GPIO.PUD_UP)#������ģ����ն˹ܽ�����echo




'''
def	GPIO_setup():
#########led��ʼ��Ϊ000##########
	GPIO.setup(LED0,GPIO.OUT,initial=GPIO.HIGH)
	GPIO.setup(LED1,GPIO.OUT,initial=GPIO.HIGH)
	GPIO.setup(LED2,GPIO.OUT,initial=GPIO.HIGH)
#########�����ʼ��ΪLOW##########
	ENA_Setup().ENA_init()
	GPIO.setup(IN1,GPIO.OUT,initial=GPIO.LOW)
	GPIO.setup(IN2,GPIO.OUT,initial=GPIO.LOW)
	ENB_Setup().ENB_init()
	GPIO.setup(IN3,GPIO.OUT,initial=GPIO.LOW)
	GPIO.setup(IN4,GPIO.OUT,initial=GPIO.LOW)
#########�����ʼ��Ϊ���룬���ڲ�����#########
	GPIO.setup(IR_R,GPIO.IN,pull_up_down=GPIO.PUD_UP)
	GPIO.setup(IR_L,GPIO.IN,pull_up_down=GPIO.PUD_UP)
	GPIO.setup(IR_M,GPIO.IN,pull_up_down=GPIO.PUD_UP)
	GPIO.setup(IRF_R,GPIO.IN,pull_up_down=GPIO.PUD_UP)
	GPIO.setup(IRF_L,GPIO.IN,pull_up_down=GPIO.PUD_UP)
##########������ģ��ܽ���������#########
	GPIO.setup(TRIG,GPIO.OUT,initial=GPIO.LOW)#������ģ�鷢��˹ܽ�����trig
	GPIO.setup(ECHO,GPIO.IN,pull_up_down=GPIO.PUD_UP)#������ģ����ն˹ܽ�����echo
'''
def	GPIOSet(gpio):
	GPIO.output(gpio,True)

def	GPIOClr(gpio):
	GPIO.output(gpio,False)
def	DigitalRead(gpio):
	return GPIO.input(gpio)
def ENAset(EA_num):
	ENA_pwm.ChangeDutyCycle(EA_num)
def ENBset(EB_num):
	ENB_pwm.ChangeDutyCycle(EB_num)

def	_FLOW_LED_():#��ˮ��
	print(" Flow led start...")
	XR.GPIOClr(XR.LED0)
	XR.GPIOClr(XR.LED1)
	XR.GPIOClr(XR.LED2)
	time.sleep(0.2)
	for i in range(0, 10):
		XR.GPIOSet(XR.LED0)
		XR.GPIOClr(XR.LED1)
		XR.GPIOClr(XR.LED2)
		time.sleep(0.2)
		XR.GPIOClr(XR.LED0)
		XR.GPIOSet(XR.LED1)
		XR.GPIOClr(XR.LED2)
		time.sleep(0.2)
		XR.GPIOClr(XR.LED0)
		XR.GPIOClr(XR.LED1)
		XR.GPIOSet(XR.LED2)
		time.sleep(0.2)
		XR.GPIOClr(XR.LED0)
		XR.GPIOClr(XR.LED1)
		XR.GPIOClr(XR.LED2)
		time.sleep(0.2)
	print(" Flow led over...")
####################################################
##�������� Open_Light()
##�������� �����LED0
##��ڲ��� ����
##���ڲ��� ����
####################################################
def	_Open_Light_():#�����LED0
	XR.GPIOClr(XR.LED0)#���������5V  ������IO��
	time.sleep(0.5)

####################################################
##�������� Close_Light()
##�������� �ش��
##��ڲ��� ����
##���ڲ��� ����
####################################################
def	_Close_Light_():#�ش��
	XR.GPIOSet(XR.LED0)#���������5V  ������IO��
	time.sleep(0.5)

class Robot_Led:
	def __init__(self):
		pass
	def	Open_Light(self):
		_Open_Light_()
	def	Close_Light(self):
		_Close_Light_()
	def FLOW_LED(self):
		_FLOW_LED_()

def _Motor_Forward_():
	#print ' M2-L FOR;M1-R FOR; '
	XR.GPIOSet(XR.ENA)
	XR.GPIOSet(XR.ENB)
	XR.GPIOSet(XR.IN1)
	XR.GPIOClr(XR.IN2)
	XR.GPIOSet(XR.IN3)
	XR.GPIOClr(XR.IN4)
	XR.GPIOClr(XR.LED1)
	XR.GPIOClr(XR.LED2)
def _Motor_Backward_():
	#print ' M2-L REV;M1-R REV; '
	XR.GPIOSet(XR.ENA)
	XR.GPIOSet(XR.ENB)
	XR.GPIOClr(XR.IN1)
	XR.GPIOSet(XR.IN2)
	XR.GPIOClr(XR.IN3)
	XR.GPIOSet(XR.IN4)
	XR.GPIOSet(XR.LED1)
	XR.GPIOClr(XR.LED2)
def _Motor_TurnLeft_():
	#print ' M2-L REV;M1-R FOR; '
	XR.GPIOSet(XR.ENA)
	XR.GPIOSet(XR.ENB)
	XR.GPIOSet(XR.IN1)
	XR.GPIOClr(XR.IN2)
	XR.GPIOClr(XR.IN3)
	XR.GPIOSet(XR.IN4)
	XR.GPIOClr(XR.LED1)
	XR.GPIOSet(XR.LED2)
def _Motor_TurnRight_():
	#print ' M2-L FOR;M1-R REV; '
	XR.GPIOSet(XR.ENA)
	XR.GPIOSet(XR.ENB)
	XR.GPIOClr(XR.IN1)
	XR.GPIOSet(XR.IN2)
	XR.GPIOSet(XR.IN3)
	XR.GPIOClr(XR.IN4)
	XR.GPIOClr(XR.LED1)
	XR.GPIOSet(XR.LED2)
def _Motor_Stop_():
	#print ' M2-L STOP;M1-R STOP; '
	XR.GPIOClr(XR.ENA)
	XR.GPIOClr(XR.ENB)
	XR.GPIOClr(XR.IN1)
	XR.GPIOClr(XR.IN2)
	XR.GPIOClr(XR.IN3)
	XR.GPIOClr(XR.IN4)
	XR.GPIOSet(XR.LED1)
	XR.GPIOClr(XR.LED2)
##########�������ٶȿ���###########################
def _ENA_Speed_(EA_num):
	print ' M1_R�ٶȱ�Ϊ %d '%EA_num
	XR.ENAset(EA_num)

def _ENB_Speed_(EB_num):
	print ' M2_L�ٶȱ�Ϊ %d '%EB_num
	XR.ENBset(EB_num)

class Robot_Direction:
	def __init__(self):
		pass
		#self.motor_flag = motor_flag
	def forward(self):
		#print " Robot go forward %d"%motor_flag
		if ((glo.motor_flag == 1)or(glo.motor_flag == 2)):
			_Motor_Forward_()
		elif ((glo.motor_flag == 3)or(glo.motor_flag == 4)):
			_Motor_Backward_()
		elif ((glo.motor_flag == 5)or(glo.motor_flag == 6)):
			_Motor_TurnLeft_()
		elif ((glo.motor_flag == 7)or(glo.motor_flag == 8)):
			_Motor_TurnRight_()
	def back(self):
		#print " Robot go back"
		if ((glo.motor_flag == 1)or(glo.motor_flag == 2)):
			_Motor_Backward_()
		elif ((glo.motor_flag == 3)or(glo.motor_flag == 4)):
			_Motor_Forward_()
		elif ((glo.motor_flag == 5)or(glo.motor_flag == 6)):
			_Motor_TurnRight_()
		elif ((glo.motor_flag == 7)or(glo.motor_flag == 8)):
			_Motor_TurnLeft_()
	def left(self):
		#print " Robot turn left"
		if ((glo.motor_flag == 1)or(glo.motor_flag == 3)):
			_Motor_TurnLeft_()
		elif ((glo.motor_flag == 2)or(glo.motor_flag == 4)):
			_Motor_TurnRight_()
		elif ((glo.motor_flag == 5)or(glo.motor_flag == 7)):
			_Motor_Forward_()
		elif ((glo.motor_flag == 6)or(glo.motor_flag == 8)):
			_Motor_Backward_()
	def right(self):
		#print " Robot turn right"
		if ((glo.motor_flag == 1)or(glo.motor_flag == 3)):
			_Motor_TurnRight_()
		elif ((glo.motor_flag == 2)or(glo.motor_flag == 4)):
			_Motor_TurnLeft_()
		elif ((glo.motor_flag == 5)or(glo.motor_flag == 7)):
			_Motor_Backward_()
		elif ((glo.motor_flag == 6)or(glo.motor_flag == 8)):
			_Motor_Forward_()
	def stop(self):
		_Motor_Stop_()
	def M1_Speed(self,EA_num):
		_ENA_Speed_(EA_num)
	def M2_Speed(self,EB_num):
		_ENB_Speed_(EB_num)

#BT_Server
BT_Server=socket(AF_INET,SOCK_STREAM)
BT_Server.bind(('',2002))
BT_Server.listen(1)
BT_buffer=[]


#tcp_server
TCP_Server=socket(AF_INET,SOCK_STREAM)
TCP_Server.bind(('',2001))
TCP_Server.listen(1)
TCP_buffer=[]
#for all socket


####################################################
##�������� ��������ƺ���,���ýǶȱ�������ֹת������
##��ڲ��� ��ServoNum(�����)��angle_from_protocol(����Ƕ�)
##���ڲ��� ����
####################################################
def _Angle_cal_(angle_from_protocol):
	angle=hex(eval('0x'+angle_from_protocol))
	angle=int(angle,16)
	if angle > G_val.servo_angle_max:
		angle = G_val.servo_angle_max
	elif angle < G_val.servo_angle_min:
		angle = G_val.servo_angle_min
	return angle

####################################################
##�������� Communication_Decode()
##�������� ��ͨ��Э�����
##��ڲ��� ����
##���ڲ��� ����
####################################################    
def _Communication_Decode_(buffer):
	#print 'Communication_decoding...'
	if buffer[0]=='00':
		if buffer[1]=='01':				#ǰ��
			go.forward()
		elif buffer[1]=='02':			#����
			go.back()
		elif buffer[1]=='03':			#��ת
			go.left()
		elif buffer[1]=='04':			#��ת
			go.right()
		elif buffer[1]=='00':			#ֹͣ
			go.stop()
		else:
			go.stop()
	elif buffer[0]=='02':
		if buffer[1]=='01':#M1_R�ٶ�
			speed=hex(eval('0x'+buffer[2]))
			speed=int(speed,16)
			go.M2_Speed(speed)
		elif buffer[1]=='02':#M2_L���ٶ�
			speed=hex(eval('0x'+buffer[2]))
			speed=int(speed,16)
			go.M1_Speed(speed)
	elif buffer[0]=='01':
		ServoNum = eval('0x'+buffer[1])
		angle  = _Angle_cal_(buffer[2])
		Servo.XiaoRGEEK_SetServoAngle(ServoNum,angle)
		if (angle%2):
			XR.GPIOSet(XR.LED1)
			XR.GPIOSet(XR.LED2)
		else:
			XR.GPIOClr(XR.LED2)
			XR.GPIOClr(XR.LED1)
	elif buffer[0]=='13':
		if buffer[1]=='01':
			G_val.Cruising_Flag = 1#����������ģʽ
			print 'Cruising_Flag�������ģʽ 1 '
		elif buffer[1]=='02':#�������Ѳ��ģʽ
			G_val.Cruising_Flag = 2
			print 'Cruising_Flag����Ѳ��ģʽ %d '%G_val.Cruising_Flag
		elif buffer[1]=='03':#����������ģʽ
			G_val.Cruising_Flag = 3
			print 'Cruising_Flag�������ģʽ %d '%G_val.Cruising_Flag
		elif buffer[1]=='04':#���볬��������ģʽ
			G_val.Cruising_Flag = 4
			print 'Cruising_Flag���������� %d '%G_val.Cruising_Flag
		elif buffer[1]=='05':#���볬��������PC��ʾ
			G_val.Cruising_Flag = 5
			print 'Cruising_Flag����������PC��ʾ %d '%G_val.Cruising_Flag
		elif buffer[1]=='06':
			G_val.Cruising_Flag = 6
			print 'Cruising_Flag������ҡͷ���� %d '%G_val.Cruising_Flag
		elif buffer[1]=='07':
			_Socket_sendbuf_(['\xFF','\xA8','\x00','\x00','\xFF'])
			G_val.Cruising_Flag = 7
		elif buffer[1]=='08':
			if buffer[2]=='00':#Path_Dect ����ģʽ
				G_val.Path_Dect_on = 0
				G_val.Cruising_Flag = 8
				print 'Cruising_Flag Path_Dect����ģʽ 8'
			elif buffer[2]=='01':#Path_Dect ѭ��ģʽ
				path_sh = 'sh '+ os.path.split(os.path.abspath(__file__))[0] + '/stop_mjpg_streamer.sh &'
				call("%s"%path_sh,shell=True)
				time.sleep(2)
				G_val.Path_Dect_on = 1
				G_val.Cruising_Flag = 9
				print 'Cruising_Flag Path_Dectѭ��ģʽ 9 '
		elif buffer[1]=='00':
			G_val.RevStatus=0
			G_val.Cruising_Flag = 0
			print 'Cruising_Flag����ģʽ %d '%G_val.Cruising_Flag
	elif buffer[0]=='a0':
		Tangle=hex(eval('0x'+buffer[1]))
		Tangle=int(Tangle,16)
		G_val.TurnAngle=Tangle
		Golen=hex(eval('0x'+buffer[2]))
		Golen=int(Golen,16)
		G_val.Golength=Golen
		G_val.RevStatus=2
	elif buffer[0]=='a1':
		Tangle=hex(eval('0x'+buffer[1]))
		Tangle=int(Tangle,16)
		G_val.TurnAngle=Tangle
		Golen=hex(eval('0x'+buffer[2]))
		Golen=int(Golen,16)
		G_val.Golength=Golen
		G_val.RevStatus=1
	elif buffer[0]=='40':
		temp=hex(eval('0x'+buffer[1]))
		temp=int(temp,16)
		print 'mode_flag====== %d '%temp
		G_val.motor_flag = temp 
	elif buffer[0]=='32':		#�洢�Ƕ�
		Servo.XiaoRGEEK_SaveServo()
		XR.GPIOSet(XR.LED1)
		XR.GPIOClr(XR.LED2)
		time.sleep(0.01)
		XR.GPIOSet(XR.LED2)
		XR.GPIOClr(XR.LED1)
	elif buffer[0]=='33':		#��ȡ�Ƕ�
		Servo.XiaoRGEEK_ReSetServo()
		XR.GPIOSet(XR.LED1)
		XR.GPIOClr(XR.LED2)
		time.sleep(0.01)
		XR.GPIOSet(XR.LED2)
		XR.GPIOClr(XR.LED1)
	elif buffer[0]=='04':		#���ص�ģʽ FF040000FF����  FF040100FF�ص�
		if buffer[1]=='00':
			XRLED.Open_Light()
		elif buffer[1]=='01':
			XRLED.Close_Light()
		else:
			print 'error1 command!'
	elif buffer == ['ef','ef','ee'] :
		print 'Heartbeat Packet!'
	elif buffer[0]=='fc':#FFFC0000FF  shutdown
		XR.GPIOClr(XR.LED0)
		XR.GPIOClr(XR.LED1)
		XR.GPIOClr(XR.LED2)
		time.sleep(0.1)
		XR.GPIOSet(XR.LED0)
		XR.GPIOSet(XR.LED1)
		XR.GPIOSet(XR.LED2)
		time.sleep(0.1)
		XR.GPIOClr(XR.LED0)
		XR.GPIOClr(XR.LED1)
		XR.GPIOClr(XR.LED2)
		time.sleep(0.1)
		XR.GPIOSet(XR.LED0)
		XR.GPIOSet(XR.LED1)
		XR.GPIOSet(XR.LED2)
		os.system("sudo shutdown -h now")
	else:
		print 'error4 command!'


def _Socket_sendbuf_(buf):
	send_buf = buf
	if(G_val.TCP_Client != False):
		for i in range(0,5):
			try:
				G_val.TCP_Client.send(send_buf[i])
				time.sleep(0.005)
			except:
				print 'send error '
	if(G_val.BT_Client != False):
		for i in range(0,5):
			try:
				G_val.BT_Client.send(send_buf[i])
				time.sleep(0.005)
			except:
				print 'send error '
	print 'ssssssss'

def _T_SOCKET_(T_Server,T_buffer,t_name):
	T_rec_flag=0
	T_count=0
	while True:
		print 'waitting for %s connection...'%t_name,"\r"
		if (t_name == 'BT'):
			G_val.BT_Client = False
			G_val.BT_Client,T_ADDR=T_Server.accept();
			T_Client = G_val.BT_Client
			print(str(T_ADDR[0])+' %s Connected!'%t_name),"\r"
		elif(t_name == 'TCP'):
			G_val.TCP_Client = False
			G_val.TCP_Client,T_ADDR=T_Server.accept();
			T_Client = G_val.TCP_Client
			print(str(T_ADDR[0])+' %s Connected!'%t_name),"\r"
		while True:
			try:
				T_data=T_Client.recv(1)
				T_data=binascii.b2a_hex(T_data)
			except:
				print "%s  Error receiving:"%t_name,"\r"
				break
			if not T_data:
				break
			if T_rec_flag==0:
				if T_data=='ff':
					T_buffer[:]=[]
					T_rec_flag=1
					T_count=0
			else:
				if T_data=='ff':
					T_rec_flag=0
					if T_count==3:
						if t_name == 'BT':
							G_val.socket_flag = 1
						elif t_name == 'TCP':
							G_val.socket_flag = 2
						T_count=0
						print t_name + " rec date :" + "\r"
						print T_buffer
						_Communication_Decode_(T_buffer)
						time.sleep(0.001)
				else:
					T_buffer.append(T_data)
					T_count+=1
		T_Client.close()
	go.stop()
	T_Server.close()
	
class XR_SOCKET:
	def __init__(self):
		pass
	def Sendbuf(self,buf):
		_Socket_sendbuf_(buf)
	def BT_Socket(self):
		_T_SOCKET_(BT_Server,BT_buffer,'BT')
	def TCP_Socket(self):
		_T_SOCKET_(TCP_Server,TCP_buffer,'TCP')


def Cruising_Mod():
    #����������ģʽ
    XRFUN.Follow()
    #�������Ѳ��ģʽ
    XRFUN.TrackLine()
    #����������ģʽ
    XRFUN.Avoiding()
    #���볬��������ģʽ##
    XRFUN.AvoidByRadar()
    #���볬�������ģʽ
    XRFUN.Send_Distance()
    #��������ͷѭ������
    PDec.Path_Dect()
    if(G_val.Cruising_Flag == 0):
        G_val.RevStatus=0
    else:
        time.sleep(0.01)
    time.sleep(0.01)
os.system("sudo hciconfig hci0 name XiaoRGEEK")
time.sleep(0.1)
os.system("sudo hciconfig hci0 reset")
time.sleep(0.3)
os.system("sudo hciconfig hci0 piscan")
time.sleep(0.2)
print 'NOW BT discoverable'

XRLED.FLOW_LED()
time.sleep(0.2)
threads = []
t1 = threading.Thread(target=PDec.Path_Dect_img_processing,args=())
threads.append(t1)
t2=threading.Thread(target=soc.BT_Socket,args=())
threads.append(t2)
t3=threading.Thread(target=soc.TCP_Socket,args=())
threads.append(t3)

path_sh = 'sh '+ os.path.split(os.path.abspath(__file__))[0] + '/start_mjpg_streamer.sh &'
call("%s"%path_sh,shell=True)
time.sleep(1)
for t in threads:
        t.setDaemon(True)
        t.start()
        time.sleep(0.05)
        print 'theads start...'
print 'all theads start...'

while True:
    try:
        Cruising_Mod()
    except:
        print 'Cruising_Mod error...'

