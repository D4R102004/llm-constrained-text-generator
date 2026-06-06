# llm-constrained-text-generator

Message generation system under structural constraints using LLMs as generator and evaluator.

Built for the Artificial Intelligence course (2025-2026) at Universidad de La Habana.

## What it does

Given a set of structural constraints (length, tone, forbidden words, required topics,
format rules), the system generates messages that satisfy ALL constraints.
The LLM acts as both generator and evaluator in an optimization loop.

## Requirements

- Python 3.12+
- [Ollama](https://ollama.com) running locally with `llama3.2:3b`

## Setup

### 1. Clone and create virtual environment

```bash
git clone git@github.com:D4R102004/llm-constrained-text-generator.git
cd llm-constrained-text-generator
python3.12 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
make install
```

### 3. Configure

```bash
cp .env.example .env
# Edit .env if needed
```

### 4. Start Ollama and pull the model

```bash
ollama pull llama3.2:3b
```

### 5. Run

```bash
make run
```

### 6. Run tests

```bash
make test
```

### 7. Run experiments

```bash
python experiments/run.py
```

Results are saved to `experiments/results/results.json`.

## Project structure

```text
src/ai_project/
  constraints/   — constraint definitions and validators
  generator/     — LLM-based message generation
  evaluator/     — LLM-based constraint satisfaction scoring
  optimizer/     — search algorithm
  dataset/       — test instance generation
  interface/     — CLI entry point
  utils/         — shared helpers

experiments/     — configs and results
docs/            — technical report
notebooks/       — exploratory analysis
```

## Architecture

The system uses an optimization loop where:

1. The **generator** (LLM) produces candidate messages given constraints.
2. The **evaluator** (LLM) scores each candidate against all constraints.
3. The **optimizer** (search algorithm) guides generation toward better solutions.

## License

Academic project — Universidad de La Habana, 2025-2026.
