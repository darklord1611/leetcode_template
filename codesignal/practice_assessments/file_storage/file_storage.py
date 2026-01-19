"""
File Storage - Abstract Base Class

This class defines the interface for a simplified file hosting service
that supports file operations, search, TTL (time-to-live), and rollback functionality.
"""
from typing import Optional


class FileStorage:
    """
    Abstract base class for a file hosting service that stores files
    with support for basic operations, time-aware operations with TTL,
    and state rollback.
    """

    def __init__(self):
        """Initialize the file storage system."""
        raise NotImplementedError("Subclasses must implement __init__")

    # Level 1 Methods: Basic Operations

    def file_upload(self, file_name: str, size: str) -> str:
        """
        Upload a file to the storage server.

        Args:
            file_name (str): Name of the file to upload
            size (str): Size of the file (e.g., "200kb")

        Returns:
            str: Result message in format "uploaded {file_name}"

        Raises:
            RuntimeError: If a file with the same name already exists
        """
        raise NotImplementedError("Subclasses must implement file_upload()")

    def file_get(self, file_name: str) -> str:
        """
        Get information about a file from storage.

        Args:
            file_name (str): Name of the file to retrieve

        Returns:
            str: Result message in format "got {file_name}" if file exists,
                 empty string if file doesn't exist
        """
        raise NotImplementedError("Subclasses must implement file_get()")

    def file_copy(self, source: str, dest: str) -> str:
        """
        Copy a file to a new location.

        Args:
            source (str): Name of the source file
            dest (str): Name of the destination file

        Returns:
            str: Result message in format "copied {source} to {dest}"

        Raises:
            RuntimeError: If the source file doesn't exist
        """
        raise NotImplementedError("Subclasses must implement file_copy()")

    # Level 2 Methods: Search and Query

    def file_search(self, prefix: str) -> str:
        """
        Search for files by prefix, sorted by size in descending order.

        Args:
            prefix (str): Prefix to search for in file names

        Returns:
            str: Result message in format "found [{file1}, {file2}, ...]"
                 where files are sorted by size (largest first)
        """
        raise NotImplementedError("Subclasses must implement file_search()")

    # Level 3 Methods: Time-Aware Operations with TTL

    def file_upload_at(self, timestamp: str, file_name: str, size: str, ttl: Optional[int] = None) -> str:
        """
        Upload a file at a specific timestamp with optional TTL.

        Args:
            timestamp (str): ISO 8601 timestamp (e.g., "2021-07-01T12:00:00")
            file_name (str): Name of the file to upload
            size (str): Size of the file (e.g., "200kb")
            ttl (Optional[int]): Time-to-live in seconds (None = no expiration)

        Returns:
            str: Result message in format "uploaded at {file_name}"
        """
        raise NotImplementedError("Subclasses must implement file_upload_at()")

    def file_get_at(self, timestamp: str, file_name: str) -> str:
        """
        Get information about a file at a specific timestamp.

        Args:
            timestamp (str): ISO 8601 timestamp
            file_name (str): Name of the file to retrieve

        Returns:
            str: Result message in format "got at {file_name}" if file exists
                 and hasn't expired, "file not found" otherwise
        """
        raise NotImplementedError("Subclasses must implement file_get_at()")

    def file_copy_at(self, timestamp: str, source: str, dest: str) -> str:
        """
        Copy a file at a specific timestamp.

        Args:
            timestamp (str): ISO 8601 timestamp
            source (str): Name of the source file
            dest (str): Name of the destination file

        Returns:
            str: Result message in format "copied at {source} to {dest}"
        """
        raise NotImplementedError("Subclasses must implement file_copy_at()")

    def file_search_at(self, timestamp: str, prefix: str) -> str:
        """
        Search for files by prefix at a specific timestamp.

        Args:
            timestamp (str): ISO 8601 timestamp
            prefix (str): Prefix to search for in file names

        Returns:
            str: Result message in format "found at [{file1}, {file2}, ...]"
                 where files are sorted by size (largest first)
        """
        raise NotImplementedError("Subclasses must implement file_search_at()")

    # Level 4 Methods: Rollback

    def rollback(self, timestamp: str) -> str:
        """
        Rollback the storage state to a specific timestamp.

        This removes all files uploaded after the rollback timestamp
        and recalculates TTL for files with expiration times.

        Args:
            timestamp (str): ISO 8601 timestamp to rollback to

        Returns:
            str: Result message in format "rollback to {timestamp}"
        """
        raise NotImplementedError("Subclasses must implement rollback()")
