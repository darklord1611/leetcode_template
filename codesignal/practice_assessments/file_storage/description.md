> ⚠️ **Disclaimer:** This is a fictional practice problem created for interview preparation only.
> It is **not** an official CodeSignal problem and is not affiliated with, authorized by, or endorsed by
> CodeSignal or any company. Any resemblance to real assessment content is coincidental.

# Scenario

Your task is to implement a simplified version of a **file hosting service**.
All operations that should be supported are listed below. Partial credit will be granted for each test passed, so
press "Submit" often to run tests and receive partial credits for passed tests. Please check tests for requirements
and argument types.

### Implementation Tips

Read the question all the way through before you start coding, but implement the operations and complete the
levels one by one, keeping in mind that **you will need to reopen and refactor functions you wrote in earlier
levels** so they satisfy the additional requirements introduced later. The set of functions is intentionally small;
most of the difficulty comes from extending the *behaviour* of the same functions across levels.
Please, do not change the existing method signatures.

## Task

File sizes are non-negative integers. All timestamps are integers and are **non-decreasing** across calls. Every
operation takes `timestamp` as its first parameter. Sizes are returned as plain integer strings (e.g. "200");
failures return "" (empty string) unless stated otherwise.

---

## Level 1 – Basic Storage

- **FILE_UPLOAD(timestamp, file_name, size)**
  - Upload a file with the given integer `size`.
  - Return "true" on success, or "" if a file with that name already exists (no overwrite).

- **FILE_GET(timestamp, file_name)**
  - Return the file's `size` as a string, or "" if no such file exists.

- **FILE_COPY(timestamp, source, dest)**
  - Copy `source` to `dest`, overwriting `dest` if it already exists.
  - Return "true" on success, or "" if `source` does not exist.

---

## Level 2 – Search

A read-only query over the files in storage.

- **FILE_SEARCH(timestamp, prefix)**
  - Return the names of files whose name starts with `prefix`, ordered by `size` **descending**, ties broken by
    name **ascending**. Return at most the top 10 names, joined by ", ". Return "" if no file matches.

---

## Level 3 – Time To Live (TTL)

Files can be given a lifetime. This forces you to **reopen `FILE_UPLOAD`, `FILE_GET`, `FILE_COPY`, and
`FILE_SEARCH`** so they account for expiry.

A file uploaded with a `ttl` is **alive** for the half-open interval `[timestamp, timestamp + ttl)` — it is live at
its upload time and at every time strictly before `timestamp + ttl`, and is **expired** at and after that. A file
uploaded without a ttl lives forever.

- **FILE_UPLOAD_WITH_TTL(timestamp, file_name, size, ttl)**
  - Upload a file alive for `[timestamp, timestamp + ttl)`.
  - Return "true" on success, or "" if a live file with that name already exists.

- **FILE_UPLOAD(timestamp, file_name, size)** *(updated)*
  - Files uploaded without a ttl live forever. The "already exists" check must treat an **expired** file as absent:
    its name is free again, and uploading replaces it.

- **FILE_GET(timestamp, file_name)** *(updated)*
  - Ignore files that are expired at the query `timestamp` (return "" as if they did not exist).

- **FILE_COPY(timestamp, source, dest)** *(updated)*
  - Copying an expired or missing `source` returns "". Copying a **live** file with a ttl gives `dest` the source's
    **remaining** ttl, so `dest` expires exactly when the source would have (same expiry time). Copying a permanent
    file makes `dest` permanent. As before, `dest` is overwritten if present.

- **FILE_SEARCH(timestamp, prefix)** *(updated)*
  - Ignore files that are expired at the query `timestamp`.

---

## Level 4 – Rollback

- **ROLLBACK(timestamp, rollback_to)** *(updated reads)*
  - Restore the entire store to its **exact state as of time `rollback_to`** (`rollback_to <= timestamp`): a file
    exists after the rollback if and only if it existed and was alive at `rollback_to`, with the same size it had then.
  - **TTL recalculation rule:** each surviving file keeps the *remaining lifetime* it had at `rollback_to`, measured
    again from `rollback_to`. Concretely, a file with an expiry time `E` (so it had `E - rollback_to` time left at
    `rollback_to`) is re-anchored so that after the rollback it is treated as having been uploaded at `rollback_to`
    with the same `E` — its expiry time `E` is unchanged. Permanent files (no ttl) stay permanent. A file whose
    upload time was after `rollback_to`, or which had already expired by `rollback_to` (`E <= rollback_to`), does not
    survive the rollback.
  - Because timestamps are non-decreasing and equal to or beyond `rollback_to`, the expiry times themselves do not
    change; the rule guarantees a file alive at `rollback_to` with `X` time left again has exactly `X` time left
    measured from `rollback_to`.
  - Return "true". After the rollback, all operations reflect the rolled-back state.
