# https://leetcode.com/problems/maximum-population-year/

from typing import List
from collections import defaultdict, Counter
from itertools import groupby


def maximumPopulation(logs: List[List[int]]) -> int:
    # Sort the logs according to the birth date
    logs_s = sorted(logs)
    # Keep track of count for each person for birth year (as answer is going to be among birthdate only)
    birth_year_population = defaultdict(int)
    # first person
    birth_year_population[logs_s[0][0]] = 1
    # logs_check[0] = 1  # first person is the first era so 1
    for i in range(1, len(logs_s)):
        birth_year_prev, death_year_prev = logs_s[i-1]
        birth_year_curr, _ = logs_s[i]
        birth_year_population[birth_year_curr] += 1
        if birth_year_curr > birth_year_prev and birth_year_curr < death_year_prev:
            # Curr Person is in same era as prev Person
            birth_year_population[birth_year_curr] += 1
        if birth_year_curr == birth_year_prev:
            continue
        if (birth_year_population[birth_year_curr] > 1 or birth_year_population[birth_year_prev] > 1):
            # Current Person same prev Person Era
            j = i-2
            while j > 0:
                b_j, d_j = logs_s[j]
                if birth_year_curr >= d_j:
                    if birth_year_population[b_j] == 1:
                        break
                else:
                    # person belongs to earlier j's person era
                    birth_year_population[birth_year_curr] += 1
                if birth_year_population[b_j] > 1 or birth_year_population[logs_s[j-1][0]] > 1:
                    j -= 1
                else:
                    break
            else:
                if j == 0 and (birth_year_curr <= logs_s[0][1]):
                    birth_year_population[birth_year_curr] += 1
    for i, _ in logs_s:
        print(f'{i} : {birth_year_population[i]}', end=', ')
    return max(logs_s, key=lambda x: birth_year_population[x[0]])[0]


def maxPopulation(logs: List[List[int]]) -> int:
    arr = [0]*101
    for birth, death in logs:
        for b in range(birth, death):
            arr[b-1950] += 1
    return max(enumerate(arr), key=lambda x: x[1])[0]+1950


def maxPopulation2(logs: List[List[int]]) -> int:
    population = defaultdict(int)
    for b, d in logs:
        population[b] += 1  # birth in particular year b
        population[d] -= 1  # death in particular year d
    years = sorted(population.keys())  # all years
    # only birth years (as answer will only among birth years)
    birth_population = []
    earlierPopulation = 0  # population before present year
    for year in years:
        current_year_population = population[year]
        total_cnt = earlierPopulation + current_year_population
        if current_year_population > 0:
            # Birth Year
            birth_population.append(
                (total_cnt, year))
        earlierPopulation = total_cnt
    return max(birth_population, key=lambda x: x[0])[1]


def maxPopulation3(self, logs: List[List[int]]) -> int:
    populationCounter = Counter(
        year for yearStart, yearEnd in logs for year in range(yearStart, yearEnd))

    _, maxYear = max((pop, -year)
                     for year, pop in populationCounter.items())
    return -maxYear


    # Ans -> 1993
logs = [[1993, 1999], [2000, 2010]]
#assert maximumPopulation(logs) == 1993
print(maxPopulation2(logs))

# Ans -> 1960
logs = [[1950, 1961], [1960, 1971], [1970, 1981]]
#assert maximumPopulation(logs) == 1960
print(maxPopulation2(logs))

# Ans -> 2022
logs = [[1982, 1998], [2013, 2042], [2010, 2035], [2022, 2050], [2047, 2048]]
#assert maximumPopulation(logs) == 2022
print(maxPopulation2(logs))

# Ans -> 2005
logs = [[2033, 2034], [2039, 2047], [1998, 2042], [2047, 2048], [
    2025, 2029], [2005, 2044], [1990, 1992], [1952, 1956], [1984, 2014]]
#assert maximumPopulation(logs) == 2005
print(maxPopulation2(logs))

# Ans -> 1983
logs = [[1982, 2048], [1968, 1973], [2010, 2018], [2003, 2016], [1952, 2003], [
    1953, 1993], [1983, 1997], [1976, 2032], [1952, 1981], [1999, 2021]]
#assert maximumPopulation(logs) == 1983
print(maxPopulation2(logs))

# Ans -> 1991
logs = [[1966, 1968], [1954, 2030], [1966, 1994], [2030, 2044], [1988, 2036], [1977, 2050], [2036, 2046], [1989, 2048], [
    2049, 2050], [2008, 2019], [2022, 2031], [1970, 2024], [1957, 1996], [1991, 2034], [1956, 1996], [1959, 1969], [2021, 2050]]
#assert maximumPopulation(logs) == 1991
print(maxPopulation2(logs))

# Ans -> 1998
logs = [[2026, 2043], [1980, 2043], [1955, 2008], [1967, 2042], [1964, 2002], [2020, 2045], [2023, 2041], [1968, 1985], [1984, 2031], [
    1959, 2008], [1993, 2001], [1977, 2012], [2047, 2049], [1993, 2015], [1998, 2003], [2028, 2047], [1982, 2030], [1978, 1989], [1963, 2005]]
#assert maximumPopulation(logs) == 1998
print(maxPopulation2(logs))

# ans = maximumPopulation(logs)
# print()
# print(ans)
