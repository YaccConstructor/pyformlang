"""
The :mod:`pyformlang.finite_automaton` module deals with finitie state automata.
"""

from .deterministic_finite_automaton import DeterministicFiniteAutomaton
from .state import State
from .symbol import Symbol
from .transition_function import TransitionFunction, DuplicateTransitionError

__all__ = ["DeterministicFiniteAutomaton",
           "State",
           "Symbol",
           "TransitionFunction",
           "DuplicateTransitionError"]