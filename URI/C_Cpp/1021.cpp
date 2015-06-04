#include <iostream>
#include <cmath>
using namespace std;

int main() {
	int a,b,c,d,e,f;
	float N;
	cin >> N;
	a = N/100;
	N = std::fmod(N,100.0);
	b = N/50;
	N = std::fmod(N,50.0);
	cout << N<<"\n";
	c = N/20;
	N = std::fmod(N,20.0);
	cout << N<<"\n";
	d = N/10;
	N = std::fmod(N,10.0);
	e = N/5;
	N = std::fmod(N,5.0);
	f = N/2;
	N = std::fmod(N,2.0);
	cout <<"NOTAS:\n"<<a<<" nota(s) de R$ 100.00\n"<<b<<" nota(s) de R$ 50.00\n"<<c<<
	" nota(s) de R$ 20.00\n"<<d<<" nota(s) de R$ 10.00\n"<<e<<" nota(s) de R$ 5.00\n"<<f<<" nota(s) de R$ 2.00\n";
	a = N/1;
	N = std::fmod(N,1);
	b = N/0.5;
	N = std::fmod(N,0.5);
	c = N/0.25;
	N = std::fmod(N,0.25);
	d = N/0.1;
	N = std::fmod(N,0.10);
	e = N/0.05;
	N = std::fmod(N,0.05);
	f = N/0.01;
	cout <<"MOEDAS:\n"<<a<<" moeda(s) de R$ 1.00\n"<<b<<" moeda(s) de R$ 0.50\n"<<c<<
	" moeda(s) de R$ 0.25\n"<<d<<" moeda(s) de R$ 0.10\n"<<e<<" moeda(s) de R$ 0.05\n"<<f<<" moeda(s) de R$ 0.01\n";

	return 0;
}