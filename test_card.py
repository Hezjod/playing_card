import unittest
import random
import sys
sys.path.insert(0, '..')

from card import Card

class AddTest(unittest.TestCase):
    
    def test_find(self):
        table = [
            [1,2,3],
            [4,5,6],
            [7,8,9],
        ]

        table2 = [
            [1,2,3,"a"],
            [4,5,6,"b"],
            [7,8,9,"c"],
        ]

        r = Card._find(
            table = table,
            watch_column = 0,
            value_to_find = 4,
            return_column = 2
        )
        self.assertEqual(r, 6)

        self.assertEqual(table, [[1,2,3],[4,5,6],[7,8,9]])

        with self.assertRaises(AssertionError):
            Card._find(
                table = [],
                watch_column = 0,
                value_to_find = 4,
                return_column = 2
            )

        with self.assertRaises(AssertionError):
            Card._find(
                table = [[1,2,3]],
                watch_column = 3,
                value_to_find = 4,
                return_column = 2
            )
        
        with self.assertRaises(AssertionError):
            Card._find(
                table = [[1,2,3]],
                watch_column = 2,
                value_to_find = 4,
                return_column = -1
            )
        
        with self.assertRaises(AssertionError):
            Card._find(
                table = table2,
                watch_column = -1,
                value_to_find = 4,
                return_column = 0
            )
        
        
        r = Card._find(
            table = table2,
            watch_column = 3,
            value_to_find = 4,
            return_column = 0
        )
        self.assertEqual(r, None)

        r = Card._find(
            table = table2,
            watch_column = 0,
            value_to_find = 7,
            return_column = 3
        )
        self.assertEqual(r, "c")

        t2 = [
            [1,2,3,"a"],
            [4,5,6,"b"],
            [7,8,9,"c"],
        ]
        self.assertEqual(table2, t2)

    def test_name(self):
        from card_names_data import data as cn_data
        for test_case in cn_data:
            c = str(Card(
                    value=test_case[0][0],
                    color=test_case[0][1],
                ))
            self.assertEqual(
                c,
                test_case[1]
            )

    def test_eq(self):
        for i in range(1,5):
            for j in range(1, 14):
                a = Card(value=j, color=i)
                b = Card(value=j, color=i)
                self.assertTrue(a == b)

        a = Card(value=14, color=5)
        b = Card(value=14, color=5)
        self.assertTrue(a == b)

        a = Card(value=14, color=6)
        b = Card(value=14, color=6)
        self.assertTrue(a == b)
    
    def test_init(self):
        for i in range(1,5):
            for j in range(1, 14):
                Card(value=j, color=i)
        Card(value=14, color=5)
        Card(value=14, color=6)


        for i in range(-20, 20):
            if i == 14:
                continue

            with self.assertRaises(AssertionError):
                Card(value=i, color=5)

            with self.assertRaises(AssertionError):
                Card(value=i, color=6)
            
        for i in range(-20, 20):
            if i == 5 or i == 6:
                continue

            with self.assertRaises(AssertionError):
                Card(value=14, color=i)

    def test_from_symbols(self):
        from colors_data import data as c_data
        from values_data import data as v_data

        for i in range(4):
            for j in range(13):
                a = Card.from_symbols(v_data[j][1], c_data[i][1])
                b = Card(value=j+1, color=i+1)
                self.assertEqual(a, b)

        a = Card(value=14, color=5)
        b = Card.from_symbols("W", "J")
        self.assertEqual(a, b)
        a = Card(value=14, color=6)
        b = Card.from_symbols("B", "J")
        self.assertEqual(a, b)

    def test_unicode(self):
        from unicode_cards_list import data as u_data

        c = Card(value=1, color=1)
        self.assertEqual(c.unicode, "🂱")
        c = Card(value=3, color=2)
        self.assertEqual(c.unicode, "🃃")
        c = Card(value=5, color=3)
        self.assertEqual(c.unicode, "🃕")
        c = Card(value=13, color=4)
        self.assertEqual(c.unicode, "🂮")


        for i in range(1,5):
            for j in range(1, 14):
                c = Card(value=j, color=i)
                self.assertEqual(c.unicode, u_data[j - 1][i - 1])
        c = Card(value=14, color=5)
        self.assertEqual(c.unicode, "🃟")
        c = Card(value=14, color=6)
        self.assertEqual(c.unicode, "🃏")

    def test_repr(self):
        for i in range(1,5):
            for j in range(1, 14):
                a = Card(value=j, color=i)
                b = eval(f"{a.__repr__()}")
                self.assertEqual(a, b)

        a = Card(value=14, color=5)
        b = eval(f"{a.__repr__()}")
        self.assertEqual(a, b)

        a = Card(value=14, color=6)
        b = eval(f"{a.__repr__()}")
        self.assertEqual(a, b)

    def test_value_name(self):
        from values_data import data as v_data

        for i in range(1,5):
            for j in range(1, 14):
                a = Card(value=j, color=i).value_name
                b = v_data[j - 1][2]
                self.assertEqual(a, b)


        a = Card(value=14, color=5).value_name
        b = "Joker"
        self.assertEqual(a, b)

        a = Card(value=14, color=6).value_name
        b = "Joker"
        self.assertEqual(a, b)
    
    def test_color_name(self):
        from colors_data import data as c_data

        for i in range(1,5):
            for j in range(1, 14):
                a = Card(value=j, color=i).color_name
                b = c_data[i - 1][2]
                self.assertEqual(a, b)


        a = Card(value=14, color=5).color_name
        b = "White"
        self.assertEqual(a, b)

        a = Card(value=14, color=6).color_name
        b = "Black"
        self.assertEqual(a, b)

    def test_value_symbol(self):
        from values_data import data as v_data

        for i in range(1,5):
            for j in range(1, 14):
                a = Card(value=j, color=i).value_symbol
                b = v_data[j -  1][1]
                self.assertEqual(a, b)

        
        a = Card(value=14, color=5).value_symbol
        self.assertEqual(a, "J")
        a = Card(value=14, color=6).value_symbol
        self.assertEqual(a, "J")

    def test_color_symbol(self):
        from colors_data import data as c_data

        for i in range(1,5):
            for j in range(1, 14):
                a = Card(value=j, color=i).color_symbol
                b = c_data[i -  1][1]
                self.assertEqual(a, b)

        
        a = Card(value=14, color=5).color_symbol
        self.assertEqual(a, "W")
        a = Card(value=14, color=6).color_symbol
        self.assertEqual(a, "B")

    def test_symbols(self):
        from colors_data import data as c_data
        from values_data import data as v_data

        for i in range(1,5):
            for j in range(1, 14):
                a = Card(value=j, color=i).symbols
                b = v_data[j - 1][1] + c_data[i -  1][1]
                self.assertEqual(a, b)

        
        a = Card(value=14, color=5).symbols
        self.assertEqual(a, "WJ")
        a = Card(value=14, color=6).symbols
        self.assertEqual(a, "BJ")
    
    def test_from_name(self):
        for i in range(1,5):
            for j in range(1, 14):
                a = Card(value=j, color=i)
                b = Card.from_name(a.name)
                self.assertEqual(a, b)
        
        a = Card(value=14, color=5)
        b = Card.from_name(a.name)
        self.assertEqual(a, b)

        a = Card(value=14, color=5)
        b = Card.from_name(a.name)
        self.assertEqual(a, b)


        with self.assertRaises(AssertionError):
            Card.from_name("a b c")
        
        with self.assertRaises(AssertionError):
            Card.from_name("Joker White")
        
        with self.assertRaises(AssertionError):
            Card.from_name("Joker Black")
        
        with self.assertRaises(AssertionError):
            Card.from_name("2 Clubs")

        with self.assertRaises(AssertionError):
            Card.from_name("King of  Hearts")
        
        with self.assertRaises(AssertionError):
            Card.from_name("King  of  Hearts")
        
        with self.assertRaises(AssertionError):
            Card.from_name("King of Hearts ")

        with self.assertRaises(AssertionError):
            Card.from_name("King of Hearts a")

    def test_from_number(self):
        # correct = []
        # for i in range(1, 5):
        #     for j in range(1, 14):
        #         a = f"({i}, {j})"
        #         correct.append(a)

        # for i in range(1, 53):
        #     a = correct[i - 1]
        #     b = divmod(i-1, 13)
        #     b = (b[0] + 1, b[1] +1)

        #     self.assertEqual(a, str(b))

        #todo todo todo todo todo todo todo todo todo todo todo todo todo
        

        pass



if __name__ == "__main__":
    unittest.main()
    