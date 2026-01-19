# Scenario

Your task is to implement a simplified version of an in-memory database.
All operations that should be supported are listed below. Partial credit will be granted for each test passed, so
press "Submit" often to run tests and receive partial credits for passed tests. Please check tests for requirements
and argument types.

### Implementation Tips

Read the question all the way through before you start coding, but implement the operations and complete the
levels one by one, not all together, keeping in mind that you will need to refactor to support additional functionality.
Please, do not change the existing method signatures.

## Task

Example of in-memory database with various records:

```plaintext
[InMemoryDatabase]
    Key: "user1"
        field: "name" -> "Alice"
        field: "age" -> "30"
        field: "city" -> "NYC"
    Key: "user2"
        field: "name" -> "Bob"
        field: "age" -> "25"
```

## Level 1 – Initial Design & Basic Functions

- **SET_FIELD(key, field, value)**
  - Set the value of a field for a given key.
  - If the key doesn't exist, create it.
  - If the field already exists for this key, overwrite the value.
  - Return the value that was set.

- **GET_FIELD(key, field)**
  - Get the value of a specific field for a given key.
  - If the key doesn't exist or the field doesn't exist for that key, return "" (empty string).
  - Otherwise, return the field's value.

- **DELETE_FIELD(key, field)**
  - Delete a specific field from a key.
  - If the key or field doesn't exist, return "false".
  - Otherwise, delete the field and return "true".
  - If this was the last field for the key, the key should be removed from the database.

- **GET(key)**
  - Get all fields for a given key.
  - Return a string in the format: "field1(value1), field2(value2), field3(value3)"
  - Fields should be sorted alphabetically by field name.
  - If the key doesn't exist, return "" (empty string).

## Level 2 – Filtering & Querying

- **SCAN(prefix)**
  - Find all keys that start with the given prefix.
  - Return a comma-separated list of keys sorted in alphabetical order.
  - If no keys match, return "" (empty string).
  - Example return format: "key1, key2, key3"

- **SCAN_BY_FIELD(field, value)**
  - Find all keys that have the specified field with the specified value.
  - Return a comma-separated list of keys sorted in alphabetical order.
  - If no keys match, return "" (empty string).
  - Example return format: "key1, key2, key3"

- **DELETE(key)**
  - Delete an entire key and all its fields from the database.
  - Return "true" if the key existed and was deleted.
  - Return "false" if the key didn't exist.

- **TOP_N_KEYS(n)**
  - Return the top n keys with the most fields.
  - Format: "key1(count1), key2(count2), key3(count3)"
  - Order by field count in descending order, then by key name in ascending alphabetical order for ties.
  - If there are fewer than n keys, return all keys.
  - Example return format: "user1(5), user2(3), user3(2)"
