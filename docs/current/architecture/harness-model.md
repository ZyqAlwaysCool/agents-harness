# Harness Model

This document defines the repository control model used by Agent Harness.

## Purpose

Agent Harness is not a business project by itself. It is a controlled engineering environment that helps an agent work inside a stable loop:

- read the current truth
- implement in the correct place
- run verification
- inspect failures
- hand off only when the result is checkable

## Base

`Base` is the repository control layer.

It defines:

- startup order
- repository map
- docs layering
- stable script entrypoints
- verification expectations
- hard boundaries that should not drift casually

`Base` is designed to stay light and stack-agnostic.

## Pack

`Pack` is the stack-specific implementation layer.

It defines:

- recommended internal structure under `app/`
- stack-specific development conventions
- stack-specific verification guidance
- framework-specific code organization suggestions

A project may replace or extend the default pack without changing the Base model.

## Policy

`Policy` is the project governance layer.

It defines project-specific switches such as:

- whether auto commit is allowed
- whether new modules require docs updates
- whether public APIs require tests
- whether agents may edit scripts directly

In this template, Policy is primarily configured in `configs/agent-harness.yaml`.

## Current Default

The current default setup is:

- Base: repository control rules defined by this template
- Pack: `python-fastapi`
- Policy: values from `configs/agent-harness.yaml`

## Design Intent

The control model follows harness engineering principles:

- the repository should be readable by the agent as an operating surface
- execution entrypoints should be stable
- verification should be part of the default work loop
- temporary notes should not be mixed with current truth
- humans should only be pulled in for high-impact decisions
