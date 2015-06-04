#include <iostream>
using namespace std;

int main() {
	int N,h,m,s;
	cin >> N;
	h = N/3600;
	m = (N-(3600*h))/60;
	s = N-(3600*h)-(60*m);
	cout <<h<<":"<<m<<":"<<s<<"\n";
	return 0;
}