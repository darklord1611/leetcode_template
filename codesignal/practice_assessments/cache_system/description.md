> ⚠️ **Disclaimer:** This is a fictional practice problem created for interview preparation only.
> It is **not** an official CodeSignal problem and is not affiliated with, authorized by, or endorsed by
> CodeSignal or any company. Any resemblance to real assessment content is coincidental.

# Scenario

Your task is to implement a simplified in-memory **cache system** for storing task computation results.
All operations that should be supported are listed below. Partial credit will be granted for each test passed, so
press "Submit" often to run tests and receive partial credits for passed tests. Please check tests for requirements
and argument types.

### Implementation Tips

Read the question all the way through before you start coding, but implement the operations and complete the
levels one by one, not all together, keeping in mind that you will need to refactor to support additional functionality.
Please, do not change the existing method signatures.

## Task

Example of a cache holding task results:

```plaintext
[CacheSystem]  capacity = 3
    "taskA" -> "result_a"   (most recently used)
    "taskB" -> "result_b"
    "taskC" -> "result_c"   (least recently used)
```

All timestamps are integers and are non-decreasing across calls. All keys and values are strings.

---

## Level 1 – Basic Cache Operations

- **PUT(timestamp, key, value)**
  - Store `value` under `key`. If `key` already exists, overwrite its value.
  - Return "true".

- **GET(timestamp, key)**
  - Return the value stored under `key`, or "" (empty string) if `key` is not present.

- **DELETE(timestamp, key)**
  - Remove `key` from the cache.
  - Return "true" if the key existed and was removed, otherwise "false".

- **EXISTS(timestamp, key)**
  - Return "true" if `key` is present, otherwise "false".
  - This operation does not affect the usage/recency tracking introduced in later levels.

---

## Level 2 – Capacity & LRU Eviction

The cache now has a maximum number of live entries. Refactor `PUT` and `GET` so that the
least-recently-used (LRU) entry is evicted when the cache is full.

- **SET_CAPACITY(timestamp, capacity)**
  - Set the maximum number of entries the cache may hold (`capacity` >= 0).
  - If the current number of entries exceeds the new capacity, evict least-recently-used entries until it fits.
  - Return the number of entries evicted as a string (e.g. "2"), or "0" if none were evicted.
  - Before this operation is ever called, the cache has unlimited capacity.

- **PUT(timestamp, key, value)** *(updated)*
  - Inserting a **new** key while the cache is at capacity must first evict the least-recently-used entry.
  - Overwriting an existing key updates its value (the entry count does not change).
  - A successful `PUT` marks `key` as the most-recently-used entry. Return "true".

- **GET(timestamp, key)** *(updated)*
  - A successful lookup marks `key` as the most-recently-used entry.
  - Return the value, or "" if not present.
  - When the cache is full, the least-recently-used entry is the one evicted by the next inserting `PUT`; this is observable by `GET`/`EXISTS` returning "" for it.

> Recency is defined by the most recent `PUT` (insert or overwrite) or successful `GET`.
> `EXISTS` and `DELETE` do not count as usage.

---

## Level 3 – Time-To-Live (TTL) & Expiration

Entries may now expire. Refactor your read operations so expired entries behave as if they were never there.

- **PUT_WITH_TTL(timestamp, key, value, ttl)**
  - Store `value` under `key` with a time-to-live of `ttl` (`ttl` > 0).
  - The entry is valid for timestamps in the range `[timestamp, timestamp + ttl)` and expires at `timestamp + ttl`.
  - Marks `key` as most-recently-used. Return "true".

- Entries created with **PUT** (no TTL) never expire.
- All read operations (**GET**, **EXISTS**) at a given `timestamp` must treat expired entries as absent
  (a `GET`/`EXISTS` after `timestamp + ttl` returns "" / "false").
  Expired entries do not count toward capacity and may be removed lazily.
- When evicting for capacity, expired entries should be purged before a live LRU entry is evicted.

---

## Level 4 – Task Dependencies & Cascading Invalidation

Cached results may depend on other cached results. When a result changes, everything derived from it becomes stale.

- **PUT_WITH_DEPS(timestamp, key, value, dependencies)**
  - Store `value` under `key`, recording that it depends on the keys listed in `dependencies` (a list of strings).
  - Marks `key` as most-recently-used. Return "true".

- **PUT / PUT_WITH_TTL / PUT_WITH_DEPS** *(updated)*
  - Whenever an existing `key` is overwritten, every entry that **transitively** depends on `key` must be invalidated
    (removed), because their cached results are now stale.

- **INVALIDATE(timestamp, key)**
  - Remove `key` and, recursively, every entry that transitively depends on `key`.
  - Return the total number of entries removed as a string (including `key` itself if it existed; "0" if `key` was absent).
  - After invalidation, `GET`/`EXISTS` returns "" / "false" for every removed dependent.

---

## Level 5 – Pinning & Eviction Priority

Some results are expensive to recompute and should be protected from eviction.

- **PIN(timestamp, key)**
  - Mark `key` as pinned. Pinned entries are never removed by capacity eviction and never expire via TTL while pinned.
  - Return "true" if `key` exists (and is now pinned), "false" if `key` is absent.

- **UNPIN(timestamp, key)**
  - Remove the pin from `key`. Return "true" if `key` exists, "false" otherwise.
  - If the entry's TTL had already elapsed while it was pinned, it is treated as expired again once unpinned.

- **PUT / PUT_WITH_TTL / PUT_WITH_DEPS** *(updated)*
  - Capacity eviction must skip pinned entries; evict the least-recently-used **unpinned**, non-expired entry.
  - If the cache is at capacity and every live entry is pinned, a `PUT` that would insert a **new** key cannot make room:
    do not insert it and return "false". (Overwriting an existing key is always allowed.)

---

## Level 6 – Statistics & Analytics

Track cache effectiveness. Starting from the first operation, count cache hits and misses on `GET`.

- A **hit** is a `GET` for a key that is present and not expired. A **miss** is a `GET` for an absent or expired key.

- **GET_STATS(timestamp)**
  - Return statistics in the exact format `hits=<H>,misses=<M>,hit_ratio=<R>` where `R` is `H / (H + M)`
    rounded to two decimal places (e.g. "hits=3,misses=1,hit_ratio=0.75"). If there have been no gets, `R` is "0.00".

- **TOP_ACCESSED(timestamp, n)**
  - Return a comma-separated list of up to `n` currently-present keys with the highest hit counts.
  - Ties are broken by most-recently-used first, then lexicographically.
  - Return "" if the cache is empty.

---

## Level 7 – Namespaces

Group cached results into independent namespaces, each with its own capacity and LRU eviction.

- All Level 1–6 operations act on the **default namespace** (the empty string `""`).

- **PUT_IN_NAMESPACE(timestamp, namespace, key, value)**
  - Store `value` under `key` within `namespace`, subject to the same capacity/eviction rules as `PUT`, per namespace. Return "true".

- **GET_IN_NAMESPACE(timestamp, namespace, key)**
  - Return the value of `key` within `namespace`, or "" if absent/expired.
  - Counts toward hit/miss statistics and recency within that namespace.

- **SET_NAMESPACE_CAPACITY(timestamp, namespace, capacity)**
  - Set the capacity for `namespace`, evicting that namespace's least-recently-used entries if needed.
  - Return the number of entries evicted as a string.

> Keys in different namespaces are independent; the same key string may exist in multiple namespaces with different values.
