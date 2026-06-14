"""
DNS Resolver - Abstract Base Class

This class defines the interface for a simplified DNS resolver that maps
domain names to IP addresses, with CNAME aliases, round-robin, TTL,
wildcard records, reverse lookups, and weighted load balancing.
"""


class DnsResolver:
	"""
	Abstract base class for a DNS resolver.

	All timestamps are integers and are non-decreasing across calls.
	Domain names and IP addresses are strings.
	"""

	def __init__(self):
		"""Initialize the DNS resolver."""
		raise NotImplementedError("Subclasses must implement __init__")

	# Level 1 Methods: A Records

	def add_record(self, timestamp: int, domain: str, ip: str) -> str:
		"""
		Register an A record mapping domain to ip (duplicates ignored).

		Returns:
		    str: "true".
		"""
		raise NotImplementedError("Subclasses must implement add_record()")

	def resolve(self, timestamp: int, domain: str) -> str:
		"""
		Resolve domain to an IP address.

		Returns:
		    str: An IP address, or "" if the domain cannot be resolved.
		"""
		raise NotImplementedError("Subclasses must implement resolve()")

	def remove_record(self, timestamp: int, domain: str) -> str:
		"""
		Remove all records for domain.

		Returns:
		    str: "true" if any record existed, otherwise "false".
		"""
		raise NotImplementedError("Subclasses must implement remove_record()")

	# Level 2 Methods: CNAME Aliases

	def add_alias(self, timestamp: int, alias: str, target: str) -> str:
		"""
		Create a CNAME record making alias point to target.

		Returns:
		    str: "true", or "false" if alias already has an A record.
		"""
		raise NotImplementedError("Subclasses must implement add_alias()")

	# Level 3 Methods: Multiple IPs & Round-Robin

	def remove_ip(self, timestamp: int, domain: str, ip: str) -> str:
		"""
		Remove a single ip from domain's A records.

		Returns:
		    str: "true" if it existed, otherwise "false".
		"""
		raise NotImplementedError("Subclasses must implement remove_ip()")

	# Level 4 Methods: Record TTL & Expiration

	def add_record_with_ttl(self, timestamp: int, domain: str, ip: str, ttl: int) -> str:
		"""
		Add an A record valid for [timestamp, timestamp + ttl).

		Returns:
		    str: "true".
		"""
		raise NotImplementedError("Subclasses must implement add_record_with_ttl()")

	# Level 5: Wildcard records are supported through add_record / resolve
	# (no new methods are introduced at this level).

	# Level 6 Methods: Reverse DNS

	def reverse_resolve(self, timestamp: int, ip: str) -> str:
		"""
		Return all (non-expired, non-wildcard) domains with an A record for ip.

		Returns:
		    str: Comma-separated, lexicographically sorted domains, or "".
		"""
		raise NotImplementedError("Subclasses must implement reverse_resolve()")

	# Level 7 Methods: Weighted Load Balancing & Analytics

	def add_record_with_weight(self, timestamp: int, domain: str, ip: str, weight: int) -> str:
		"""
		Add (or update) an A record domain -> ip with the given weight (>= 1).

		Returns:
		    str: "true".
		"""
		raise NotImplementedError("Subclasses must implement add_record_with_weight()")

	def get_resolution_stats(self, timestamp: int, domain: str) -> str:
		"""
		Return how many times each IP has been returned by resolve for domain.

		Returns:
		    str: Comma-separated "ip:count" entries sorted by ip,
		         or "" if domain has never been resolved.
		"""
		raise NotImplementedError("Subclasses must implement get_resolution_stats()")

	def top_domains(self, timestamp: int, n: int) -> str:
		"""
		Return up to n domains with the most resolve calls so far.

		Returns:
		    str: Comma-separated domains (ties broken lexicographically),
		         or "" if there have been no resolutions.
		"""
		raise NotImplementedError("Subclasses must implement top_domains()")
