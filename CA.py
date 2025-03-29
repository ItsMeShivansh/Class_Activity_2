def find_cube_pairs(target):  # Collon was missing after function declaration 
    solutions = [];
    max_num = round(target ** (1/3))  # Error: targ, Correction: target, Error: ***, Correction: ***

    for a in range(1, max_num + 1):   # Error: ranges , Correction: ranges,  Error: colon missing, Correction: added colon
        for b in range(a, max_num + 1):      # Error: ranges, Correction: ranges, Error: colon missing, Correction: added colon
            if a**3 + b**3 == target:    # Error: targ, Correction: target, Error: colon missing, Correction: added colon
                solutions.append((a, b));  # Error: sol, Correction: solutions
    return solutions    # Error: sol, Correction: solutions

pairs = find_cube_pairs(1729)    # Error: extra commas
print("Valid cube pairs for 1729:")      # Error: printf,  Correction: print, Error: 1728, # Correction: 1729
for a, b in pairs:      # Error: pair  Correction: pairs, Error: colon missing, Correction: added colon
    print(f" → {a}³ + {b}³ = {a**3} + {b**3} = 1728")   # Error: printf,  Correction: print

