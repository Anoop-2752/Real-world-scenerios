## Problem Statement

Design a login system where a user can enter their username and password. The system should allow only three attempts for entering the correct credentials. If the user enters incorrect credentials three times, the account should be locked.

## Key Operation

Authentication with failure tracking and account locking after three incorrect attempts.

### Key Operation

Authentication with failure tracking and account locking after three incorrect attempts.

## Data Structure
- Dictionary (dict) – Stores usernames and passwords.
- Integer (int) – Keeps track of login attempts.

## Solution Explanation

1. Define a dictionary with usernames and corresponding passwords.
2. Use a loop to allow users to enter credentials.
3. Check credentials:
- If correct → Display a success message and break the loop.
- If incorrect → Increment the attempt counter.
4. If three failed attempts occur, lock the account and exit.

