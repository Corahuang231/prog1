#include <cstdlib>
// Integer class 

class Integer {
public:
	Integer(int);
	int get();
	int fib();
	void set(int);
private:
	int val;
	int fib_pri(int);
};

Integer::Integer(int n) {
	val = n;
}

int Integer::get() {
	return val;
}
int Integer::fib() {
	return fib_pri(val);
}

int Integer::fib_pri(int n) {
	if (n == 0)
		return 0;
	if (n == 1 || n == 2)
		return 1;
	if (n >= 2)
		return fib_pri(n - 1) + fib_pri(n - 2);
}

void Integer::set(int n) {
	val = n;
}


extern "C" {
	Integer* Integer_new(int n) { return new Integer(n); }
	int Integer_get(Integer* integer) { return integer->get(); }
	int Integer_fib(Integer* integer) { return integer->fib(); }
	void Integer_set(Integer* integer, int n) { integer->set(n); }
	void Integer_delete(Integer* integer) {
		if (integer) {
			delete integer;
			integer = nullptr;
		}
	}
}
