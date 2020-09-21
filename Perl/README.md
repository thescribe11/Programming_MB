## Changes:

Added input validation to fix the bug where non-numerical values are evaluated as the scalar value 0.

## Industry:

Automation.

## How to run:

1. Open your terminal.
2. `cd` to the directory holding the scripts.
3. `~/$ perl <script>`. This works on Linux without having to install anything; since you have a Mac, it might be different.


## Program Logic

```
start
|
<while loop until user says doesn't want to continue>
    | - Accept user input
    | - Make sure input is a float
    | - Convert to Celsius
    | - Print Celsius
    | - If Farenheit > 100:
        | - Give high heat warning
    | - Else if farenheit < 0:
        | - Give low heat warning
    | - Ask if user wants to continue
|
Progam end
```
