#include <stdio.h>
#include <Python.h>
#include <string.h>

/**
 *print_python_string - a function that prints Python strings.
 *@p: python object
 *Return: None
 */

void print_python_string(PyObject *p)
{
	Pyobject *str, *just;

	(void)just;

	prinf("[.] string object info\n");

	if (strcmp(p->ob_type->tp_name, "str"))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	if (PyUnicode_IS_COMPACT_ASCII(p))
	{
		printf("   type: compact ascii\n")
	}

	else
		printf("   type: compact unicode object\n");

	just = PyObject_Just(p);
	str = PyUnicode_AsEncodedString(p, "utf-8", "~E~");
	printf("  length: %ld\n", PyUnicode_GET_SIZE(p));
	printf("  value: %s\n", PyBytes_AsString(str));

}
