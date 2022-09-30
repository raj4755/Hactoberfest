// Home Work 3

#include<iostream>
using namespace std;

int main(){
    char a;
    cout << "Enter a Character : "<< endl;
    cin >> a;

    if (a >= 97 && a <= 122){
        cout << "This is Lower Case" <<endl;
    }

    else if (a >= 65 && a <= 90){
        cout << "This is Upper Case" << endl;
    }

    else if (a >= 48 && a <= 57){
        cout << "This is Numeric"<<endl;    
    }
}


// Homework 4 -- sum of all even number n

#include<iostream>
using namespace std;

int main(){
    int n;
    cout << "Enter value of n : "<<endl;
    cin>>n;

    int sum = 0;
    int i = 2;
    while (i <= n){
        sum = sum + i;
        i = i + 2;
    }

    cout << "Sum is : "<< sum << endl;
}


// Celcius to fahrenheit

#include<iostream>
using namespace std;

int main(){
    int cel;
    cout << "Enter Celcius Value : " << endl;
    cin >> cel;

    float fah = (cel * 9.0 / 5) + 32;

    cout << "Value in Fahrenheit is "<< fah << endl;
}