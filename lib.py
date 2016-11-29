#!/usr/bin/env python

'''
' lib.py
'
' Class definition and implementatin
' for Turing Machine simulator.
'
' Will Badart
' NOV 2016
'''

class TM:

    #####################
    # Constructor
    # None init(self:TM, defn_fs:file)
    #####################

    def __init__(self, defn_fs):

        # Read in all lines from definition file
        #   Strip whitespace from line endings
        lines = [l.rstrip() for l in defn_fs.readlines()\
                if l.rstrip()]

        # Set TM properties acording to the input file and
        #   the format specified in the project spec
        self.name = lines[0]
        self.E    = lines[1].split(',')  # sigma
        self.G    = self.E + [lines[2]]  # gamma
        self.Q    = lines[3].split(',')
        self.q0   = lines[4]             # initial state
        self.qA   = lines[5]             # accept stats
        self.qR   = lines[6]             # reject state
        self.d    = {}                   # delta

        # Read transition rules into delta
        for i, l in enumerate(lines[7:]):

            # Distinguish the left hand side of the rule
            #   from the right hand side
            lhs, rhs = [h.split(',') for h in l.split('|')]

            # Dump the rule to stdout
            print 'Rule#{}:{}|{}'.format(i + 1,\
                    *[','.join(s) for s in [lhs, rhs]])

            # Log the mapping in self.d
            #    i + 1 is recorded as the rule number
            self.d[(lhs[0], lhs[1])] =\
                    (rhs[0], rhs[1], rhs[2], i + 1)

        # Print a newline for readability
        print


    #####################
    # Top level file test function
    # None test(self:TM, test_fs:file)
    #####################

    def test(self, test_fs):

        # Report the name of the file containing
        #   the strings that will be tested
        print '\n{}\nTEST FILE: "{}"\n'\
                .format(self.name, test_fs.name)

        # Parse the strings and strip trailing whitespace
        strings = [l.rstrip() for l in test_fs.readlines()]
        for s in strings:

            # DFA-like:
            #  Print string acceptance and final
            #  tape configutation
            print '{}:{}\n'.format(\
                    'Accepted' if self.test_string(s)\
                        else 'Rejected',
                    ''.join(self.tape))


    #####################
    # Unit test of individual string
    # bool test_string(self:TM, w:str)
    #####################

    def test_string(self, w):

        # Reset machine
        self.reset()

        # Initialize tape with input string
        #   Report initial tape status
        #   Initialize step # to track transitions
        self.tape = list(w)
        print 'Tape: {}'.format(''.join(self.tape))
        stepno = 1

        while not self.done():

            # Read the tape character
            #   Grab transition for current config
            c   = self.tape[self.head]
            rhs = self.d.get((self.q, c))

            # Sanity check: transition rule exists
            if rhs is None:
                return False

            # Report current configuration
            print '{}@{}#{}:{},{}|{},{},{}'.format(\
                    stepno
                  , self.head\
                    # rule number
                  , rhs[3]\
                  , self.q\
                  , self.tape[self.head]\
                    # new state
                  , rhs[0]\
                    # new tape symbol
                  , rhs[1]\
                    # new tape index
                  , self.head - 1 if rhs[2] == 'L'\
                          else self.head + 1\
                  )

            # Transition to next state, perform
            #   tape operations
            self.transition(rhs)

        return self.accepting()


    #####################
    # Move to the next state based on configuration
    # None transition(self:TM, rhs:4-tuple)
    #####################

    def transition(self, rhs):
        self.q               = rhs[0]
        self.tape[self.head] = rhs[1]
        self.head += 1 if rhs[2] == 'R' else -1
        while self.head >= len(self.tape):
            self.tape.append('_')


    #####################
    # Reports if a final state has been reached
    # bool done(self:TM)
    #####################

    def done(self):
        return self.q == self.qA or self.q == self.qR


    #####################
    # Report current state of acceptance
    # bool accepting(self:TM)
    #####################

    def accepting(self):
        return self.q == self.qA


    #####################
    # Restore TM to initial state, clear stats
    # None reset(self:TM)
    #####################

    def reset(self):
        self.q    = self.q0
        self.tape = []
        self.head = 0

