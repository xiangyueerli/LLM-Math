LLM-Math is a comprehensive evaluation framework for assessing large language models on college-level mathematics tasks. The project leverages multiple evaluation methods—including Baseline (non-cot), Chain-of-Thought (cot), and CoMAT (comat)—to process the MMLU Redux dataset and generate detailed results in CSV and JSON formats. It integrates key scripts for dataset processing (mmlu_redux.py), evaluation execution (main.py), and analytical assessment (shapley_value_evaluation.py), while providing supporting utilities (utils.py). The framework not only delivers comprehensive logs and output files but also conducts Shapley value analysis to quantify the contributions of individual components in the evaluation, ensuring a robust and transparent benchmarking process.

## File Descriptions

### `main.py`

This is the main script that sets up the entire process. It involves loading datasets, model initialisation, and evaluation.


To execute the main script, use the following command:

```bash
cd MMLU_NLU
```

```bash
python main.py --dataset  mmlu-redux-college_mathematics  --method <method_name> --model <model_name> 
```

Available methods include:

- comat: CoMAT

### `mmlu_redux.py`

This file contains functions used to processing the MMLU-Redux datasets.

- **`process_mmlu_redux_questions`**: Processes questions from the MMLU-Redux dataset and evaluates them.

### `MMLU-Redux-College_Mathematics/`

This directory contains CSV files that store output for MMLU-Redux-College_Mathematics (using GPT-4o model) dataset:

- **`CoMAT_MMLU-Redux-College_Mathematics.csv`**: Stores the output for the MMLU-Redux-College-Mathematics dataset using the CoMAT method.
- **`CoT_MMLU-Redux-College_Mathematics.csv`**: Stores the output for the MMLU-Redux-College-Mathematics dataset using the CoT method.

### `MMLU-Redux-college_mathematics_prompts/`

This directory contains prompt files associated with the College Mathematics dataset:

- **`comat.txt`**: Prompt file for the CoMAT method.

### `shapley_value_evaluation.py`

This script evaluates the Shapley value, a concept from cooperative game theory. The Shapley value is used to fairly distribute the total gains among participants based on their individual contributions.

### `utils.py`

This file contains the functions for making predictions using different models and evaluating their outputs, the model includes : 

- **`predict_gpt`**: Uses OpenAI's GPT model to generate a response based on the provided messages.
