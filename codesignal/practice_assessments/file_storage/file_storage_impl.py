from typing import Optional

from file_storage import FileStorage


class FileStorageImpl(FileStorage):
	"""
	Implementation of the FileStorage interface.

	Students should implement all methods defined in the FileStorage base class.
	Implement one level at a time, keeping in mind that you will need to refactor
	to support additional functionality in later levels.
	"""

	def __init__(self):
		"""Initialize the file storage system."""
		# TODO: implement
		self.file_to_size = {}
		self.file_to_timestamp = {}

	# Level 1 Methods: Basic Operations

	def file_upload(self, file_name: str, size: str) -> str | RuntimeError:
		"""Upload a file to the storage server."""
		# TODO: implement
		if file_name in self.file_to_size:
			return RuntimeError("File already exists")

		self.file_to_size[file_name] = size

		return f"uploaded {file_name}"

	def file_get(self, file_name: str) -> str | None:
		"""Get information about a file from storage."""
		# TODO: implement
		if file_name in self.file_to_size:
			return f"got {file_name}"

		return None

	def file_copy(self, source: str, dest: str) -> str | RuntimeError:
		"""Copy a file to a new location."""
		# TODO: implement
		if source not in self.file_to_size:
			return RuntimeError("Source file not exists")

		self.file_to_size[dest] = self.file_to_size[source]

		return f"copied {source} to {dest}"

	# Level 2 Methods: Search and Query

	def file_search(self, prefix: str) -> str:
		"""Search for files by prefix, sorted by size in descending order."""
		# TODO: implement
		matched_files = []

		for file_name, size in self.file_to_size.items():
			if file_name.startswith(prefix):
				matched_files.append((file_name, size))

		# sort by size descending and then name ascending
		matched_files.sort(key=lambda x: (-int(x[1][:-2]), x[0]))

		return_str = "found ["
		return_str += ", ".join([file_name for file_name, size in matched_files])

		return_str += "]"

		return return_str

	# Level 3 Methods: Time-Aware Operations with TTL

	def file_upload_at(self, timestamp: str, file_name: str, size: str, ttl: Optional[int] = None) -> str:
		"""Upload a file at a specific timestamp with optional TTL."""
		# TODO: implement

		try:
			self.file_upload(file_name, size)
		except RuntimeError as e:
			return str(e)

		# no ttl -> infinite
		if ttl:
			self.file_to_timestamp[file_name] = (timestamp, ttl)

		return f"uploaded at {file_name}"

	def file_get_at(self, timestamp: str, file_name: str) -> str:
		"""Get information about a file at a specific timestamp."""
		# TODO: implement
		res = self.file_get(file_name)
		# if the requested timestamp is after the file's ttl expiration, return None
		if res is None:
			return None

		if file_name in self.file_to_timestamp:
			upload_time, ttl = self.file_to_timestamp[file_name]

			# check if the file is expired
			from datetime import datetime, timedelta

			upload_dt = datetime.fromisoformat(upload_time)
			request_dt = datetime.fromisoformat(timestamp)
			if request_dt > upload_dt + timedelta(seconds=ttl):
				return None

		return f"got at {file_name}"

	def file_copy_at(self, timestamp: str, source: str, dest: str) -> str:
		"""Copy a file at a specific timestamp."""
		# TODO: implement
		pass

	def file_search_at(self, timestamp: str, prefix: str) -> str:
		"""Search for files by prefix at a specific timestamp."""
		# TODO: implement
		pass

	# Level 4 Methods: Rollback

	def rollback(self, timestamp: str) -> str:
		"""Rollback the storage state to a specific timestamp."""
		# TODO: implement
		pass
