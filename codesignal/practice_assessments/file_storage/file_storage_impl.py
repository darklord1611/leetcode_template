from file_storage import FileStorage


class FileStorageImpl(FileStorage):
	"""
	Implementation of the FileStorage interface.

	The function set is small on purpose. Implement one level at a time and
	expect to reopen earlier functions to satisfy later requirements.
	"""

	def __init__(self):
		"""Initialize the file storage system."""
		# TODO: implement
		pass

	# Level 1 Methods: Basic Storage

	def file_upload(self, timestamp: int, file_name: str, size: int) -> str:
		"""Upload a file with the given size."""
		# TODO: implement
		pass

	def file_get(self, timestamp: int, file_name: str) -> str:
		"""Get the size of a file."""
		# TODO: implement
		pass

	def file_copy(self, timestamp: int, source: str, dest: str) -> str:
		"""Copy a file, overwriting dest if it already exists."""
		# TODO: implement
		pass

	# Level 2 Methods: Search

	def file_search(self, timestamp: int, prefix: str) -> str:
		"""Find files whose name starts with prefix."""
		# TODO: implement
		pass

	# Level 3 Methods: TTL

	def file_upload_with_ttl(self, timestamp: int, file_name: str, size: int, ttl: int) -> str:
		"""Upload a file that is alive for [timestamp, timestamp + ttl)."""
		# TODO: implement
		pass

	# Level 4 Methods: Rollback

	def rollback(self, timestamp: int, rollback_to: int) -> str:
		"""Restore the store to its exact state as of time rollback_to."""
		# TODO: implement
		pass
