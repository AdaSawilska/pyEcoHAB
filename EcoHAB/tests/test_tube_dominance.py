#!/usr/bin/env python
from __future__ import print_function, division, absolute_import
from EcoHAB import tube_dominance as tubed
import unittest

class TestGetMoreStates(unittest.TestCase):
    def test_catch_threshold_len_states(self):
        tubed.mouse_attention_span = 50
        antennas = [5, 6, 6, 5, 5, 6, 7, 6, 5, 5, 6, 6, 6, 7]
        times = [101.976,
                 103.148,
                 109.37,
                 109.761,
                 211.214,
                 211.98,
                 217.953,
                 218.61,
                 223.347,
                 223.769,
                 225.192,
                 225.942,
                 228.772,
                 228.972]
        idx = 0
        states, readouts, midx = tubed.get_more_states(antennas, times, idx)
        self.assertEqual(len(states), 4)
    def test_catch_threshold_equal_len_states_times(self):
        tubed.mouse_attention_span = 50
        antennas = [5, 6, 6, 5, 5, 6, 7, 6, 5, 5, 6, 6, 6, 7]
        times = [101.976,
                 103.148,
                 109.37,
                 109.761,
                 211.214,
                 211.98,
                 217.953,
                 218.61,
                 223.347,
                 223.769,
                 225.192,
                 225.942,
                 228.772,
                 228.972]
        idx = 0
        states, readouts, midx = tubed.get_more_states(antennas, times, idx)
        self.assertEqual(len(states), len(readouts))

    def test_catch_threshold_equal_len_midx(self):
        tubed.mouse_attention_span = 50
        antennas = [5, 6, 6, 5, 5, 6, 7, 6, 5, 5, 6, 6, 6, 7]
        times = [101.976,
                 103.148,
                 109.37,
                 109.761,
                 211.214,
                 211.98,
                 217.953,
                 218.61,
                 223.347,
                 223.769,
                 225.192,
                 225.942,
                 228.772,
                 228.972]
        idx = 0
        states, readouts, midx = tubed.get_more_states(antennas, times, idx)
        self.assertEqual(len(states), midx)
    
    def test_catch_3rd_len_states(self):
        tubed.mouse_attention_span = 50
        antennas = [5, 6, 6, 5, 5, 6, 7, 6, 5, 5, 6, 6, 6, 7]
        times = [101.976,
                 103.148,
                 109.37,
                 109.761,
                 111.214,
                 111.98,
                 117.953,
                 118.61,
                 123.347,
                 123.769,
                 125.192,
                 125.942,
                 128.772,
                 128.972]
        idx = 0
        states, readouts, midx = tubed.get_more_states(antennas, times, idx)
        self.assertEqual(len(states), 7)

    def test_catch_3rd_equal_len_states_times(self):
        tubed.mouse_attention_span = 50
        antennas = [5, 6, 6, 5, 5, 6, 7, 6, 5, 5, 6, 6, 6, 7]
        times = [101.976,
                 103.148,
                 109.37,
                 109.761,
                 111.214,
                 111.98,
                 117.953,
                 118.61,
                 123.347,
                 123.769,
                 125.192,
                 125.942,
                 128.772,
                 128.972]
        idx = 0
        states, readouts, midx = tubed.get_more_states(antennas, times, idx)
        self.assertEqual(len(states), len(readouts))

    def test_catch_3rd_equal_len_midx(self):
        tubed.mouse_attention_span = 50
        antennas = [5, 6, 6, 5, 5, 6, 7, 6, 5, 5, 6, 6, 6, 7]
        times = [101.976,
                 103.148,
                 109.37,
                 109.761,
                 111.214,
                 111.98,
                 117.953,
                 118.61,
                 123.347,
                 123.769,
                 125.192,
                 125.942,
                 128.772,
                 128.972]
        idx = 0
        states, readouts, midx = tubed.get_more_states(antennas, times, idx)
        self.assertEqual(len(states), midx)

    def test_catch_end(self):
        tubed.mouse_attention_span = 50
        antennas = [5, 6, 6, 5, 5, 6, 5, 6, 5, 5, 6, 6, 6, 5]
        times = [101.976,
                 103.148,
                 109.37,
                 109.761,
                 111.214,
                 111.98,
                 117.953,
                 118.61,
                 123.347,
                 123.769,
                 125.192,
                 125.942,
                 128.772,
                 128.972]
        idx = 0
        states, readouts, midx = tubed.get_more_states(antennas, times, idx)
        self.assertEqual(len(states), midx)

    def test_catch_equal_len_antennas_states(self):
        tubed.mouse_attention_span = 50
        antennas = [5, 6, 6, 5, 5, 6, 5, 6, 5, 5, 6, 6, 6, 5]
        times = [101.976,
                 103.148,
                 109.37,
                 109.761,
                 111.214,
                 111.98,
                 117.953,
                 118.61,
                 123.347,
                 123.769,
                 125.192,
                 125.942,
                 128.772,
                 128.972]
        idx = 0
        states, readouts, midx = tubed.get_more_states(antennas, times, idx)
        self.assertEqual(len(states), len(antennas))

    def test_catch_equal_len_antennas_readouts(self):
        tubed.mouse_attention_span = 50
        antennas = [5, 6, 6, 5, 5, 6, 5, 6, 5, 5, 6, 6, 6, 5]
        times = [101.976,
                 103.148,
                 109.37,
                 109.761,
                 111.214,
                 111.98,
                 117.953,
                 118.61,
                 123.347,
                 123.769,
                 125.192,
                 125.942,
                 128.772,
                 128.972]
        idx = 0
        states, readouts, midx = tubed.get_more_states(antennas, times, idx)
        self.assertEqual(len(states), len(readouts))

class TestCheckTwoMice(unittest.TestCase):
    def test_lab_pushing_mouse2_pushing_mouse1(self):
        m1_antennas = [5, 6, 5, 5, 5, 5, 5, 6, 6, 6, 7]
        m1_times  = [705.074,#5
                     708.091,#6
                     710.577,#5
                     744.813,#5
                     746.72,#5
                     758.851,#5
                     802.624,#5
                     808.095,#6
                     809.252,#6
                     809.564,#6
                     813.675]#7

       
        m2_antennas = [6, 6, 6, 6, 6, 5, 5, 5, 6, 5, 4, 4]
        m2_times =  [751.348,#6
                     753.771,#6
                     755.115,#6
                     755.865,#6
                     764.666,#6
                     768.856,#5
                     769.184,#5
                     794.072,#5
                     796.386,#6
                     801.342,#5
                     807.86,#4
                     814.3]#4
        out = tubed.does_mouse1_push_out(m1_antennas,
                                         m1_times,
                                         m2_antennas,
                                         m2_times)
        self.assertFalse(out)
    
    def test_lab_pushing_mouse1_pushing_mouse2(self):
        m2_antennas = [5, 6, 5, 5, 5, 5, 5, 6, 6, 6, 7]
        m2_times  = [705.074,#5
                     708.091,#6
                     710.577,#5
                     744.813,#5
                     746.72,#5
                     758.851,#5
                     802.624,#5
                     808.095,#6
                     809.252,#6
                     809.564,#6
                     813.675]#7

       
        m1_antennas = [6, 6, 6, 6, 6, 5, 5, 5, 6, 5, 4, 4]
        m1_times =  [751.348,#6
                     753.771,#6
                     755.115,#6
                     755.865,#6
                     764.666,#6
                     768.856,#5
                     769.184,#5
                     794.072,#5
                     796.386,#6
                     801.342,#5
                     807.86,#4
                     814.3]#4
        out = tubed.does_mouse1_push_out(m1_antennas,
                                         m1_times,
                                         m2_antennas,
                                         m2_times)
        self.assertTrue(out)
    
    def test_mouse_simple_pushing_mouse2(self):
        m1_antenna = [3, 4, 4, 5]
        m1_times = [938.187, 939.297, 940.297, 942.267]
        m2_antenna = [4, 4, 3]
        m2_times = [936.827, 941.892, 943.486]
        out = tubed.does_mouse1_push_out(m1_antenna,
                                         m1_times,
                                         m2_antenna,
                                         m2_times)
        
        self.assertTrue(out)

    def test_mouse1_mouse_2_different_directions(self):
       
        m1_antenna = [1, 2, 2, 1, 8]
        m1_times = [59.462, 60.447, 64.418, 64.934, 81.723]

        m2_antenna = [2, 3, 4, 5, 6, 7]
        m2_times = [57.727, 74.407, 74.922, 77.392, 79.628, 94.855]
        
        out = tubed.does_mouse1_push_out(m1_antenna,
                                         m1_times,
                                         m2_antenna,
                                         m2_times)
        self.assertFalse(out)

    def test_mouse_2_does_nothing(self):
        m1_antenna = [3, 4, 5]
        m1_times = [7.865, 8.287, 10.523]
        m2_antenna = [4, 5]
        m2_times = [5.677, 15.51]
        out = tubed.does_mouse1_push_out(m1_antenna,
                                         m1_times,
                                         m2_antenna,
                                         m2_times)
        self.assertFalse(out)

    def test_mice_in_different_parts_of_EcoHAB(self):
        m1_antenna = [3, 2, 1]
        m1_times = [7.865, 8.287, 10.523]
        m2_antenna = [4, 5]
        m2_times = [5.677, 15.51]
        out = tubed.does_mouse1_push_out(m1_antenna,
                                         m1_times,
                                         m2_antenna,
                                         m2_times)
        self.assertFalse(out)


if __name__ == '__main__':
    unittest.main()
