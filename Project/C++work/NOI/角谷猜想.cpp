#include <iostream>
using namespace std;
int main(){
	int num;
	cin>>num;
	while(num != 1){
		if(num%2!=0){
			cout<<num<<"*3+1=";
			num = num*3+1;
			cout<<num<<endl;
			continue;
		}else{
			cout<<num<<"/2=";
			num = num/2;
			cout<<num<<endl;
			continue;
		}
	}
	cout<<"End"<<endl;

	return 0;
}