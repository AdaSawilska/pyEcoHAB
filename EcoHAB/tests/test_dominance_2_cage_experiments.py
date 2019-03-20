#!/usr/bin/env python
from __future__ import print_function, division, absolute_import
from EcoHAB import dominance_2_cage_experiments as dom
import unittest
import numpy as np

class TestGetStates(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dt = 0.1
        cls.t_start = 600.0
        cls.t_end = 800.0
        cls.home_antenna_1 = 3
        cls.home_antenna_2 = 4

        cls.antennas = [3, 4, 4, 3, 3, 4, 4, 3, 3, 4, 4, 3, 3, 4, 4, 3, 3]
        cls.times = [641.083, #3 #0
                      642.135, #4 #1
                      675.134, #4 #2
                      675.869, #3 #3
                      681.127, #3 #4
                      681.734, #4 #5
                      692.744, #4 #6
                      693.207, #3 #7
                      701.82,  #3 #8
                      702.603, #4 #9
                      703.499, #4 #10
                      703.961, #3 #11
                      723.136, #3 #12
                      725.633, #4 #13
                      734.133, #4 #14
                      734.945, #3 #15
                      783.411] #3 #16
        cls.out_1 = dom.get_states_mouse(cls.antennas,
                                         cls.times,
                                         cls.t_start,
                                         cls.t_end,
                                         cls.home_antenna_1,
                                         cls.dt)
        cls.out_2 = dom.get_states_mouse(cls.antennas,
                                         cls.times,
                                         cls.t_start,
                                         cls.t_end,
                                         cls.home_antenna_2,
                                         cls.dt)
        # for i, x in enumerate(cls.out_2):
        #     print(i, x)
    def test_same_length(self):
        self.assertEqual(len(self.out_1),
                         len(self.out_2))
    
    def test_different_results_for_different_home_antenna(self):
        for i, x in enumerate(self.out_1):
            if x != 1:
                self.assertNotEqual(x, self.out_2[i])

    def test_different_results_for_home_antenna_1(self):
        self.assertFalse(np.all(self.out_1 == self.out_1[0]))

    def test_different_results_for_home_antenna_2(self):
        self.assertFalse(np.all(self.out_2 == self.out_2[0]))

    def test_same_results_pipe(self):
        for i, x in enumerate(self.out_1):
            if x == 1:
                self.assertEqual(x, self.out_2[i])
                
    def test_different_home_for_home_antenna_1(self):
        self.assertTrue(np.any(self.out_1 == 0))

    def test_different_home_for_home_antenna_2(self):
        self.assertTrue(np.any(self.out_2 == 0))

    def test_threshold_1(self):
        timestamp_1 = int(round((self.times[9] - self.t_start)/self.dt))
        timestamp_2 = int(round((self.times[9] - self.t_start)/self.dt))
        self.assertTrue(np.all(self.out_1[timestamp_1:timestamp_2] == 1))

    def test_threshold_1(self):
        timestamp_1 = int(round((self.times[9] - self.t_start)/self.dt))
        timestamp_2 = int(round((self.times[9] - self.t_start)/self.dt))
        self.assertTrue(np.all(self.out_2[timestamp_1:timestamp_2] == 1))

if __name__ == '__main__':
    unittest.main()
