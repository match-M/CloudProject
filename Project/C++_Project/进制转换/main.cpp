#include <iostream>
using namespace std;
int main(){
	long long in_decimalSystem = 0;
	long long out_binaryValue = 0;
	long long in_binaryValue = 0;
	long long out_decimalSystem = 0;
	int n = 0;
	char ch;

	cout<<"1.十进制转二进制\n";
	cout<<"2.二进制转十进制\n";
	cout<<"->";
	cin>>n;

	switch (n){
		case 1:
			cout<<"please input numbers:";
			cin>>in_decimalSystem;
			break;
	
		default:
			break;
	}
}