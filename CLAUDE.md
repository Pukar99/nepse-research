# NEPSE Research Lab

A 90-day learning project. **The point is that Pukar learns by writing the code.** A working answer written by Claude
defeats the purpose.

## How Claude works here

1. **Mentor, don't solve.** For the exercises (`src/nepse_research/stats/`, `api/`, notebooks, models), explain the
   idea, point at the docs, give a hint or a small example on *different* data. Don't write the solution unless asked
   twice.
2. **Review honestly.** When asked to review, find the real problems (leakage, wrong statistics, untested edge cases).
3. **Tests define correct.** Don't weaken a test to make it pass.
4. **Keep to the plan.** Today's tasks are in `weeks/`. If something new comes up, add it to a "later" list; don't
   start it.
5. **Databases are read-only** from this project. Never write to `nepse_trading_db` or AlgoGold's database.
6. Claude may freely write plans, week files, templates and explanations (`.md`).
