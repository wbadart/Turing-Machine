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
$ ./tm.py --help  # or ./tm.py -h
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
respectively. **A note on the Mystery Machine:** the
files associated with this machine have been renamed
from `Mystery.txt` and `MysterTest.txt` to `MM.txt` and
`MM-Test.txt` to follow the convention of the other
files.

Output
------

This snippet contains the commands to recreate the output
dump. It can be executed simply by running `tail
README.md -n 14 | head -n 12 | sh > output.dump`.

The results have been pre-generated and placed in the file
`output.dump`.

```
for m in `ls M?.txt`; do
    n=`echo $m | cut -b 2`
    if [ -e M$n-Accept.txt ]; then
        ./tm.py $m M$n-Accept.txt
    fi
    if [ -e M$n-Reject.txt ]; then
        ./tm.py $m M$n-Reject.txt
    fi
    if [ -e M$n-Test.txt ]; then
        ./tm.py $m M$n-Test.txt
    fi
done
```

