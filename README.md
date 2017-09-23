# LibChopeBot (CZ1003 Python3 Telegram Bot Project)
https://trello.com/b/S2FfT0F1

Bot chope kursi LWN (Booking)

## Dependencies
- python 3.5.x
- python-telegram-bot (Python Telegram Wrapper -pretty sure)
- splinter (browser automation)

# Comment Convention
- pake beginian kalo niat (?)

      # NOTE: This is here because sometimes an intermittent issue appears.
      # OPTIMIZE: This could be reworked to not do a O(N2) lookup.
      # TODO: from John: Add a check here to ensure these are always strings.
      # HACK: I am doing something here that is horrible, but it works for now...
      # XXX: Let's do this better next time? It's bad.
      # FIXME: We sometimes get an undefined index in this array.
      # BUG: If the user inputs "Easter" we always output "Egg", even if they wanted a "Bunny"

## Style Guide (flake8)
- Please install flake8 linter
- Sebelum kita semua lelah antara satu sama lain
- Kebiasaan CP (variable 3 karakter) mohon bertobat
- Gausah strict" amat but as long as kita sama" nyaman

### TL;DR
- variablesLikeThis
- ClassLikeThis
- GLOBAL_AND_CONST_LIKE_THIS
- function_like_this
- 4 Spaces (NOT TABS)
- Keep it short <78 chars / line
- Op Operand Notation
```python
income = (
    gross_wages
    + taxable_interest
    + (dividends - qualified_dividends)
    - ira_deduction
    - student_loan_interest)
```
- Separate lines for import
```python
import numpy
import math
from foo import bar, baz #acceptable leh
```
- please untuk comment space after '#'
```python
# DO: Like this
#ga kyk begini
```
- NO Trailing Space
- Last line newline

## Some Tips
- kalo bisa di pylint
- pake pyvenv kalo di linux
- sublime text 3 dev itu dewa (gw kasih settingannya nnt)
