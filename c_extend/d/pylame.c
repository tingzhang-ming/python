#include <Python.h>
#include <lame.h>

int encode(char*, char*);

static PyObject * pylame_encode(PyObject* self, PyObject* args) {
  int status;
  char* inPath;
  char* outPath;
  if (!PyArg_ParseTuple(args, "ss", &inPath, &outPath)) {
    return NULL;
  }
  status = encode(inPath, outPath);
  return Py_BuildValue("i", status);
}

static PyMethodDef pylame_methods[] = {
  {"encode", pylame_encode, METH_VARARGS, NULL},
  {NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC initpylame() {
  Py_InitModule3("pylame", pylame_methods, "an simple lame module.");
}
