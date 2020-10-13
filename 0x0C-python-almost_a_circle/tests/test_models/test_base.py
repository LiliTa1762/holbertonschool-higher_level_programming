#!/usr/bin/python3
"""
Unittest for Base class
"""

import unittest
import inspect
import pep8
import json
from models import base 


Base = base.Base

class TestBaseDocs(unittest.TestCase):
    """Checking the docu and style of Base class"""
    @classmethod
    def setUpClass(cls):
        """Setting for doc tests"""
        cls.base_funcs = inspect.getmembers(Base, inspect.isfunction)

    def test_pep8_conformance_base(self):
        """pep8 tests for base"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_docstring(self):
        """Module docstring test"""
        self.assertTrue(len(base.__doc__) >= 1)

    def test_class_docstring(self):
        """Base class docstring test"""
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_functions_docstrings(self):
        """Presence of docstrings in all functions"""
        for function in self.base_funcs:
            self.assertTrue(len(function[1].__doc__) >= 1)

class TestBase(unittest.TestCase):
    """Checking functionality of Base class"""
    def test_a_id_value(self):
        obj = Base(5)
        self.assertEqual(obj.id, 5)
    
    def test_b_id_value(self):
        obj = Base()
        self.assertEqual(obj.id, 1)

    def test_c_too_many_args(self):
        """too many args to init"""
        with self.assertRaises(TypeError):
            b = Base(1, 1)

    def test_d_nb_private(self):
        """nb_objects as private instance att"""
        b = Base(3)
        with self.assertRaises(AttributeError):
            print(b.nb_objects)
        with self.assertRaises(AttributeError):
            print(b.__nb_objects)

    def test_e_to_json_string(self):
        """To json string"""
        Base._Base__nb_objects = 0
        d1 = {"id": 9, "width": 5, "height": 6, "x": 7, "y": 8}
        d2 = {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0}
        json_s = Base.to_json_string([d1, d2])
        self.assertTrue(type(json_s) is str)
        d = json.loads(json_s)
        self.assertEqual(d, [d1, d2])

    def test_f_empty_to_json_string(self):
        """Getting empty list/ None"""
        json_s = Base.to_json_string([])
        self.assertTrue(type(json_s) is str)
        self.assertEqual(json_s, "[]")

    def test_g_None_to_json_String(self):
        """None to json string"""
        json_s = Base.to_json_string(None)
        self.assertTrue(type(json_s) is str)
        self.assertEqual(json_s, "[]")

    def test_h_from_json_string(self):
        """from_json_string"""
        json_str = '[{"id": 9, "width": 5, "height": 6, "x": 7, "y": 8}, \
{"id": 2, "width": 2, "height": 3, "x": 4, "y": 0}]'
        json_l = Base.from_json_string(json_str)
        self.assertTrue(type(json_l) is list)
        self.assertEqual(len(json_l), 2)
        self.assertTrue(type(json_l[0]) is dict)
        self.assertTrue(type(json_l[1]) is dict)
        self.assertEqual(json_l[0],
                         {"id": 9, "width": 5, "height": 6, "x": 7, "y": 8})
        self.assertEqual(json_l[1],
                         {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0})

    def test_j_from_json_None(self):
        """With a None string"""
        self.assertEqual([], Base.from_json_string(None))

if __name__ == '__main__':
    unittest.main()
