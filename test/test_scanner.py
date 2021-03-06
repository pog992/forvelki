import unittest
from forvelki.scanner import lexer

class TestLexer(unittest.TestCase):
    
    def test_comparison(self):
        source = "2 < 3.5"
        
        lexer.input(source)
        tokens = [token.type for token in lexer]
        
        expected = ['INTEGER', 'COMP_LT', 'FLOAT']
        self.assertListEqual(expected, tokens)
        
    def test_brackets(self):
        source = "[{}]()"
        
        lexer.input(source)
        tokens = [token.type for token in lexer]
        
        expected = ['[', '{', '}', ']', '(', ')']
        self.assertListEqual(expected, tokens)
        
    def test_operators(self):
        source = "!+*-/"
        
        lexer.input(source)
        tokens = [token.type for token in lexer]
        
        expected = ['!', '+', '*', '-', '/']
        self.assertListEqual(expected, tokens)
        
    def test_function(self):
        src = """[x,y->t=1;z+1];"""
        lexer.input(src)
        self.assertEquals(14, len(list(lexer)))