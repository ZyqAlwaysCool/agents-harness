# Agent Harness

[English](./README.md) | [简体中文](./README.zh-CN.md)

`Agent Harness` is a repository starter for agent-first software development.

It is built around a simple idea:

> Agent Harness does not provide complete knowledge. It provides a controlled track for knowledge to grow from chaos into stability.

The goal is not to make the model "more creative." The goal is to make the repository readable, executable, verifiable, and correctable enough that a strong model can operate with less human micromanagement.

## Why This Exists

Modern coding models are powerful engines, but raw model capability alone does not produce stable software delivery. Without structure, projects drift:

- knowledge mixes current truth with temporary notes
- every new session has to rebuild context from scratch
- verification depends on human reminders
- high-impact changes are easy to make in the wrong way

Agent Harness applies harness engineering ideas to the repository itself.

It treats the repository as the control surface for the agent:

- the repository layout acts as the track
- docs layering acts as memory control
- fixed scripts act as execution entrypoints
- verification acts as the dashboard
- human confirmation boundaries act as the guardrails

This project is directly informed by OpenAI's article on harness engineering:

- OpenAI, "Harness engineering: using Codex in an agentic world"
  https://openai.com/zh-Hans-CN/index/harness-engineering/

## Core Model

The repository control model has three layers:

- `Base`: repository-level control rules that stay stable across projects
- `Pack`: stack-specific implementation guidance
- `Policy`: project-level governance switches defined in [`configs/agent-harness.yaml`](./configs/agent-harness.yaml)

The current default pack is `python-fastapi`.

## What The Repository Provides

- [`AGENTS.md`](./AGENTS.md): the startup map for the agent
- [`docs/`](./docs): layered knowledge, with `docs/current/` as current truth
- [`app/`](./app): the only business-code root
- [`scripts/`](./scripts): stable entrypoints for setup, development, verification, and replay
- [`standards/`](./standards): base and pack-level standards
- [`configs/agent-harness.yaml`](./configs/agent-harness.yaml): project-level policy switches
- [`standards/skills/manifest.yaml`](./standards/skills/manifest.yaml): skill declarations used by the repository control surface

## How To Use It

### 1. Start With The Repository, Not With Code

Create a new project from this template, then adapt the control surface before asking the agent to build business logic.

Typical first steps:

1. rename the project and update [`configs/agent-harness.yaml`](./configs/agent-harness.yaml)
2. review [`AGENTS.md`](./AGENTS.md) and keep it as a startup map plus hard boundaries
3. decide whether the default `python-fastapi` pack fits the project
4. adjust policy switches, docs structure, and scripts if needed
5. run `./scripts/setup`

### 2. First Conversation: Understand The Track, Then Discuss The Need

For the very first agent session, do not start with implementation.

A better order is:

1. ask the agent to read the control surface and summarize the repository model
2. align on the project need, scope, and constraints
3. let the agent propose the initial `app/` structure if it is not already decided
4. confirm the structure and the first set of current-truth docs
5. only then move into implementation

In practice, the first conversation should usually be about **repository understanding plus requirement clarification**, not coding.

### 3. Let Knowledge Grow In Layers

At the beginning, the project may not have complete requirements or architecture. That is expected.

Use the docs layers deliberately:

- `docs/worklog/` for active discussion and temporary notes
- `docs/current/` for confirmed current truth
- `docs/adr/` for important decisions
- `docs/archive/` for retired content

The point is not to write a lot of docs early. The point is to make sure each piece of knowledge goes to the right layer.

## How Developers Modify The Framework

This starter is meant to be changed.

The intended customization model is:

- keep `Base` stable unless you want to change the repository control philosophy
- change `Pack` when the stack or internal code organization changes
- change `Policy` when you want a different level of agent autonomy or review strictness
- evolve `scripts/` implementations while keeping entrypoint names stable

In other words:

- use `Base` to control drift
- use `Pack` to adapt the stack
- use `Policy` to tune governance

## Default Verification Loop

The default verification entrypoint is:

```bash
./scripts/check
```

The default development flow is:

```bash
./scripts/setup
./scripts/dev
./scripts/check
```

The goal is that the agent should be able to complete a verification loop by default, instead of stopping after code generation.

## Current Direction

This repository is still an evolving framework.

The current plan is practical and iterative:

1. apply the framework to a real new project
2. use GPT-5.4, Claude Code, or similar agents inside this constrained environment
3. observe where the framework helps and where it still leaks drift
4. refine the framework through real project experience
5. repeat

This matters because Agent Harness should not be designed only from theory. It should be shaped by actual agent behavior under real development pressure.

## Near-Term Iteration Focus

The next improvements are expected to come from practice in real projects, especially around:

- stronger pack details
- better replay and debugging affordances
- sharper human confirmation boundaries
- better skill declarations and integrations
- clearer verification contracts for agent handoff

## Quick Start

```bash
./scripts/setup
./scripts/dev
./scripts/check
```

## Status

This is a v0.1 template focused on a Python-first starting point. The repository control model is intentionally broader than Python, but the first shipped pack is `python-fastapi`.
