#include <iostream>
using namespace std;
int main(){
	int students[6];
	int num;

	for(int i = 0; i <= 4; i++){
		cin>>students[i];
	}

	for(int i = 0; i <= 4; i++){
		int m;
		//记录数组的数据
		num = students[i];		
		//判断能否被3整除
		if(num%3 != 0){
			m = num%3;
			num = num - m;
		}
		//处理头尾的数据
		if(i == 0){
			num = num/3;
			students[0] = num;
			students[1] = students[1] + num;
			students[4] = students[4] + num;
			continue;
		}
		if(i == 4){
			num = num/3;
			students[4] = num;
			students[3] = students[3] + num;
			students[0] = students[0] + num;
			break;
		}
		//正常数据处理
		num = num/3;
		students[i] = num;
		students[i+1] = students[i+1] + num;
		students[i-1] = students[i-1] + num;

	}

	//输出
	for(int i = 0; i <= 4; i++){
		cout<<students[i]<<" ";
	}

	return 0;

}