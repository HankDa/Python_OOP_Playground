from typing import List

car_size = {"Small":0, "Medium":1, "Large":2}

class Car:
    def __init__(self,size= "nan", color="nan", brand="nan") -> None:
        self._size:str = size
        self._color:str = color
        self._brand:str = brand
    @property
    def size(self):
        return self._size
    def display_info(self):
        return f"{self._size} {self._color} {self._brand}"
class ParkingSpot:
    def __init__(self,size:str,car = None) -> None:
        self._size = size
        self._parkedCar: Car = car
    @property
    def parked(self)->bool:
        if self._parkedCar:
            return True
        return False
    @property
    def size(self)->str:
        return self._size
    def park(self,car:Car) -> bool:
        if self.parked or car_size[self.size] < car_size[car.size]:
            return False
        self._parkedCar = car
        return True
    def leave(self)->bool:
        if self._parkedCar:
            self._parkedCar = None
            return True
        return False
    def display_info(self)->str:
        if self._parkedCar:
            return self._parkedCar.display_info()
        return "Empty"
        
class ParkingLot:
    def __init__(self,spots_size:list[str]) -> None:
        # Note: [ParkingSpot()]*n -> which will shallow copy the object to all the element in the list.
        self._spots: list[ParkingSpot] = [ParkingSpot(size) for size in spots_size]
        self._size= len(spots_size)
        self._free_spots= self._size
    @property
    def spots(self):
        return self._spots
    @property
    def size(self):
        return self._size
    def park(self, spot, car):
        for i in range(spot, self.size):
            if self.spots[i].park(car):
                self._free_spots -= 1
                return True
        for i in range(spot):
            if self.spots[i].park(car):
                self._free_spots -= 1
                return True
        return False

    def display_spot(self,spot) -> str:
        if self.spots[spot]:
            return self.spots[spot].display_info()
        return "Empty"
    def print_free_spots(self) -> str:
        # free_spot = [str(i) for i in range(self.size) if not self.spots[i].parked]
        # note: filter return the element that is true statment. 
        # free_spot = filter(lambda spot: not spot.parked,self.spots)
        return self._free_spots
        
def parking_system(spots: List[str], instructions: List[List[str]]) -> List[str]:
    parkingLot = ParkingLot(spots)
    res = []
    for instruction in instructions:
        fun_call, *args = instruction
        if fun_call == "park": 
            spot ,*car = args
            parkingLot.park(int(spot), Car(*car))
        elif fun_call == "print":
            # TODO: implement print function  
            res.append(parkingLot.display_spot(int(args[0])))
        elif fun_call == "print_free_spots":
            res.append(parkingLot.print_free_spots())
    return res

if __name__ == '__main__':
    spots = ["Small","Medium","Large","Small","Medium","Large"]
    instructions = [
    ["park", "2", "Medium", "Red", "Ford"],
    ["park", "2", "Large", "Green", "Honda"],
    ["print_free_spots"],
    ["print", "2"],
    ["print", "3"],
    ["park", "2", "Small", "Red", "Tesla"],
    ["print", "2"],
    ["print", "3"],
    ["park", "3", "Small", "Red", "Tesla"],
    ["print", "5"],
    ["print_free_spots"],
    ["park", "3", "Large", "Black", "Ferrari"],
    ["print_free_spots"]
    ]

    res = parking_system(spots, instructions)
    for line in res:
        print(line)
