#include <Python.h>
#include <stdio.h>

static PyObject* foo_bar(PyObject* self, PyObject* args) {
    Py_RETURN_NONE;
}

static PyObject* foo_bar2(PyObject* self, PyObject* args) {
    int iNum;
    double fNum;
    char* str;
    if (!PyArg_ParseTuple(args, "ids", &iNum, &fNum, &str)) {
        return NULL;
    }
    printf("iNum: %d, fNum: %f, str: %s\n", iNum, fNum, str);
    Py_RETURN_NONE;
}

static PyObject* foo_bar3(PyObject* self, PyObject* args) {
    int iNum;
    double fNum;
    char* str;
    int iNum2 = 4;
    double fNum2 = 5.0;
    char *str2 = "hello";
    if (!PyArg_ParseTuple(args, "ids|ids", &iNum, &fNum, &str,&iNum2, &fNum2, &str2)) {
        return NULL;
    }
    printf("iNum: %d, fNum: %f, str: %s, iNum2: %d, fNum2: %f, str2: %s, \n", iNum, fNum, str, iNum2, fNum2, str2);
    Py_RETURN_NONE;
}

static PyObject* foo_bar4(PyObject* self, PyObject* args, PyObject* kw) {
    static char* kwlist[] = {"i", "d", "s",NULL};
    int iNum = 0;
    double fNum = 2.0f;
    char* str = "thing";
    if (!PyArg_ParseTupleAndKeywords(args,kw,"i|ds",kwlist,&iNum,&fNum,&str)) {
        printf("ERROR");
        return NULL;
    }
    printf("num is: %d,%f,%s\n",iNum,fNum,str);
    Py_RETURN_NONE;
}

static PyObject* foo_add_sub(PyObject* self, PyObject* args) {
    int num1,num2;
    if (!PyArg_ParseTuple(args, "ii", &num1, &num2)) {
        return NULL;
    }
    return Py_BuildValue("ii", num1 + num2, num1 - num2);
}

static PyMethodDef foo_methods[] = {
    {"bar",(PyCFunction)foo_bar,METH_NOARGS,NULL},
    {"bar2",(PyCFunction)foo_bar2,METH_VARARGS,NULL},
    {"bar3",(PyCFunction)foo_bar3,METH_VARARGS,NULL},
    {"bar4",(PyCFunction)foo_bar4,METH_VARARGS|METH_KEYWORDS,NULL},
    {"add_sub",(PyCFunction)foo_add_sub,METH_VARARGS,NULL},
    {NULL,NULL,0,NULL}
};

PyMODINIT_FUNC initfoo() {
    Py_InitModule3("foo", foo_methods, "My first extension module.");
}

