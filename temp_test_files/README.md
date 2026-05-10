# Temporary Test Files

This folder holds ad hoc, historical, or one-off test/debug files that used to sit in the repository root.

Use this folder for:

- manual diagnosis scripts
- old root-level `test_*.py` experiments
- temporary chart/debug HTML
- temporary Vercel or dev-server logs
- generated verification scripts that are not part of the formal suite

Do not use this folder for formal regression tests. Put maintained pytest coverage in `tests/`.

The application does not depend on files in this folder at runtime.
