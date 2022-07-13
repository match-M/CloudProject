#include "two_tools.h"
#include <bits/stdc++.h>
#include <ctype.h>
#include <string>
using namespace std;
int main(){
	//类对象
	mainLogin mL;
	mainSign mS;

	int n;

	//Login变量
	string name;
	string password;

	bool isError_Login = true;

	//Sign变量
	char ch[18];

	string new_name;
	string new_password;
	string confirm_password;

	bool isError_Sign = true;
	bool isError_Sign_name = true;
	bool isError_Sign_password = true;
	bool Password_error = true;

	cout<<"\t\t登录选项\n";
	cout<<"\t\t1.登录\n";
	cout<<"\t\t2.注册\n";
	cout<<"\t\t->";
	cin>>n;

	if(n == 1){
		cout<<"用户名：";
		cin>>name;
		cout<<"  密码：";
		cin>>password;

		mL.Login(name, password);
		mL.Read_data();
		isError_Login = mL.Value();

		if(isError_Login){
			cout<<"用户名或密码有误！"<<endl;
		}else{
			cout<<name<<",欢迎你！"<<endl;
		}

	}else if(n == 2){

		cout<<"用户名：";
		cin>>new_name;
		cout<<"  密码：";
		cin>>new_password;
		cout<<"确认密码：";
		cin>>confirm_password;

		mS.Sign(new_name, new_password, confirm_password);
		mS.Read_data();

		if(new_password == confirm_password){
			for(int i = 0; i <= new_password.size(); i++){
				ch[i] = new_password[i];
				if(((ch[i] >= 'a')&&(ch[i] <= 'z')) || ((ch[i] >= 'A')&&(ch[i] <= 'Z'))
		 			|| (ch[i] == '_')
					|| ((ch[i] >= '0')&&(ch[i]  <= '9'))){  //防止中文密码
						Password_error = false;
						continue;
					}else{
						
						//废话
						if(Password_error){
							Password_error = true;
						}
					}
			}

			if(!Password_error){
				isError_Sign = mS.Value();
				
				if(!isError_Sign){
					if((new_name.size() <= 12) && (new_name != " ")){
						if((confirm_password.size() >= 6) && (confirm_password.size() <= 18)){
							mS.sign();
							mS.Write_data();
							cout<<"注册成功！"<<new_name<<" ,欢迎你！\n";
						}else{
							cout<<"密码过长或过短!"<<endl;
						}
								
					}else{
						cout<<"名字过长或为空！"<<endl;
					}
				}else{
					cout<<"用户名以存在！"<<endl;
				}

			}else{
				cout<<"密码带有非法字符!"<<endl;
			}

		}else{
			if(new_password != confirm_password){
				cout<<"两次密码不一致！"<<endl;
			}
		}
		
	}
	return 0; 
}
