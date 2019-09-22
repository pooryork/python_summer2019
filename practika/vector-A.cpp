#include <iostream> 
#include <vector> 
#include <algorithm> 
 
using namespace std; 
int main() 
{ 
	setlocale (0,"") ;
    vector <int> v;
    int k, n, x;
	cout << "Задание: вставить два нулевых элемента после k-го" << endl ;
	cout << "Введите кол-во элементов: " ;
    cin >> n ;
	cout << "Введите k-ый элемент: " ;
	cin >> k ;
	cout << "Введите элементы (через пробел): " ;
    for (int i = 0; i < n; i++)
    {    
        cin >> x;
        v.push_back(x);
    }
	cout << "Ответ: " ;
    v.insert(v.begin() + k, 2, 0);
    for (int i = 0; i < v.size(); i++)
        cout << v[i] << " ";
    cout << endl;
    system("pause"); 
    return 0; 
}