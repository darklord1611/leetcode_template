> ⚠️ **Disclaimer:** This is a fictional practice problem created for interview preparation only.
> It is **not** an official CodeSignal problem and is not affiliated with, authorized by, or endorsed by
> CodeSignal or any company. Any resemblance to real assessment content is coincidental.

# Scenario

Your task is to implement a simplified version of an **in-memory key-value database**.
Each *key* names a *record*, and a record is a set of *fields*, each field holding a string
value. All operations that should be supported are listed below. Partial credit will be granted
for each test passed, so press "Submit" often to run tests and receive partial credits for passed
tests. Please check tests for requirements and argument types.

### Implementation Tips

Read the question all the way through before you start coding, but implement the operations and
complete the levels one by one, keeping in mind that **you will need to reopen and refactor
functions you wrote in earlier levels** so they satisfy the additional requirements introduced
later. The set of functions is intentionally small; most of the difficulty comes from extending
the *behaviour* of the same functions across levels. Functions whose behaviour changes in a later
level are marked *(updated)* there. Please, do not change the existing method signatures.

## Task

Every stateful operation takes a `timestamp: int` as its first parameter. Timestamps are integers
and are **non-decreasing** across calls. All return values are strings. Records hold `field=value`
pairs; whenever a record is rendered, its fields are sorted by field name in ascending order and
joined with `", "`. A query that finds nothing returns "" (empty string).

---

## Level 1 – Field Operations

- **set_field(timestamp, key, field, value)**
  - Set `field` to `value` on `key`, creating the record if it does not yet exist; an existing
    field's value is overwritten.
  - Return "true".

- **get_field(timestamp, key, field)**
  - Return the value of `field` on `key`, or "" if the key or the field is absent.

- **delete_field(timestamp, key, field)**
  - Remove `field` from `key`.
  - Return "true" if the field existed and was removed, otherwise "false". If removing the field
    leaves the record with no fields, the key no longer exists.

- **get_record(timestamp, key)**
  - Return the record's fields as `field=value` pairs sorted by field name ascending, joined with
    `", "` (e.g. `"a=1, b=2"`).
  - Return "" if the key has no fields.

---

## Level 2 – Scans & Ranking

Read-only queries over the records built in Level 1.

- **scan_prefix(timestamp, key, prefix)**
  - Return the `field=value` pairs of `key` whose **field name** starts with `prefix`, sorted by
    field name ascending and joined with `", "`.
  - Return "" if the key is absent or no field name matches the prefix.

- **top_n_keys(timestamp, n)**
  - Return the top `n` keys ranked by their number of fields, in descending order; ties are broken
    by key name in ascending alphabetical order.
  - Format: `"key1(count1), key2(count2), ..."`. If there are fewer than `n` keys, return all of
    them. Return "" if there are no keys.

---

## Level 3 – TTL (Time-To-Live)

Fields may now expire. This forces you to **reopen `set_field`, `get_field`, `delete_field`,
`get_record`, `scan_prefix` and `top_n_keys`**.

- **set_field_with_ttl(timestamp, key, field, value, ttl)**
  - Set `field` to `value` on `key` with a lifetime of `ttl`. The field is valid for the half-open
    interval `[timestamp, timestamp + ttl)` and expires (becomes absent) at `timestamp + ttl`.
  - Return "true".

- **set_field** *(updated)*
  - A plain `set_field` makes the field **permanent**: it clears any TTL previously attached to that
    field, and fields created by plain `set_field` never expire.

- **All reads** *(updated)*: `get_field`, `get_record`, `scan_prefix` and `top_n_keys` must ignore
  any field that is expired at the query `timestamp` (treat it as absent). Expired fields do not
  count toward a key's field count in `top_n_keys`, and a key whose every field has expired is
  treated as absent. Expired fields may be purged lazily.

---

## Level 4 – Backup & Restore

- **backup(timestamp)**
  - Take a snapshot of the entire database at `timestamp`. For every ttl-field, store its
    **remaining ttl** at `timestamp`, defined as `expire_at - timestamp` (always > 0 for a live
    field, since expired fields are not part of the snapshot). Permanent fields are stored as
    permanent.
  - Return the number of keys that have at least one live field at `timestamp`, as a string.

- **restore(timestamp, backup_timestamp)**
  - Find the most recent backup whose backup time is `<= backup_timestamp` and make it the current
    state. If no such backup exists, do nothing.
  - On restore, the entire current database is replaced by the snapshot. Permanent fields stay
    permanent. For each ttl-field the **remaining lifetime is preserved**, recalculated relative to
    the restore time:

    ```
    new_expire_at = timestamp + saved_remaining_ttl
    ```

    where `timestamp` is the restore time and `saved_remaining_ttl` is the value recorded by
    `backup`. (Equivalently, a field that had `r` time units left to live when it was backed up
    again has exactly `r` time units left to live the moment it is restored.)
  - Return "true".
  - After a restore, all reads reflect the restored state.
