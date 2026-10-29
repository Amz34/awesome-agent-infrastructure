# Awesome Agent Infrastructure

**A live-checked index of building blocks for self-hosting AI agents and LLM workloads — runtimes, memory, retrieval, tool servers, evals and the reliability plumbing that keeps them up on small, cheap boxes.**

[![Follow @Amz34](https://img.shields.io/github/followers/Amz34?label=Follow%20%40Amz34&style=social)](https://github.com/Amz34)
[![Stars](https://img.shields.io/github/stars/Amz34/awesome-agent-infrastructure?style=social)](https://github.com/Amz34/awesome-agent-infrastructure)
[![Forks](https://img.shields.io/github/forks/Amz34/awesome-agent-infrastructure?style=social)](https://github.com/Amz34/awesome-agent-infrastructure/network/members)
![entries](https://img.shields.io/badge/entries-135-blue)
[![refresh](https://github.com/Amz34/awesome-agent-infrastructure/actions/workflows/refresh.yml/badge.svg)](https://github.com/Amz34/awesome-agent-infrastructure/actions)
[![license](https://img.shields.io/badge/license-MIT-lightgrey)](LICENSE)

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
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | 79,362 | - | 🌊 The original agent harness. Deploy intelligent multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive memory, self-learning  | 2026-10-26 |
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | 60,114 | - | Framework for orchestrating role-playing, autonomous AI agents. By fostering collaborative intelligence, CrewAI empowers agents to work together seamlessly, tackling complex tasks. | 2026-10-26 |
| [CherryHQ/cherry-studio](https://github.com/CherryHQ/cherry-studio) | 52,989 | - | AI productivity studio with smart chat, autonomous agents, and 300+ assistants. Unified access to frontier LLMs | 2026-10-26 |
| [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | 49,360 | - | Ultra-lightweight, open-source, self-hosted personal AI agent framework in Python with WebUI, tools, memory, MCP, multi-agent workflows, automation, and chat apps | 2026-10-26 |
| [zhayujie/CowAgent](https://github.com/zhayujie/CowAgent) | 47,600 | - | Open-source personal AI assistant & Agent Harness. Plans tasks, runs tools and skills, self-evolves with memory and knowledge. Multi-agent, multi-model, multi-channel. Lightweight, | 2026-10-25 |
| [herdrdev/herdr](https://github.com/herdrdev/herdr) | 45,907 | - | the runtime your coding agents live on | 2026-10-23 |
| [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | 32,457 | - | Fully autonomous AI Agents system capable of performing complex penetration testing tasks | 2026-10-22 |
| [Fosowl/agenticSeek](https://github.com/Fosowl/agenticSeek) | 27,544 | - | Fully Local Manus AI. No APIs, No $200 monthly bills. Enjoy an autonomous agent that thinks, browses the web, and code for the sole cost of electricity. | 2026-10-22 |
| [activepieces/activepieces](https://github.com/activepieces/activepieces) | 25,229 | - | AI Agents & MCPs & AI Workflow Automation • (~400 MCP servers for AI agents) • AI Automation / AI Agent with MCPs • AI Workflows & AI Agents • MCPs for AI Agents | 2026-10-26 |
| [cft0808/edict](https://github.com/cft0808/edict) | 17,017 | - | 🏛️ 三省六部制 · OpenClaw Multi-Agent Orchestration System — 9 specialized AI agents with real-time dashboard, model config, and full audit trails | 2026-09-28 |
| [opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | 16,176 | - | Secure, Fast, and Extensible Sandbox runtime for AI agents. | 2026-10-26 |
| [microsoft/agent-framework](https://github.com/microsoft/agent-framework) | 14,317 | - | A framework for building, orchestrating and deploying AI agents and multi-agent workflows with support for Python and .NET. | 2026-10-25 |
| [aden-hive/hive](https://github.com/aden-hive/hive) | 11,122 | - | Multi-Agent Harness for Production AI | 2026-10-26 |
| [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | 11,054 | - | Omnigent is an open-source AI agent framework and meta-harness: orchestrate Claude Code, Codex, Cursor, Pi, and custom agents — swap harnesses without rewriting, enforce policies a | 2026-10-26 |
| [strands-agents/harness-sdk](https://github.com/strands-agents/harness-sdk) | 8,952 | - | Build an agent harness and control it end-to-end. Open-source SDK for production AI agents in Python & TypeScript - any model, any cloud. | 2026-10-26 |

## Agent Memory & Context Engineering

_Persistent memory, context budgeting and state stores for long-running agents._

| Project | Stars | License | What it does | Last push |
|---|---:|---|---|---|
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | 103,224 | - | Persistent Context Across Sessions for Every Agent – Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessi | 2026-10-25 |
| [mem0ai/mem0](https://github.com/mem0ai/mem0) | 67,832 | - | The Memory Layer for AI Agents - Drop-in memory infrastructure for AI agents and apps. Context that persists. Built for production. | 2026-10-23 |
| [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | 40,855 | - | Self-evolving Context Database for AI Agents. Unify Agent Memory, Knowledge RAG and Skills. | 2026-10-26 |
| [topoteretes/cognee](https://github.com/topoteretes/cognee) | 32,764 | - | Cognee is the open-source AI memory platform for agents. Give your AI agents persistent long-term memory with small models for free | 2026-10-23 |
| [supermemoryai/supermemory](https://github.com/supermemoryai/supermemory) | 31,400 | - | Memory and context engine + app that is extremely fast, scalable, and can be run fully locally. The Memory API for the AI era. | 2026-10-25 |
| [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | 29,958 | - | TencentDB Agent Memory is a team-level memory hub for AI Agents — turning conversations, docs, and code into four reusable memory assets (Chat Memory, Skill, LLM-Wiki, Code-Graph)  | 2026-10-26 |
| [deepset-ai/haystack](https://github.com/deepset-ai/haystack) | 26,845 | - | Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over r | 2026-10-24 |
| [MemoriLabs/Memori](https://github.com/MemoriLabs/Memori) | 17,141 | - | Memori is agent-native memory infrastructure. A LLM-agnostic layer that turns agent execution and conversation into structured, persistent state for production systems. Built for e | 2026-10-03 |
| [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) | 14,562 | - | Personal memory across agents | 2026-10-26 |
| [semantica-agi/semantica](https://github.com/semantica-agi/semantica) | 14,251 | - | Graph-Native Infrastructure for Context and Accountable AI Systems | 2026-10-26 |
| [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | 13,628 | - | One portable memory layer for every AI agent: local-first, Markdown-native, user-owned, and self-evolving across apps, tools, and workflows. | 2026-10-22 |
| [MemTensor/MemOS](https://github.com/MemTensor/MemOS) | 12,101 | - | Self-evolving memory OS for LLM & AI Agents: ultra-persistent memory, hybrid-retrieval, and cross-task skill reuse, with 35.24% token savings and DeepSeek Harness support. | 2026-10-24 |
| [plastic-labs/honcho](https://github.com/plastic-labs/honcho) | 7,776 | - | Memory library for building stateful agents | 2026-10-26 |
| [volcengine/MineContext](https://github.com/volcengine/MineContext) | 5,542 | - | MineContext is your proactive context-aware AI partner（Context-Engineering+ChatGPT Pulse） | 2026-05-07 |
| [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain) | 4,922 | - | Persistent memory for Claude Code, Codex and 6 other AI agents, stored as plain markdown in your Obsidian vault. New: Crew, one shared logbook so Claude Code, Codex, Cursor and Gro | 2026-10-25 |

## MCP & Tool Servers

_Model Context Protocol servers, clients and tool bridges._

| Project | Stars | License | What it does | Last push |
|---|---:|---|---|---|
| [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | 54,176 | - | Chrome DevTools for coding agents | 2026-10-26 |
| [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | 47,505 | - | Local code intelligence for developers and AI agents. Connect code, docs and infrastructure in a persistent graph, with CBM Lens, MCP tools, agent integrations and change-aware tes | 2026-10-26 |
| [LibreChat-AI/LibreChat](https://github.com/LibreChat-AI/LibreChat) | 46,336 | - | Enhanced ChatGPT Clone: Features Agents, MCP, Skills, DeepSeek, Anthropic, AWS, OpenAI, Responses API, Azure, Groq, o1, GPT-5, Mistral, OpenRouter, Vertex AI, Gemini, Artifacts, AI | 2026-10-26 |
| [github/github-mcp-server](https://github.com/github/github-mcp-server) | 33,964 | - | GitHub's official MCP Server | 2026-10-23 |
| [ahujasid/mcp-for-blender](https://github.com/ahujasid/mcp-for-blender) | 32,378 | - | Community plugin to control Blender 3D with any LLM of your choice. Not affiliated with the official Blender Foundation. | 2026-10-24 |
| [oraios/serena](https://github.com/oraios/serena) | 30,724 | - | A powerful MCP toolkit for coding, providing semantic retrieval and editing capabilities - the IDE for your agent | 2026-10-20 |
| [PrefectHQ/fastmcp](https://github.com/PrefectHQ/fastmcp) | 28,205 | - | 🚀 The fast, Pythonic way to build MCP servers and clients. | 2026-10-26 |
| [pascalorg/editor](https://github.com/pascalorg/editor) | 25,116 | - | Open-source 3D architectural editor with a local CLI, MCP tools, and practical workflows for humans and AI agents. | 2026-10-25 |
| [modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk) | 24,669 | - | The official Python SDK for Model Context Protocol servers and clients | 2026-10-25 |
| [czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp) | 23,139 | - | A MCP for Claude Desktop / Claude Code / Windsurf / Cursor to build n8n workflows for you | 2026-10-25 |
| [Evil0ctal/Douyin_TikTok_Download_API](https://github.com/Evil0ctal/Douyin_TikTok_Download_API) | 20,907 | - | 🚀 自托管的抖音、TikTok、B 站数据采集与无水印视频下载 API，支持 AI agent 通过 MCP 调用与离线语音转文字，Docker 一键部署。/ Self-hosted TikTok, Douyin & Bilibili scraper and no-watermark video downloader — async REST API, MC | 2026-10-26 |
| [microsoft/mcp-for-beginners](https://github.com/microsoft/mcp-for-beginners) | 17,513 | - | This open-source curriculum introduces the fundamentals of Model Context Protocol (MCP) through real-world, cross-language examples in .NET, Java, TypeScript, JavaScript, Rust and  | 2026-10-25 |
| [xpzouying/xiaohongshu-mcp](https://github.com/xpzouying/xiaohongshu-mcp) | 16,574 | - | MCP for xiaohongshu.com | 2026-10-26 |
| [budtmo/docker-android](https://github.com/budtmo/docker-android) | 16,034 | - | Android in docker solution with noVNC supported, video recording, mcp server and AI-agent | 2026-10-26 |
| [xerj-org/xerj](https://github.com/xerj-org/xerj) | 15,682 | - | Local-first search engine and MCP server for AI agents. One Rust binary indexes code, docs, logs, JSONL/CSV and PDFs for BM25 full-text, vector and hybrid search, code search witho | 2026-10-26 |

## RAG & Vector Search

_Retrieval stacks, embedding stores and document search engines._

| Project | Stars | License | What it does | Last push |
|---|---:|---|---|---|
| [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | 92,886 | - | RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs | 2026-10-26 |
| [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | 77,852 | - | Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers. Library, proxy, MCP se | 2026-10-24 |
| [pathwaycom/serviette](https://github.com/pathwaycom/serviette) | 58,762 | - | A no-code RAG server that keeps answers in sync with your documents. Works with 8 vector databases. Built on Pathway. | 2026-10-16 |
| [milvus-io/milvus](https://github.com/milvus-io/milvus) | 46,483 | - | Milvus is a high-performance, cloud-native vector database built for scalable vector ANN search | 2026-10-26 |
| [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | 40,338 | - | [EMNLP2025] LightRAG: Simple and Fast Retrieval-Augmented Generation | 2026-10-22 |
| [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | 39,745 | - | 📑 PageIndex: Document Index for Vectorless, Reasoning-based RAG | 2026-10-26 |
| [patchy631/ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub) | 38,437 | - | In-depth tutorials on LLMs, RAGs and real-world AI agent applications. | 2026-10-12 |
| [microsoft/graphrag](https://github.com/microsoft/graphrag) | 36,449 | - | A modular graph-based Retrieval-Augmented Generation (RAG) system | 2026-10-26 |
| [Tencent/WeKnora](https://github.com/Tencent/WeKnora) | 35,482 | - | Open-source LLM knowledge platform: turn raw documents into a queryable RAG, an autonomous reasoning agent, and a self-maintaining Wiki. | 2026-10-26 |
| [qdrant/qdrant](https://github.com/qdrant/qdrant) | 35,253 | - | Qdrant - High-performance, massive-scale Vector Database and Vector Search Engine for the next generation of AI. Also available in the cloud https://cloud.qdrant.io/ | 2026-10-26 |
| [NirDiamant/RAG_Techniques](https://github.com/NirDiamant/RAG_Techniques) | 30,008 | - | This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial. | 2026-10-22 |
| [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | 24,135 | - | "RAG-Anything: All-in-One RAG Framework" | 2026-10-26 |
| [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | 17,423 | - | A vector index built on TurboQuant, written in Rust with Python bindings | 2026-10-07 |
| [weaviate/weaviate](https://github.com/weaviate/weaviate) | 16,915 | - | Weaviate is an open-source vector database that stores both objects and vectors, allowing for the combination of vector search with structured filtering with the fault tolerance an | 2026-10-26 |
| [memvid/memvid](https://github.com/memvid/memvid) | 16,610 | - | Memory layer for AI Agents. Replace complex RAG pipelines with a serverless, single-file memory layer. Give your agents instant retrieval and long-term memory. | 2026-07-14 |

## Local & On-Prem Inference

_Run models on your own box: quantised runtimes and inference servers._

| Project | Stars | License | What it does | Last push |
|---|---:|---|---|---|
| [nomic-ai/gpt4all](https://github.com/nomic-ai/gpt4all) | 77,357 | - | GPT4All: Run Local LLMs on Any Device. Open-source and available for commercial use. | 2025-05-27 |
| [openvinotoolkit/openvino](https://github.com/openvinotoolkit/openvino) | 11,068 | - | OpenVINO™ is an open source toolkit for optimizing and deploying AI inference | 2026-10-26 |
| [Tiiny-AI/PowerInfer](https://github.com/Tiiny-AI/PowerInfer) | 9,850 | - | High-speed Large Language Model Serving for Local Deployment | 2026-05-11 |
| [xorbitsai/inference](https://github.com/xorbitsai/inference) | 9,627 | - | Swap GPT for any LLM by changing a single line of code. Xinference lets you run open-source, speech, and multimodal models on cloud, on-prem, or your laptop — all through one unifi | 2026-10-26 |
| [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) | 9,413 | - | ~95% on SimpleQA (e.g. Qwen3.6-27B on a 3090). Supports all local and cloud LLMs (llama.cpp, Ollama, Google, ...). 10+ search engines - arXiv, PubMed, your private documents. Every | 2026-10-26 |
| [FareedKhan-dev/kimi-k3-in-c](https://github.com/FareedKhan-dev/kimi-k3-in-c) | 9,188 | - | A 2.78-trillion-parameter Kimi K3 running inference on a single CPU in 8.24 GB of RAM. Portable C99: no BLAS, no framework, no GPU. | 2026-10-02 |
| [bentoml/BentoML](https://github.com/bentoml/BentoML) | 8,920 | - | The easiest way to serve AI apps and models - Build Model Inference APIs, Job queues, LLM apps, Multi-model pipelines, and more! | 2026-10-23 |
| [ai-dynamo/dynamo](https://github.com/ai-dynamo/dynamo) | 8,386 | - | A Datacenter Scale Distributed Inference Serving Framework | 2026-10-26 |
| [drumih/turbo-fieldfare](https://github.com/drumih/turbo-fieldfare) | 7,052 | - | Gemma 4 26B-A4B inference in ~2 GB of RAM on any M-series MacBook | 2026-10-15 |
| [cactus-compute/cactus](https://github.com/cactus-compute/cactus) | 6,160 | - | Quantization, kernels, runtime and inference engine for mobiles, wearables, smart home and robots. | 2026-09-26 |
| [kserve/kserve](https://github.com/kserve/kserve) | 6,158 | - | Standardized Distributed Generative and Predictive AI Inference Platform for Scalable, Multi-Framework Deployment on Kubernetes | 2026-10-26 |
| [lemonade-sdk/lemonade](https://github.com/lemonade-sdk/lemonade) | 5,999 | - | Lemonade helps users discover and run local AI apps by serving optimized LLMs right from their own GPUs and NPUs. Join our discord: https://discord.gg/5xXzkMu8Zk | 2026-10-26 |
| [Michael-A-Kuykendall/shimmy](https://github.com/Michael-A-Kuykendall/shimmy) | 5,992 | - | ⚡ Pure-Rust WebGPU inference engine — OpenAI-API compatible, GGUF native, runs on any GPU. No Python. No llama.cpp. Single binary. | 2026-10-19 |
| [gpustack/gpustack](https://github.com/gpustack/gpustack) | 5,892 | - | A GPU cluster manager for high-performance AI model serving (vLLM, SGLang) and on-demand SSH-accessible GPU instances. | 2026-10-26 |
| [maziyarpanahi/openmed](https://github.com/maziyarpanahi/openmed) | 5,713 | - | Local-first healthcare AI: clinical NER and HIPAA PII de-identification on hardware you control. 2,200+ medical models, 35 model-backed PII languages, and Python, MLX, Android and  | 2026-10-26 |

## LLM Ops: Evals & Observability

_Tests, evals, tracing and prompt tooling that keep quality measurable._

| Project | Stars | License | What it does | Last push |
|---|---:|---|---|---|
| [langfuse/langfuse](https://github.com/langfuse/langfuse) | 36,504 | - | 🪢 Open source agent evals & observability: Trace, evaluate, and improve LLM applications with one open platform. | 2026-10-26 |
| [comet-ml/opik](https://github.com/comet-ml/opik) | 22,928 | - | Debug, evaluate, and monitor your LLM applications, RAG systems, and agentic workflows with comprehensive tracing, automated evaluations, and production-ready dashboards. | 2026-10-26 |
| [confident-ai/deepeval](https://github.com/confident-ai/deepeval) | 19,108 | - | The LLM Evaluation Framework | 2026-10-23 |
| [raga-ai-hub/RagaAI-Catalyst](https://github.com/raga-ai-hub/RagaAI-Catalyst) | 16,180 | - | Python SDK for Agent AI Observability, Monitoring and Evaluation Framework. Includes features like agent, llm and tools tracing, debugging multi-agentic system, self-hosted dashboa | 2026-02-11 |
| [vibrantlabsai/ragas](https://github.com/vibrantlabsai/ragas) | 16,151 | - | Supercharge Your LLM Application Evaluations 🚀 | 2026-02-24 |
| [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix) | 12,006 | - | AI Observability & Evaluation | 2026-10-26 |
| [oumi-ai/oumi](https://github.com/oumi-ai/oumi) | 9,414 | - | Easily fine-tune (SFT/RL), evaluate, and deploy Qwen, Gemma, or any open agentic LLM/VLM! | 2026-10-23 |
| [evidentlyai/evidently](https://github.com/evidentlyai/evidently) | 8,011 | - | Evidently is ​​an open-source ML and LLM observability framework. Evaluate, test, and monitor any AI-powered system or data pipeline. From tabular data to Gen AI. 100+ metrics. | 2026-09-29 |
| [traceloop/openllmetry](https://github.com/traceloop/openllmetry) | 7,508 | - | Open-source observability for your GenAI or LLM application, based on OpenTelemetry | 2026-10-19 |
| [FailproofAI/failproofai](https://github.com/FailproofAI/failproofai) | 6,635 | - | Observability and enforcement for AI agent harnesses. Capture every run and runtime reliability with policy enforcement. | 2026-10-25 |
| [jeinlee1991/chinese-llm-benchmark](https://github.com/jeinlee1991/chinese-llm-benchmark) | 6,492 | - | 非线智能 NoneLinear - ReLE评测：中文AI大模型能力评测（持续更新）：目前已囊括374个大模型，覆盖chatgpt、gpt-5.4、谷歌gemini-3.1-pro、Claude-4.6、文心ERNIE-X1.1、ERNIE-5.0、qwen3.6-max、qwen3.6-plus、百川、讯飞星火、商汤senseChat等商用模型， 以及st | 2026-10-21 |
| [Helicone/helicone](https://github.com/Helicone/helicone) | 6,238 | - | 🧊 Open source LLM observability platform. One line of code to monitor, evaluate, and experiment. YC W23 🍓 | 2026-10-24 |
| [Giskard-AI/giskard-oss](https://github.com/Giskard-AI/giskard-oss) | 5,923 | - | 🐢 Open-Source Evaluation & Testing library for LLM Agents | 2026-10-26 |
| [langwatch/langwatch](https://github.com/langwatch/langwatch) | 4,991 | - | Open-Source Agent Observability & Evals for AI Platform teams. Trace, test, route and govern every agent & coding assistant in the company. | 2026-10-26 |
| [latitude-dev/latitude-llm](https://github.com/latitude-dev/latitude-llm) | 4,734 | - | Open-source observability for AI agents. Find where your agents fail, dispatch your coding agent to fix it, and verify the fix against real traces. | 2026-10-26 |

| [flik2002/openclaw-monitor](https://github.com/flik2002/openclaw-monitor) | ![GitHub Repo stars](https://img.shields.io/github/stars/flik2002/openclaw-monitor?style=social) | - | Free open-source monitoring dashboard for OpenClaw AI agents — token usage, session tracking, 7-day trends, multi-model support. Vue 3 + ECharts. | 2026-09-15 |

## Reliability & Cost Control

_Watchdogs, alerting, uptime checks and budget guards for unattended workloads._

| Project | Stars | License | What it does | Last push |
|---|---:|---|---|---|
| [louislam/uptime-kuma](https://github.com/louislam/uptime-kuma) | 92,925 | - | A fancy self-hosted monitoring tool | 2026-10-26 |
| [prometheus/prometheus](https://github.com/prometheus/prometheus) | 66,773 | - | The Prometheus monitoring system and time series database. | 2026-10-26 |
| [alibaba/Sentinel](https://github.com/alibaba/Sentinel) | 23,148 | - | A powerful flow control component enabling reliability, resilience and monitoring for microservices. (面向云原生微服务的高可用流控防护组件) | 2026-05-27 |
| [ccfos/nightingale](https://github.com/ccfos/nightingale) | 13,390 | - | Open-source, self-hosted alerting for metrics, logs, and databases. Includes a built-in AI agent and MCP server. | 2026-10-22 |
| [keephq/keep](https://github.com/keephq/keep) | 12,444 | - | The open-source AIOps and alert management platform | 2026-10-22 |
| [TwiN/gatus](https://github.com/TwiN/gatus) | 12,409 | - | Automated developer-oriented status page with alerting and incident support | 2026-10-26 |
| [bluewave-labs/Checkmate](https://github.com/bluewave-labs/Checkmate) | 10,988 | - | Checkmate is an open-source, self-hosted tool designed to track and monitor server hardware, uptime, response times, and incidents in real-time with beautiful visualizations. Don't | 2026-10-26 |
| [openstatusHQ/openstatus](https://github.com/openstatusHQ/openstatus) | 9,233 | - | Open-source status page, incident response and uptime monitoring | 2026-10-26 |
| [zabbix/zabbix](https://github.com/zabbix/zabbix) | 6,507 | - | Real-time monitoring of IT components and services, such as networks, servers, VMs, applications and the cloud. | 2026-10-23 |
| [animir/node-rate-limiter-flexible](https://github.com/animir/node-rate-limiter-flexible) | 3,597 | - | Atomic and non-atomic counters and rate limiting tools. Limit resource access at any scale. | 2026-10-19 |
| [express-rate-limit/express-rate-limit](https://github.com/express-rate-limit/express-rate-limit) | 3,313 | - | Basic rate-limiting middleware for the Express web server | 2026-10-23 |
| [robusta-dev/robusta](https://github.com/robusta-dev/robusta) | 3,125 | - | Better Prometheus alerts for Kubernetes - smart grouping, AI enrichment, and automatic remediation | 2026-10-25 |
| [alibaba/sentinel-golang](https://github.com/alibaba/sentinel-golang) | 2,963 | - | Sentinel Go enables reliability and resiliency for Go microservices | 2026-07-02 |
| [cstate/cstate](https://github.com/cstate/cstate) | 2,900 | - | 🔥 Open source static (serverless) status page. Uses hyperfast Go & Hugo, minimal HTML/CSS/JS, customizable, outstanding browser support (IE8+), preloaded CMS, read-only API, badges | 2026-10-17 |
| [bucket4j/bucket4j](https://github.com/bucket4j/bucket4j) | 2,816 | - | Java rate limiting library based on token-bucket algorithm. | 2026-10-04 |

## Free-Tier & Low-Cost Infrastructure

_Lightweight tooling that fits small 2 vCPU / 12 GB always-free boxes._

| Project | Stars | License | What it does | Last push |
|---|---:|---|---|---|
| [immich-app/immich](https://github.com/immich-app/immich) | 117,270 | - | High performance self-hosted photo and video management solution. | 2026-10-26 |
| [nocodb/nocodb](https://github.com/nocodb/nocodb) | 65,365 | - | 🔥 🔥 🔥 A Free & Self-hostable Airtable Alternative | 2026-10-26 |
| [coollabsio/coolify](https://github.com/coollabsio/coolify) | 64,763 | - | An open-source, self-hostable PaaS alternative to Vercel, Heroku & Netlify that lets you easily deploy static sites, databases, full-stack applications and 360+ one-click services  | 2026-10-26 |
| [usememos/memos](https://github.com/usememos/memos) | 64,083 | - | Memos is an open-source, self-hosted note-taking app that brings your everyday thoughts together in a personal timeline. Your data stays yours, and you choose what to keep private  | 2026-10-26 |
| [go-gitea/gitea](https://github.com/go-gitea/gitea) | 58,695 | - | Git with a cup of tea! Painless self-hosted all-in-one software development service, including Git hosting, code review, team collaboration, package registry and CI/CD | 2026-10-26 |
| [siyuan-note/siyuan](https://github.com/siyuan-note/siyuan) | 46,939 | - | An open-source, privacy-first, self-hosted knowledge workspace where humans and AI agents work together 开源、隐私优先、自托管的知识工作空间，让人与智能体在此协作 | 2026-10-26 |
| [khoj-ai/khoj](https://github.com/khoj-ai/khoj) | 37,832 | - | Your AI second brain. Self-hostable. Get answers from the web or your docs. Build custom agents, schedule automations, do deep research. Turn any online or local LLM into your pers | 2026-08-02 |
| [glanceapp/glance](https://github.com/glanceapp/glance) | 37,699 | - | A self-hosted dashboard that puts all your feeds in one place | 2026-10-20 |
| [feder-cr/invisible_dots](https://github.com/feder-cr/invisible_dots) | 32,250 | - | Open-source, self-hosted alternative to OpenAI Dots, Grok Bot. Built to be undetectable by anti-bot systems. | 2026-10-25 |
| [dokku/dokku](https://github.com/dokku/dokku) | 32,201 | - | A docker-powered PaaS that helps you build and manage the lifecycle of applications | 2026-10-25 |
| [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | 32,171 | - | Privacy first AI meeting note taker. Download Free and open source granola, otter ai, fireflies alternative. Parakeet / Whisper live transcription, on-device speaker diarization, b | 2026-10-24 |
| [karakeep-app/karakeep](https://github.com/karakeep-app/karakeep) | 29,992 | - | A self-hostable bookmark-everything app (links, notes and images) with AI-based automatic tagging and full text search | 2026-10-26 |
| [lissy93/dashy](https://github.com/lissy93/dashy) | 26,814 | - | 🚀 A self-hostable personal dashboard built for you. Includes status-checking, widgets, themes, icon packs, a UI editor and tons more! | 2026-10-23 |
| [henrygd/beszel](https://github.com/henrygd/beszel) | 26,548 | - | Lightweight server monitoring with historical data, docker stats, and alerts. | 2026-10-25 |
| [Termix-SSH/Termix](https://github.com/Termix-SSH/Termix) | 15,675 | - | Self-hosted, plugin-based server management. | 2026-10-25 |

## Learning & Reference

_Curated lists, books and courses worth reading before you build._

| Project | Stars | License | What it does | Last push |
|---|---:|---|---|---|
| [agulli/atlas-agents](https://github.com/agulli/atlas-agents) | 751 | - | Official code repository for "Hands-on AI Agents" by Antonio Gulli. Production-grade patterns (ReAct, CoT, Reflection, Plan-and-Execute, Multi-Agent Swarms). | 2026-07-17 |
| [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | 524,849 | - | 😎 Awesome lists about all kinds of interesting topics [NOTE: Pull requests are temporarily disabled until I have a chance to catch up with the existing ones] | 2026-09-02 |
| [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | 330,528 | - | A list of Free Software network services and web applications which can be hosted on your own servers | 2026-10-22 |
| [vinta/awesome-python](https://github.com/vinta/awesome-python) | 330,340 | - | The definitive list that answers "I want to do X in Python, which tool should I use?" | 2026-10-26 |
| [avelino/awesome-go](https://github.com/avelino/awesome-go) | 190,412 | - | A curated list of awesome Go frameworks, libraries and software | 2026-10-26 |
| [f/prompts.chat](https://github.com/f/prompts.chat) | 174,600 | - | f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy. | 2026-10-26 |
| [Hack-with-Github/Awesome-Hacking](https://github.com/Hack-with-Github/Awesome-Hacking) | 123,660 | - | A collection of various awesome lists for hackers, pentesters and security researchers | 2026-07-26 |
| [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | 123,589 | - | A collection of DESIGN.md files analysis by popular brand design systems. Drop one into your project and let coding agents generate a matching UI. | 2026-10-14 |
| [jaywcjlove/awesome-mac](https://github.com/jaywcjlove/awesome-mac) | 117,061 | - |  This project is dedicated to collecting high-quality macOS software and organizing them systematically by different categories for easy search and use. | 2026-10-26 |
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | 96,880 | - | A collection of MCP servers. | 2026-10-23 |
| [MunGell/awesome-for-beginners](https://github.com/MunGell/awesome-for-beginners) | 90,730 | - | A list of awesome beginners-friendly projects. | 2026-10-01 |
| [binhnguyennus/awesome-scalability](https://github.com/binhnguyennus/awesome-scalability) | 75,099 | - | The Patterns of Scalable, Reliable, and Performant Large-Scale Systems | 2026-01-04 |
| [enaqx/awesome-react](https://github.com/enaqx/awesome-react) | 75,060 | - | A collection of awesome things regarding React ecosystem | 2026-09-04 |
| [fffaraz/awesome-cpp](https://github.com/fffaraz/awesome-cpp) | 74,033 | - | A curated list of awesome C++ (or C) frameworks, libraries, resources, and shiny things. Inspired by awesome-... stuff. | 2026-10-26 |
| [sindresorhus/awesome-nodejs](https://github.com/sindresorhus/awesome-nodejs) | 67,270 | - | :zap: Delightful Node.js packages and resources [BECAUSE OF TOO MUCH SPAM AND LOW-QUALITY SUBMISSIONS, SUBMISSIONS ARE PAUSED TEMPORARILY] | 2026-09-02 |
| [Solido/awesome-flutter](https://github.com/Solido/awesome-flutter) | 61,674 | - | An awesome list that curates the best Flutter libraries, tools, tutorials, articles and more. | 2026-09-03 |

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

## Why this index lives on GitHub

![Branching history and distributed collaboration](docs/assets/github-benefits-collaboration.jpg)

![Automated verification pipeline](docs/assets/github-benefits-cicd.jpg)

The value of a living index is not the file itself, it is the pipeline around it:

- **Continuous verification.** GitHub Actions re-checks every entry against the GitHub API on a daily schedule, so the list cannot silently rot.
- **Versioned history.** Every verdict change is a reviewable commit — you can see exactly when a project was archived, renamed, or revived.
- **Open collaboration.** Issues and pull requests are the contribution path, and the same automated gate that verifies entries also verifies suggestions.
- **Zero-cost distribution.** Static hosting on GitHub Pages serves the [live dashboard](https://amz34.github.io/awesome-agent-infrastructure/) with no server to operate.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) — or open a **Suggest a project** issue and the gate will be checked in the next refresh.

## 👤 Maintainer & Ecosystem

Curated and maintained by **[Aamir Zameer (@Amz34)](https://github.com/Amz34)** — AI Automation Engineer & Systems Architect.

👉 **[Follow @Amz34 on GitHub](https://github.com/Amz34)** for weekly live-tested agent architecture updates, free-tier deployments, and zero-token runtime patterns.

### Production Suites from the Author
- **[az-zero-token-data-engine](https://github.com/Amz34/az-zero-token-data-engine)** — Local deterministic Pandas/OpenPyXL tabular engine slashing 98% LLM token consumption on enterprise sheets.
- **[antigravity-zero-token-suite](https://github.com/Amz34/antigravity-zero-token-suite)** — Production edge agent runtime on Google Antigravity + Gemini Flash offloading AST to local Linux POSIX compute.
- **[selfhosted-agent-stack](https://github.com/Amz34/selfhosted-agent-stack)** — Hardened 24/7 crash-proof agent ops on free-tier cloud (watchdog daemons, zram, auto-reaping).
- **[hermes-slack-agents](https://github.com/Amz34/hermes-slack-agents)** — Multi-tenant Slack AI agent gateway with isolated memory and zero per-seat SaaS costs.
- **[ai-can-run](https://github.com/Amz34/ai-can-run)** — Client-side in-browser hardware detection and VRAM math engine ranking open models.

## License

MIT — see [LICENSE](LICENSE). Copy, remix, republish freely.
