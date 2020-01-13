# Web Cache Poisoning

## Instructions

Caching might seem unexciting, but it's crucial for fast user experiences, and has considerable security implications.

**Cache Poisoning** is an important attack through which an attacker tricks a cache into caching a malicious file, _instead_ of the file the cache should serve.

In this exercise, you'll read about cache poisoning attacks, and how they're used. Refer to this write-up: <https://portswigger.net/blog/practical-web-cache-poisoning>

Use the questions below to guide your reading.

## Questions

- Read the introduction and **Caching 101** sections.

- Read the **Cache Keys** section, and answer the following questions:
  - What must a cache do when it receives a request for a resource? Why is this tricky?
  - Caches use _____ _____ to address this problem.
    - Also: Define this term.

- Read the **Cache Poisoning Section**, and answer the questions below.
  - What is the objective of a cache poisoning attack?
  - What is the easiest way to poison a cache?

- You're encouraged to read the remaining sections yourself, but they _are not_ required for this exercise.
