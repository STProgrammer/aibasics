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
        
        self.content =  ['MARKUSSEN;ANNE;GAUTEVARDEN 24;2404;ELVERUM',
                    'MARKUSSEN;ANNA;FURUKROK 23;7530;MERÅKER',
                    'MARIDAL;ØYSTEIN ANDRE;GULSET TERRASSE 59;7054;RANHEIM',
                    'MARIDAL;WEIJIAN;TEIGJORDET 56;7585;ELVARLI',
                    'MANJOSSOV;TOVE JORUN EIDE;SÆTERÅSEN 11;3926;PORSGRUNN',
                    'MANJOSSOV;TROND-ESPEN;VÅGSGATA 36;4017;STAVANGER',
                    'MANJOSSOV;UNNI MERETHE;BURSTUEN 85;3535;KRØDEREN',
                    'MARHAUG;VIDAR;ØDELI 69;2688;LOM',
                    'MARHAUG;VIDAR;MOENSTUBBEN 38;4329;SANDNES',
                    'MARHAUG;VIATCHESLAV;STRØMSBU TERRASSE 62;7037;TRONDHEIM',
                    'MANNVIK;TIM;ONKENHAUG 58;7350;BUVIKA',
                    'MANNVIK;SVEIN-INGVAR;SPRETTEDALEN 82;5774;LOFTHUS',
                    'MANNVIK;STEIN ROAR;ANFINNSTOVA 27;7230;KVENVÆR',
                    'MANNVIK;SIGRID;LØKSTAD 66;3223;SANDEFJORD',
                    'MANNVIK;TOR-ARNE;ÅRSETHAUGEN 51;8009;BODØ',
                    'MANNVIK;TRULS MAGNE;RENDALEN 112;4974;SØNDELED',
                    'MANNVIK;VARATHARAJAN;SKREDLUND 12;8042;BLIKSVÆR',
                    'MARKUSSEN;ARNFINN JOHAN;TVARA NEDRE 113;1870;ØRJE',
                    'MARKUSSEN;BENT;GUDBRANDS VEI 84;2652;SVINGVOLL',
                    'MARKUSSEN;BJØRN ROGER;BLOMTUN 60;7670;INDERØY',
                    'MARTUSHOV;GRO BEATE;LÆRUM ØSTRE 46;5718;MYRDAL',
                    'MARTUSHOV;FRITS ANDRE;URETRÆ 15;6380;TRESFJORD',
                    'MARTUSHOV;EVA HARRIET;SUNDBY MELLEM 22;5032;MINDE',
                    'MARTINUSSEN;KARL-ARNE;TYRIHAUGEN 26;2671;OTTA',
                    'MARTINUSSEN;KIRSTI ANJA JACOBSEN;DRAGSNO 45;4395;HOMMERSÅK',
                    'MARTINUSSEN;KRISTER;MALI FURUNES VEG 44;4505;MANDAL',
                    'MARTNES;ROALD;PEDER RISTVEDTS VEI 93;0367;OSLO',
                    'MARTNES;RUBEN;BIEVEIEN 51;5178;LODDEFJORD',
                    'MARTNES;RUNE HÅVARD;JÅTTÅHAGEN 55;5995;YTRØYGREND',
                    'MARTNES;RUTH INGUNN;VASENDEN 32;5222;NESTTUN',
                    'MARTNES;PER NORVALD;SVARTISGATA 52;8516;NARVIK',
                    'MARTNES;PER KÅRE;ONSTAD NORDRE 1;5001;BERGEN',
                    'MARTNES;PER ATLE;OLSAKER 85;7418;TRONDHEIM',]
        self.size = len(self.content)


    def test_insert_value(self):
        btree1 = BinaryTree()
        for p in self.content:
            person = self.person(*p.split(';'))
            node = BinaryTreeNode(person)
            self.assertEqual(node, btree1.insert(value = person))
    
    def test_insert_node(self):
        for p in self.content:
            self.binarytree.insert(value = self.person(*p.split(';')))
        value1 = self.person('WIKILUND','JOHAN', 'SVETUN 11', '8510', 'NARVIK')
        node1 = BinaryTreeNode(value1)
        value2 = self.person('ALFRED', 'POLLEN', 'gate 11', '1234', 'KONGSBERG')
        node2 = BinaryTreeNode(value2)
        self.assertEqual(node1, self.binarytree.insert(treenode=node1))
        self.assertEqual(node2, self.binarytree.insert(treenode=node2))
        for p in self.content:
            person = self.person(*p.split(';'))
            node = BinaryTreeNode(person)
            self.assertEqual(node, self.binarytree.find(person))
    
    
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


    def test_insert_duplicate(self):
        for p in self.content:
            self.binarytree.insert(value = self.person(*p.split(';')))
        for p in self.content:  
            with self.assertRaisesRegex(Exception, "Duplicate key"):
                self.binarytree.insert(value = self.person(*p.split(';')))
                
    def test_insert_single_duplicate(self):
        person = self.person('AAKVIK', 'ANNE-MARIT', 'RISØYVEGEN 17', '1705', 'SARPSBORG')
        self.binarytree.insert(value = person)
        with self.assertRaisesRegex(Exception, "Duplicate key"):
            self.binarytree.insert(value = person)
    

    def test_insert_None_value(self):
        with self.assertRaisesRegex(Exception, "Attempt to insert an empty space into Binary Tree"):
            self.binarytree.insert(value = None)

    def test_findMin(self):
        for p in self.content:
            self.binarytree.insert(value = self.person(*p.split(';')))
        min_value = self.person('MANJOSSOV','TOVE JORUN EIDE','SÆTERÅSEN 11','3926','PORSGRUNN')
        node = BinaryTreeNode(min_value)
        self.assertEqual(node, self.binarytree.findMin())

    
    def test_findMin_empty(self):
        emptytree = BinaryTree()
        self.assertEqual(None, emptytree.findMin())
        
    
    def test_findMax(self):
        for p in self.content:
            self.binarytree.insert(value = self.person(*p.split(';')))
        max_value = self.person('MARTUSHOV','GRO BEATE','LÆRUM ØSTRE 46','5718','MYRDAL')
        node = BinaryTreeNode(max_value)
        self.assertEqual(node, self.binarytree.findMax())
    
    def test_findMax_empty(self):
        emptytree = BinaryTree()
        self.assertEqual(None, emptytree.findMax())
    
    
    def test_find(self):
        for p in self.content:
            self.binarytree.insert(value = self.person(*p.split(';')))
        for p in self.content:
            person = self.person(*p.split(';'))
            node = BinaryTreeNode(person)
            self.assertEqual(node, self.binarytree.find(person))
    
    def test_find_key_not_found(self):
        for p in self.content:
            self.binarytree.insert(value = self.person(*p.split(';')))
        person = self.person('NOBODY','NOT EXISTING', 'ALAPMO 72', '7290', 'STØREN')
        with self.assertRaises(KeyError):
            self.binarytree.find(person)
    
    def test_find_in_empty_tree(self):
        tree = BinaryTree()
        value = self.person('SKARSHAUG','ASBJØRN HARALD', 'ALAPMO 72', '7290', 'STØREN')
        with self.assertRaises(KeyError):
            self.binarytree.find(value)

    def test_deleteMin(self):
        for p in self.content:
            self.binarytree.insert(value = self.person(*p.split(';')))
        contents = sorted(self.content)
        for p in contents:
            person = self.person(*p.split(';'))
            node = BinaryTreeNode(person)
            self.assertEqual(node, self.binarytree.deleteMin())
    
    def test_deleteMin_empty(self):
        emptytree = BinaryTree()
        self.assertEqual(None, emptytree.deleteMin())
    

    def test_deleteMin_root(self):
        btree = BinaryTree()
        min_value = self.person('AAAAAA', 'AAAAA', 'AA street', '1234', 'AACity')
        btree.insert(value = min_value)
        btree.insert(value = self.person('Zero', 'Zero', 'Zero street', '1234', 'ZeroCity'))
        next_min_value = self.person('AAKVIK', 'ANNE-MARIT', 'RISØYVEGEN 17', '1705', 'SARPSBORG')
        btree.insert(value = next_min_value)
        next_min_node = BinaryTreeNode(next_min_value)
        min_node = BinaryTreeNode(min_value)
        self.assertEqual(min_node, btree.deleteMin())
        self.assertEqual(next_min_node, btree.find(next_min_value))
    
    
    def test_deleteMax(self):
        for p in self.content:
            self.binarytree.insert(value = self.person(*p.split(';')))
        contents = reversed(sorted(self.content))
        for p in contents:
            person = self.person(*p.split(';'))
            node = BinaryTreeNode(person)
            val = self.binarytree.deleteMax()
            self.assertEqual(node, val)

    
    def test_deleteMax_empty(self):
        emptytree = BinaryTree()
        val = emptytree.deleteMax()
        self.assertEqual(None, emptytree.deleteMax())


    def test_deleteMax_root(self):
        btree = BinaryTree()
        value1 = self.person('Zero', 'Zero', 'Zero street', '1234', 'ZeroCity')
        value2 = self.person('AAKVIK', 'ANNE-MARIT', 'RISØYVEGEN 17', '1705', 'SARPSBORG')
        value3 = self.person('AAAAAA', 'AAAAA', 'AA street', '1234', 'AACity')
        btree.insert(value = value1)
        btree.insert(value = value2)
        btree.insert(value = value3)
        max_node = BinaryTreeNode(value1)
        next_max_node = BinaryTreeNode(value2)
        self.assertEqual(max_node, btree.deleteMax())
        self.assertEqual(next_max_node, btree.find(value2))


    def test_delete_one_by_one(self):
        for p in self.content:
            self.binarytree.insert(value = self.person(*p.split(';')))
        test_cases = self.content
        for p in test_cases:
            value = self.person(*p.split(';'))
            node = BinaryTreeNode(value)
            with self.subTest():
                self.setUp()
                for p in self.content:
                    self.binarytree.insert(value = self.person(*p.split(';')))
                node2 = self.binarytree.delete(value)
                self.assertEqual(node, node2)
                #This loop is to test if all other values still exists after delete
                treesize = 0
        #        for p in self.content:
        #            person = self.person(*p.split(';'))
        #            node = BinaryTreeNode(person)
        #            if node == self.binarytree.find(person):
        #                treesize += 1
        #        self.assertEqual(treesize , self.size - 1)
    
    
    def test_delete_all(self):
        for p in self.content:
            self.binarytree.insert(value = self.person(*p.split(';')))
        test_cases = self.content
        for p in test_cases:
            value = self.person(*p.split(';'))
            node = BinaryTreeNode(value)
            with self.subTest():
                node2 = self.binarytree.delete(value)
                self.size -= 1
                self.assertEqual(node, node2)
                #This loop is to test if all other values still exists after delete
       #         treesize = 0
       ##         for p in self.content:
        #            person = self.person(*p.split(';'))
        #            node = BinaryTreeNode(person)
        ##            if node == self.binarytree.find(person):
         #               treesize += 1
         #       self.assertEqual(treesize , self.size)
    
    
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
    
    def test_delete_empty(self):
        person = self.person('AAKVIK', 'ANNE-MARIT', 'RISØYVEGEN 17', '1705', 'SARPSBORG')
        emptytree = BinaryTree()
        self.assertEqual(None, emptytree.delete(person))
    
    
    def test_delete_nonexistent(self):
        person1 = self.person('NOBODY', 'NO ONE','ONSTAD NORDRE 1','5001','NONE')
        self.assertEqual(None, self.binarytree.delete(person1))
        
    def test_delete_single_value(self):
        btree = BinaryTree()
        value1 = self.person('AAKVIK', 'ANNE-MARIT', 'RISØYVEGEN 17', '1705', 'SARPSBORG')
        btree.insert(value = value1);
        btree.delete(value1)
        node = BinaryTreeNode(value1)
        with self.assertRaises(KeyError):
            btree.find(value1)




        


if __name__ == '__main__':
    import sys;sys.argv = ['', 'BinaryTreeTest']
    unittest.main()