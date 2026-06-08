---
date: '2025-02-01T00:00:00+00:00'
title: 'Python Polars: the Definitive Guide is out'
description: "After almost two years of writing, Python Polars: the Definitive Guide is published by O'Reilly. Here is what is in it and why we wrote it."
categories: [polars, book]
tags: [python, polars, data-engineering, oreilly, dataframe, book]
images:
  - "/images/pp-cover-800w.jpg"
socialShare: true
showReadingTime: true
---

[![Book cover for Python Polars: the Definitive Guide](/images/pp-cover-800w.jpg "Python Polars: the Definitive Guide")](https://polarsguide.com)

After almost two years of writing, [Python Polars: the Definitive Guide](https://polarsguide.com) is out. Jeroen Janssens and I started working on it in the summer of 2023, and it is now available from O'Reilly.

## Why we wrote it

Polars was growing fast. The community was active, the library was improving quickly, and more and more teams were asking whether they should switch from Pandas. But there was no comprehensive resource that covered the full API, explained the design philosophy, and showed how to apply it to real problems.

Jeroen and I had both been using Polars in production. At Xomnia, we converted a 20,000-line Pandas codebase to Polars and cut processing time from five hours to one second, with a 98% reduction in compute cost. We had learned what works, what does not, and what surprises people when they first pick it up. That experience is what the book is built around.

## What is in it

The book is for Python practitioners who work with data and want to go beyond Pandas. It covers:

- **The Polars data model:** How DataFrames and Series work in Polars, and how the design differs from Pandas in ways that matter in practice.
- **Expressions and contexts:** The expression system is the core of Polars. Once you understand it, the rest of the API clicks into place. We spend a lot of time here.
- **Lazy vs eager evaluation:** When to use each, how the Lazy API constructs a query plan, and how Polars optimizes it before running anything.
- **Joining and aggregating:** How to combine and summarize data correctly and efficiently, including group-by operations that would be slow or awkward in Pandas.
- **Streaming:** How to process datasets that are larger than available memory without changing much of your code.
- **Real-world pipelines:** Patterns for cleaning, transforming, and loading data in production settings.
- **Interoperability:** Working with NumPy, Arrow, pandas, and common visualization libraries without unnecessary copying or conversion overhead.

## GPU and cloud

While writing the book, we had the chance to benchmark Polars on GPU hardware with Nvidia and Dell. The results were significant. We also cover where Polars Cloud fits in for teams that need to scale beyond a single machine.

## Where to get it

The first chapter is available to [read for free online](https://polarsguide.com). The full book is on [O'Reilly](https://www.oreilly.com/library/view/python-polars-the/9781098156077/).

If you have been on the fence about switching from Pandas, this is a good place to start.
