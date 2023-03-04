from typing import List
class Car:
    size = {"Small":0, "Medium":1, "Large":2}
    def __init__(self,size= "nan", color="nan", brand="nan") -> None:
        self._size:str = size
        self._color:str = color
        self._brand:str = brand
    def display_info(self):
        return f"{self._size} {self._color} {self._brand}"
class ParkingSpot:
    def __init__(self) -> None:
        self._parkedCar: Car = None
    @property
    def parked(self)->bool:
        if self._parkedCar:
            return True
        return False
    def park(self,car:Car) -> bool:
        if self._parkedCar:
            return False
        self._parkedCar = car
        return True
    def leave(self):
        if self._parkedCar:
            self._parkedCar = None
            return True
        return False
    def display_info(self):
        if self._parkedCar:
            return self._parkedCar.display_info()
        return "Empty"
        
class ParkingLot:
    def __init__(self,n) -> None:
        # Note: [ParkingSpot()]*n -> which will shallow copy the object to all the element in the list.
        self._spots: list[ParkingSpot] = [ParkingSpot() for _ in range(n)]
        self._size= n
        self._free_spot= n
    @property
    def spots(self):
        return self._spots
    @property
    def size(self):
        return self._size
    def park(self, spot, car):
        while spot < self._size and self.spots[spot].parked:
            spot += 1
        if spot == self._size: 
            return False
        self.spots[spot].park(car)
        return True
    def display_spot(self,spot) -> str:
        if self.spots[spot]:
            return self.spots[spot].display_info()
        return "Empty"
    def print_free_spots(self) -> str:
        free_spot = [str(i) for i in range(self.size) if not self.spots[i].parked]
        return ",".join(free_spot)
        
def parking_system(n: int, instructions: List[List[str]]) -> List[str]:
    parkingLot = ParkingLot(n)
    res = []
    for instruction in instructions:
        fun_call = instruction[0]
        if fun_call == "park": 
            spot = int(instruction[1])
            parkingLot.park(spot, Car(*instruction[2::]))
        elif fun_call == "print":
            # TODO: implement print function  
            spot = int(instruction[1])
            res.append(parkingLot.display_spot(spot))
        elif fun_call == "print_free_spots":
            res.append(parkingLot.print_free_spots())
    return res

if __name__ == '__main__':
    n = 5
    instructions = [
    ["park", "1", "Small", "Silver", "BMW"],
    ["park", "1", "Large", "Black", "Nissan"],
    ["print", "1"],
    ["print", "2"],
    ["print", "3"],
    ["print_free_spots"]
    ]

    res = parking_system(n, instructions)
    for line in res:
        print(line)
