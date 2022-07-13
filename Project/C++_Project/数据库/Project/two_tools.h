#pragma once
#include <fstream>
#include <string.h>
#include <iostream>
using namespace std;

class Login{

	public:
		void contrast(string name, string password);

	private:

		static string user_name[55];
		static string user_password[55];
		static string name;
		static string password;

		int id();
		void read();

	void contrast(string name, string password){
		this->name = name;
		this->password = password;
	}

	int id(){
		int value = 0;
		int len = 0;
		len = this->password.size();

		value = len%55;
	}

	void read(){
		
	}
};