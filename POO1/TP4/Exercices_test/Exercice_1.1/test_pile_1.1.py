# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 21:57:18 2019

@author: Ondina Draia-Nicolau
"""

import pile_file_obj
import unittest

class TestPile(unittest.TestCase):
    
    """Verifie que la méthode dépiler et sommet levent une exception si la pile est vide"""
    
    def setUp(self):
        """Initialisation des tests."""
        self.pile = list(range(0))
        
    def test_depiler(self):
        """Verifie qu'une pile vide ne peut être dépilée, lévée d'exception si la pile est vide"""
        self.assertRaises(IndexError, pile_file_obj.Pile.depiler, self)
        
    def test_sommet(self):
        """Verifie egalement qu'on ne peut lire le sommet d'une pile vide"""
        self.assertRaises(IndexError, pile_file_obj.Pile.sommet, self)        

if __name__ == '__main__':
	unittest.main() 
