#include <iostream>
using namespace std;
int main(){
	double a,b;
	cin>>a>>b;
	if(a < 60.00 || b < 60.00){
		cout<<"1"<<endl;
	}else{
		if(a >=60.00 && b >= 60.00){
			cout<<"0"<<endl;
		}
		
	}
	
	return 0;
}