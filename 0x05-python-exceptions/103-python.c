#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: A PyObject list object.
 */
void print_python_list(PyObject *p)
{
    int list_size, list_alloc, i;
    const char *type;
    PyListObject *list = (PyListObject *)p;
    PyVarObject *var = (PyVarObject *)p;

    list_size = var->ob_size;
    list_alloc = list->allocated;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %d\n", list_size);
    printf("[*] Allocated = %d\n", list_alloc);

    for (i = 0; i < list_size; i++)
    {
        type = ((PyObject *)(list->ob_item[i]))->ob_type->tp_name;
        printf("Element %d: %s\n", i, type);
    }
}

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @p: A PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
    unsigned char i, byte_size;
    PyBytesObject *bytes = (PyBytesObject *)p;

    printf("[.] bytes object info\n");
    if (strcmp(((PyObject *)bytes)->ob_type->tp_name, "bytes") != 0)
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    printf("  size: %ld\n", PyBytes_GET_SIZE(p));
    printf("  trying string: %s\n", PyBytes_AS_STRING(p));

    byte_size = (PyBytes_GET_SIZE(p) > 10) ? 10 : PyBytes_GET_SIZE(p);

    printf("  first %d bytes: ", byte_size);
    for (i = 0; i < byte_size; i++)
    {
        printf("%02hhx", PyBytes_AS_STRING(p)[i]);
        if (i == (byte_size - 1))
            printf("\n");
        else
            printf(" ");
    }
}

/**
 * print_python_float - Prints basic info about Python float objects.
 * @p: A PyObject float object.
 */
void print_python_float(PyObject *p)
{
    PyFloatObject *f = (PyFloatObject *)p;
    double value = f->ob_fval;

    if (strcmp(((PyObject *)f)->ob_type->tp_name, "float") != 0)
    {
        printf("[ERROR] Invalid Float Object\n");
        return;
    }

    printf("[.] float object info\n");
    printf("  value: %.*g\n", 16, value);
}
