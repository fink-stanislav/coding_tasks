
import unittest
import games.bot_saves_princess as bsp


class TestBotSavesPrincess(unittest.TestCase):

    def _get_grid(self):
        grid = [
            ['-', '-', '-', '-', 'm'],
            ['-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', 'p'],
        ]
        return grid

    def test_get_bot_coords(self):
        grid = self._get_grid()
        self.assertListEqual(bsp.get_bot_coords(grid), [3, 2])
    
    def test_princess_coords(self):
        grid = self._get_grid()
        self.assertListEqual(bsp.get_princess_coords(grid), [0, 2])

    def test_next_move(self):
        grid = self._get_grid()
        
        while True:
            r = bsp.nextMove(0, 0, 0, grid)
            if not r:
                return
            print r


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()