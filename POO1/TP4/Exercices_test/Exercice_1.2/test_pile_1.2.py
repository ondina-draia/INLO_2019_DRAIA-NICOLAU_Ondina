# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 23:53:58 2019

@author: Ondina Draia-Nicolau
"""

import pile_file_obj
import unittest

class TestPile(unittest.TestCase):
    """Tests pour verifier les axiomes d'une pile"""
     
    def setUp(self):
        """Initiation des tests"""
        p = pile_file_obj.Pile() #recuperation de l'objet pile cree grace a Pile()
        self.pile = p.pile
    
    def test_pile_cree_vide(self):
        """Teste si une pile venant d'etre cree est vide"""
        self.assertTrue(pile_file_obj.Pile.estVide(self)) #estVide renvoie true si la pile est vide, assertTrue verifie cela
        
    def test_pile_empile_nonvide(self):
        """Teste que toute pile venant d'etre empilee est non vide"""
        pile_file_obj.Pile.empiler(self, 'a')
        self.assertTrue(self.pile) #une pile non vide renvoie le boolean true, si elle est bien vide, assertTrue renvoie que le test est valide
        
    def test_pile_empile_depile(self):
        """Teste que toute pile venant d'etre empilee puis depilee reste inchangee"""
        pile_base = self.pile #la pile avant qu'on empile et depile un element
        pile_file_obj.Pile.empiler(self, 'b')
        pile_file_obj.Pile.depiler(self)
        pile_depil = self.pile #la pile apres empilement et depilement d'un element
        self.assertEqual(pile_base, pile_depil)
         
    def test_sommet_elt(self):
        """Teste que tout sommet d'une pile auquelle on vient d'empiler un element e est donc e"""
        elt = 'a'
        pile_file_obj.Pile.empiler(self,elt)
        somm = pile_file_obj.Pile.sommet(self) #somm pour sommet de la pile
        self.assertEqual(elt, somm)
        
if __name__ == '__main__':
    unittest.main() 