import unittest
from BinaryTree import BinaryTree
from BinaryTreeNode import BinaryTreeNode
from collections import namedtuple

'''
Jeg har forsøk å lage treet brukt i testen veldig ubalansert.

DeleteMin gir en feil. Feilen rettes når du endrer de siste to linjene fra:
    # If no left branch exists, the root item is the smallest in the tree
    else:
        self._root = parent.right
        return self._root

til:
    # If no left branch exists, the root item is the smallest in the tree
    else:
        delnode = self._root
        self._root = parent.right
        return delnode
    
Med den nye koden gir ikke deleteMin() feil lenger på testen.

DeleteMax også gir en feil når root-noden er den største. 
Når jeg leger til denne koden før "While True" så gir den ikke feil lenger:
        if parent.right == None:
            print("No right value", parent.value)
            self._root = parent.left
            return parent

Og koden ikke gir forventede "exceptions"
'''

class BinaryTreeTest(unittest.TestCase):
    def setUp(self):
        self.person = namedtuple('person', ['lastname', 'firstname', 'address',
                                            'postal_code', 'city'])
        self.binarytree = BinaryTree()
        
        self.size = 0
        
        self.content =  ['RINDSTAD;MORGAN;FJELLSENDE 118;1397;NESØYA',
                        'REPPEN;SONJA;HJORTESTIEN 69;4658;TVEIT',
                        'GRANMO;BJØRN WILLY;LEIF TRONSTADS VEG 4;8251;ROGNAN',
                        'FIGENSCHOU;KIM ROBERT;MUNKEBERGET 57;1322;HØVIK',
                        'SITTAMPALAM;THARMAVANAN;WALHALD 25;8638;STORFORSHEI',
                        'JOHANSSON;JOHNNY GRØNENG;SANDERLIENVEGEN 94;8390;REINE',
                        'BJØRKHAUG;BJØRN NORMAN;LERVIKEN 27;9138;KARLSØY',
                        'VOLDEN;GRETHE;SILJETUN 81;6320;ISFJORDEN',
                        'STENMO;BIRGIT GØRIL;SKIPEVÅG 5;5216;LEPSØY',
                        'STEEL;ROAR;ÅRLEITE 38;0596;OSLO',
                        'FØLEIDE;PÅL KJETIL;SELDALVEIEN 74;9788;KUNES',
                        'ROMANOVA;TOM-EIRIK;HESTDAL 74;6729;KALVÅG',
                        'TOVÅS;STINE SOLLIE;NEDREGJERDET 24;5405;STORD',
                        'ANFINSEN;ANN-CHRISTIN;GYLTA 17;8042;BLIKSVÆR',
                        'SJÅVÅG;JAN HARRIS;KROKEN 1 72;9262;TROMSØ',
                        'PEDERSEN JR.;KIRILL ALEXANDROVICH;HELLARTUNET 14;4680;BYGLANDSFJORD',
                        'KLAVENES;ULLA;SAGSTUA 102;9258;TROMSØ',
                        'LINDBERG BJERK;KURT K.;FANEBUST 15;4450;SIRA',
                        'MAXIMOVA;INGUNN;KVAALE 67;5216;LEPSØY',
                        'SVARHOLT;JOHN KRISTIAN;SKOGSNARET 23;4294;KOPERVIK',
                        'KLEPPE;JØRN ØINES;KIRSTEN FLAGSTADS VEI 62;4679;FLEKKERØY',
                        'HERVING;DAN RAYNER;VIKGARD 7;8280;KJØPSVIK',
                        'KJÆMPENES;INGMAR;GRØNLUND 14;5931;MANGER',
                        'HASS;TERJE MIKAL;ØVRE VERKET 82;6457;BOLSØYA',
                        'SVENSEN;SURESH;KOPARNESET 59;8380;RAMBERG',
                        'BØE;VIKTOR B;LYSNINGEN 21;8726;UTSKARPEN',
                        'CHELOUATI;NIKOLAI;VESTLI SØNDRE 59;5719;FINSE',
                        'VALÅMO;MADS BØRGE;STRANDI IDROTTSPLASS 33;5786;EIDSFJORD',
                        'MANJOSSOV;DENIS;EVANGER 68;2415;HERADSBYGD',
                        'KRAINIK;SOLVEIG IRENE;KNORREBAKKEN 110;8160;GLOMFJORD',
                        'FOURMAN;NILS ASGEIR;SØNNLI 74;6411;MOLDE',
                        'RIISE;SAM;AAREBROTSVAAGEN 115;4823;NEDENES',
                        'MATHIASSEN;TRULS ALEXANDER;ØVRE LIANE 0;6727;BREMANGER',
                        'AAMODT;ERIK MAGNUS;RASTAVEGEN 21;5001;BERGEN',
                        'HOLMEN;THIEN PHUOC;MARYVELL 54;9279;TROMSØ',
                        'RYDNING;HILDE LILL;STOR-RENHOLDTVEIEN 6;3884;RAULAND',
                        'NERGAARD;SASIHARAN;TULLUAN 82;5183;OLSVIK',
                        'LYSFJORD;STIG HÅVARD;THORBU 23;2215;MATRAND',
                        'ASPEGREN;HANS-OTTO;SELKNATTEN 40;6947;LAVIK',]
        self.size = len(self.content)


    def test_insert_value(self):
        btree1 = BinaryTree()
        for p in self.content:
            person = self.person(*p.split(';'))
            node = BinaryTreeNode(person)
            self.assertEqual(node, btree1.insert(value = person))
    
    
    def test_insert_to_empty_tree(self):
        btree = BinaryTree(None)
        person = self.person('WIKILUND','JOHAN', 'SVETUN 11', '8510', 'NARVIK')
        node = BinaryTreeNode(person)
        self.assertEqual(node, btree.insert(value=person))
        
    def test_insert_node_to_empty_tree(self):
        btree = BinaryTree(None)
        person = self.person('WIKILUND','JOHAN', 'SVETUN 11', '8510', 'NARVIK')
        node = BinaryTreeNode(person)
        self.assertEqual(node, btree.insert(treenode=node))
    
    def test_insert_None_value(self):
        with self.assertRaisesRegex(Exception, "Attempt to insert an empty space into Binary Tree"):
            self.binarytree.insert(value = None)

    def test_findMin(self):
        for p in self.content:
            self.binarytree.insert(value = self.person(*p.split(';')))
        self.size = len(self.content)
        min_value = self.person('AAMODT','ERIK MAGNUS','RASTAVEGEN 21','5001','BERGEN')
        node = BinaryTreeNode(min_value)
        self.assertEqual(node, self.binarytree.findMin())
        
    
    def test_findMax(self):
        for p in self.content:
            self.binarytree.insert(value = self.person(*p.split(';')))
        self.size = len(self.content)
        max_value = self.person('VOLDEN','GRETHE','SILJETUN 81','6320','ISFJORDEN')
        node = BinaryTreeNode(max_value)
        node = self.binarytree.findMax()
        self.assertEqual(node, self.binarytree.findMax())
    
    
    def test_find(self):
        for p in self.content:
            self.binarytree.insert(value = self.person(*p.split(';')))
        self.size = len(self.content)
        for p in self.content:
            person = self.person(*p.split(';'))
            node = BinaryTreeNode(person)
            self.assertEqual(node, self.binarytree.find(person))
    
    def test_find_in_empty_tree(self):
        tree = BinaryTree()
        value = self.person('SKARSHAUG','ASBJØRN HARALD', 'ALAPMO 72', '7290', 'STØREN')
        with self.assertRaises(KeyError):
            self.binarytree.find(value)

    def test_deleteMin(self):
        for p in self.content:
            self.binarytree.insert(value = self.person(*p.split(';')))
        min_value = self.person('AAMODT','ERIK MAGNUS','RASTAVEGEN 21','5001','BERGEN')
        node = BinaryTreeNode(min_value)
        self.assertEqual(node, self.binarytree.deleteMin())
    
    
    def test_deleteMax(self):
        for p in self.content:
            self.binarytree.insert(value = self.person(*p.split(';')))
        max_value = self.person('VOLDEN','GRETHE','SILJETUN 81','6320','ISFJORDEN')
        node = BinaryTreeNode(max_value)
        self.assertEqual(node, self.binarytree.deleteMax())


    def test_delete(self):
        for p in self.content:
            self.binarytree.insert(value = self.person(*p.split(';')))
        person1 = self.person('TOVÅS','STINE SOLLIE','NEDREGJERDET 24','5405','STORD')
        person2 = self.person('CHELOUATI','NIKOLAI','VESTLI SØNDRE 59','5719','FINSE')
        person3 = self.person('VALÅMO','MADS BØRGE','STRANDI IDROTTSPLASS 33','5786','EIDSFJORD')
        person4 = self.person('MANJOSSOV','DENIS','EVANGER 68','2415','HERADSBYGD')
        person5 = self.person('KRAINIK','SOLVEIG IRENE','KNORREBAKKEN 110','8160','GLOMFJORD')
        node1 = BinaryTreeNode(person1)
        node2 = BinaryTreeNode(person2)
        node3 = BinaryTreeNode(person3)
        node4 = BinaryTreeNode(person4)
        node5 = BinaryTreeNode(person5)
        self.assertEqual(node1 , self.binarytree.delete(person1))
        self.assertEqual(node2 , self.binarytree.delete(person2))
        self.assertEqual(node3 , self.binarytree.delete(person3))
        self.assertEqual(node4 , self.binarytree.delete(person4))
        self.assertEqual(node5 , self.binarytree.delete(person5))
        #check if size is reduced by 5
        self.size -= 5
        treesize = 0
        for p in self.content:
            person = self.person(*p.split(';'))
            if None != self.binarytree.find(person):
                treesize += 1
        self.assertEqual(treesize , self.size)
    
    
    def test_delete_left_tree(self):
        btree = BinaryTree()
        value1 = self.person('AAKVIK', 'ANNE-MARIT', 'RISØYVEGEN 17', '1705', 'SARPSBORG')
        value2 = self.person('AAJVIK', 'ANNE-MARIT', 'RISØYVEGEN 17', '1705', 'SARPSBORG')
        value3 = self.person('AAIVIK', 'ANNE-MARIT', 'RISØYVEGEN 17', '1705', 'SARPSBORG')
        btree.insert(value=value1); btree.insert(value=value2); btree.insert(value=value3)
        node = BinaryTreeNode(value1)
        self.assertEqual(node, btree.delete(value1))
        node = BinaryTreeNode(value2)
        self.assertEqual(node, btree.find(value2))
        node = BinaryTreeNode(value3)
        self.assertEqual(node, btree.find(value3))
        
    def test_delete_single_value(self):
        btree = BinaryTree()
        value1 = self.person('AAKVIK', 'ANNE-MARIT', 'RISØYVEGEN 17', '1705', 'SARPSBORG')
        btree.insert(value = value1);
        btree.delete(value1)
        node = BinaryTreeNode(value1)
        with self.assertRaises(KeyError):
            self.binarytree.find(value1)






        


if __name__ == '__main__':
    import sys;sys.argv = ['', 'BinaryTreeTest']
    unittest.main()