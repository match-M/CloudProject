#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;
/*定义struct的类型，类型名叫：tWindow*/
struct tWindow{
	int left,
		right,
		top,
		bottom;
};
/*定义2个tWindow类型的变量winA和winB表示2个窗口*/
tWindow winA, winB,
	tmp; /*临时变量*/

/*定义1个函数， 输入窗口变量*/
tWindow inData(){
	tWindow tmp;
	cin>>tmp.left>>tmp.right>>tmp.top>>tmp.bottom;
	return tmp;
}

int main(){
	/*输入数据*/
	winA = inData();
	winB = inData();
	/*判断计算, tmp是重叠窗口*/
	tmp.left = max(winA.left, winB.left);
	tmp.right = min(winA.right, winB.right);
	tmp.top = max(winA.top, winB.top);
	tmp.bottom = min(winA.bottom, winB.bottom);
	int s = (tmp.right - tmp.left)*(tmp.bottom-tmp.top);

	if((tmp.right <= tmp.left)||(tmp.bottom <= tmp.top)){
		s = 0;
	}
	/*输出*/
	cout<<s<<endl;

	return 0;
}