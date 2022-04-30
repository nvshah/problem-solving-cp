# https://leetcode.com/problems/seat-reservation-manager/
import heapq

'''
2 Ways to implement 
1) Min-Heap
2) TreeSet

'''

class SeatManager:
    '''min-Heap Impl'''

    def __init__(self, n: int):
        # minHeap := {unreservedSeats}
        self.unreservedSeats = [i for i in range(1,n+1)]   # Initially all seats are not reserved 

        # No Heapify is reequired :- as the {unreservedSeats} is in sorted order already
        # arr is already followig min-heap-invariant

    def reserve(self) -> int:
        # take sit from {unreservedSeats}
        return heapq.heappop(self.unreservedSeats)
        

    def unreserve(self, seatNumber: int) -> None:
        # Free-Up Reserved sit :- {seatNumber}
        heapq.heappush(self.unreservedSeats, seatNumber)