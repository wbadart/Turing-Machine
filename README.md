Turing Machine Simulator
========================

This Python (2.x) based program simulates the behavior of
a Turing machine based on a definition file. The program
is tuned to simulate *language recognizers* rather than
general computing machines.

Usage
-----

The program requires [Python 2](https://python.org) and
has been tested and verified specifically on version
2.7.12.

```
usage: ./tm.py DEFN_FNAME TEST_FNAME [ -h ]
    DEFN_FNAME     Name of file containing TM definition
    TEST_FNAME     Name of file containing test strings
    -h             Show this help message
```

Student Test Machine
--------------------

The specifications for the student test machine are in
`M4.txt`. `M4-Accept.txt` and `M4-Reject.txt` contain
lists of strings that M4 should accept and reject,
respectively.

Output
------

This snippet contains the commands to recreate the output
dump.

```
for m in `ls M?.txt`; do
    n=`echo $m | cut -b 2`
    if [ -e M$n-Accept.txt ]; then
        ./tm.py $m M$n-Accept.txt >> output.dump
    fi
    if [ -e M$n-Reject.txt ]; then
        ./tm.py $m M$n-Reject.txt >> output.dump
    fi
done
```

