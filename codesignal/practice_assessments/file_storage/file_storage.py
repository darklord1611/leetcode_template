"""
File Storage - Abstract Base Class

A simplified file hosting service. The set of operations is intentionally small:
later levels extend the BEHAVIOUR of the same functions rather than adding many
new ones. Implement one level at a time and expect to reopen earlier functions.
"""


class FileStorage:
	"""Abstract base class for the file storage system."""

	def __init__(self):
		"""Initialize the file storage system."""
		raise NotImplementedError("Subclasses must implement __init__")

	# Level 1 Methods: Basic Storage

	def file_upload(self, timestamp: int, file_name: str, size: int) -> str:
		"""
		Upload a file with the given size (an integer).

		Returns:
		    str: "true" if uploaded, or "" if a live file with that name
		         already exists (no overwrite).
		"""
		raise NotImplementedError("Subclasses must implement file_upload()")

	def file_get(self, timestamp: int, file_name: str) -> str:
		"""
		Get the size of a file.

		Returns:
		    str: The file's size as a string, or "" if it does not exist
		         (or is expired at this timestamp).
		"""
		raise NotImplementedError("Subclasses must implement file_get()")

	def file_copy(self, timestamp: int, source: str, dest: str) -> str:
		"""
		Copy a file, overwriting dest if it already exists.

		Returns:
		    str: "true" on success, or "" if the source does not exist
		         (or is expired at this timestamp).
		"""
		raise NotImplementedError("Subclasses must implement file_copy()")

	# Level 2 Methods: Search
	# (Read-only query over the files stored by Level 1.)

	def file_search(self, timestamp: int, prefix: str) -> str:
		"""
		Find files whose name starts with prefix.

		Returns:
		    str: Up to the top 10 names, ordered by size desc then name asc,
		         joined by ", ", or "" if none match.
		"""
		raise NotImplementedError("Subclasses must implement file_search()")

	# Level 3 Methods: TTL
	# (file_upload, file_get, file_copy, and file_search must be reopened to
	#  respect time-to-live and ignore expired files.)

	def file_upload_with_ttl(self, timestamp: int, file_name: str, size: int, ttl: int) -> str:
		"""
		Upload a file that is alive for [timestamp, timestamp + ttl).

		Returns:
		    str: "true" if uploaded, or "" if a live file with that name
		         already exists.
		"""
		raise NotImplementedError("Subclasses must implement file_upload_with_ttl()")

	# Level 4 Methods: Rollback
	# (The read operations must reflect the rolled-back state.)

	def rollback(self, timestamp: int, rollback_to: int) -> str:
		"""
		Restore the entire store to its exact state as of time rollback_to,
		recalculating TTLs so each surviving file keeps its remaining lifetime
		measured from rollback_to.

		Returns:
		    str: "true".
		"""
		raise NotImplementedError("Subclasses must implement rollback()")
