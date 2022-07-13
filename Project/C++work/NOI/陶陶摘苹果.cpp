#include <iostream>
using namespace std;
int main(){
	int apple_distance[15];
	int hand_length;
	int num = 0;

	for(int i = 0; i < 10; i++){
		cin>>apple_distance[i];
	}
	cin>>hand_length;
	hand_length = hand_length + 30;

	for(int i = 0; i < 10; i++){
		if(apple_distance[i] <= hand_length){
			num++;
		}
	}

	cout<<num<<endl;

	return 0;
}