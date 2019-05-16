from typing import Generic, TypeVar, Dict, List, Optional
from abc import ABC, abstractmethod

# new type for program
V = TypeVar('V')

# base for all Constraints
class Constraint(Generic[V,D], ABC):
    # variables that the Constraint is between
    def __init__(self,variables: List[V]) -> None:
        self.variables = variables

        # must be overridden by subclasses
        @abstractmethod
        def satisfied(self, assignment: DICT[V,D] -> bool):
            ...

class CSP(Generic[V,D]):
    # creates the constraints dict
    def __init__(self, variables: List[V], domains: Dict[V, List[D]]) -> None:
        self.variables: List[V] = variables # variables to be constrained
        self.domains: Dict[V,List[D]] = domains
        self.constraints: Dict[V, List[Constraint[V, D]] = {}

        for variable in self.variables:
            self.constraints[variable] = []
            if variable not in self.domains:
                raise LookupError("Every variable should have a domain assigned to it")

    # goes through all of the variables touched by a given constraint and adds itself
    # to the constraints mapping for each of them
    def add_constraint(self, constraint: Constraint[V,D]) -> None:
        for variable in constraint.variables:
            if variable not in self.variables:
                raise LookupError('Variable in constraint not in CSP')
            else:
                self.constraints[variable].append(constraint)

    # check assignment variables constraints are met
    def consistent(self, variable: V, assignment: Dict[V,D]) -> bool:
        for constraint in self.constraints[variable]:
            if not constraint.satisfied(assignment):
                return False
        return True

    def backtracking_search(self, assignment: Dict[V, D] = {}) -> Optional[Dict[V, D]]:
        # assignment is complete if every variable is assigned (our base case)
        if len(assignment) == len(self.variables):
            return assignment

            # get all variables in the CSP but not in the assignment
            unassigned: List[V] = [v for v in self.variables if v not in assignment]

            # get the every possible domain value of the first unassigned variable
            first: V = unassigned[0]
            for value in self.domains[first]:
                local_assignment = assignment.copy()
                local_assignment[first] = value
                # if we're still consistent, we recurse (continue)
                if self.consistent(first, local_assignment):
                    result: Optional[Dict[V, D]] = self.backtracking_search(local_assignment)
            # if we didn't find the result, we will end up backtracking
                if result is not None:
                    return result
    return None
