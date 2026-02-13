# Math Reasoning Agent with Process Supervision

A math reasoning agent that uses **Tool-Integrated Reasoning (TIR)** with LLM-based self-critique. Designed for evaluating and collecting step-level trajectories on the [Omni-MATH](https://huggingface.co/datasets/KbsdJames/Omni-MATH) dataset (4,428 olympiad-level problems).

Supports **Qwen2.5-Math-7B-Instruct** and **DeepSeek-Math-7B-Instruct** served via [vLLM](https://github.com/vllm-project/vllm).

---

## Agent Flow

The agent runs a multi-turn loop where **reasoning**, **code execution**, and **critique** are interleaved. Here is the exact sequence for each turn:

```
┌──────────────────────────────────────────────────────────────────┐
│  TURN N                                                          │
│                                                                  │
│  1. THINK (Generate)                                             │
│     Model generates text given [system prompt, problem, history] │
│     Generation stops on: "```output", max_tokens, or EOS        │
│     ↓                                                            │
│  2. PARSE                                                        │
│     Split response into typed chunks:                            │
│       • REASONING — natural-language reasoning paragraphs        │
│       • CODE      — ```python ... ``` blocks                    │
│       • ANSWER    — text containing \boxed{...}                  │
│     ↓                                                            │
│  3. CHECK: Does the response contain \boxed{...}?               │
│     YES → extract final answer, end loop                         │
│     NO  → continue to step 4                                     │
│     ↓                                                            │
│  4. ACT (Execute Code)                                           │
│     If a ```python block was detected:                           │
│       • Run code in a subprocess (timeout: 30s)                  │
│       • Pre-imports: sympy, math, numpy, fractions, itertools    │
│       • Capture stdout or traceback                              │
│       • Inject result as ```output\n...\n``` into messages       │
│     ↓                                                            │
│  5. CRITIQUE (LLM Self-Critique)                                 │
│     If critique is enabled and due this turn:                    │
│       • Make a SEPARATE LLM call with the critique prompt        │
│       • Send: problem + all reasoning so far + current step      │
│       • Parse structured response (CORRECT/ERROR/SUGGESTION)     │
│       • If error found → inject "[Critique]: ..." into messages  │
│       • If correct → do nothing, continue                        │
│     ↓                                                            │
│  6. Loop back to step 1 for TURN N+1                             │
│     (up to max_turns, default 15)                                │
└──────────────────────────────────────────────────────────────────┘
```

### Concrete Example

For a problem like _"What is the sum of the first 100 positive integers?"_:

| Turn | What happens | Message injected |
|------|-------------|-----------------|
| 1 | Model reasons: "I can use the formula n(n+1)/2..." then writes a `python` block: `print(100 * 101 // 2)` | — |
| 1 | Code executes → stdout: `5050` | ````output\n5050\n``` ` |
| 1 | Critique checks the reasoning step → CORRECT: yes | _(nothing injected)_ |
| 2 | Model sees the output `5050`, writes: "The answer is \boxed{5050}" | — |
| — | Loop ends. Final answer: `5050` | — |

### Critique Scheduling

Critique frequency is configurable:

| Config | Behavior |
|--------|----------|
| `frequency: 1` | Critique runs every turn |
| `frequency: 3` | Critique runs every 3rd turn |
| `after_code_only: true` | Critique runs only after code output steps |
| `enabled: false` | No critique at all (faster, for sampling runs) |

When critique detects an error, the feedback is injected as a user message so the model can self-correct in the next turn.

---

## Project Structure

```
src/
  config.py                      # Pydantic settings (model, generation, tools)
  agent/
    base.py                      # Core agent loop: generate → parse → execute → observe
    math_agent.py                # High-level orchestrator (setup client + tools + loop)
    parser.py                    # Parse model output: ```python blocks, \boxed{}, reasoning steps
    prompts.py                   # System prompts (Qwen TIR, DeepSeek, critique template)
  tools/
    python_interpreter.py        # Subprocess executor with timeout, sympy pre-imported
    critique.py                  # LLM-based critique with structured output parsing
  backend/
    vllm_client.py               # Async client wrapping vLLM's OpenAI-compatible API
  data/
    trajectory.py                # Pydantic models: Step, StepType, Trajectory, CritiqueResult
    collector.py                 # Buffered JSONL export + summary statistics
  evaluation/
    omnimath.py                  # Load Omni-MATH from HuggingFace, filter by domain/difficulty
    answer_extraction.py         # Extract \boxed{}, normalize LaTeX, compare (string + numeric + sympy)
    metrics.py                   # Accuracy, per-domain/difficulty breakdown, step-level stats

scripts/
  run_single.py                  # Run agent on one problem (interactive or CLI)
  evaluate.py                    # Batch evaluation on Omni-MATH
  analyze_results.py             # Error analysis: categorize failures by type

configs/
  qwen_7b.yaml                  # Qwen2.5-Math-7B-Instruct (greedy, critique ON)
  deepseek_7b.yaml              # DeepSeek-Math-7B-Instruct (greedy, critique ON)
  qwen_7b_majority.yaml         # Qwen2.5-Math-7B-Instruct (temp=0.7, critique OFF, for sampling)
```

---

## Setup

### 1. Install Python dependencies

```bash
# Create and activate a conda environment
conda create -n process-supervision python=3.12 pip -y
conda activate process-supervision

# Install requirements
pip install -r requirements.txt
```

### 2. Start the vLLM server

The agent talks to a vLLM server via its OpenAI-compatible API. You need a GPU machine with enough VRAM (~16 GB for a 7B model).

**For Qwen2.5-Math-7B-Instruct:**

```bash
python -m vllm.entrypoint.openai.api_server \
    --model Qwen/Qwen2.5-Math-7B-Instruct \
    --host 0.0.0.0 \
    --port 8000 \
    --dtype auto \
    --max-model-len 4096
```

**For DeepSeek-Math-7B-Instruct:**

```bash
python -m vllm.entrypoint.openai.api_server \
    --model deepseek-ai/deepseek-math-7b-instruct \
    --host 0.0.0.0 \
    --port 8000 \
    --dtype auto \
    --max-model-len 4096
```

Verify the server is up:

```bash
curl http://localhost:8000/v1/models
```

### 3. (Optional) Adjust config

Edit the YAML files in `configs/` to change:
- `model.api_base` — if vLLM is running on a different host/port
- `model.served_model_name` — if you used `--served-model-name` when starting vLLM
- `critique.enabled` — set to `false` to disable critique for faster runs
- `generation.temperature` — `0.0` for greedy, `0.7` for diverse sampling
- `max_turns` — maximum agent loop iterations (default 15)

---

## Running the Pipeline

### Run on a Single Problem

**Pass a problem directly on the command line:**

```bash
python scripts/run_single.py \
    --config configs/qwen_7b.yaml \
    --problem "What is the sum of all positive integers less than 100 that are divisible by 3 or 5?" \
    --ground-truth "2318"
```

**Interactive mode (type the problem, press Enter on an empty line to submit):**

```bash
python scripts/run_single.py --config configs/qwen_7b.yaml
```

**With debug logging to see every LLM call and code execution:**

```bash
python scripts/run_single.py --config configs/qwen_7b.yaml --problem "Solve x^2 - 5x + 6 = 0" -v
```

The trajectory is saved to `results/qwen_7b/single_run.json`.

### Run Batch Evaluation on Omni-MATH

**Evaluate on the full dataset (4,428 problems):**

```bash
python scripts/evaluate.py --config configs/qwen_7b.yaml
```

**Evaluate on a subset (first 50 problems):**

```bash
python scripts/evaluate.py --config configs/qwen_7b.yaml --max-problems 50
```

**Filter by domain or difficulty:**

```bash
python scripts/evaluate.py \
    --config configs/qwen_7b.yaml \
    --domain algebra \
    --difficulty "easy" \
    --max-problems 100
```

**Run with concurrency (multiple problems solved in parallel):**

```bash
python scripts/evaluate.py \
    --config configs/qwen_7b.yaml \
    --max-problems 200 \
    --concurrency 4
```

**Use a different model:**

```bash
python scripts/evaluate.py --config configs/deepseek_7b.yaml --max-problems 50
```

**Override output directory:**

```bash
python scripts/evaluate.py \
    --config configs/qwen_7b.yaml \
    --max-problems 50 \
    --output-dir results/experiment_001
```

Evaluation outputs:
- `results/<model>/trajectories.jsonl` — full step-level trajectories for every problem
- `results/<model>/report.json` — accuracy breakdown by domain and difficulty

### Run Error Analysis

After evaluation, analyze what went wrong:

```bash
python scripts/analyze_results.py results/qwen_7b/trajectories.jsonl
```

**Save the analysis report to a file:**

```bash
python scripts/analyze_results.py results/qwen_7b/trajectories.jsonl -o results/qwen_7b/error_analysis.json
```

The analysis categorizes failures into:

| Category | Meaning |
|----------|---------|
| `no_answer` | Agent exhausted max turns without producing `\boxed{}` |
| `wrong_reasoning` | Wrong answer, no code was used |
| `computation_error` | Code execution returned an error/traceback |
| `critique_missed` | Critique marked a wrong step as correct |
| `critique_rejected` | Critique flagged an error but the model didn't fix it |
| `wrong_code_logic` | Code ran successfully but produced the wrong result |
| `other` | Doesn't fit the above categories |

---

## Configuration Reference

All configs use the same schema (see `src/config.py`). Key fields:

```yaml
model:
  name: "Qwen/Qwen2.5-Math-7B-Instruct"   # HuggingFace model name
  api_base: "http://localhost:8000/v1"       # vLLM server URL
  api_key: "EMPTY"                           # API key (vLLM default)

generation:
  temperature: 0.0      # 0.0 = greedy, 0.7 = diverse sampling
  top_p: 1.0            # nucleus sampling parameter
  max_tokens: 2048      # max tokens per generation
  stop_sequences:        # stop generation on these strings
    - "```output"

critique:
  enabled: true          # toggle critique on/off
  frequency: 1           # critique every N turns
  after_code_only: false  # only critique after code execution

python_tool:
  enabled: true
  timeout_seconds: 30    # kill subprocess after this many seconds

max_turns: 15            # max agent loop iterations
max_context_tokens: 3800 # stay under model's 4K context window
output_dir: "results/qwen_7b"
```

---

## Trajectory Data Format

Each trajectory is stored as a JSON line in `trajectories.jsonl`. Structure:

```json
{
  "problem": "What is 2 + 2?",
  "ground_truth": "4",
  "steps": [
    {"step_idx": 0, "step_type": "reasoning", "content": "This is a simple addition..."},
    {"step_idx": 1, "step_type": "code", "content": "print(2 + 2)"},
    {"step_idx": 2, "step_type": "code_output", "content": "```output\n4\n```"},
    {"step_idx": 3, "step_type": "answer", "content": "The answer is \\boxed{4}"}
  ],
  "final_answer": "4",
  "is_correct": true,
  "model_name": "Qwen/Qwen2.5-Math-7B-Instruct",
  "metadata": {"domain": "algebra", "difficulty": "easy", "problem_idx": 42}
}
```

Step types: `reasoning`, `code`, `code_output`, `critique`, `answer`. This format is designed for downstream PRM (Process Reward Model) training — each step can be annotated with a `label` field (correctness score 0-1).
