# Module 2 Assignment: Prime Factors

In this assignment, you will build an algorithm that will generate a list of
the prime factors for a given number.

Prime factors (also known as prime numbers or a prime) are numbers which cannot
be formed as the result of a multiplication
(https://en.wikipedia.org/wiki/Prime_number).

Using the Three Rules of TDD, develop the algorithm based on each assertion
listed below. After each step **commit your work** using `git commit`.


### Completing the assignment
- Fork this repository and then clone it from your own GitHub account. Do not
  clone this repository directly from the Sheridan GitHub account
- There are 8 steps to complete. For each step, the following is expected:
    1. A test to be written with the specified assertion before any code is
      written.
    2. Only enough code is written to make the test pass.
    3. A git commit exists for each step


### Evaluation
There are 8 steps to this assignment. The expected deliverable

## Requirements

Write a function called `generate_prime_factors` in the module `prime.py`. This
function will accept an integer as an argument, and return a list of integers.

E.g.
```python
>>> generate_prime_factors(6)
[2, 3]
```


### Step 1:
Write a test that asserts that when `generate_prime_factors` is called with a
data type that is not an integer (e.g. a string or float), a ValueError is
raised. Write the appropriate code to solve this and then commit the changes.


### Step 2:
Write a test that asserts that when `generate_prime_factors` is called with
`1`, an empty list is returned. Solve & commit.


### Step 3:
Write a test that asserts that when `generate_prime_factors` is called with
`2`, the list `[2]` is returned. Solve & commit.


### Step 4:
Write a test that asserts that when `generate_prime_factors` is called with
`3`, the list `[3]` is returned. Solve & commit.


### Step 5:
Write a test that asserts that when `generate_prime_factors` is called with
`4`, the list `[2, 2]` is returned. Solve & commit.


### Step 6:
Write a test that asserts that when `generate_prime_factors` is called with
`6`, the list `[2, 3]` is returned. Solve & commit.


### Step 7:
Write a test that asserts that when `generate_prime_factors` is called with
`8`, the list `[2, 2, 2]` is returned. Solve & commit.


### Step 8:
Write a test that asserts that when `generate_prime_factors` is called with
`9`, the list `[3, 3]` is returned. Solve & commit.
