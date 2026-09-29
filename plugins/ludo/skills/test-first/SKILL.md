---
name: test-first
description: Write the test before the code, so every feature is proven to work and stays working, following red, green, refactor. Explained for beginners with Python (pytest) or JavaScript (vitest or jest). Use when the user says "test first", "TDD", "write tests", "make sure it keeps working", "how do I know my code works", or is building something they'll keep changing.
---

# Test first

A test is a small program that checks your program. Written first, it forces you to decide exactly what "working" means, and it catches it the moment a later change breaks something.

## The loop: red, green, refactor

1. **Red**: write one small test for one behavior, like "an empty list returns 0". Run it. It must fail, and fail for the right reason (the feature doesn't exist yet). A test that passes before the code exists proves nothing.
2. **Green**: write the simplest code that makes that test pass. Nothing extra.
3. **Refactor**: clean up the code with the test still passing.
4. Repeat for the next behavior.

## Setup

- Python: `pip install pytest`, tests in `test_<name>.py`, functions named `test_...`, run `pytest`.
- JavaScript or TypeScript: `npm install -D vitest`, tests in `<name>.test.js`, run `npx vitest run`.

## What to test

- The normal case, with real-looking input.
- The edges: empty input, one item, a very large input, a missing value, odd characters.
- The mistakes: what should happen with bad input? (a clear error, not a crash)
- Every bug you fix: first write a test that reproduces it, then fix it, so it can never come back quietly.

## Rules

- One behavior per test, named so the name says what broke: `test_empty_cart_total_is_zero`.
- Tests must actually check something. A test that runs code without asserting a result is a fake pass.
- Don't test the library; test your code.
- Run the whole test suite before saying anything is done, and show the output.
