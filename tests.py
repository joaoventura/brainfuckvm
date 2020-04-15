"""
 Tests the brainfuckVM.

"""

import io
import unittest
from unittest.mock import patch

from brainfuck import BrainFuckVM


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.bf = BrainFuckVM()

    def test_inc_block(self):
        """Char + increases values."""
        self.bf.eval('+++')
        self.assertEqual(self.bf.blocks[0], 3)

    def test_dec_block(self):
        """Char - decreases values."""
        self.bf.blocks[0] = 3
        self.bf.eval('--')
        self.assertEqual(self.bf.blocks[0], 1)

    def test_move_right(self):
        """Char > moves pointer to the right."""
        self.bf.pointer = 0
        self.bf.eval('>')
        self.assertEqual(self.bf.pointer, 1)

    def test_move_left(self):
        """Char < moves pointer to the left."""
        self.bf.pointer = 1
        self.bf.eval('<')
        self.assertEqual(self.bf.pointer, 0)

    def test_move_left_zero(self):
        """Pointer cannot be less than zero."""
        self.bf.pointer = 0
        self.bf.eval('<')
        self.assertEqual(self.bf.pointer, 0)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print(self, stdout):
        """Char . should print character to stdout."""
        self.bf.blocks[0] = 51
        self.bf.eval('.')
        self.assertEqual(stdout.getvalue(), '3')

    @patch('sys.stdin', io.StringIO('1'))
    def test_read(self):
        """Char , should read character from stdin."""
        self.bf.eval(',')
        self.assertEqual(self.bf.blocks[0], 49)

    def test_loops(self):
        """Tests single loops."""
        self.bf.blocks[0] = 3
        self.bf.eval('[-]')
        self.assertEqual(self.bf.blocks[0], 0)

    def test_loops_add_numbers(self):
        """Tests single loops to add two numbers."""
        self.bf.blocks[0] = 3
        self.bf.blocks[1] = 5
        self.bf.eval('>[-<+>]')
        self.assertEqual(self.bf.blocks[0], 8)


