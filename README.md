# Problem Statement

Write a software library that accepts 2 version string as input and
returns whether one is greater than, equal, or less than the other.
As an example: “1.2” is greater than “1.1”.
Please provide all test cases you could think of.

## Solution

A version is a string that matches the following regex:
```
"^v?(\d+)(?:.(\d+))?(?:.(\d+))?(?:-?(a|b|rc)(\d+)?)?$"
```
E.g. v0.11.22-rc3.

We then compare each of the parts using normal number/string comparison.
There is type coersion so that we can compare Versions to int and floats.

### Assumptions
1. v1 is equivalent to v1.0.0
2. A version without a candidate is greater than its candidate counterpart
   e.g. v2 > v2rc > v2b > v2a