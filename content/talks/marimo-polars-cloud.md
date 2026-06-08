---
title: "A First Technical Preview of Polars Cloud"
date: 2025-07-31
summary: "Live demo of Polars Cloud: distributed execution, the Query Profiler, and multi-node clusters. Hosted as a marimo livestream."
draft: false
---

{{< youtube "TTMecrbUDqk" >}}

In this marimo-hosted livestream, I gave the first technical preview of Polars Cloud and showed how Polars can scale from a single node to a distributed cluster.

## Key Points

### Polars and its growth

Polars has come a long way since its early days. Download numbers are high and adoption keeps accelerating. More and more teams are asking whether they should switch from Pandas.

### Polars Cloud features

The main focus of the session is Polars Cloud: a platform that lets you run distributed queries across multiple machines without rewriting your code. We are working towards a generous free tier so anyone can experiment with it.

### Streaming engine and lazy execution

I explain how the streaming engine works: it processes data in chunks rather than loading everything into memory at once. Combined with lazy execution, Polars optimizes a full query plan before running anything. That combination is what makes the performance at scale possible.

### Live demo

I run a query live and compare the results against Pandas. The lazy API does the heavy lifting, and the performance difference is significant.

### Future and community

I close out with a look at what is coming next and how you can get involved through Discord. Polars Cloud is still early, and we are actively looking for feedback.
