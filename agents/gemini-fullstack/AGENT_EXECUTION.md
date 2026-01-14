# Agent Execution Details

## Agent Details

| Attribute | Description |
| :--- | :--- |
| **Interaction Type** | Workflow |
| **Complexity** | Advanced |
| **Agent Type** | Multi Agent |
| **Components** | Multi-agent, Function calling, Web search, React frontend, Human-in-the-Loop |
| **Vertical** | Horizontal |

## How the Agent Thinks: A Two-Phase Workflow


The backend agent, defined in `app/agent.py`, follows a sophisticated workflow to move from a simple topic to a fully-researched report.

The following diagram illustrates the agent's architecture and workflow:

![ADK Gemini Fullstack Architecture](https://github.com/GoogleCloudPlatform/agent-starter-pack/blob/main/docs/images/adk_gemini_fullstack_architecture.png?raw=true)

This process is broken into two main phases:

### Phase 1: Plan & Refine (Human-in-the-Loop)

This is the collaborative brainstorming phase.

1.  **You provide a research topic.**
2.  The agent generates a high-level research plan with several key goals (e.g., "Analyze the market impact," "Identify key competitors").
3.  The plan is presented to **you**. You can approve it, or chat with the agent to add, remove, or change goals until you're satisfied. Nothing happens without your explicit approval.

### Phase 2: Execute Autonomous Research

Once you approve the plan, the agent's `research_pipeline` takes over and works autonomously.

1.  **Outlining:** It first converts the approved plan into a structured report outline (like a table of contents).
2.  **Iterative Research & Critique Loop:** For each section of the outline, it repeats a cycle:
    *   **Search:** It performs web searches to gather information.
    *   **Critique:** A "critic" model evaluates the findings for gaps or weaknesses.
    *   **Refine:** If the critique finds weaknesses, the agent generates more specific follow-up questions and searches again. This loop continues until the research meets a high-quality bar.
3.  **Compose Final Report:** After the research loop is complete, a final agent takes all the verified findings and writes a polished report, automatically adding inline citations that link back to the original sources.

You can edit key parameters (Gemini models, research loop iterations) in the `ResearchConfiguration` dataclass within `app/config.py`.

### Example Interaction

> **User:** A report on the last Google I/O
>
> **Agent:** Here's a research plan for a report on the last Google I/O:
>
> *   Analyze the key announcements and product updates made at Google I/O 2025.
> *   Identify the central themes and strategic directions emphasized by Google during the event, particularly concerning AI, Android, and other emerging technologies like Android XR.
> *   Investigate the reception and industry impact of the major product unveilings and feature enhancements.
> *   Examine any significant shifts or continuities in Google's developer strategy as presented at the conference.
> *   Assess the implications of the announced technologies and initiatives for developers, consumers, and the broader tech landscape.
>
> Does this plan look good, or would you like to refine it further? Once approved, I can initiate the research.
>
> **User:** Looks good!
> *(The agent proceeds to autonomously execute the research, showing its progress on the timeline.)*
>
> **Agent:**
> 
> Google I/O 2025: Key Announcements and Highlights
> ....
