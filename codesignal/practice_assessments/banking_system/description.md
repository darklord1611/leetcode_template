> ⚠️ **Disclaimer:** This is a fictional practice problem created for interview preparation only.
> It is **not** an official CodeSignal problem and is not affiliated with, authorized by, or endorsed by
> CodeSignal or any company. Any resemblance to real assessment content is coincidental.

# Scenario

Your task is to implement a simplified version of a **banking system**.
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

All amounts and balances are non-negative integers. All timestamps are integers and are **non-decreasing** across
calls. Balances are returned as plain integer strings (e.g. "1500"); failures return "" (empty string) unless stated
otherwise.

---

## Level 1 – Basic Operations

- **CREATE_ACCOUNT(timestamp, account_id)**
  - Create a new account with the given `account_id` and an initial balance of 0.
  - Return "false" if an account with that id already exists, otherwise "true".

- **DEPOSIT(timestamp, account_id, amount)**
  - Add `amount` to the account's balance.
  - Return the new balance as a string, or "" if the account does not exist.

- **PAY(timestamp, account_id, amount)**
  - Withdraw `amount` from the account (a payment to an external party).
  - Return "" if the account does not exist or has insufficient funds; otherwise return the new balance.

- **TRANSFER(timestamp, source_account_id, target_account_id, amount)**
  - Move `amount` from the source account to the target account.
  - Return "" if either account does not exist, if source and target are the same account, or if the source has
    insufficient funds; otherwise return the **source** account's new balance.

---

## Level 2 – Outgoing Totals & Ranking

Introduce a ranking of accounts by how much money has *left* them. You must **reopen `PAY` and `TRANSFER`** so they
accumulate an "outgoing" total per account.

- An account's **outgoing total** is the sum of all successful `PAY` amounts plus all successful outgoing `TRANSFER`
  amounts. Deposits and *incoming* transfers do **not** count.

- **TOP_SPENDERS(timestamp, n)**
  - Return the top `n` accounts ranked by outgoing total, in descending order; ties broken by `account_id` in
    ascending alphabetical order.
  - Format: `"id1(total1), id2(total2), ..."`. If there are fewer than `n` accounts, return all of them.
  - Accounts with an outgoing total of 0 are included (ranked last by the tie-break rule).

---

## Level 3 – Scheduled Payments

Payments can be scheduled to execute in the future. This introduces an ordering requirement that forces you to
**reopen every transaction operation**.

- **SCHEDULE_PAYMENT(timestamp, account_id, amount, delay)**
  - Register a payment of `amount` from `account_id` to be executed at time `timestamp + delay` (`delay` > 0).
  - Return a unique payment id of the form `"payment1"`, `"payment2"`, ... (a global counter increasing in the order
    payments are scheduled), or "" if the account does not exist. Funds are **not** checked at scheduling time.

- **CANCEL_PAYMENT(timestamp, account_id, payment_id)**
  - Cancel a previously scheduled payment that has not yet executed and belongs to `account_id`.
  - Return "true" if it was cancelled, otherwise "false".

- **Scheduled payment execution (the key rule):** a scheduled payment executes at its scheduled time. Before any
  operation does its own work at time `timestamp`, the system must first execute every pending scheduled payment whose
  scheduled time is `<= timestamp`, in order of scheduled time (ties broken by the order they were scheduled). Executing
  a payment deducts `amount` from the source account **and counts toward its outgoing total** — but only if the account
  has sufficient funds at execution time; otherwise the scheduled payment is cancelled with no effect.
  - This means `DEPOSIT`, `PAY`, `TRANSFER`, and `TOP_SPENDERS` must all process due scheduled payments first.

---

## Level 4 – Merging Accounts & Historical Balance

- **MERGE_ACCOUNTS(timestamp, account_id_1, account_id_2)**
  - Merge `account_id_2` into `account_id_1`: balances are added together, outgoing totals are added together, and any
    pending scheduled payments from `account_id_2` are reassigned to `account_id_1`. After the merge `account_id_2`
    no longer exists.
  - Return "false" if the two ids are equal or either account does not exist; otherwise "true".
  - All operations must continue to work correctly after merges (e.g. `TOP_SPENDERS` reflects the combined outgoing
    total under `account_id_1`, and any operation referring to a merged-away account fails as if it does not exist).

- **GET_BALANCE(timestamp, account_id, time_at)**
  - Return the balance that `account_id` had at the historical time `time_at` (`time_at <= timestamp`), taking into
    account every operation and scheduled-payment execution that had occurred by `time_at`.
  - Return "" if the account did not exist at `time_at`, or if it had already been merged into another account by
    `time_at`.
