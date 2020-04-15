# Brainfuck VM

A simple brainfuck interpreter in Python 3.

Usage:
```python3
> bf = BrainFuckVM()
> bf.eval('''
    ++++++++++[>+++++++>++++++++++>+++>+<<<<-]
    >++.>+.+++++++..+++.>++.<<+++++++++++++++.
    >.+++.------.--------.>+.>.''')

Hello World

> bf.state()
0 87 100 33 [10] 0 0 0 0 0 
```

## Some examples

Set the value of block #1 as 3
```python
> bf.eval('+++')
> bf.state()

[3] 0 0 0 0 0 0 0 0 0 
```

Set block #1 = 1, move pointer to block #2 and set block #2 = 4
```python
> bf.eval('+>++++')
> bf.state()

1 [4] 0 0 0 0 0 0 0 0 
```

Add 5 + 2 with the result on block #1
```python
> bf.eval('+++++>++[-<+>]')
> bf.state()

7 [0] 0 0 0 0 0 0 0 0 
```

Multiply 4 * 3 with the result on block #3
```python3
> bf.eval('++++>+++[<[->>+>+<<<]>>>[-<<<+>>>]<<-]')
> bf.state()

4 [0] 12 0 0 0 0 0 0 0
```

## More information

Repl.it is very good for comparison (https://repl.it/languages/brainfuck) and a simple tutorial with instructions can be found at https://gist.github.com/roachhd/dce54bec8ba55fb17d3a.