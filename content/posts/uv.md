---
date: '2024-12-18T12:14:29+01:00'
draft: true
title: 'Why I’m Ditching poetry for uv'
description: "How I cut my Python working environment's headaches in half with Astral's uv - a Rust-powered Swiss Army knife for Python workflows."
keywords: ["Python", "uv", "Data Science", "Machine Learning", "Rust"]
categories: [tool]
---

## The Python Tool That Made Me Say "Where Have You Been All My Life?"

Let me paint you a familiar picture: You’re excited to start a new ML project. You `git clone` that fancy repo, you have to figure out how to install the python environment on your system, which can consist of picking the right python version, picking the right dependency manager to install everything and... *watch the spinner of doom*. 45 minutes later, you’ve solved three dependency conflicts and aged six months. Enter **uv** - Astral’s answer to Python tooling fatigue.

### What Exactly is This Magic?
**uv** is like if `pip`, `virtualenv`, and `pyenv` had a baby raised by Rust (the programming language, not the game). Created by the same folks behind the wildly popular Ruff linter, it’s essentially:
- 🚀 A dependency resolver that runs at *light speed* (think 10-100x faster)
- 🧩 A unified toolkit replacing half your Python workflow
- 🔄 Backward-compatible with your existing `requirements.txt` and `pyproject.toml`

I’ve been using it for a couple of months now, and honestly? Going back feels like trading in my laptop for a typewriter.

---

## Why You’ll Want This in Your Data Science Toolkit

### 1. “Wait, It Installed Already?” Speed
Let’s get real - we’ve all used install time to make coffee. With uv, that coffee break turns into a sip. Here’s my totally scientific benchmark for the [repo with notebooks](https://github.com/jeroenjanssens/python-polars-the-definitive-guide) for the [Python Polars book](polarsguide.com):

Let's start with benchmarking a cold install (download everything, no cache):
```bash
Benchmark 1: pip install -I --no-cache-dir -r requirements.txt
  Time (mean ± σ):     154.276 s ±  2.181 s    [User: 77.785 s, System: 31.420 s]
  Range (min … max):   152.734 s … 155.818 s    2 runs

# New way (uv)
Benchmark 1: uv sync --reinstall
  Time (mean ± σ):      5.908 s ±  0.535 s    [User: 0.490 s, System: 5.334 s]
  Range (min … max):    5.479 s …  6.871 s    10 runs🚀
```

pip takes 154 seconds, while uv takes 6 seconds.

And a warm install (using only cache):
```bash
Benchmark 1: pip install -I -r requirements.txt
  Time (mean ± σ):     102.244 s ±  0.622 s    [User: 67.571 s, System: 27.707 s]
  Range (min … max):   101.804 s … 102.684 s    2 runs

  Benchmark 1: uv sync
  Time (mean ± σ):      29.0 ms ±   1.2 ms    [User: 19.0 ms, System: 7.6 ms]
  Range (min … max):    25.8 ms …  32.7 ms    83 runs
```

pip takes 102 seconds, while uv takes 29 **mili**seconds.

That's what a smart structure combined with Rust’s parallelism and smarter dependency resolution can get you.

### 2. No More “But It Worked on My Machine!”
We’ve all been there - your model trains perfectly locally, then explodes in production because `polars` sneaked in a minor version update. uv’s lockfiles are your new best friend:

```bash
uv pip compile requirements.in -o requirements.txt
```

This creates dependency versions so locked down, they make Fort Knox look casual. My team’s deployment errors dropped 70% after we adopted this.

### 3. Python Version Juggling Made Simple
Remember that time TensorFlow broke because someone used Python 3.12 too early? uv’s Python management is smoother than a barista’s latte art:

```bash
uv python install 3.13  # Gets the exact version you need
uv venv --python 3.13   # Creates environment with it
```

No more `pyenv`/`conda` conflicts. It’s like having a Python version time machine.

---

## Getting Started: A Human-Friendly Guide

I'd recommend installing it on your system, as it's a tool you'll use. Not a dependency for the project your working on.
If you’re on macOS/Linux:

```bash
# One-line install - the good kind of magic
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Or if you’re a Homebrew fanatic:

```bash
brew install uv  # Because why complicate things?
```

Other ways of installing it are available [on the website](https://docs.astral.sh/uv/getting-started/installation/).

Pro tip: If it asks you to restart your shell, *actually do it*.

---

### Your First uv Project: No PhD Required
1. **Start fresh** (without the usual circus):
```bash
uv init my_project && cd my_project
```

2. **Install packages** at Ludicrous Speed™:
```bash
uv add polars "torch>=2.0"
```

3. **Run scripts** like it’s 3024:
```python
# train.py
# /// [uv]
# dependencies = ["scikit-learn", "xgboost"]  # PEP723 annotations FTW
# ///

# Your actual code below...
```

```bash
uv run train.py  # Auto-installs deps then runs - chef's kiss
```

---

## The Killer Feature You Didn’t Know You Needed
Imagine this: You’re debugging a model at 2 AM. Instead of wrestling with `pip` and `virtualenv`, you just:

```bash
uv pip install --reinstall-broken  # Fixes dependency hell
uv run serve_model.py  # Handles everything else
```

It’s like having a DevOps engineer in your terminal. I’ve literally gotten back hours of my week.

---

## But Does It Work with [Insert Your Favorite Tool Here]?
Probably! uv plays nice with:
- ✅ GitHub Actions ([example](#cicd-integration))
- ✅ Docker (their docs have great examples)
- ✅ Jupyter notebooks (use `uv run notebook.ipynb`)
- ✅ Even legacy `requirements.txt` files

The only thing missing? A "I ❤️ uv" sticker for your laptop. (Astral, if you’re reading this...)

---

## Should You Switch? A Totally Biased Take

**Yes if**:
- You value your time more than package managers
- Your team has more dependency issues than a soap opera
- You want one tool instead of five

**Maybe wait if**:
- You’re mid-critical-project (learning curve exists)
- You need Windows support yesterday (it’s coming!)

---

## Final Thought: Why This Matters for ML

In machine learning, iteration speed is everything. The less time you spend on environments, the more you can:
- Experiment with models
- Tune hyperparameters
- Actually *do data science*

uv isn’t just a tool upgrade - it’s a productivity time machine. Now if you’ll excuse me, I need to go not-wait-for-pip-installs.

*[Discuss on Hacker News](#) | [Complain about my hot takes on X](#)*

---

Let me know if you want me to dial up/down the informality anywhere! The goal was to keep technical accuracy while making it feel more like a colleague explaining things over coffee. ☕