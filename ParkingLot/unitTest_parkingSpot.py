import unittest
from parkingSpots import *


class MyTest(unittest.TestCase):

    def setUp(self):
        self.car1 = Car("Small", "Black", "BMW")
        self.car2 = Car("Medium", "Black", "BMW")
        self.parkingSpot1 = ParkingSpot("Small")
        self.parkingSpot2 = ParkingSpot("Medium")
        self.spots_size = ["Small","Medium","Large","Small","Medium","Large"]
        self.parkLot_size = len(self.spots_size)
        self.parkingLot = ParkingLot(self.spots_size)
    
    '''Car Testing'''
    def test_car_display_info(self):
        self.assertEqual(self.car1.display_info(), "Small Black BMW")

    '''Parking Spot Testing'''
    def test_parkingSpot_park(self):
        # car size greater than spot size: Expected False
        self.assertFalse(self.parkingSpot1.park(self.car2))
        # car size smaller than spot size: Expected True
        self.assertTrue(self.parkingSpot2.park(self.car1))
        # Spot already parked: Expected False
        self.parkingSpot1.park(self.car1)
        self.assertFalse(self.parkingSpot1.park(self.car1))

    def test_parkingSpot_leave(self):
        self.parkingSpot1.park(self.car1)
        self.assertTrue(self.parkingSpot1.leave())
        self.assertTrue(not self.parkingSpot1.leave())
    def test_car_display_info(self):
        self.parkingSpot1.park(self.car1)
        self.assertEqual(self.parkingSpot1.display_info(), "Small Black BMW")
        self.parkingSpot1.leave()
        self.assertEqual(self.parkingSpot1.display_info(), "Empty")

    '''Parking Lot Testing'''
    def test_parkingLot_spot(self):
        self.assertEqual(len(self.parkingLot.spots),self.parkLot_size)
        self.assertIsInstance(self.parkingLot.spots[0],ParkingSpot)
    def test_parkingLot_park(self):
        for _ in range(self.parkLot_size):
            self.assertTrue(self.parkingLot.park(0,self.car1))
        self.assertTrue(not self.parkingLot.park(0,self.car1))
    def test_parkingLot_display_spot(self):
        self.parkingLot.park(0,self.car1)
        self.assertEqual(self.parkingLot.display_spot(0), "Small Black BMW")
        self.assertEqual(self.parkingLot.display_spot(1), "Empty")
    def test_parkingLot_print_free_spots(self):
        self.assertEqual(self.parkingLot.print_free_spots(), self.parkLot_size)
        self.parkingLot.park(0,self.car1)
        self.assertEqual(self.parkingLot.print_free_spots(), self.parkLot_size-1)
        self.parkingLot.park(0,self.car1)
        self.assertEqual(self.parkingLot.print_free_spots(), self.parkLot_size-2)

    
    
    
if __name__ == '__main__':
    unittest.main()