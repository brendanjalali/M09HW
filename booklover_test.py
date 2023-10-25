from booklover import BookLover
import unittest

class BookLoverTestSuite(unittest.TestCase): 
    
    def test_1_add_book(self):
        # add a book and test if it is in `book_list`
        booklover1 = BookLover('Katherine', 'k@k.com', 'Fantasy')
        booklover1.add_book('Dune 1', 3)
        book = 'Dune 1'
        self.assertTrue(any(booklover1.book_list['book_name'] == book))
        
    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        booklover1 = BookLover('Katherine', 'k@k.com', 'Fantasy')
        booklover1.add_book('Dune 1', 3)
        booklover1.add_book('Dune 1', 3)
        book = 'Dune 1'
        expected = 1
        self.assertEqual(booklover1.num_books_read(), expected)
        
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        booklover1 = BookLover('Katherine', 'k@k.com', 'Fantasy')
        booklover1.add_book('Dune 1', 3)
        self.assertTrue(booklover1.has_read('Dune 1'))
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        booklover1 = BookLover('Katherine', 'k@k.com', 'Fantasy')
        booklover1.add_book('Dune 1', 3)
        self.assertFalse(booklover1.has_read('Dune 5'))
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        booklover1 = BookLover('Katherine', 'k@k.com', 'Fantasy')
        booklover1.add_book('Dune 1', 3)
        booklover1.add_book('Dune 2', 3)
        booklover1.add_book('Dune 3', 3)
        booklover1.add_book('Dune 4', 3)
        expected = 4
        self.assertEqual(booklover1.num_books_read(), expected)
        
    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        booklover1 = BookLover('Katherine', 'k@k.com', 'Fantasy')
        booklover1.add_book('Dune 1', 3)
        booklover1.add_book('Dune 2', 5)
        expected = 1
        actual = len(booklover1.fav_books()['book_rating'] > 3)
        self.assertEqual(actual, expected)
        
        
if __name__ == '__main__':
    unittest.main(verbosity=2)