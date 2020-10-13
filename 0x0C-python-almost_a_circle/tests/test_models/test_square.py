#!/usr/bin/python3
"""
Unittest for Base class
"""

import unittest
import inspect
import io
import os
import pep8
import json
from models import square 
from models.base import Base
from contextlib import redirect_stdout

Square = square.Square


class TestSquareDocs(unittest.TestCase):
    """Checking the docu and style of Square class"""
    @classmethod
    def setUpClass(cls):
        """Setting for doc tests"""
        cls.sq_funcs = inspect.getmembers(Square, inspect.isfunction)

    def test_pep8_conformance_square(self):
        """pep8 tests for square"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0,
                        "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """Presence of a module docstring"""
        self.assertTrue(len(square.__doc__) >= 1)

    def test_class_docstring(self):
        """Presence of a class docstring"""
        self.assertTrue(len(Square.__doc__) >= 1)

    def test_func_docstrings(self):
        """Presence of docstrings in all functions"""
        for func in self.sq_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestSquare(unittest.TestCase):
    """Checking functionality of the Square class"""
    @classmethod
    def setUpClass(cls):
        """Setting up classmethod"""
        Base._Base__nb_objects = 0
        cls.s1 = Square(1)
        cls.s2 = Square(2, 3)
        cls.s3 = Square(4, 5, 6)
        cls.s4 = Square(7, 8, 9, 10)

    def test_a_id(self):
        """Checking id functionality"""
        self.assertEqual(self.s1.id, 1)
        self.assertEqual(self.s2.id, 2)
        self.assertEqual(self.s3.id, 3)
        self.assertEqual(self.s4.id, 10)

    def test_b_size(self):
        """Checking size functionality"""
        self.assertEqual(self.s1.size, 1)
        self.assertEqual(self.s2.size, 2)
        self.assertEqual(self.s3.size, 4)
        self.assertEqual(self.s4.size, 7)

    def test_c_width(self):
        """Checking width functionality"""
        self.assertEqual(self.s1.width, 1)
        self.assertEqual(self.s2.width, 2)
        self.assertEqual(self.s3.width, 4)
        self.assertEqual(self.s4.width, 7)

    def test_d_height(self):
        """Checking height functionality"""
        self.assertEqual(self.s1.height, 1)
        self.assertEqual(self.s2.height, 2)
        self.assertEqual(self.s3.height, 4)
        self.assertEqual(self.s4.height, 7)

    def test_e_x(self):
        """Checking x functionality"""
        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s2.x, 3)
        self.assertEqual(self.s3.x, 5)
        self.assertEqual(self.s4.x, 8)

    def test_f_y(self):
        """Checking y functionality"""
        self.assertEqual(self.s1.y, 0)
        self.assertEqual(self.s2.y, 0)
        self.assertEqual(self.s3.y, 6)
        self.assertEqual(self.s4.y, 9)

    def test_h_mandatory_size(self):
        """Size must exist"""
        with self.assertRaises(TypeError):
            s = Square()

    def test_i_typeerror_size(self):
        """Size other type"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square("hello")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square(True)

    def test_j_typeerror_x(self):
        """x other type"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(1, "hello")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(1, True)

    def test_k_typeerror_y(self):
        """Test non-ints for y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(1, 1, "hello")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(1, 1, True)

    def test_l_valueerror_size(self):
        """Test ints <= 0 for size"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s = Square(-1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s = Square(0)

    def test_m_valueerror_x(self):
        """Test ints < 0 for x"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s = Square(1, -1)

    def test_n_valueerror_y(self):
        """Test ints <= 0 for y"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s = Square(1, 1, -1)

    def test_o_area(self):
        """Checking area method"""
        self.assertEqual(self.s1.area(), 1)
        self.assertEqual(self.s2.area(), 4)
        self.assertEqual(self.s3.area(), 16)
        self.assertEqual(self.s4.area(), 49)

    def test_p_area_args(self):
        """Too many args for area()"""
        with self.assertRaises(TypeError):
            a = self.s1.area(1)

    def test_q_basic_display(self):
        """Basic display"""
        s = Square(3, 0, 0, 1)
        with io.StringIO() as buf, redirect_stdout(buf):
            self.s1.display()
            output = buf.getvalue()
            self.assertEqual(output, "#\n")
        with io.StringIO() as buf, redirect_stdout(buf):
            s.display()
            output = buf.getvalue()
            self.assertEqual(output, ("#" * 3 + "\n") * 3)

    def test_r_display_too_many_args(self):
        """Test display with too many args"""
        with self.assertRaises(TypeError):
            self.s1.display(1)

    def test_s_str_method(self):
        """Checking __str__ method"""
        self.assertEqual(str(self.s1), "[Square] (1) 0/0 - 1")
        self.assertEqual(str(self.s2), "[Square] (2) 3/0 - 2")
        self.assertEqual(str(self.s3), "[Square] (3) 5/6 - 4")
        self.assertEqual(str(self.s4), "[Square] (10) 8/9 - 7")

    def test_t_display_xy(self):
        """Testing the display method with x and y"""
        with io.StringIO() as buf, redirect_stdout(buf):
            self.s2.display()
            output = buf.getvalue()
            self.assertEqual(output, (" " * 3 + "#" * 2 + "\n") * 2)

        with io.StringIO() as buf, redirect_stdout(buf):
            self.s3.display()
            output = buf.getvalue()
            self.assertEqual(output, "\n" * 6 +
                            (" " * 5 + "#" * 4 + "\n") * 4)

        with io.StringIO() as buf, redirect_stdout(buf):
            self.s4.display()
            output = buf.getvalue()
            self.assertEqual(output, "\n" * 9 +
                            (" " * 8 + "#" * 7 + "\n") * 7)

    def test_u_update_args(self):
        """Testing the udpate method with *args"""
        s = Square(1, 0, 0, 1)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 1")
        s.update(89)
        self.assertEqual(str(s), "[Square] (89) 0/0 - 1")
        s.update(89, 2)
        self.assertEqual(str(s), "[Square] (89) 0/0 - 2")
        s.update(89, 2, 3)
        self.assertEqual(str(s), "[Square] (89) 3/0 - 2")
        s.update(89, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (89) 3/4 - 2")

    def test_w_update_args_setter(self):
        """Update method uses setter with *args"""
        s = Square(1, 0, 0, 1)
        with self.assertRaises(TypeError):
            s.update(1, "hello")
        with self.assertRaises(TypeError):
            s.update(1, 1, "hello")
        with self.assertRaises(TypeError):
            s.update(1, 1, 1, "hello")
        with self.assertRaises(ValueError):
            s.update(1, 0)
        with self.assertRaises(ValueError):
            s.update(1, -1)
        with self.assertRaises(ValueError):
            s.update(1, 1, -1)
        with self.assertRaises(ValueError):
            s.update(1, 1, 1, -1)

    def test_wa_update_too_many_args(self):
        """Too many args for update"""
        s = Square(1, 0, 0, 1)
        s.update(1, 1, 1, 1, 2)
        self.assertEqual(str(s), "[Square] (1) 1/1 - 1")

    def test_wb_update_no_args(self):
        """No args for update"""
        s = Square(1, 0, 0, 1)
        s.update()
        self.assertEqual(str(s), "[Square] (1) 0/0 - 1")

    def test_wc_update_kwargs(self):
        """Update method with **kwargs"""
        s = Square(1, 0, 0, 1)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 1")
        s.update(size=10)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 10")
        s.update(size=11, x=2)
        self.assertEqual(str(s), "[Square] (1) 2/0 - 11")
        s.update(y=3, size=4, x=5, id=89)
        self.assertEqual(str(s), "[Square] (89) 5/3 - 4")

    def test_wd_update_kwargs_setter(self):
        """Update method uses setter with **kwargs"""
        s = Square(1, 1, 1, 1)
        with self.assertRaises(TypeError):
            s.update(size="hello")
        with self.assertRaises(TypeError):
            s.update(x="hello")
        with self.assertRaises(TypeError):
            s.update(y="hello")
        with self.assertRaises(ValueError):
            s.update(size=-1)
        with self.assertRaises(ValueError):
            s.update(size=0)
        with self.assertRaises(ValueError):
            s.update(x=-1)
        with self.assertRaises(ValueError):
            s.update(y=-1)

    def test_we_mix_args_kwargs(self):
        """Output for mixed args and kwargs"""
        s = Square(1, 0, 0, 1)
        s.update(2, 2, 2, 2, size=3, x=3, y=3, id=3)
        self.assertEqual(str(s), "[Square] (2) 2/2 - 2")

    def test_wf_extra_kwargs(self):
        """Random kwargs"""
        s = Square(1, 0, 0, 1)
        s.update(hello=2)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 1")

    def test_wg_to_dict(self):
        """Regular to_dictionary"""
        d1 = self.s1.to_dictionary()
        self.assertEqual({"id": 1, "size": 1, "x": 0, "y": 0}, d1)
        d2 = self.s2.to_dictionary()
        self.assertEqual({"id": 2, "size": 2, "x": 3, "y": 0}, d2)
        d3 = self.s3.to_dictionary()
        self.assertEqual({"id": 3, "size": 4, "x": 5, "y": 6}, d3)
        d4 = self.s4.to_dictionary()
        self.assertEqual({"id": 10, "size": 7, "x": 8, "y": 9}, d4)
        self.assertTrue(type(d1) is dict)
        self.assertTrue(type(d2) is dict)
        self.assertTrue(type(d3) is dict)
        self.assertTrue(type(d4) is dict)
        s = Square(1, 1, 1, 1)
        s.update(**d4)
        self.assertEqual(str(s), str(self.s4))
        self.assertNotEqual(s, self.s4)

    def test_wh_save_to_file(self):
        """Regular use of save_to_file"""
        s1 = Square(1, 1, 1, 1)
        s2 = Square(2, 2, 2, 2)
        l = [s1, s2]
        Square.save_to_file(l)
        with open("Square.json", "r") as f:
            ls = [s1.to_dictionary(), s2.to_dictionary()]
            self.assertEqual(json.dumps(ls), f.read())

    def test_wi_file_empty(self):
        """save_to_file with empty list"""
        l = []
        Square.save_to_file(l)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_wj_file_None(self):
        """save_to_file with None"""
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_wk_create(self):
        """Normal use of create"""
        s1 = {"id": 2, "size": 3, "x": 4, "y": 0}
        s2 = {"id": 9, "size": 6, "x": 7, "y": 8}
        s1c = Square.create(**s1)
        s2c = Square.create(**s2)
        self.assertEqual("[Square] (2) 4/0 - 3", str(s1c))
        self.assertEqual("[Square] (9) 7/8 - 6", str(s2c))
        self.assertIsNot(s1, s1c)
        self.assertIsNot(s2, s2c)
        self.assertNotEqual(s1, s1c)
        self.assertNotEqual(s2, s2c)

    def test_wl_load_from_file_no_file(self):
        """Checking use of load_from_file with no file"""
        try:
            os.remove("Square.json")
        except:
            pass
        self.assertEqual(Square.load_from_file(), [])

    def test_wm_load_from_file_empty_file(self):
        """Checking use of load_from_file with empty file"""
        try:
            os.remove("Square.json")
        except:
            pass
        open("Square.json", 'a').close()
        self.assertEqual(Square.load_from_file(), [])
