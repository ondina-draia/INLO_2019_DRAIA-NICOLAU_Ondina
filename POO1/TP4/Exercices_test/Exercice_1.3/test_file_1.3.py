# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 17:28:09 2019

@author: Draia-Nicolau Ondina
"""

import pile_file_obj
import unittest

class TestFile(unittest.TestCase):
    """Tests pour verifier les axiomes d'une file"""
    
    def setUp(self):
        """Initiation des tests"""
        f = pile_file_obj.File() #recuperation de l'objet file cree grace a File()
        self.file = f.file
        
    def test_tete_elt(self):
        """Si une file est vide, alors la tête d’une file sur laquelle on enfile un élément e est e"""
        e = 'a'
        pile_file_obj.File.enfiler(self,e)
        tete = pile_file_obj.File.tete(self)
        self.assertEqual(e, tete)
    
    def test_tete_inchangee(self):
        """Si une file n’est pas vide, alors la tête d’une file sur laquelle on enfile un élément e est identique
            à la tête de la file avant l’opération d’enfilement"""
        pile_file_obj.File.enfiler(self,'a') #la file n'est donc pas vide, premier élément 'a'
        tete_av = pile_file_obj.File.tete(self) #tete avant l'enfilement d'un nouveau element, ici 'a'
        pile_file_obj.File.enfiler(self,'b') #on enfile un élément b
        tete_ap = pile_file_obj.File.tete(self) #tete apres l'enfilement d'un nouveau élément, normalement cela doit rester a
        self.assertEqual(tete_av, tete_ap)
        
    def test_enf_def_vide(self):
        """Une file vide qui subit un enfilement suivi d’un défilement est toujours une file vide"""
        file_av = self.file
        pile_file_obj.File.enfiler(self,'a')
        pile_file_obj.File.defiler(self)
        file_ap = self.file
        self.assertEqual(file_av, file_ap)
    
    def test_defilenfil_enfildefil(self):
        """Sur une file non vide, un enfilement suivi d’un défilement est identique à un défilement suivi d’un
            enfilement"""
        #on verfie donc que la taille de la file reste inchangée 
        pile_file_obj.File.enfiler(self,'a') #la file n'est donc pas vide, premier élément 'a'
        #enfilement suivi d'un defilement
        pile_file_obj.File.enfiler(self,'b') #on enfile 'b'
        pile_file_obj.File.defiler(self) #et on le defile
        file_ed = len(self.file) #ed: empilemenr depilement
        #defilement suivi d'un enfilement
        pile_file_obj.File.defiler(self) #on defile la file donc a sera enleve
        pile_file_obj.File.enfiler(self,'a') 
        file_de = len(self.file) #de: depilement enfilement
        #on verfie donc que la taille de la file reste inchangée
        self.assertEqual(file_ed, file_de)

if __name__ == '__main__':
    unittest.main() 