# LeetCode Daily Challenge (2025-09-21)
# Title: Design Movie Rental System
# Difficulty: Hard
# URL: https://leetcode.com/problems/design-movie-rental-system/
#
# You have a movie renting company consisting of n shops. You want to implement a renting system that supports searching for, booking, and returning movies. The system should also support generating a report of the currently rented movies.
#
# Each movie is given as a 2D integer array entries where entries[i] = [shopi, moviei, pricei] indicates that there is a copy of movie moviei at shop shopi with a rental price of pricei. Each shop carries at most one copy of a movie moviei.
#
# The system should support the following functions:
#
#
# 	Search: Finds the cheapest 5 shops that have an unrented copy of a given movie. The shops should be sorted by price in ascending order, and in case of a tie, the one with the smaller shopi should appear first. If there are less than 5 matching shops, then all of them should be returned. If no shop has an unrented copy, then an empty list should be returned.
# 	Rent: Rents an unrented copy of a given movie from a given shop.
# 	Drop: Drops off a previously rented copy of a given movie at a given shop.
# 	Report: Returns the cheapest 5 rented movies (possibly of the same movie ID) as a 2D list res where res[j] = [shopj, moviej] describes that the jth cheapest rented movie moviej was rented from the shop shopj. The movies in res should be sorted by price in ascending order, and in case of a tie, the one with the smaller shopj should appear first, and if there is still tie, the one with the smaller moviej should appear first. If there are fewer than 5 rented movies, then all of them should be returned. If no movies are currently being rented, then an empty list should be returned.
#
#
# Implement the MovieRentingSystem class:
#
#
# 	MovieRentingSystem(int n, int[][] entries) Initializes the MovieRentingSystem object with n shops and the movies in entries.
# 	List&lt;Integer&gt; search(int movie) Returns a list of shops that have an unrented copy of the given movie as described above.
# 	void rent(int shop, int movie) Rents the given movie from the given shop.
# 	void drop(int shop, int movie) Drops off a previously rented movie at the given shop.
# 	List&lt;List&lt;Integer&gt;&gt; report() Returns a list of cheapest rented movies as described above.
#
#
# Note: The test cases will be generated such that rent will only be called if the shop has an unrented copy of the movie, and drop will only be called if the shop had previously rented out the movie.
#
#


# Your solution starts here
from collections import defaultdict
from typing import List

from sortedcontainers import SortedSet


class MovieRentingSystem:
	def __init__(self, n: int, entries: List[List[int]]):  # O(nlogn)
		# we need to keep track of unrented copies for a specific movie, sorted by price ascending and then also shop_id ascending

		# we also need to keep track of rented movies for the report, sorted according to the order (price, movie_id, shop_id)

		# also maintain a lookup of (movie, shop) -> price
		self.movie_shop_to_price = defaultdict(int)
		self.rented_movies = SortedSet()
		self.movie_to_price_shop = defaultdict(SortedSet)

		for entry in entries:
			shop, movie, price = entry

			self.movie_shop_to_price[(shop, movie)] = price
			self.movie_to_price_shop[movie].add((price, shop))

	def search(self, movie: int) -> List[int]:
		top_5 = []
		for price, shop in self.movie_to_price_shop[movie]:
			top_5.append(shop)

			if len(top_5) == 5:
				break
		return top_5

	def rent(self, shop: int, movie: int) -> None:  # O(logn)
		price = self.movie_shop_to_price[(shop, movie)]
		self.movie_to_price_shop[movie].discard((price, shop))
		self.rented_movies.add((price, shop, movie))

	def drop(self, shop: int, movie: int) -> None:  # O(logn)
		price = self.movie_shop_to_price[(shop, movie)]
		self.movie_to_price_shop[movie].add((price, shop))
		self.rented_movies.discard((price, shop, movie))

	def report(self) -> List[List[int]]:
		top_rented = []

		for _, shop, movie in self.rented_movies:
			top_rented.append([shop, movie])
			if len(top_rented) == 5:
				break

		return top_rented


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()
