#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;
/*定义struct的类型，类型名叫：tNode*/
struct tNode{
	int data,  /*数值*/
		rank,  /*排名*/
		index; /*下标*/
};

int N;
tNode a[10001];	/*数组*/

bool cmpData(tNode x, tNode y){
	return x.data < y.data;
}
bool cmpIndex(tNode x, tNode y){
	return x.index < y.index;
}

int main(){
	/*输入数据*/
	cin>>N;
	for(int i = 0; i < N; i++){
		cin>>a[i].data;
		a[i].index = i;
	}
	/*根据值排序，求rank*/
	sort(a ,a+N, cmpData);
	for(int i = 0; i < N; i++){
		a[i].rank = i + 1;
	}
	/*根据下标排序*/
	sort(a ,a+N, cmpIndex);
	/*输出*/
	for(int i = 0; i < N; i++){
		cout<<a[i].rank<<" ";
	}
	cout<<endl;
	return 0;

}