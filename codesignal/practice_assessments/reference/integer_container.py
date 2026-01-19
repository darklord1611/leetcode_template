"""
Integer Container - Abstract Base Class

This class defines the interface for an integer container data structure
that supports adding and deleting integers (including duplicates).
"""


class IntegerContainer:
    """
    Abstract base class for an integer container that stores integers
    and supports add and delete operations.

    The container allows duplicate values and tracks the total count
    of elements stored.
    """

    def __init__(self):
        """Initialize the integer container."""
        raise NotImplementedError("Subclasses must implement __init__")

    def add(self, value: int) -> int:
        """
        Add an integer to the container.

        Args:
            value (int): The integer value to add to the container

        Returns:
            int: The total number of elements in the container after adding

        Example:
            >>> container = IntegerContainerImpl()
            >>> container.add(10)
            1
            >>> container.add(20)
            2
            >>> container.add(10)  # Duplicates are allowed
            3
        """
        raise NotImplementedError("Subclasses must implement add()")

    def delete(self, value: int) -> bool:
        """
        Delete one occurrence of an integer from the container.

        Args:
            value (int): The integer value to delete from the container

        Returns:
            bool: True if the value was found and deleted, False otherwise

        Example:
            >>> container = IntegerContainerImpl()
            >>> container.add(10)
            1
            >>> container.add(10)
            2
            >>> container.delete(10)
            True
            >>> container.delete(10)
            True
            >>> container.delete(10)  # No more occurrences
            False
        """
        raise NotImplementedError("Subclasses must implement delete()")
