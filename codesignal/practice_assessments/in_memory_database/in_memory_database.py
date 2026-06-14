"""
In-Memory Database - Abstract Base Class

A simplified in-memory key-value database with field-level granularity. The set
of operations is intentionally small: later levels extend the BEHAVIOUR of the
same functions rather than adding many new ones. Implement one level at a time
and expect to reopen earlier functions.
"""


class InMemoryDatabase:
	"""Abstract base class for the in-memory database."""

	def __init__(self):
		"""Initialize the in-memory database."""
		raise NotImplementedError("Subclasses must implement __init__")

	# Level 1 Methods: Field Operations

	def set_field(self, timestamp: int, key: str, field: str, value: str) -> str:
		"""
		Set a field's value for a key, creating the record if needed.

		Returns:
		    str: "true".
		"""
		raise NotImplementedError("Subclasses must implement set_field()")

	def get_field(self, timestamp: int, key: str, field: str) -> str:
		"""
		Get a field's value for a key.

		Returns:
		    str: The value, or "" if the key or field is absent.
		"""
		raise NotImplementedError("Subclasses must implement get_field()")

	def delete_field(self, timestamp: int, key: str, field: str) -> str:
		"""
		Delete a field from a key.

		Returns:
		    str: "true" if the field existed and was removed, otherwise "false".
		"""
		raise NotImplementedError("Subclasses must implement delete_field()")

	def get_record(self, timestamp: int, key: str) -> str:
		"""
		Get a key's record as "field=value" pairs sorted by field name asc.

		Returns:
		    str: ", "-joined pairs, or "" if the key has no live fields.
		"""
		raise NotImplementedError("Subclasses must implement get_record()")

	# Level 2 Methods: Scans & Ranking
	# (Read-only queries over the records built by the Level 1 functions.)

	def scan_prefix(self, timestamp: int, key: str, prefix: str) -> str:
		"""
		Get a key's "field=value" pairs whose field name starts with prefix.

		Returns:
		    str: ", "-joined pairs sorted by field name asc, or "" if none.
		"""
		raise NotImplementedError("Subclasses must implement scan_prefix()")

	def top_n_keys(self, timestamp: int, n: int) -> str:
		"""
		Get the top n keys by number of live fields.

		Returns:
		    str: "key(count)" pairs (desc by count, ties by key asc), ", "-joined,
		         or "" if there are no keys.
		"""
		raise NotImplementedError("Subclasses must implement top_n_keys()")

	# Level 3 Methods: TTL
	# (set_field, get_field, delete_field, get_record, scan_prefix and
	#  top_n_keys must all be reopened to ignore fields expired at the query time.)

	def set_field_with_ttl(self, timestamp: int, key: str, field: str, value: str, ttl: int) -> str:
		"""
		Set a field that is valid for [timestamp, timestamp + ttl).

		Returns:
		    str: "true".
		"""
		raise NotImplementedError("Subclasses must implement set_field_with_ttl()")

	# Level 4 Methods: Backup & Restore
	# (The read functions must be reopened to reflect the restored state.)

	def backup(self, timestamp: int) -> str:
		"""
		Snapshot the database, recording each ttl-field's remaining ttl.

		Returns:
		    str: The number of keys with at least one live field.
		"""
		raise NotImplementedError("Subclasses must implement backup()")

	def restore(self, timestamp: int, backup_timestamp: int) -> str:
		"""
		Restore the most recent backup whose time is <= backup_timestamp.

		Returns:
		    str: "true".
		"""
		raise NotImplementedError("Subclasses must implement restore()")
