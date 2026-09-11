# Awesome Agent Infrastructure

**A live-checked index of building blocks for self-hosting AI agents and LLM workloads — runtimes, memory, retrieval, tool servers, evals and the reliability plumbing that keeps them up on small, cheap boxes.**

![entries](https://img.shields.io/badge/entries-135-blue) ![refresh](https://github.com/Amz34/awesome-agent-infrastructure/actions/workflows/refresh.yml/badge.svg) [![license](https://img.shields.io/badge/license-MIT-lightgrey)](LICENSE)

Every entry is pulled from live GitHub metadata and passed the same gate: active (pushed since `2025-04-01`), not archived, not a fork, **>= 800 stars**, a real description, and at least one keyword match proving it belongs in its section. Nothing is paid or hand-placed, so the list stays honest as projects die.

## Contents

1. [Agent Frameworks & Orchestration](#agent-frameworks--orchestration) — Runtimes and orchestration layers that plan, call tools and run multi-step work.
2. [Agent Memory & Context Engineering](#agent-memory--context-engineering) — Persistent memory, context budgeting and state stores for long-running agents.
3. [MCP & Tool Servers](#mcp--tool-servers) — Model Context Protocol servers, clients and tool bridges.
4. [RAG & Vector Search](#rag--vector-search) — Retrieval stacks, embedding stores and document search engines.
5. [Local & On-Prem Inference](#local--on-prem-inference) — Run models on your own box: quantised runtimes and inference servers.
6. [LLM Ops: Evals & Observability](#llm-ops-evals--observability) — Tests, evals, tracing and prompt tooling that keep quality measurable.
7. [Reliability & Cost Control](#reliability--cost-control) — Watchdogs, alerting, uptime checks and budget guards for unattended workloads.
8. [Free-Tier & Low-Cost Infrastructure](#free-tier--low-cost-infrastructure) — Lightweight tooling that fits small 2 vCPU / 12 GB always-free boxes.
9. [Learning & Reference](#learning--reference) — Curated lists, books and courses worth reading before you build.

---

## Agent Frameworks & Orchestration

_Runtimes and orchestration layers that plan, call tools and run multi-step work._

| Project | Stars | License | What it does | Last push |
|---|---:|---|---|---|
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | 72,063 | - | 🌊 The original agent meta-harness. Deploy intelligent multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive memory, self-lear | 2026-09-11 |
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | 58,366 | - | Framework for orchestrating role-playing, autonomous AI agents. By fostering collaborative intelligence, CrewAI empowers agents to work together seamlessly, tackling complex tasks. | 2026-09-11 |
| [CherryHQ/cherry-studio](https://github.com/CherryHQ/cherry-studio) | 51,672 | - | AI productivity studio with smart chat, autonomous agents, and 300+ assistants. Unified access to frontier LLMs | 2026-09-11 |
| [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | 48,016 | - | Ultra-lightweight, open-source, self-hosted personal AI agent framework in Python with WebUI, tools, memory, MCP, multi-agent workflows, automation, and chat apps | 2026-09-11 |
| [zhayujie/CowAgent](https://github.com/zhayujie/CowAgent) | 46,899 | - | Open-source super AI assistant & Agent Harness. Plans tasks, runs tools and skills, self-evolves with memory and knowledge. Multi-agent, multi-model, multi-channel. Lightweight, ex | 2026-09-11 |
| [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | 39,098 | - | Teams-first Multi-agent orchestration for Claude Code | 2026-09-11 |
| [herdrdev/herdr](https://github.com/herdrdev/herdr) | 37,641 | - | the runtime your coding agents live on | 2026-09-11 |
| [Fosowl/agenticSeek](https://github.com/Fosowl/agenticSeek) | 27,192 | - | Fully Local Manus AI. No APIs, No $200 monthly bills. Enjoy an autonomous agent that thinks, browses the web, and code for the sole cost of electricity. | 2026-09-07 |
| [activepieces/activepieces](https://github.com/activepieces/activepieces) | 24,402 | - | AI Agents & MCPs & AI Workflow Automation • (~400 MCP servers for AI agents) • AI Automation / AI Agent with MCPs • AI Workflows & AI Agents • MCPs for AI Agents | 2026-09-11 |
| [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | 22,901 | - | Fully autonomous AI Agents system capable of performing complex penetration testing tasks | 2026-09-10 |
| [cft0808/edict](https://github.com/cft0808/edict) | 16,868 | - | 🏛️ 三省六部制 · OpenClaw Multi-Agent Orchestration System — 9 specialized AI agents with real-time dashboard, model config, and full audit trails | 2026-09-07 |
| [opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | 15,121 | - | Secure, Fast, and Extensible Sandbox runtime for AI agents. | 2026-09-11 |
| [microsoft/agent-framework](https://github.com/microsoft/agent-framework) | 13,474 | - | A framework for building, orchestrating and deploying AI agents and multi-agent workflows with support for Python and .NET. | 2026-09-11 |
| [aden-hive/hive](https://github.com/aden-hive/hive) | 11,035 | - | Multi-Agent Harness for Production AI | 2026-09-05 |
| [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | 9,849 | - | Omnigent is an open-source AI agent framework and meta-harness: orchestrate Claude Code, Codex, Cursor, Pi, and custom agents — swap harnesses without rewriting, enforce policies a | 2026-09-11 |

## Agent Memory & Context Engineering

_Persistent memory, context budgeting and state stores for long-running agents._

| Project | Stars | License | What it does | Last push |
|---|---:|---|---|---|
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | 93,663 | - | Persistent Context Across Sessions for Every Agent – Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessi | 2026-09-11 |
| [mem0ai/mem0](https://github.com/mem0ai/mem0) | 65,114 | - | The Memory Layer for AI Agents - Drop-in memory infrastructure for AI agents and apps. Context that persists. Built for production. | 2026-09-11 |
| [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | 36,629 | - | Self-evolving Context Database for AI Agents. Unify Agent Memory, Knowledge RAG and Skills. | 2026-09-11 |
| [topoteretes/cognee](https://github.com/topoteretes/cognee) | 30,639 | - | Cognee is the open-source AI memory platform for agents. Give your AI agents persistent long-term memory across sessions with a self-hosted knowledge graph engine. | 2026-09-11 |
| [supermemoryai/supermemory](https://github.com/supermemoryai/supermemory) | 29,623 | - | Memory and context engine + app that is extremely fast, scalable, and can be run fully locally. The Memory API for the AI era. | 2026-09-10 |
| [deepset-ai/haystack](https://github.com/deepset-ai/haystack) | 26,476 | - | Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over r | 2026-09-11 |
| [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | 26,353 | - | TencentDB Agent Memory is a team-level memory hub for AI Agents — turning conversations, docs, and code into four reusable memory assets (Chat Memory, Skill, LLM-Wiki, Code-Graph)  | 2026-09-11 |
| [MemoriLabs/Memori](https://github.com/MemoriLabs/Memori) | 16,597 | - | Memori is agent-native memory infrastructure. A LLM-agnostic layer that turns agent execution and conversation into structured, persistent state for production systems. Built for e | 2026-09-03 |
| [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) | 14,404 | - | Personal memory across agents | 2026-09-10 |
| [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | 12,878 | - | One portable memory layer for every AI agent: local-first, Markdown-native, user-owned, and self-evolving across apps, tools, and workflows. | 2026-09-09 |
| [semantica-agi/semantica](https://github.com/semantica-agi/semantica) | 12,657 | - | Graph-Native Infrastructure for Context and Accountable AI Systems | 2026-09-11 |
| [MemTensor/MemOS](https://github.com/MemTensor/MemOS) | 11,286 | - | Self-evolving memory OS for LLM & AI Agents: ultra-persistent memory, hybrid-retrieval, and cross-task skill reuse, with 35.24% token savings and DeepSeek Harness support. | 2026-09-09 |
| [gsd-build/gsd-2](https://github.com/gsd-build/gsd-2) | 7,774 | - | A powerful meta-prompting, context engineering and spec-driven development system that enables agents to work for long periods of time autonomously without losing track of the big  | 2026-05-22 |
| [plastic-labs/honcho](https://github.com/plastic-labs/honcho) | 7,112 | - | Memory library for building stateful agents | 2026-09-10 |
| [volcengine/MineContext](https://github.com/volcengine/MineContext) | 5,507 | - | MineContext is your proactive context-aware AI partner（Context-Engineering+ChatGPT Pulse） | 2026-05-07 |

## MCP & Tool Servers

_Model Context Protocol servers, clients and tool bridges._

| Project | Stars | License | What it does | Last push |
|---|---:|---|---|---|
| [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | 51,636 | - | Chrome DevTools for coding agents | 2026-09-11 |
| [danny-avila/LibreChat](https://github.com/danny-avila/LibreChat) | 43,026 | - | Enhanced ChatGPT Clone: Features Agents, MCP, Skills, DeepSeek, Anthropic, AWS, OpenAI, Responses API, Azure, Groq, o1, GPT-5, Mistral, OpenRouter, Vertex AI, Gemini, Artifacts, AI | 2026-09-11 |
| [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | 42,941 | - | High-performance code intelligence MCP server. Indexes codebases into a persistent knowledge graph — average repo in milliseconds. 158 languages, sub-ms queries, 99% fewer tokens.  | 2026-09-10 |
| [github/github-mcp-server](https://github.com/github/github-mcp-server) | 32,865 | - | GitHub's official MCP Server | 2026-09-10 |
| [oraios/serena](https://github.com/oraios/serena) | 29,174 | - | A powerful MCP toolkit for coding, providing semantic retrieval and editing capabilities - the IDE for your agent | 2026-09-08 |
| [ahujasid/blender-mcp](https://github.com/ahujasid/blender-mcp) | 28,182 | - | Community plugin to control Blender 3D with any LLM of your choice | 2026-09-07 |
| [PrefectHQ/fastmcp](https://github.com/PrefectHQ/fastmcp) | 27,614 | - | 🚀 The fast, Pythonic way to build MCP servers and clients. | 2026-09-10 |
| [modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk) | 24,270 | - | The official Python SDK for Model Context Protocol servers and clients | 2026-09-10 |
| [pascalorg/editor](https://github.com/pascalorg/editor) | 23,317 | - | Open-source 3D architectural editor with a local CLI, MCP tools, and practical workflows for humans and AI agents. | 2026-09-11 |
| [czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp) | 22,871 | - | A MCP for Claude Desktop / Claude Code / Windsurf / Cursor to build n8n workflows for you | 2026-09-11 |
| [microsoft/mcp-for-beginners](https://github.com/microsoft/mcp-for-beginners) | 17,196 | - | This open-source curriculum introduces the fundamentals of Model Context Protocol (MCP) through real-world, cross-language examples in .NET, Java, TypeScript, JavaScript, Rust and  | 2026-09-11 |
| [budtmo/docker-android](https://github.com/budtmo/docker-android) | 15,842 | - | Android in docker solution with noVNC supported, video recording and mcp server | 2026-09-11 |
| [xpzouying/xiaohongshu-mcp](https://github.com/xpzouying/xiaohongshu-mcp) | 15,741 | - | MCP for xiaohongshu.com | 2026-09-10 |
| [CoplayDev/unity-mcp](https://github.com/CoplayDev/unity-mcp) | 14,127 | - | Unity MCP acts as a bridge between AI assistants and your Unity Editor. Give your LLM tools to manage assets, control scenes, edit scripts, and automate tasks within Unity. | 2026-09-05 |
| [modelcontextprotocol/typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk) | 13,371 | - | The official TypeScript SDK for Model Context Protocol servers and clients | 2026-09-11 |

## RAG & Vector Search

_Retrieval stacks, embedding stores and document search engines._

| Project | Stars | License | What it does | Last push |
|---|---:|---|---|---|
| [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | 90,519 | - | RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs | 2026-09-11 |
| [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | 71,498 | - | Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers. Library, proxy, MCP se | 2026-09-10 |
| [pathwaycom/llm-app](https://github.com/pathwaycom/llm-app) | 58,937 | - | Ready-to-run cloud templates for RAG, AI pipelines, and enterprise search with live data. 🐳Docker-friendly.⚡Always in sync with Sharepoint, Google Drive, S3, Kafka, PostgreSQL, rea | 2026-07-05 |
| [milvus-io/milvus](https://github.com/milvus-io/milvus) | 46,058 | - | Milvus is a high-performance, cloud-native vector database built for scalable vector ANN search | 2026-09-11 |
| [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | 39,572 | - | [EMNLP2025] LightRAG: Simple and Fast Retrieval-Augmented Generation | 2026-09-11 |
| [The-Vibe-Company/quivr](https://github.com/The-Vibe-Company/quivr) | 39,507 | - | Opiniated RAG for integrating GenAI in your apps 🧠 Focus on your product rather than the RAG. Easy integration in existing products with customisation! Any LLM: GPT4, Groq, Llama.  | 2026-08-31 |
| [patchy631/ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub) | 37,480 | - | In-depth tutorials on LLMs, RAGs and real-world AI agent applications. | 2026-09-10 |
| [microsoft/graphrag](https://github.com/microsoft/graphrag) | 35,945 | - | A modular graph-based Retrieval-Augmented Generation (RAG) system | 2026-09-08 |
| [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | 35,619 | - | 📑 PageIndex: Document Index for Vectorless, Reasoning-based RAG | 2026-09-11 |
| [qdrant/qdrant](https://github.com/qdrant/qdrant) | 34,495 | - | Qdrant - High-performance, massive-scale Vector Database and Vector Search Engine for the next generation of AI. Also available in the cloud https://cloud.qdrant.io/ | 2026-09-11 |
| [NirDiamant/RAG_Techniques](https://github.com/NirDiamant/RAG_Techniques) | 29,439 | - | This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial. | 2026-09-04 |
| [Cinnamon/kotaemon](https://github.com/Cinnamon/kotaemon) | 25,746 | - | An open-source RAG-based tool for chatting with your documents. | 2026-07-14 |
| [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | 23,293 | - | "RAG-Anything: All-in-One RAG Framework" | 2026-09-02 |
| [Tencent/WeKnora](https://github.com/Tencent/WeKnora) | 22,243 | - | Open-source LLM knowledge platform: turn raw documents into a queryable RAG, an autonomous reasoning agent, and a self-maintaining Wiki. | 2026-09-11 |
| [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | 16,886 | - | A vector index built on TurboQuant, written in Rust with Python bindings | 2026-08-21 |

## Local & On-Prem Inference

_Run models on your own box: quantised runtimes and inference servers._

| Project | Stars | License | What it does | Last push |
|---|---:|---|---|---|
| [nomic-ai/gpt4all](https://github.com/nomic-ai/gpt4all) | 77,385 | - | GPT4All: Run Local LLMs on Any Device. Open-source and available for commercial use. | 2025-05-27 |
| [openvinotoolkit/openvino](https://github.com/openvinotoolkit/openvino) | 10,832 | - | OpenVINO™ is an open source toolkit for optimizing and deploying AI inference | 2026-09-11 |
| [Tiiny-AI/PowerInfer](https://github.com/Tiiny-AI/PowerInfer) | 9,789 | - | High-speed Large Language Model Serving for Local Deployment | 2026-05-11 |
| [xorbitsai/inference](https://github.com/xorbitsai/inference) | 9,565 | - | Swap GPT for any LLM by changing a single line of code. Xinference lets you run open-source, speech, and multimodal models on cloud, on-prem, or your laptop — all through one unifi | 2026-09-11 |
| [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) | 9,072 | - | ~95% on SimpleQA (e.g. Qwen3.6-27B on a 3090). Supports all local and cloud LLMs (llama.cpp, Ollama, Google, ...). 10+ search engines - arXiv, PubMed, your private documents. Every | 2026-09-10 |
| [bentoml/BentoML](https://github.com/bentoml/BentoML) | 8,834 | - | The easiest way to serve AI apps and models - Build Model Inference APIs, Job queues, LLM apps, Multi-model pipelines, and more! | 2026-09-07 |
| [ai-dynamo/dynamo](https://github.com/ai-dynamo/dynamo) | 8,027 | - | A Datacenter Scale Distributed Inference Serving Framework | 2026-09-11 |
| [FareedKhan-dev/kimi-k3-in-c](https://github.com/FareedKhan-dev/kimi-k3-in-c) | 7,550 | - | A 2.78-trillion-parameter Kimi K3 running inference on a single CPU in 8.24 GB of RAM. Portable C99: no BLAS, no framework, no GPU. | 2026-09-10 |
| [drumih/turbo-fieldfare](https://github.com/drumih/turbo-fieldfare) | 6,700 | - | Gemma 4 26B-A4B inference in ~2 GB of RAM on any M-series MacBook | 2026-09-08 |
| [Osmantic/ODS](https://github.com/Osmantic/ODS) | 6,387 | - | Turn your PC, Mac, or Linux box into an AI server. LLM inference, chat UI, voice, agents, workflows, RAG, and image generation. | 2026-09-11 |
| [cactus-compute/cactus](https://github.com/cactus-compute/cactus) | 6,000 | - | Quantization, kernels, runtime and inference engine for mobiles, wearables, smart home and robots. | 2026-09-08 |
| [kserve/kserve](https://github.com/kserve/kserve) | 5,872 | - | Standardized Distributed Generative and Predictive AI Inference Platform for Scalable, Multi-Framework Deployment on Kubernetes | 2026-09-11 |
| [Michael-A-Kuykendall/shimmy](https://github.com/Michael-A-Kuykendall/shimmy) | 5,864 | - | ⚡ Pure-Rust WebGPU inference engine — OpenAI-API compatible, GGUF native, runs on any GPU. No Python. No llama.cpp. Single binary. | 2026-08-30 |
| [lemonade-sdk/lemonade](https://github.com/lemonade-sdk/lemonade) | 5,688 | - | Lemonade helps users discover and run local AI apps by serving optimized LLMs right from their own GPUs and NPUs. Join our discord: https://discord.gg/5xXzkMu8Zk | 2026-09-11 |
| [gpustack/gpustack](https://github.com/gpustack/gpustack) | 5,672 | - | A GPU cluster manager for high-performance AI model serving (vLLM, SGLang) and on-demand SSH-accessible GPU instances. | 2026-09-10 |

## LLM Ops: Evals & Observability

_Tests, evals, tracing and prompt tooling that keep quality measurable._

| Project | Stars | License | What it does | Last push |
|---|---:|---|---|---|
| [langfuse/langfuse](https://github.com/langfuse/langfuse) | 34,474 | - | 🪢 Open source agent evals & observability: Trace, evaluate, and improve LLM applications with one open platform. | 2026-09-11 |
| [comet-ml/opik](https://github.com/comet-ml/opik) | 21,932 | - | Debug, evaluate, and monitor your LLM applications, RAG systems, and agentic workflows with comprehensive tracing, automated evaluations, and production-ready dashboards. | 2026-09-11 |
| [confident-ai/deepeval](https://github.com/confident-ai/deepeval) | 18,219 | - | The LLM Evaluation Framework | 2026-09-08 |
| [raga-ai-hub/RagaAI-Catalyst](https://github.com/raga-ai-hub/RagaAI-Catalyst) | 16,160 | - | Python SDK for Agent AI Observability, Monitoring and Evaluation Framework. Includes features like agent, llm and tools tracing, debugging multi-agentic system, self-hosted dashboa | 2026-02-11 |
| [vibrantlabsai/ragas](https://github.com/vibrantlabsai/ragas) | 15,705 | - | Supercharge Your LLM Application Evaluations 🚀 | 2026-02-24 |
| [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix) | 11,416 | - | AI Observability & Evaluation | 2026-09-11 |
| [evidentlyai/evidently](https://github.com/evidentlyai/evidently) | 7,907 | - | Evidently is ​​an open-source ML and LLM observability framework. Evaluate, test, and monitor any AI-powered system or data pipeline. From tabular data to Gen AI. 100+ metrics. | 2026-09-11 |
| [traceloop/openllmetry](https://github.com/traceloop/openllmetry) | 7,428 | - | Open-source observability for your GenAI or LLM application, based on OpenTelemetry | 2026-08-10 |
| [jeinlee1991/chinese-llm-benchmark](https://github.com/jeinlee1991/chinese-llm-benchmark) | 6,431 | - | 非线智能 NoneLinear - ReLE评测：中文AI大模型能力评测（持续更新）：目前已囊括374个大模型，覆盖chatgpt、gpt-5.4、谷歌gemini-3.1-pro、Claude-4.6、文心ERNIE-X1.1、ERNIE-5.0、qwen3.6-max、qwen3.6-plus、百川、讯飞星火、商汤senseChat等商用模型， 以及st | 2026-09-08 |
| [Helicone/helicone](https://github.com/Helicone/helicone) | 6,146 | - | 🧊 Open source LLM observability platform. One line of code to monitor, evaluate, and experiment. YC W23 🍓 | 2026-08-31 |
| [Giskard-AI/giskard-oss](https://github.com/Giskard-AI/giskard-oss) | 5,810 | - | 🐢 Open-Source Evaluation & Testing library for LLM Agents | 2026-09-09 |
| [latitude-dev/latitude-llm](https://github.com/latitude-dev/latitude-llm) | 4,632 | - | Open-source observability for AI agents. Find where your agents fail, dispatch your coding agent to fix it, and verify the fix against real traces. | 2026-09-11 |
| [pydantic/logfire](https://github.com/pydantic/logfire) | 4,471 | - | AI observability platform for production LLM and agent systems. | 2026-09-11 |
| [EvolvingLMMs-Lab/lmms-eval](https://github.com/EvolvingLMMs-Lab/lmms-eval) | 4,399 | - | One-for-All Multimodal Evaluation Toolkit Across Text, Image, Video, and Audio Tasks | 2026-09-11 |
| [truera/trulens](https://github.com/truera/trulens) | 3,547 | - | Evaluation and Tracking for LLM Experiments and AI Agents | 2026-09-11 |

## Reliability & Cost Control

_Watchdogs, alerting, uptime checks and budget guards for unattended workloads._

| Project | Stars | License | What it does | Last push |
|---|---:|---|---|---|
| [louislam/uptime-kuma](https://github.com/louislam/uptime-kuma) | 91,257 | - | A fancy self-hosted monitoring tool | 2026-09-11 |
| [prometheus/prometheus](https://github.com/prometheus/prometheus) | 66,042 | - | The Prometheus monitoring system and time series database. | 2026-09-11 |
| [alibaba/Sentinel](https://github.com/alibaba/Sentinel) | 23,146 | - | A powerful flow control component enabling reliability, resilience and monitoring for microservices. (面向云原生微服务的高可用流控防护组件) | 2026-05-27 |
| [ccfos/nightingale](https://github.com/ccfos/nightingale) | 13,285 | - | Nightingale is to monitoring and alerting what Grafana is to visualization. | 2026-09-11 |
| [keephq/keep](https://github.com/keephq/keep) | 12,308 | - | The open-source AIOps and alert management platform | 2026-09-09 |
| [TwiN/gatus](https://github.com/TwiN/gatus) | 12,052 | - | Automated developer-oriented status page with alerting and incident support | 2026-09-08 |
| [bluewave-labs/Checkmate](https://github.com/bluewave-labs/Checkmate) | 10,805 | - | Checkmate is an open-source, self-hosted tool designed to track and monitor server hardware, uptime, response times, and incidents in real-time with beautiful visualizations. Don't | 2026-09-11 |
| [openstatusHQ/openstatus](https://github.com/openstatusHQ/openstatus) | 9,102 | - | 🫖 Status page with uptime monitoring & API monitoring as code 🫖 | 2026-09-11 |
| [zabbix/zabbix](https://github.com/zabbix/zabbix) | 6,365 | - | Real-time monitoring of IT components and services, such as networks, servers, VMs, applications and the cloud. | 2026-09-11 |
| [animir/node-rate-limiter-flexible](https://github.com/animir/node-rate-limiter-flexible) | 3,585 | - | Atomic and non-atomic counters and rate limiting tools. Limit resource access at any scale. | 2026-06-08 |
| [express-rate-limit/express-rate-limit](https://github.com/express-rate-limit/express-rate-limit) | 3,305 | - | Basic rate-limiting middleware for the Express web server | 2026-09-07 |
| [robusta-dev/robusta](https://github.com/robusta-dev/robusta) | 3,092 | - | Better Prometheus alerts for Kubernetes - smart grouping, AI enrichment, and automatic remediation | 2026-09-08 |
| [alibaba/sentinel-golang](https://github.com/alibaba/sentinel-golang) | 2,963 | - | Sentinel Go enables reliability and resiliency for Go microservices | 2026-07-02 |
| [cstate/cstate](https://github.com/cstate/cstate) | 2,893 | - | 🔥 Open source static (serverless) status page. Uses hyperfast Go & Hugo, minimal HTML/CSS/JS, customizable, outstanding browser support (IE8+), preloaded CMS, read-only API, badges | 2026-08-27 |
| [bucket4j/bucket4j](https://github.com/bucket4j/bucket4j) | 2,800 | - | Java rate limiting library based on token-bucket algorithm. | 2026-08-28 |

## Free-Tier & Low-Cost Infrastructure

_Lightweight tooling that fits small 2 vCPU / 12 GB always-free boxes._

| Project | Stars | License | What it does | Last push |
|---|---:|---|---|---|
| [immich-app/immich](https://github.com/immich-app/immich) | 113,825 | - | High performance self-hosted photo and video management solution. | 2026-09-11 |
| [nocodb/nocodb](https://github.com/nocodb/nocodb) | 64,928 | - | 🔥 🔥 🔥 A Free & Self-hostable Airtable Alternative | 2026-09-11 |
| [usememos/memos](https://github.com/usememos/memos) | 62,912 | - | Open-source, self-hosted note-taking tool built for quick capture. Markdown-native, lightweight, and fully yours. | 2026-09-10 |
| [coollabsio/coolify](https://github.com/coollabsio/coolify) | 61,675 | - | An open-source, self-hostable PaaS alternative to Vercel, Heroku & Netlify that lets you easily deploy static sites, databases, full-stack applications and 280+ one-click services  | 2026-09-11 |
| [go-gitea/gitea](https://github.com/go-gitea/gitea) | 57,950 | - | Git with a cup of tea! Painless self-hosted all-in-one software development service, including Git hosting, code review, team collaboration, package registry and CI/CD | 2026-09-11 |
| [siyuan-note/siyuan](https://github.com/siyuan-note/siyuan) | 46,300 | - | An open-source, privacy-first, self-hosted knowledge workspace where humans and AI agents work together 开源、隐私优先、自托管的知识工作空间，让人与智能体在此协作 | 2026-09-11 |
| [khoj-ai/khoj](https://github.com/khoj-ai/khoj) | 37,271 | - | Your AI second brain. Self-hostable. Get answers from the web or your docs. Build custom agents, schedule automations, do deep research. Turn any online or local LLM into your pers | 2026-08-02 |
| [glanceapp/glance](https://github.com/glanceapp/glance) | 36,981 | - | A self-hosted dashboard that puts all your feeds in one place | 2026-09-05 |
| [dokku/dokku](https://github.com/dokku/dokku) | 32,128 | - | A docker-powered PaaS that helps you build and manage the lifecycle of applications | 2026-09-10 |
| [plausible/analytics](https://github.com/plausible/analytics) | 29,023 | - | Open source, privacy-first web analytics. Lightweight, cookie-free Google Analytics alternative. Self-hosted or cloud. | 2026-09-11 |
| [karakeep-app/karakeep](https://github.com/karakeep-app/karakeep) | 28,959 | - | A self-hostable bookmark-everything app (links, notes and images) with AI-based automatic tagging and full text search | 2026-08-31 |
| [ArchiveBox/ArchiveBox](https://github.com/ArchiveBox/ArchiveBox) | 28,268 | - | 🗃 Open source self-hosted web archiving. Takes URLs/browser history/bookmarks/Pocket/Pinboard/etc., saves HTML, JS, PDFs, media, and more... | 2026-09-07 |
| [lissy93/dashy](https://github.com/lissy93/dashy) | 26,421 | - | 🚀 A self-hostable personal dashboard built for you. Includes status-checking, widgets, themes, icon packs, a UI editor and tons more! | 2026-09-11 |
| [henrygd/beszel](https://github.com/henrygd/beszel) | 25,292 | - | Lightweight server monitoring with historical data, docker stats, and alerts. | 2026-09-10 |
| [n8n-io/self-hosted-ai-starter-kit](https://github.com/n8n-io/self-hosted-ai-starter-kit) | 15,242 | - | The Self-hosted AI Starter Kit is an open-source template that quickly sets up a local AI environment. Curated by n8n, it provides essential tools for creating secure, self-hosted  | 2026-07-23 |

## Learning & Reference

_Curated lists, books and courses worth reading before you build._

| Project | Stars | License | What it does | Last push |
|---|---:|---|---|---|
| [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | 505,006 | - | 😎 Awesome lists about all kinds of interesting topics [NOTE: Pull requests are temporarily disabled until I have a chance to catch up with the existing ones] | 2026-09-02 |
| [vinta/awesome-python](https://github.com/vinta/awesome-python) | 319,911 | - | The definitive list that answers "I want to do X in Python, which tool should I use?" | 2026-09-01 |
| [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | 318,485 | - | A list of Free Software network services and web applications which can be hosted on your own servers | 2026-09-11 |
| [avelino/awesome-go](https://github.com/avelino/awesome-go) | 183,797 | - | A curated list of awesome Go frameworks, libraries and software | 2026-09-10 |
| [f/prompts.chat](https://github.com/f/prompts.chat) | 169,948 | - | f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy. | 2026-09-09 |
| [Hack-with-Github/Awesome-Hacking](https://github.com/Hack-with-Github/Awesome-Hacking) | 120,139 | - | A collection of various awesome lists for hackers, pentesters and security researchers | 2026-07-26 |
| [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | 115,321 | - | A collection of DESIGN.md files analysis by popular brand design systems. Drop one into your project and let coding agents generate a matching UI. | 2026-07-31 |
| [jaywcjlove/awesome-mac](https://github.com/jaywcjlove/awesome-mac) | 113,549 | - |  This project is dedicated to collecting high-quality macOS software and organizing them systematically by different categories for easy search and use. | 2026-09-11 |
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | 94,795 | - | A collection of MCP servers. | 2026-09-08 |
| [MunGell/awesome-for-beginners](https://github.com/MunGell/awesome-for-beginners) | 89,149 | - | A list of awesome beginners-friendly projects. | 2026-07-25 |
| [enaqx/awesome-react](https://github.com/enaqx/awesome-react) | 74,558 | - | A collection of awesome things regarding React ecosystem | 2026-09-04 |
| [binhnguyennus/awesome-scalability](https://github.com/binhnguyennus/awesome-scalability) | 73,854 | - | The Patterns of Scalable, Reliable, and Performant Large-Scale Systems | 2026-01-04 |
| [fffaraz/awesome-cpp](https://github.com/fffaraz/awesome-cpp) | 73,228 | - | A curated list of awesome C++ (or C) frameworks, libraries, resources, and shiny things. Inspired by awesome-... stuff. | 2026-09-05 |
| [sindresorhus/awesome-nodejs](https://github.com/sindresorhus/awesome-nodejs) | 66,773 | - | :zap: Delightful Node.js packages and resources [BECAUSE OF TOO MUCH SPAM AND LOW-QUALITY SUBMISSIONS, SUBMISSIONS ARE PAUSED TEMPORARILY] | 2026-09-02 |
| [Solido/awesome-flutter](https://github.com/Solido/awesome-flutter) | 61,154 | - | An awesome list that curates the best Flutter libraries, tools, tutorials, articles and more. | 2026-09-03 |

---

## Picking a stack from this list

- **Starting out?** Take one runtime from *Agent Frameworks & Orchestration*, one store from *Agent Memory & Context Engineering*, then a watchdog from *Reliability & Cost Control* before anything runs unattended.
- **Free tier only (e.g. 2 vCPU / 12 GB)?** *Free-Tier & Low-Cost Infrastructure* and *Local & On-Prem Inference* are where small-box-friendly projects live.
- **Data cannot leave your network?** *Local & On-Prem Inference* + *RAG & Vector Search* is the fully offline path.
- **Nothing is measured, nothing improves:** add the *LLM Ops* section before scaling prompt or model changes.

## How this list stays honest

- Rebuilt from the GitHub API by [`build_awesome.py`](build_awesome.py) — the same script in this repo, run weekly by [the refresh workflow](../../actions/workflows/refresh.yml).
- Hard gate: stars >= 800, pushed >= 2025-04-01, not archived, not a fork, keyword-verified section assignment.
- A project that goes stale or archived drops out automatically on the next run.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) — or open a **Suggest a project** issue and the gate will be checked in the next refresh.

## More from this author

- [selfhosted-agent-stack](https://github.com/Amz34/selfhosted-agent-stack) — the hardened 2 vCPU / 12 GB agent box these picks are tested on.
- [ai-can-run](https://github.com/Amz34/ai-can-run) — a small, honest runner for AI tasks.

## License

MIT — see [LICENSE](LICENSE). Copy, remix, republish freely.
