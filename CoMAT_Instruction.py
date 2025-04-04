INSTRUCTION = """Task Description: You are given a college mathematics question. Your task is to convert it into a symbolic representation and solve it using strict logical reasoning, without any reliance on memorized answers or external knowledge. Rigorously follow these steps:

1) Identify and define all the predicates, functions, and variables in the problem.
2) Parse the entire problem into logical rules based strictly on the defined predicates, functions, and variables. Ensure that the multiple-choice options do not influence this step in any way.
3) Write all the facts explicitly mentioned in the problem as logical statements.
4) Parse the question into a symbolic form using only the defined predicates and variables, without any influence from the provided answer choices.
5) Solve the problem step by step using only the symbolic representations and logical reasoning. Provide clear reasoning for each step.
6) Derive the final answer based solely on your symbolic solution and step-by-step reasoning.
7) Only after deriving your answer, match it to the closest option provided, without considering the order or labeling of the options.

IMPORTANT:
- Base your entire solution on the symbolic representation and logical reasoning.
- Do not rely on any prior knowledge, memorized answers, or previous examples.
- The order and labeling of options should not influence your reasoning or answer in any way.
- Evaluate only the symbolic rules and facts you've derived, not the provided answer choices.

After completing the symbolic representation and reasoning, provide the final answer as a single letter corresponding to the option that best matches your derived answer.

This approach ensures an unbiased solution focused entirely on logical reasoning through symbolic rules, minimizing any impact from option swapping or prior knowledge.

The model should **evaluate only the symbolic rules and facts** provided and not the provided answer choices to ensure an unbiased solution. Provide the final answer based purely on logical reasoning as a single letter.

-----------
Here is an example:
Question:
If f(x) = x^2 + 3x + 2 and g(x) = 2x + 1, find f(g(2)).
A: 3
B: 42
C: 5
D: 30
E: 500

Example Answer:
###
1. Define predicates and functions:
   f(x): function that takes x and returns x^2 + 3x + 2
   g(x): function that takes x and returns 2x + 1

2. Parse problem into logical rules:
   ∀x: f(x) = x^2 + 3x + 2
   ∀x: g(x) = 2x + 1

3. Facts:
   No additional facts given.

4. Parse the question:
   Find f(g(2))

5. Solve step by step:
[Think step by step and answer the question]
1. First, we need to calculate g(2):
g(2) = 2(2) + 1 = 4 + 1 = 5
2. Now we have f(g(2)) = f(5)
3. Calculate f(5):
f(5) = 5^2 + 3(5) + 2
= 25 + 15 + 2
= 42

6. Derived answer: 42

7. Match to provided options: B

Final Answer: B

Note: The reasoning process was based solely on the symbolic representation and logical rules, without relying on the order or labeling of the options."""
