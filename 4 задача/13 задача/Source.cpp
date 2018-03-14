#include <iostream>
#include <fstream>
#include <stack>
#include <string>
#include <algorithm>
#include <ctype.h>
using namespace std;

class errore
{
public:
	virtual void void_errore(ostream &output) = 0;
};

class expression_is_incorrect :public errore
{
public:
	void void_errore(ostream &output)
	{
		output<< "выражение не корректно" << endl;
	}
};

class division_by_zero :public errore
{
public:
	void void_errore(ostream &output)
	{
		output << "деление на ноль" << endl;
	}
};

class the_erection_of_a_negative_power :public errore
{
public:
	void void_errore(ostream &output)
	{
		output << "возведение в отрицательную степень" << endl;
	}
};

int prior(char a)
{
	switch (a)
	{
	case '^':
		return 4;
	case '*':
	case '/':
	case '%':
		return 3;
	case '+':
	case '-':
		return 2;
	case '(':
		return 1;
	default:
		break;
	}
}

string RPN(string s)
{
	string k="";
	stack<char> q;
	char x, a;
	bool f = false;
	for (int i = 0; i < s.length(); i++)
	{
		a=s[i];
		if (isdigit(a))
		{
			k += a;
			if (f)
			{
				k += '.';
				f = false;
			}
		}
		else
			if (a == '+' || a == '-' || a == '*' || a == '/' || a == '%' || a == '^' || a == '(' || a == ')')
			{
				if (a == ')')
				{
					if (!q.empty())
						x = q.top();
					else
						throw new expression_is_incorrect();
					if (x=='(')
						throw new expression_is_incorrect();
					while (x != '(')
					{
						k += x;
						q.pop();
						if (!q.empty())
							x = q.top();
						else
							throw new expression_is_incorrect();
					}
					q.pop();
				}

				if (a == '(')
					q.push(a);

				if (a == '-')
					if (i == 0)
						f = true;
					else
						if (s[i - 1] == '(')
							f = true;

				if (a == '+' || a == '-' || a == '*' || a == '/' || a == '%' || a == '^')
				{
					if (!f)
						if (q.empty())
							q.push(a);
						else
							if (prior(a) >= prior(q.top()))// || q.top()=='(')
								q.push(a);
							else
							{
								x = q.top();
								while ((!q.empty()) && (prior(x) >= prior(a)))
								{
									k += x;
									q.pop();
									if (!q.empty())
										x = q.top();
								}
								q.push(a);
							}
				}
			}
			else
				throw new expression_is_incorrect();
	}
	while (!q.empty())
	{
		x = q.top();
		k += x;
		q.pop();
	}
	return k;
}

int result(string s)
{
	int a1, a2;
	stack<int> q;
	for (int i = 0; i < s.length(); i++)
	{
		if (isdigit(s[i]))
			q.push(s[i] - 48);
		else
		{
			a1 = q.top();
			q.pop();
			if (s[i] == '.')
				q.push(-a1);
			else
			{
				if (q.empty())
					throw new expression_is_incorrect();
				a2 = q.top();
				q.pop();
				switch (s[i])
				{
				case '/':
				{
					if(a1==0)
						throw new division_by_zero();
					a2 = a2 / a1; 
					break; 
				}
				case '*':a2 = a2*a1; break;
				case '-':a2 = a2 - a1; break;
				case '+':a2 = a2 + a1; break;
				case '%':a2 = a2%a1; break;
				case '^': 
				{
					if (a1<0)
						throw new the_erection_of_a_negative_power();
					a2 = pow(a2, a1); 
					break; 
				}
				default:
					break;
				}
				q.push(a2);
			}
		}
	}
	a1 = q.top();
	q.pop();
	if (!q.empty())
		throw new expression_is_incorrect();
	return a1;
}

int main()
{
	setlocale(LC_ALL, "Russian");
	ifstream f("input.txt");
	ofstream fo("result.txt");
	string s;
	int h;
	getline(f, s);
	fo << endl;
	while (!f.eof())
	{
		getline(f, s);//считали строку
		try
		{
			fo << RPN(s) << endl;
			//fo << result(RPN(s)) << endl;
		}
		catch (errore *a)
		{
			a->void_errore(fo);
		}
	}
	f.close();
	fo.close();
	//system("pause");
	return 0;
}