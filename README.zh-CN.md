# Agent Harness

[English](./README.md) | [简体中文](./README.zh-CN.md)

`Agent Harness` 是一个面向 agent-first 软件开发的仓库起步模板。

它围绕一个很核心的判断来设计：

> Agent Harness 提供的不是完整知识，而是知识从混沌生长到稳定的受控轨道。

它的目标不是让模型“更自由发挥”，而是让仓库本身足够可读、可执行、可验证、可纠偏，从而让一个强模型在更少人工微操的前提下稳定工作。

## 为什么要做这个

现代编码模型已经是非常强的引擎，但只有模型能力本身，并不能自然导向稳定的软件交付。没有结构约束时，项目很容易漂移：

- 当前真相和临时记录混在一起
- 每次新会话都要重新建立上下文
- 验证依赖人工反复提醒
- 高影响改动容易在错误边界内发生

Agent Harness 的目标，就是把 harness engineering 的思想落实到仓库本身。

它把仓库视为 agent 的控制面：

- 仓库结构是轨道
- 文档分层是记忆控制
- 固定脚本是执行入口
- 验证闭环是仪表盘
- 人工确认边界是护栏

这个项目的设计直接参考了 OpenAI 关于 harness engineering 的文章：

- OpenAI，《Harness engineering: using Codex in an agentic world》
  https://openai.com/zh-Hans-CN/index/harness-engineering/

## 核心模型

这个仓库的控制模型分为三层：

- `Base`：跨项目稳定存在的仓库级控制规则
- `Pack`：与技术栈相关的实现指导层
- `Policy`：定义在 [`configs/agent-harness.yaml`](./configs/agent-harness.yaml) 中的项目治理开关

当前默认的 pack 是 `python-fastapi`。

## 仓库提供了什么

- [`AGENTS.md`](./AGENTS.md)：agent 的启动地图
- [`docs/`](./docs)：分层知识系统，其中 `docs/current/` 是当前真相层
- [`app/`](./app)：唯一业务代码根目录
- [`scripts/`](./scripts)：稳定的 setup、开发、验证、replay 入口
- [`standards/`](./standards)：Base 与 Pack 层标准
- [`configs/agent-harness.yaml`](./configs/agent-harness.yaml)：项目级 policy 开关
- [`standards/skills/manifest.yaml`](./standards/skills/manifest.yaml)：仓库控制面使用的 skills 声明

## 开发者如何使用

### 1. 先调整仓库控制面，不要一上来就写业务代码

你应该先基于模板创建新项目，再去调整控制面，而不是立即让 agent 编码业务逻辑。

典型步骤是：

1. 重命名项目，并修改 [`configs/agent-harness.yaml`](./configs/agent-harness.yaml)
2. 阅读并调整 [`AGENTS.md`](./AGENTS.md)，让它保持“启动地图 + 硬边界”的角色
3. 判断默认的 `python-fastapi` pack 是否适合当前项目
4. 根据需要调整 policy、文档结构和脚本
5. 运行 `./scripts/setup`

### 2. 第一次对话：先理解轨道，再讨论需求

对于一个全新的项目，第一次和 agent 的对话不建议直接进入实现。

更合理的顺序是：

1. 先让 agent 读取控制面并总结仓库模型
2. 再与 agent 对齐项目需求、范围和约束
3. 如果 `app/` 内部结构尚未确定，让 agent 提出结构建议
4. 由开发者确认结构和第一批 current truth 文档
5. 然后再进入实现

也就是说，第一次对话通常应该是：

**仓库理解 + 需求澄清**，而不是直接写代码。

### 3. 让知识分层生长，而不是一开始就写满文档

项目初期需求不完整、架构未定型是正常状态。

这时关键不是把文档写很多，而是把知识放到正确层级：

- `docs/worklog/`：活跃讨论与临时记录
- `docs/current/`：已确认的当前真相
- `docs/adr/`：重要决策
- `docs/archive/`：已废弃材料

重点不是“多写文档”，而是“不要把不同状态的知识混在一起”。

## 开发者该如何修改这个框架

这个模板本来就是允许被修改和演进的。

推荐的修改方式是：

- 如果你想改变仓库控制哲学，修改 `Base`
- 如果你想适配新的技术栈或代码组织方式，修改 `Pack`
- 如果你想调整 agent 自主程度或治理强度，修改 `Policy`
- 如果你想增强执行方式，可以修改 `scripts/` 的实现，但尽量保持入口名稳定

也就是：

- 用 `Base` 控制漂移
- 用 `Pack` 适配技术栈
- 用 `Policy` 调整治理方式

## 默认验证闭环

默认的总验证入口是：

```bash
./scripts/check
```

默认开发路径是：

```bash
./scripts/setup
./scripts/dev
./scripts/check
```

目标是让 agent 默认能够完成“实现 -> 验证 -> 交付”的闭环，而不是停留在代码生成阶段。

## 当前的演进方向

这个仓库本身就是一个持续迭代的框架，而不是一次性定型的规范包。

当前的计划是：

1. 先把这套框架应用到一个真实的新项目里
2. 让 GPT-5.4、Claude Code 等 agent 在这套受控环境里开发项目
3. 观察它在哪些地方有效，哪些地方仍然会漂移
4. 基于真实使用体验继续优化框架
5. 持续循环

这一点很重要，因为 Agent Harness 不应该只靠抽象讨论来设计，它必须经受真实项目迭代压力下的检验。

## 近期迭代重点

后续的优化大概率会来自真实项目实践，尤其包括：

- 更完整的 pack 细则
- 更好的 replay 与调试能力
- 更锋利的人类接管边界
- 更清晰的 skill 声明与集成方式
- 更稳定的 agent 交付验证契约

## 快速开始

```bash
./scripts/setup
./scripts/dev
./scripts/check
```

## 当前状态

当前版本是一个 v0.1 的 Python-first 起点。它的仓库控制模型并不与 Python 强绑定，但第一版内置的默认 pack 是 `python-fastapi`。
