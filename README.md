# Counters

![Python package](https://github.com/mavaras/counters/workflows/Python%20package/badge.svg)


**counters** is a code stats monitoring tool that provides both calling counter and flow chain for/between functions. It allows you to see and control what are your 'heat'/more concurrent functions as well as know what the function call chain is in all or part of your code.


You can use **counters** with sync, async or mixed function call chains.


Additonal features or data are being considered to added to this proyect (WIP).

## Getting started
You need to have **python** >= **3.7**
```python
import counter

@counter
def first():
    third()
    second()

@counter
def second():
    print(second.calls)  # you can get any function calls in real-time

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


**counters** provides other features you may use for take control of your code flow.
You can use ***block*** to avoid some function to be executed more than *X* times.

In this example, we only want *first()* to be executed 2 times, independently of the code context given (notice that *range(8)* in *main()*)

```python

@counter(block=2)
def first():
    print('first')
    second()

@counter
def second():
    print('second')

def main():
    for _ in range(8):
        first()

main()
```

If you execute this code you'll get the following output.
```
first
second
first
second
```

So if you call the *format_calls()*, you get that *first()* is only executed ***block*** times.
```
✓ Traced functions with its number of calls

    second ·-> 2
    first ·-> 2
```

## Examples
You may take a look at the [examples](https://github.com/mavaras/counters/tree/master/examples) folder where you'll find both sync and async code.
