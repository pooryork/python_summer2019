#include <iostream> 
#include <vector> 
#include <algorithm> 
 
using namespace std; 
int main() 
{ 
	setlocale (0,"") ;
    vector <int> v;
    int k, n, x;
	cout << "�������: �������� ��� ������� �������� ����� k-��" << endl ;
	cout << "������� ���-�� ���������: " ;
    cin >> n ;
	cout << "������� k-�� �������: " ;
	cin >> k ;
	cout << "������� �������� (����� ������): " ;
    for (int i = 0; i < n; i++)
    {    
        cin >> x;
        v.push_back(x);
    }
	cout << "�����: " ;
    v.insert(v.begin() + k, 2, 0);
    for (int i = 0; i < v.size(); i++)
        cout << v[i] << " ";
    cout << endl;
    system("pause"); 
    return 0; 
}