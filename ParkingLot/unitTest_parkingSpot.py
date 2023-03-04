import unittest
from parkingSpots import *


class MyTest(unittest.TestCase):

    def setUp(self):
        self.car1 = Car("Small", "Black", "BMW")
        self.parkingSpot = ParkingSpot()
        self.parkLot_size = 10
        self.parkingLot = ParkingLot(self.parkLot_size)
    
    '''Car Testing'''
    def test_car_display_info(self):
        self.assertEqual(self.car1.display_info(), "Small Black BMW")

    '''Parking Spot Testing'''
    def test_parkingSpot_park(self):
        self.assertTrue(self.parkingSpot.park(self.car1))
        self.assertTrue(not self.parkingSpot.park(self.car1))
    def test_parkingSpot_leave(self):
        self.parkingSpot.park(self.car1)
        self.assertTrue(self.parkingSpot.leave())
        self.assertTrue(not self.parkingSpot.leave())
    def test_car_display_info(self):
        self.parkingSpot.park(self.car1)
        self.assertEqual(self.parkingSpot.display_info(), "Small Black BMW")
        self.parkingSpot.leave()
        self.assertEqual(self.parkingSpot.display_info(), "Empty")

    '''Parking Lot Testing'''
    def test_parkingLot_spot(self):
        self.assertAlmostEquals(len(self.parkingLot.spots),self.parkLot_size)
        self.assertIsInstance(self.parkingLot.spots[0],ParkingSpot)
    def test_parkingLot_park(self):
        for _ in range(self.parkLot_size):
            self.assertTrue(self.parkingLot.park(0,self.car1))
        self.assertTrue(not self.parkingLot.park(0,self.car1))
    def test_parkingLot_display_spot(self):
        self.parkingLot.park(0,self.car1)
        self.assertEqual(self.parkingLot.display_spot(0), "Small Black BMW")
        self.assertEqual(self.parkingLot.display_spot(1), "Empty")
    def test_parkingLot_display_spot(self):
        self.assertEqual(self.parkingLot.print_free_spots(), "0,1,2,3,4,5,6,7,8,9")
        self.parkingLot.park(0,self.car1)
        self.assertEqual(self.parkingLot.print_free_spots(), "1,2,3,4,5,6,7,8,9")
    
if __name__ == '__main__':
    unittest.main()