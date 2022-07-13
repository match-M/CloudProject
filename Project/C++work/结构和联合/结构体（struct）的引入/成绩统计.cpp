#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
using namespace std;
/*定义struct的类型，类型名叫:tStudent*/
struct tStudent{
	string name;
	int cha, math;
	int total;
};
/*定义一个数组A，每个元素是tStudent型的*/
tStudent A[110];
int N;
int main(){
	/*输入数据*/
	cin>>N;
	for(int i = 0; i < N; i++){
		cin>>A[i].name;
		cin>>A[i].cha>>A[i].math;
		A[i].total = A[i].cha + A[i].math;
	}
	/*冒泡排序*/
	for(int last = N-1; last > 0; last--)
	for(int j = 0; j < last; j++){  /*一趟冒泡*/
		if(A[j].total < A[j+1].total) /*小的交换到后面*/
			swap(A[j],A[j+1]);
	}
	/*输出*/
	cout<<endl;
	for(int i = 0; i < N; i++){
		cout<<A[i].name<<" "<<A[i].cha<<" "<<A[i].math<<" "<<A[i].total<<endl;
	}

	return 0;
}