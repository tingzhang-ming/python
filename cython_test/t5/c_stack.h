#include "/root/python3/include/python3.6m/Python.h"

extern "C"{
    class C_Stack {
        private:
        struct Node {
            PyObject* val;
            Node* prev;
        };
        Node* tail;

        public:
        C_Stack();

        ~C_Stack();

        PyObject* peek();

        void push(PyObject* val);

        PyObject* pop();
    };
}