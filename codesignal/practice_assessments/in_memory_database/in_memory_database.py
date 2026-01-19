"""
In-Memory Database - Abstract Base Class

This class defines the interface for an in-memory key-value database
with field-level granularity, TTL support, and backup/restore capabilities.
"""


class InMemoryDatabase:
    """
    Abstract base class for an in-memory database that manages keys with
    multiple fields, supports time-aware operations with TTL, and provides
    backup and restore functionality.
    """

    def __init__(self):
        """Initialize the in-memory database."""
        raise NotImplementedError("Subclasses must implement __init__")

    # Level 1 Methods: Basic Field Operations

    def set_field(self, key: str, field: str, value: str) -> str:
        """
        Set a field value for a key.

        Args:
            key (str): The key to set the field for
            field (str): The field name
            value (str): The value to set

        Returns:
            str: The value that was set
        """
        raise NotImplementedError("Subclasses must implement set_field()")

    def get_field(self, key: str, field: str) -> str:
        """
        Get a field value for a key.

        Args:
            key (str): The key to get the field from
            field (str): The field name

        Returns:
            str: The field value, or "" if key or field doesn't exist
        """
        raise NotImplementedError("Subclasses must implement get_field()")

    def delete_field(self, key: str, field: str) -> str:
        """
        Delete a field from a key.

        Args:
            key (str): The key to delete the field from
            field (str): The field name to delete

        Returns:
            str: "true" if field was deleted, "false" if key or field doesn't exist
        """
        raise NotImplementedError("Subclasses must implement delete_field()")

    def get(self, key: str) -> str:
        """
        Get all fields for a key.

        Args:
            key (str): The key to get all fields from

        Returns:
            str: Formatted string "field1(value1), field2(value2), ..."
                 sorted alphabetically by field name, or "" if key doesn't exist
        """
        raise NotImplementedError("Subclasses must implement get()")

    def delete(self, key: str) -> str:
        """
        Delete a key and all its fields.

        Args:
            key (str): The key to delete

        Returns:
            str: "true" if key was deleted, "false" if key doesn't exist
        """
        raise NotImplementedError("Subclasses must implement delete()")

    # Level 2 Methods: Filtering and Querying

    def scan(self, prefix: str) -> str:
        """
        Get all keys that start with the given prefix.

        Args:
            prefix (str): The prefix to match keys against

        Returns:
            str: Comma-separated list of matching keys sorted alphabetically,
                 or "" if no matches found
        """
        raise NotImplementedError("Subclasses must implement scan()")

    def scan_by_field(self, field: str, value: str) -> str:
        """
        Get all keys that have a specific field with a specific value.

        Args:
            field (str): The field name to search for
            value (str): The value to match

        Returns:
            str: Comma-separated list of matching keys sorted alphabetically,
                 or "" if no matches found
        """
        raise NotImplementedError("Subclasses must implement scan_by_field()")

    def top_n_keys(self, n: int) -> str:
        """
        Get the top N keys by number of fields.

        Args:
            n (int): Number of top keys to return

        Returns:
            str: Formatted string "key1(count), key2(count), ..."
                 sorted by field count descending, then by key name ascending
        """
        raise NotImplementedError("Subclasses must implement top_n_keys()")

    # Level 3 Methods: Time-Aware Operations with TTL

    def set_field_at(self, timestamp: int, key: str, field: str, value: str) -> str:
        """
        Set a field value for a key at a specific timestamp.

        Args:
            timestamp (int): The timestamp for the operation
            key (str): The key to set the field for
            field (str): The field name
            value (str): The value to set

        Returns:
            str: The value that was set
        """
        raise NotImplementedError("Subclasses must implement set_field_at()")

    def set_field_with_ttl(self, timestamp: int, key: str, field: str, value: str, ttl: int) -> str:
        """
        Set a field value with a time-to-live (TTL) in milliseconds.

        The field expires at timestamp + ttl (exclusive). At the expiration time,
        the field is no longer accessible.

        Args:
            timestamp (int): The timestamp for the operation
            key (str): The key to set the field for
            field (str): The field name
            value (str): The value to set
            ttl (int): Time-to-live in milliseconds

        Returns:
            str: The value that was set
        """
        raise NotImplementedError("Subclasses must implement set_field_with_ttl()")

    def get_field_at(self, timestamp: int, key: str, field: str) -> str:
        """
        Get a field value at a specific timestamp, respecting TTL.

        Args:
            timestamp (int): The timestamp for the query
            key (str): The key to get the field from
            field (str): The field name

        Returns:
            str: The field value if it exists and hasn't expired, "" otherwise
        """
        raise NotImplementedError("Subclasses must implement get_field_at()")

    def get_at(self, timestamp: int, key: str) -> str:
        """
        Get all non-expired fields for a key at a specific timestamp.

        Args:
            timestamp (int): The timestamp for the query
            key (str): The key to get all fields from

        Returns:
            str: Formatted string "field1(value1), field2(value2), ..."
                 sorted alphabetically by field name, excluding expired fields,
                 or "" if key doesn't exist or all fields are expired
        """
        raise NotImplementedError("Subclasses must implement get_at()")

    def scan_at(self, timestamp: int, prefix: str) -> str:
        """
        Get all keys with non-expired fields that start with the given prefix.

        Args:
            timestamp (int): The timestamp for the query
            prefix (str): The prefix to match keys against

        Returns:
            str: Comma-separated list of matching keys (with at least one non-expired field)
                 sorted alphabetically, or "" if no matches found
        """
        raise NotImplementedError("Subclasses must implement scan_at()")

    def scan_by_field_at(self, timestamp: int, field: str, value: str) -> str:
        """
        Get all keys that have a non-expired field with a specific value at a timestamp.

        Args:
            timestamp (int): The timestamp for the query
            field (str): The field name to search for
            value (str): The value to match

        Returns:
            str: Comma-separated list of matching keys sorted alphabetically,
                 or "" if no matches found
        """
        raise NotImplementedError("Subclasses must implement scan_by_field_at()")

    def delete_field_at(self, timestamp: int, key: str, field: str) -> str:
        """
        Delete a field from a key at a specific timestamp.

        Args:
            timestamp (int): The timestamp for the operation
            key (str): The key to delete the field from
            field (str): The field name to delete

        Returns:
            str: "true" if field was deleted, "false" if key or field doesn't exist
        """
        raise NotImplementedError("Subclasses must implement delete_field_at()")

    # Level 4 Methods: Backup and Restore

    def backup(self, timestamp: int) -> str:
        """
        Create a backup of the database at a specific timestamp.

        Captures all keys and their non-expired fields at the given timestamp.
        Backups are numbered sequentially starting from 1 (backup_1, backup_2, etc.).

        Args:
            timestamp (int): The timestamp to create the backup at

        Returns:
            str: The backup ID (e.g., "backup_1", "backup_2", ...)
        """
        raise NotImplementedError("Subclasses must implement backup()")

    def get_backup_info(self, backup_id: str) -> str:
        """
        Get information about a backup.

        Args:
            backup_id (str): The backup ID (e.g., "backup_1")

        Returns:
            str: Formatted string "keys:N,fields:M,timestamp:T"
                 where N is the number of keys, M is the total number of fields,
                 and T is the backup timestamp
        """
        raise NotImplementedError("Subclasses must implement get_backup_info()")

    def restore(self, timestamp: int, backup_id: str) -> str:
        """
        Restore the database from a backup at a specific timestamp.

        Clears all existing data and restores from the backup. For fields with TTL
        in the backup, the TTL is recalculated based on the restore timestamp:
        - Original expiration time = backup_timestamp + (original_timestamp + ttl - backup_timestamp)
        - New expiration time = restore_timestamp + (original_timestamp + ttl - backup_timestamp)

        Args:
            timestamp (int): The timestamp to restore at
            backup_id (str): The backup ID to restore from

        Returns:
            str: The number of keys restored as a string
        """
        raise NotImplementedError("Subclasses must implement restore()")

    def compare(self, backup_id1: str, backup_id2: str) -> str:
        """
        Compare two backups and return keys that differ.

        A key differs if:
        - It exists in one backup but not the other
        - It exists in both but has different fields or values

        Args:
            backup_id1 (str): First backup ID to compare
            backup_id2 (str): Second backup ID to compare

        Returns:
            str: Comma-separated list of keys that differ, sorted alphabetically,
                 or "" if no differences found
        """
        raise NotImplementedError("Subclasses must implement compare()")
