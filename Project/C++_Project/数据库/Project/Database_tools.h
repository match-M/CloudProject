#pragma once
#include <fstream>
#include <string.h>
#include <iostream>
using namespace std;

//定义主登入类
class mainLogin{
	//定义可访问的成员数据和成员函数
	public:
		//封装私有的成员函数，变为公开的
		void Login(string name, string password);
		void Read_data();
		bool Value();

	//定义不可访问的成员数据和成员函数
	private:
		//定义为静态成员变量
		static string user_name[55];
		static string user_password[55];
		static string name;
		static string password;
	
		void is_Login(string name, string password);
		void isOpenText_read(); //打开.txt文件读取
		bool isValue(); //判断用户名或密码是否正确

};

string mainLogin::user_name[55];
string mainLogin::user_password[55];
string mainLogin::name;
string mainLogin::password;


//构造mainLogin的成员函数is_Login
void mainLogin::is_Login(string name, string password){
	//把外部数据传给mainLogin的成员变量
	this->name = name;
	this->password = password;
}

//封装私有的成员函数is_Login
void mainLogin::Login(string name, string password){
	mainLogin mL;
	mL.is_Login(name, password);
}


//构造mainLogin的成员函数isOpenText_read
void mainLogin::isOpenText_read(){
	
	ifstream nameFile;
	ifstream passwordFile;

	
	nameFile.open("user_name.txt");
	passwordFile.open("user_password.txt");

	int n = 0;

	while((!nameFile.eof())&&(!passwordFile.eof())){
       	nameFile>>user_name[n];
	   	passwordFile>>user_password[n];
    	n++;
    } 
    nameFile.close();
    passwordFile.close();

}

//封装私有的成员函数isOpenText_read
void mainLogin::Read_data(){
	mainLogin mL;
	mL.isOpenText_read();
}


//构造mainLogin的成员函数isValue
bool mainLogin::isValue(){
	bool isError = true;

	for(int j = 0; j <= sizeof(user_name)/sizeof(user_name[0]); j++){
		if((this->name == user_name[j]) && (this->password == user_password[j])){
			isError = false;
			return isError;
		}else{
			isError = true;
		}
	}
	return isError;

}

//封装私有的成员函数isValue
bool mainLogin::Value(){
	mainLogin mL;
	bool isError = false;
	isError = mL.isValue();
	return isError;
}



//定义注册主类
class mainSign{
	//定义可访问的成员数据和成员函数
	public:
		//封装私有的成员函数，变为公开的
		void Sign(string name, string password, string confirm_password);
		bool Value();
		void sign();
		void Read_data();
		void Write_data();
		void read();
		void id();
		

	//定义不可访问的成员数据和成员函数
	private:
		//定义为静态成员变量
		static string isNew_user_name;
		static string isNew_user_password;
		static string read_user_name[55];
		static string read_user_password[55];
		static string write_new_userName[55];
		static string write_new_userPassword[55];
		static string isInputuser_name;
		static string isInputuser_password;
		static string isConfirm_password;
		static int n;

		void is_Sign(string name, string password, string confirm_password);
		bool isValue(); //判断是否有重复的用户名
		void is_sign();  
		void isOpenText_read(); //打开.txt文件读取
		void isOpendText_write(); //打开.txt文件写
		void is_read();
		int is_id();

};

string mainSign::isNew_user_name;
string mainSign::isNew_user_password;
string mainSign::read_user_name[55];
string mainSign::read_user_password[55];
string mainSign::write_new_userName[55];
string mainSign::write_new_userPassword[55];
string mainSign::isInputuser_name;
string mainSign::isInputuser_password;
string mainSign::isConfirm_password;
int mainSign::n = 0;

//构造mainSign的成员函数Sign
void mainSign::is_Sign(string name, string password, string confirm_password){
	
	this->isInputuser_name = name;
	this->isInputuser_password = password;
	this->isConfirm_password = confirm_password;
}

//封装私有的成员函数is_Sign
void mainSign::Sign(string name, string password, string Confirm_password){
	mainSign mS;
	mS.is_Sign(name,password,Confirm_password);
}


//构造mainSign的成员函数openText_read
void mainSign::isOpenText_read(){

	ifstream nameFile;
	ifstream passwordFile;

	nameFile.open("user_name.txt");
	passwordFile.open("user_password.txt");

	int i = 0;

	while((!nameFile.eof())&&(!passwordFile.eof())){
       nameFile>>read_user_name[i];
	   passwordFile>>read_user_password[i];
	   i++;
    } 
    nameFile.close();
    passwordFile.close();

}

//封装私有的成员函数isOpenText_read
void mainSign::Read_data(){
	mainSign mS;
	mS.isOpenText_read();
}


//构造mainSign的成员函数isValue
bool mainSign::isValue(){

	bool isError = false;
	int num = 0;
	num = is_id();
	if(read_user_name[num] == isInputuser_name){
		isError = true;
	}
	
	return isError;
}

//封装私有的成员函数isValue
bool mainSign::Value(){
	mainSign mS;
	bool isError = false;
	isError = mS.isValue();
	return isError;
}


//构造mainSign的成员函数sign
void mainSign::is_sign(){
	
	this->isNew_user_name = isInputuser_name;
	this->isNew_user_password = isConfirm_password;

	string ch ;
	int num = 0;

	num = is_id();

	write_new_userName[num] = isNew_user_name;
	write_new_userPassword[num] = isNew_user_password;

}

//封装私有的成员函数is_sign
void mainSign::sign(){
	mainSign mS;
	mS.is_sign();
}


//构造mainSign的成员函数openText_write
void mainSign::isOpendText_write(){

	ofstream nameFile;
	ofstream passwordFile;

	nameFile.open("user_name.txt",ios::app);
	passwordFile.open("user_password.txt",ios::app);

	for(int i = 0; i <= sizeof(write_new_userName)/sizeof(write_new_userName[0]); i++){
		nameFile<<'\n'<<write_new_userName[i];
		passwordFile<<'\n'<<write_new_userPassword[i];
	}

	nameFile.close();
	passwordFile.close();

}

//封装私有的成员函数isOpenText_werite
void mainSign::Write_data(){
	mainSign mS;
	mS.isOpendText_write();
}


//构造mainSign的成员函数is_id
int mainSign::is_id(){

	string str;

	char ch[13];
	int value;
	int ishashValue;
	int num = 0;

	for(int i = 0; i <= isInputuser_password.size(); i++){
		ch[i] = isInputuser_password[i];
	}

	for(int i = 0; i < isInputuser_password.size(); i++){
		if(((ch[i] >= 'a')&&(ch[i] <= 'z')) || ((ch[i] >= 'A')&&(ch[i] <= 'Z')) 
		&& ((ch[i + 1] >= 'a')&&(ch[i + 1] <= 'z')) || ((ch[i + 1] >= 'A')&&(ch[i + 1] <= 'Z'))
		||(ch[i] == '_') || (ch[i + 1] == '_')){
			//确定为字母或符号
			value = value + int(ch[i]) + int(ch[i+1]); // 获取ASCII值，并相加。
			continue;

		}else if(((ch[i] >= 'a')&&(ch[i] <= 'z')) || ((ch[i] >= 'A')&&(ch[i] <= 'Z'))
		 || (ch[i] == '_')
		&&((ch[i + 1] >= '0')&&(ch[i + 1]  <= '9'))){
			//第一个为字母或符号，第二个为数字
			value = value + int(ch[i]) + ch[i + 1];
			continue;

		}else if(((ch[i] >= '0')&&(ch[i]  <= '9')) 
		&& ((ch[i + 1] >= 'a')&&(ch[i + 1] <= 'z')) || ((ch[i + 1] >= 'A')&&(ch[i + 1] <= 'Z')) || (ch[i + 1] == '_')){
			//第一个为数字，第二个为字母或符号
			value = value + ch[i] + int(ch[i + 1]);
			continue;

		}else if(((ch[i] >= '0')&&(ch[i]  <= '9')) && ((ch[i + 1] >= '0')&&(ch[i + 1]  <= '9'))){
			//两个都是数字
			value = value + ch[i] + ch[i + 1];
			continue;

		}

		for(int i = 0; i <= isInputuser_name.size(); i++){
			ch[i] = isInputuser_name[i];
		}

		for(int i = 0; i <= isInputuser_name.size(); i++){
			if(((ch[i] >= 'a')&&(ch[i] <= 'z')) || ((ch[i] >= 'A')&&(ch[i] <= 'Z'))){
				value = value + int(ch[i]);
			}else if((ch[i] >= '0')&&(ch[i]  <= '9')) {
				value = value + ch[i];
			}
		}
	}

	ishashValue = value%55;

	return ishashValue;

	
}

