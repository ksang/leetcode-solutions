class Solution(object):
	def findItinerary(self, tickets):
		"""
		:type tickets: List[List[str]]
		:rtype: List[str]
		"""
		flights = {}
		for t in tickets:
			if flights.has_key(t[0]):
				flights[t[0]].append(t[1])
			else:
				flights[t[0]] = [t[1]]
		for f in flights.keys():
			flights[f] = sorted(flights[f])[::-1]
		res, march = [], ["JFK"]
		print flights
		while march:
			while flights.has_key(march[-1]) and flights[march[-1]]:
				march.append(flights[march[-1]].pop())
			res.append(march.pop())
		return res[::-1]


if __name__ == '__main__':
	tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
	print Solution().findItinerary(tickets)