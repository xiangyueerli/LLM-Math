import pandas as pd
import itertools
import numpy as np

steps = [1, 2, 3, 4]

def get_missing_steps(row, steps):
    """
    Get missing steps as a tuple for each row.
    
    Example:
        Input: row = {'step1_missing': 1, 'step2_missing': 0, 'step3_missing': 1, 'step4_missing': 0},
               steps = [1, 2, 3, 4]
        Output: (2, 4)
    """
    missing_steps = [step for step in steps if row[f'step{step}_missing'] == 0]
    return tuple(sorted(missing_steps))

def generate_all_subsets(steps):
    """
    Generate all possible subsets for the missing steps.

    Example:
        Input: steps = [1, 2, 3]
        Output: [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]
    """
    all_subsets_missing = []
    for r in range(len(steps) + 1):
        subsets_r = list(itertools.combinations(steps, r))
        all_subsets_missing.extend(subsets_r)
    return all_subsets_missing

def compute_v_S(df, all_subsets_missing):
    """
    Compute v(S) for all subsets of missing steps.

    Example:
        Input: 
            df = pd.DataFrame({'missing_steps': [(), (1,), (2,), (1, 2)], 'is_correct': [0.8, 0.7, 0.6, 0.5]})
            all_subsets_missing = [(), (1,), (2,), (1, 2)]
        Output: 
            v_S = {(): 0.8, (1,): 0.7, (2,): 0.6, (1, 2): 0.5}
    """
    v_S = df.groupby('missing_steps')['is_correct'].mean().to_dict()
    return v_S

def compute_marginal_contributions(steps, v_S):
    """
    Compute the marginal contributions for each step.

    Example:
        Input:
            steps = [1, 2]
            v_S = {(): 0.85, (1,): 0.67, (2,): 0.72, (1, 2): 0.75}
        Output:
            Delta_sum = {1: 0.08, 2: 0.12}, valid_permutations_count = 2
    """
    permutations = list(itertools.permutations(steps))
    Delta_sum = {i: 0.0 for i in steps}
    valid_permutations_count = 0

    total_steps_set = set(steps)

    for pi in permutations:
        valid_permutation = True
        for i in steps:
            idx_i = pi.index(i)
            S_i = list(pi[:idx_i])
            missing_S_i_sorted = tuple(sorted(S_i))
            missing_S_i_union_i_sorted = tuple(sorted(S_i + [i]))
            v_S_i = v_S.get(missing_S_i_sorted, np.nan)
            v_S_i_union_i = v_S.get(missing_S_i_union_i_sorted, np.nan)
            if np.isnan(v_S_i) or np.isnan(v_S_i_union_i):
                valid_permutation = False
                break
            else:
                delta = v_S_i_union_i - v_S_i
                Delta_sum[i] += delta
        if valid_permutation:
            valid_permutations_count += 1
    return Delta_sum, valid_permutations_count

def compute_shapley_values(Delta_sum, valid_permutations_count, steps):
    """
    Compute the Shapley values for each step.

    Example:
        Input: 
            Delta_sum = {1: 0.08, 2: 0.12}
            valid_permutations_count = 2
            steps = [1, 2]
        Output: 
            Shapley_values = {1: 0.04, 2: 0.06}
    """
    shapley_values = {i: Delta_sum[i] / valid_permutations_count for i in steps}
    return shapley_values

def main():
    df = pd.read_csv('evaluation_with_steps.csv')

    df['missing_steps'] = df.apply(get_missing_steps, axis=1, args=(steps,))

    ######################################################################################
    # Question 7.1: INSERT CODE HERE: Generate all possible subsets for the missing steps#
    ######################################################################################
    ###############################################
    # Question 7.2: INSERT CODE HERE: Compute v(S)#
    ###############################################
    #############################################################
    # Question 7.3: INSERT CODE HERE: Compute the Shapley values#
    #############################################################
    all_subsets = generate_all_subsets(steps)
    v_S = compute_v_S(df, all_subsets)
    Delta_sum, valid_count = compute_marginal_contributions(steps, v_S)
    shapley_values = compute_shapley_values(Delta_sum, valid_count, steps)
    print("Shapley values:", shapley_values)
if __name__ == "__main__":
    main()
