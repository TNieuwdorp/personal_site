---
date: "2025-01-17T18:58:03+01:00"
title: "Why I'm Ditching poetry for uv"
description: "How I cut my Python working environment's headaches in half with Astral's uv - a Rust-powered Swiss Army knife for Python workflows."
keywords: ["Python", "uv", "Data Science", "Machine Learning", "Rust"]
categories: [tool]
---

## Where Have You Been All My Life?

Let me paint you a familiar picture: You're excited to start a new Python project.
You `git clone` that fancy repo and you have to figure out how to install the python environment on your system. 
It can consist of installing the right python version, picking the right dependency manager to install everything and waiting 45 minutes for everything to install, only to run into yanked versions, or incompatibilities for your specific config.
Enter **uv** - Astral's answer to Python tooling fatigue.

### What Exactly is This Magic?
**uv** is like if `pip`, `virtualenv`, and `pyenv` had a baby raised by Rust. 
Created by the same folks behind the wildly popular `ruff` linter, it's essentially:
- 🧩 A unified toolkit replacing half your Python workflow
- 🚀 A dependency resolver that runs at *light speed* (think 10-100x faster)
- 🔄 Backward-compatible with your existing `requirements.txt` and `pyproject.toml`

I've been using it for a couple of months now, and honestly? 
Going back would feel like punishment.

---

## Why You'll Want This in Your Data Science Toolkit

### 1. “Wait, It Installed Already?” Speed
Let's get real - we've all used install time to make coffee. With uv, that coffee break turns into a sip. I've benchmarked the install times for `pip` and `uv` for the [repo with notebooks](https://github.com/jeroenjanssens/python-polars-the-definitive-guide) for our [Python Polars book](polarsguide.com), and these are the results:

![Benchmark showing the difference between pip for a cold and a warm install.](/images/benchmark.png "Benchmark")

For a cold install (where the package managers have to download everything) pip takes 154 seconds, while uv takes 6 seconds.
For a warm install (where all packages are in cache) pip takes 102 seconds, while uv takes 29 **mili**seconds.

That's what a smart structure combined with Rust's parallelism and smarter dependency resolution can get you.

### 2. Environment Ready To Go
Much like `poetry`, `uv` works with lockfiles.
In these files the specific versions are saved so that you can test that everything works in that specific configuration.
But on top of that `uv` also takes care of you having the right python version to run everything with. 
This makes one `uv sync` the only command you run to get up and running.

### 3. Python Version Juggling Made Simple
Remember that time `numpy` broke because someone used Python 3.12 too early? `uv`'s Python management is smoother than a barista's latte art:

```bash
uv python install 3.13  # Gets the exact version you need
uv venv --python 3.13   # Creates environment with it
```

No more `pyenv`/`conda` conflicts or trouble getting the right version on your system.

---

## Getting Started: A Human-Friendly Guide

I'd recommend installing it on your system, as it's a tool you'll use. Not a dependency for the project your working on.
If you're on macOS/Linux:

```bash
# One-line install - the good kind of magic
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Or if you're a Homebrew fanatic:

```bash
brew install uv  # Because why complicate things?
```

Other (subpar) ways of installing it are available [on the website](https://docs.astral.sh/uv/getting-started/installation/).

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

3a. **Set-up virtual environment**:
```bash
uv sync
source .venv/bin/activate
```

3b. **Run scripts** like it's 3025:
```python
# plot.py
# /// [uv]
# dependencies = ["polars", "plotnine"]  # PEP723 annotations FTW
# ///

# Your actual code below...
```

```bash
uv run plot.py
```
Auto-installs deps into an ephemeral environment and then runs it - chef's kiss

---

## But Does It Work with [Insert Your Favorite Tool Here]?
Probably! uv plays nice with:
- ✅ GitHub Actions ([example](#cicd-integration))
- ✅ Docker (their docs have great examples)
- ✅ Jupyter notebooks (use `uv run notebook.ipynb`)
- ✅ Even legacy `requirements.txt` files
- ⛔️ A [tool.poetry] set-up in pyproject.toml (But it's relatively easy to migrate)

The only thing missing? A "I ❤️ uv" sticker for your laptop. (Astral, if you're reading this...)

---

## Should You Switch?

**Yes if**:
- You value your time more than package managers
- You want one tool instead of five

**Maybe wait if**:
- You're mid-critical-project (learning curve exists)
- Your project config is a nightmare to migrate
- Your life depends on [dependabot support](https://github.com/dependabot/dependabot-core/issues/10478) (Coming this quarter!)

---

`uv` isn't just a tool upgrade - it's a productivity boost. 
My main takeaway from this tool is that **performance is, in fact, a feature**!
Ultimately that leaves me more time to browse memes, which is, of course, what life is actually about.

![Drake meme showing the commands uv replaces.](/images/uv-meme.jpg "uv meme")


{{% comment %}}
import polars as pl
from plotnine import *
from plotnine import position_dodge

# Create the dataframe with explicit orientation
data = [
    ("pip", 154.276, "Cold Install"),
    ("uv", 5.908, "Cold Install"),
    ("pip", 102.244, "Warm Install"),
    ("uv", 0.029, "Warm Install")
]
df = pl.DataFrame(
    data,
    schema=["Tool", "Time", "InstallType"],
    orient="row"  # Fixes data orientation warning
).with_columns(
    pl.col("InstallType").cast(pl.Categorical)
)

# Create the horizontal bar chart
plot = (
    ggplot(df, aes(x="InstallType", y="Time", fill="Tool"))
    + geom_col(
        position=position_dodge(width=0.7),
        width=0.6,
        color="white",
        size=0.5,
        alpha=0.9
    )
    + coord_flip()
    + labs(
        title="Package Manager Performance Comparison",
        x="Install Type",
        y="Time (seconds)",
        fill="Package Manager"
    )
    + scale_fill_manual(values={"pip": "#FF6F42", "uv": "#42A5F5"})
    # Set the order of InstallType - now with Warm Install first
    + scale_x_discrete(
        limits=["Warm Install", "Cold Install"],
        labels=["Warm Install", "Cold Install"]
    )
    + theme_dark()
    + theme(
        text=element_text(color="white"),
        panel_background=element_rect(fill="#1a1a1a"),
        plot_background=element_rect(fill="#1a1a1a"),
        legend_background=element_rect(fill="#1a1a1a"),
        legend_position="top",
        axis_title_y=element_text(margin={"r": 15}),
        axis_title_x=element_text(margin={"t": 10}),
        panel_grid_major_x=element_line(color="#333333"),
        panel_grid_minor_x=element_blank(),
        plot_title=element_text(size=14, ha="center", margin={"b": 15}),
    )
    # Annotate UV warm install with visible line
    + geom_segment(
        df.filter(
            (pl.col("Tool") == "uv") & (pl.col("InstallType") == "Warm Install")
        ).to_pandas(),
        aes(x=1.38, xend=1.38, y=0, yend=0.029),
        color="#42A5F5",
        size=1.5,
        inherit_aes=False
    )
)

# For Jupyter notebook display
plot.save("benchmark.png", dpi=300)

{{% /comment %}}
