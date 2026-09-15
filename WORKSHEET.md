# COMP 485 — Senior Software Engineering
## In-Class Exercise: Code Coverage Analysis (in PyCharm)

**Name:** ______________________________    **Date:** ______________

---

## Part 1 — Setup

1. Accept the assignment on GitHub Classroom (link on the Canvas home page).
2. Clone your GitHub Classroom repository to your local machine.
3. Open the project in PyCharm.
4. If PyCharm prompts you, configure the project interpreter
   (**Settings > Project > Python Interpreter**). Python 3.9 or newer will work.
5. Install pytest:

   ```
   pip install pytest
   ```

6. Tell PyCharm to use pytest:
   **Settings > Tools > Python Integrated Tools > Testing > Default test runner: pytest**
7. Turn on branch coverage:
   **Settings > Build, Execution, Deployment > Coverage** — enable branch coverage.
8. Run `main.py`, both with the green arrow and from PyCharm's terminal
   (`python main.py`). Enter a few numbers; type `quit` to exit.

---

## Part 2 — Why you can't just run the test file

9. In the terminal, from the project root, try running the test file the way
   you'd run any other script:

   ```
   python tests/test_prime_finder.py
   ```

   **a. What error did you get?**

   ________________________________________________________________

   **b. Why?** When you run a script, Python puts *that script's folder* on the
   import path — here, `tests/`. The project root is never added, so `primes`
   can't be found. Write the fix in one sentence:

   ________________________________________________________________

10. Now put the project root on the import path and run it again:

    ```
    # macOS / Linux
    PYTHONPATH=. python tests/test_prime_finder.py

    # Windows PowerShell
    $env:PYTHONPATH="."; python tests/test_prime_finder.py

    # Windows cmd  (two lines - do NOT put "&&" on the set line,
    #               it would assign ". " with a trailing space)
    set PYTHONPATH=.
    python tests/test_prime_finder.py
    ```

    **a. The import error is gone. How many tests ran?**

    ________________________________________________________________

    **b. Why did nothing run?** (Hint: `unittest` files ended with
    `unittest.main()`. pytest has no equivalent — something has to *collect*
    and run them.)

    ________________________________________________________________

    ________________________________________________________________

> **Takeaway:** test files are not scripts. Always run them through the runner:
> `pytest` from the terminal, or PyCharm's run configuration.

---

## Part 3 — Measuring coverage

11. Run the tests properly, both ways:
    - terminal: `pytest`
    - PyCharm: right-click the `tests` directory > **Run 'pytest in tests'**
12. Run the tests **with coverage** (the shield icon, or
    **Run 'pytest in tests' with Coverage**).
13. Generate an **HTML** coverage report and open it in your browser.
14. Filter the results to the `primes` package.
15. Record the coverage stats:

| File | Statements | Missing | Branches | Partial | Coverage % |
|---|---|---|---|---|---|
| `primes/__init__.py` | | | | | |
| `primes/prime_finder.py` | | | | | |
| **TOTAL** | | | | | |

---

## Part 4 — Improving the suite

16. Identify one **untested method** in the `primes` package:

    ________________________________________________________________

17. Identify one **untested statement** (give the line number):

    ________________________________________________________________

18. Identify one **partially tested branch** (give the line number, and say
    which way the branch was never taken):

    ________________________________________________________________

    ________________________________________________________________

19. Write a new test case that increases coverage:

    ```python




    ```

20. Re-run with coverage and regenerate the HTML report.
    **Did coverage improve?** If not, correct your test case and try again.

21. Record the updated stats:

| File | Statements | Missing | Branches | Partial | Coverage % |
|---|---|---|---|---|---|
| `primes/__init__.py` | | | | | |
| `primes/prime_finder.py` | | | | | |
| **TOTAL** | | | | | |

---

## Part 5 — What coverage doesn't tell you

22. From the project root, run:

    ```
    python -c "from primes.prime_finder import PrimeFinder; print(PrimeFinder().list_first_n_primes(10))"
    ```

    **What did it print? Is that correct?**

    ________________________________________________________________

23. Find the existing test for `list_first_n_primes`.
    **What does it assert? What does it fail to assert?**

    ________________________________________________________________

    ________________________________________________________________

24. That test passes, and those lines count as covered.
    **So what does "100% coverage" actually guarantee about this code?**

    ________________________________________________________________

    ________________________________________________________________

---

## Bonus (2 pts on Exam 1)

Reach **100% coverage** on the `primes` package.

- Commit your new test cases.
- Push to your GitHub Classroom repository.
