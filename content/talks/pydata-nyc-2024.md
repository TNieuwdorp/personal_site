---
title: "PyData NYC 2024 Talk"
date: 2024-11-08
summary: "What we learned by converting a large codebase from Pandas to Polars."
draft: false
images:
  - "/images/benchmark.png"
---


{{< youtube B2Ljp2Fb-l0 >}}

The talk presents the experience of converting a large codebase from Pandas to Polars, highlighting significant performance improvements, maintainability, and practical lessons learned throughout the process. The speakers discuss the challenges faced, the benefits of using Polars, and the methodologies applied during the migration.

## Key Points

- **Codebase Transition:** Converted a 20,000-line codebase from Pandas to Polars, resulting in a 98% cost reduction and improved maintainability.
- **Performance Gains:** Processing time reduced from 5 hours (Pandas) to 1 second (Polars) for large datasets.
- **Use of Lazy API:** Leveraged Polars' Lazy API for deferred computation, reducing memory usage and execution time.
- **Benchmarking Importance:** Regular benchmarking identified performance improvements and validated optimizations.
- **Community Support:** Engaged with the Polars community for insights and problem-solving during the transition.
- **Iterative Improvement Approach:** Incremental migration, starting with low-hanging fruit, allowed gradual integration of Polars.
- **Final Results:** Achieved 20% overall processing time reduction, handled 50 sample datasets with 40 GB RAM.
- **Book Announcement:** Announced 'The Definitive Guide to Polars' to share project insights and help others transition.
