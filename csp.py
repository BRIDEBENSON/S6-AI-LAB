def csp_backtracking(assignment, VARIABLES, DOMAINS):
    if len(assignment) == len(VARIABLES):
        return assignment
    for var in VARIABLES:
        if var not in assignment:
            unassigned_var = var
            break
    for value in DOMAINS:
        assignment[unassigned_var] = value
        if is_consistent(assignment):
            result = csp_backtracking(assignment, VARIABLES, DOMAINS)
            if result:
                return result
        assignment.pop(unassigned_var)
    return None

def is_consistent(assignment):
    values = list(assignment.values())
    return len(values) == len(set(values))


assignment = {}
VARIABLES = ["var1", "var2", "var3"]
DOMAINS = ["Monday", "Tuesday", "Wednesday"]
    
solution = csp_backtracking(assignment, VARIABLES, DOMAINS)

if solution:
    print("Solution found:")
    print(solution)
else:
    print("No solution found.")