#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

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
        type = list->ob_item[i]->ob_type->tp_name;
        printf("Element %d: %s\n", i, type);
        if (strcmp(type, "bytes") == 0)
            print_python_bytes(list->ob_item[i]);
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
    if (strcmp(p->ob_type->tp_name, "bytes") != 0)
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
    printf("  trying string: %s\n", bytes->ob_sval);

    if (((PyVarObject *)p)->ob_size > 10)
        byte_size = 10;
    else
        byte_size = ((PyVarObject *)p)->ob_size + 1;

    printf("  first %d bytes: ", byte_size);
    for (i = 0; i < byte_size; i++)
    {
        printf("%02hhx", bytes->ob_sval[i]);
        if (i == (byte_size - 1))
            printf("\n");
        else
            printf(" ");
    }
}
