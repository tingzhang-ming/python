#include <Python.h>
#include <lame.h>

typedef struct {
    PyObject_HEAD
    FILE* outfp;
    lame_global_flags* gfp;
}clame_EncoderObject;

static PyObject* Encoder_new(PyTypeObject* type, PyObject* args, PyObject* kw) {
    clame_EncoderObject* self = (clame_EncoderObject* )type->tp_alloc(type, 0);
    self->outfp = NULL;
    self->gfp = NULL;
    return (PyObject*)self;
}

static void Encoder_dealloc(clame_EncoderObject* self) {
    if (self->gfp) {
        lame_close(self->gfp);
    }
    if (self->outfp) {
        fclose(self->outfp);
    }
    self->ob_type->tp_free(self);
}

static int Encoder_init(clame_EncoderObject* self, PyObject* args, PyObject* kw) {
    char* outPath;
    if (!PyArg_ParseTuple(args, "s", &outPath)) {
        return -1;
    }
    if (self->outfp || self->gfp) {    
        PyErr_SetString(PyExc_Exception, "__init__ already called");
        return -1;
    }
    self->outfp = fopen(outPath, "wb");
    self->gfp = lame_init();
    lame_init_params(self->gfp);
    return 0;
}

static PyObject* Encoder_encode(clame_EncoderObject* self, PyObject* args) {
    char* in_buffer;
    int in_length;
    int mp3_length;
    char* mp3_buffer;
    int mp3_bytes;
    if (!(self->outfp || self->gfp)) {
        PyErr_SetString(PyExc_Exception, "encoder not open");
        return NULL;
    }
    if (!PyArg_ParseTuple(args, "s#", &in_buffer, &in_length)) {
        return NULL;
    }
    in_length /= 2;
    mp3_length = (int)(1.25 * in_length) + 7200;
    mp3_buffer = (char*)malloc(mp3_length);
    if (in_length > 0) {
        mp3_bytes = lame_encode_buffer_interleaved(self->gfp, (short*)in_buffer, in_length/2, mp3_buffer, mp3_length);
        if (mp3_bytes > 0) {
            fwrite(mp3_buffer, 1, mp3_bytes, self->outfp);
        }
    }
    free(mp3_buffer);
    Py_RETURN_NONE;
}

static PyObject* Encoder_close(clame_EncoderObject* self) {
    int mp3_length;
    char* mp3_buffer;
    int mp3_bytes;
    if (!(self->outfp && self->gfp)) {
        PyErr_SetString(PyExc_Exception, "encoder not open");
        return NULL;
    }
    mp3_length = 7200;
    mp3_buffer = (char*)malloc(mp3_length);
    mp3_bytes = lame_encode_flush(self->gfp, mp3_buffer, sizeof(mp3_buffer));
    if (mp3_bytes > 0) {
        fwrite(mp3_buffer, 1, mp3_bytes, self->outfp);        
    }
    free(mp3_buffer);
    lame_close(self->gfp);
    self->gfp = NULL;
    fclose(self->outfp);
    self->outfp = NULL;
    Py_RETURN_NONE;
}

static PyMethodDef Encoder_methods[] = {
    {"encode", (PyCFunction)Encoder_encode, METH_VARARGS, "encodes and writes data to the output file."},
    {"close", (PyCFunction)Encoder_close, METH_NOARGS, "close the output file."},
    {NULL, NULL, 0, NULL}
};

static PyTypeObject clame_EncoderType = {
    PyObject_HEAD_INIT(NULL)
    0,                                    // ob_size
    "clame.Encoder",                    // tp_name
    sizeof(clame_EncoderObject),        // tp_basicsize
    0,                                    // tp_itemsize
    (destructor)Encoder_dealloc,        // tp_dealloc
    0,                                    // tp_print
    0,                                    // tp_getattr
    0,                                    // tp_setattr
    0,                                    // tp_compare
    0,                                    // tp_repr
    0,                                    // tp_as_number
    0,                                    // tp_as_sequence
    0,                                    // tp_as_mapping
    0,                                    // tp_hash
    0,                                     // tp_call
    0,                                    // tp_str
    0,                                    // tp_getattro
    0,                                    // tp_setattro
    0,                                    // tp_as_buffer
    Py_TPFLAGS_DEFAULT,                    // tp_flags
    "My first encoder object.",            // tp_doc
    0,                                    // tp_traverse
    0,                                    // tp_clear
    0,                                    // tp_richcompare
    0,                                    // tp_weaklistoffset
    0,                                    // tp_iter
    0,                                    // tp_iternext
    Encoder_methods,                    // tp_methods
    0,                                    // tp_members
    0,                                    // tp_getset
    0,                                    // tp_base
    0,                                    // tp_dict
    0,                                    // tp_descr_get
    0,                                    // tp_descr_set
    0,                                    // tp_dictoffset
    (initproc)Encoder_init,                // tp_init
    0,                                    // tp_alloc
    Encoder_new,                        // tp_new
    0,                                    // tp_free
};

static PyMethodDef clame_methods[] = {    
    {NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC initclame() {
    PyObject* m;
    if (PyType_Ready(&clame_EncoderType) < 0)
        return;
    m = Py_InitModule3("clame", clame_methods, "My second lame module.");
    Py_INCREF(&clame_EncoderType);
    PyModule_AddObject(m, "Encoder", (PyObject*) &clame_EncoderType);
}