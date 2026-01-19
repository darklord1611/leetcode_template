# Scenario

Your task is to implement a simplified version of a banking system.
All operations that should be supported are listed below. Partial credit will be granted for each test passed, so
press "Submit" often to run tests and receive partial credits for passed tests. Please check tests for requirements
and argument types.

### Implementation Tips

Read the question all the way through before you start coding, but implement the operations and complete the
levels one by one, not all together, keeping in mind that you will need to refactor to support additional functionality.
Please, do not change the existing method signatures.

## Task

Example of banking system with various accounts:

```plaintext
[BankingSystem]
    Account ID: "account1", Balance: 1000
    Account ID: "account2", Balance: 500
    Account ID: "account3", Balance: 2500
```

## Level 1 – Initial Design & Basic Functions

- **CREATE_ACCOUNT(timestamp, account_id)**
  - Create a new account with the given account_id and initial balance of 0.
  - If an account with the same account_id already exists, the operation should return "false".
  - Otherwise, return "true".

- **DEPOSIT(timestamp, account_id, amount)**
  - Deposit the specified amount into the account.
  - If the account doesn't exist, return "" (empty string).
  - Otherwise, return the new balance as a string.

- **WITHDRAW(timestamp, account_id, amount)**
  - Withdraw the specified amount from the account.
  - If the account doesn't exist, return "" (empty string).
  - If the account has insufficient funds (balance < amount), return "" (empty string).
  - Otherwise, return the new balance as a string.

- **TRANSFER(timestamp, source_account_id, target_account_id, amount)**
  - Transfer the specified amount from the source account to the target account.
  - If either account doesn't exist, return "" (empty string).
  - If the source account has insufficient funds, return "" (empty string).
  - Otherwise, return the new balance of the source account as a string.

## Level 2 – Data Structures & Data Processing

- **TOP_SPENDERS(timestamp, n)**
  - Return the top n accounts that have spent the most money (total outgoing amount through WITHDRAW and TRANSFER operations).
  - Format: Return a comma-separated list of "account_id(total_outgoing)" ordered by total_outgoing in descending order.
  - In case of a tie, sort by account_id in ascending lexicographical order.
  - If there are fewer than n accounts, return all accounts that have made transactions.
  - Example return format: "account1(500), account2(300), account3(100)"

- **GET_PAYMENT_HISTORY(timestamp, account_id, n)**
  - Return the n most recent payment operations (DEPOSIT, WITHDRAW, TRANSFER) for the given account.
  - Format: Return a comma-separated list where each entry is "operation_type(amount)".
  - For TRANSFER, use "TRANSFER_IN(amount)" if the account received money, "TRANSFER_OUT(amount)" if it sent money.
  - Order by most recent first.
  - If the account doesn't exist, return "" (empty string).
  - If there are fewer than n operations, return all available operations.
  - Example return format: "DEPOSIT(100), WITHDRAW(50), TRANSFER_OUT(25)"

## Level 3 – Refactoring & Time-based Operations

The system now needs to handle scheduled transactions. Implement scheduled variants of payment operations:

- **SCHEDULE_PAYMENT(timestamp, account_id, amount, payment_type, delay)**
  - Schedule a DEPOSIT or WITHDRAW operation to execute at (timestamp + delay milliseconds).
  - payment_type is either "DEPOSIT" or "WITHDRAW".
  - The scheduled payment should execute automatically when any operation occurs at or after the scheduled time.
  - Return "true" if scheduled successfully, "" (empty string) if account doesn't exist.
  - Note: Scheduled payments should be processed in chronological order before the current operation.

- **ACCEPT_PAYMENT(timestamp, account_id, reference_id)**
  - Some transactions require two-factor authentication or approval.
  - When a WITHDRAW or TRANSFER exceeds 1000, it requires acceptance before completion.
  - reference_id is the operation identifier returned by the original WITHDRAW/TRANSFER.
  - Return the new balance if accepted successfully, "" if the reference doesn't exist or already processed.
  - Important: Operations requiring acceptance return a reference_id in format "payment_{sequential_number}" instead of the balance.

**Modified Operations for Level 3:**

- **WITHDRAW(timestamp, account_id, amount)** - Now returns "payment_{id}" if amount > 1000, requiring ACCEPT_PAYMENT
- **TRANSFER(timestamp, source_account_id, target_account_id, amount)** - Now returns "payment_{id}" if amount > 1000, requiring ACCEPT_PAYMENT

- **TOP_ACTIVITY(timestamp, n)**
  - Return top n accounts with the most total transaction count (including scheduled and pending payments).
  - Format: "account_id(count)" ordered by count descending, then by account_id ascending.
  - Example: "account1(15), account2(12), account3(8)"
