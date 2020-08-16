from bf_interpreter import bf_interpreter


bf = bf_interpreter(wrapping=True)



# add 2 ints
# s = ",>,[<+>-]<."
s = """
,       ; read character and store it in p1
>       ; move pointer to p2
,       ; read character and store it in p2
[           ; enter loop
    <       ; move to p1
    +       ; increment p1
    >       ; move to p2
    -       ; decrement p2
]           ; we exit the loop when the last cell is empty
<       ; go back to p1
.       ; print p1
"""

# can
s = "++++++++++[>+++++++>++++++>++++++++<<<-]>---.>+++++.>--."

# hello world
s = "++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>++.>+.+++++++..+++.<<++.>+++++++++++++++.>.+++.------.--------.<<+.<."

s = """
>+>+>++>++>++>++++>++[>[<+++++>-]<<]>[<+>-]<
"""

bf.interpret(s)
bf.print_program_array()
