# https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/
from typing import Optional
import math


# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
		trav = head
		while trav and (follower := trav.next):
			gcd = math.gcd(trav.val, follower.val)
			trav.next = ListNode(gcd, follower)
			trav = follower
		return head
