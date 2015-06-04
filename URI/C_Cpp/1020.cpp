#include <iostream>
using namespace std;

int main() {
	int N,a,m,d;
	cin >> N;
	a = N/365;
	m = (N-(365*a))/30;
	d = N-(365*a)-(30*m);
	cout <<a<<" ano(s)\n"<<m<<" mes(es)\n"<<d<<" dia(s)\n";
	return 0;
}