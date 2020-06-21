# Counters
![Python package](https://github.com/mavaras/counters/workflows/Python%20package/badge.svg)


**counters** is a code stats monitoring tool that provides both calling counter and flow chain for/between functions. It allows you to see what are your 'heat'/more concurrent functions as well as know what the function call chain is in all or part of your code.
You can use **counters** with sync, async or mixed function call chains.
Additonal features or data are being considered to added to this proyect (WIP).

## Getting started

```python
import counter

@counter
def first():
    third()
    second()

@counter
def second():
    pass

@counter
def third():
    fourth()
    second()

@counter
def fourth():
    second()

@counter
def main():
    for _ in range(2):
        first()

main()
format_levels()
format_calls()
```

Here we have a collection of functions with nested calls. If you run it, all the functions decorated will be traced and you'll have the chain of the execution flow:

```bash
✓ Traced functions nested call chain

    L   1    2    3    4    5    6    7    8    9    10    11
    |    ·-> main
    |    |    ·-> first
    |    |    |    ·-> third
    |    |    |    |    ·-> fourth
    |    |    |    |    |    ·-> second
    |    |    |    |    ·-> second
    |    |    |    ·-> second
    |    |    ·-> first
    |    |    |    ·-> third
    |    |    |    |    ·-> fourth
    |    |    |    |    |    ·-> second
    |    |    |    |    ·-> second
    |    |    |    ·-> second
```

You can also get the calls:

```bash
✓ Traced functions with its number of calls

    second ·-> 6
    fourth ·-> 2
    third ·-> 2
    first ·-> 2
    main ·-> 1
  ```

## Examples
You may take a look at the [examples](https://github.com/mavaras/counters/examples) folder.
