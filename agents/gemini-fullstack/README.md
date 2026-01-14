# Gemini Fullstack Agent Development Kit (ADK) Quickstart

The **Gemini Fullstack Agent Development Kit (ADK) Quickstart** is a production-ready blueprint for building a sophisticated, fullstack research agent with Gemini. It's built to demonstrate how the ADK helps structure complex agentic workflows, build modular agents, and incorporate critical Human-in-the-Loop (HITL) steps.

<table>
  <thead>
    <tr>
      <th colspan="2">Key Features</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>🏗️</td>
      <td>**Fullstack & Production-Ready:** A complete React frontend and ADK-powered FastAPI backend, with deployment options for <a href="https://cloud.google.com/run">Google Cloud Run</a> and <a href="https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview">Vertex AI Agent Engine</a>.</td>
    </tr>
    <tr>
      <td>🧠</td>
      <td>**Advanced Agentic Workflow:** The agent uses Gemini to **strategize** a multi-step plan, **reflect** on findings to identify gaps, and **synthesize** a final, comprehensive report.</td>
    </tr>
    <tr>
      <td>🔄</td>
      <td>**Iterative & Human-in-the-Loop Research:** Involves the user for plan approval, then autonomously loops through searching (via Gemini function calling) and refining its results until it has gathered sufficient information.</td>
    </tr>
  </tbody>
</table>

Here is the agent in action:

<img src="https://github.com/GoogleCloudPlatform/agent-starter-pack/blob/main/docs/images/adk_gemini_fullstack.gif?raw=true" width="80%" alt="Gemini Fullstack ADK Preview">

This project adapts concepts from the [Gemini FullStack LangGraph Quickstart](https://github.com/google-gemini/gemini-fullstack-langgraph-quickstart) for the frontend app. 

## 🚀 Getting Started: From Zero to Running Agent in 1 Minute
**Prerequisites:** **[Python 3.10+](https://www.python.org/downloads/)**, **[Node.js](https://nodejs.org/)**, **[uv](https://github.com/astral-sh/uv)**

You have two options to get started. Choose the one that best fits your setup:

*   A. **[Google AI Studio](#a-google-ai-studio)**: Choose this path if you want to use a **Google AI Studio API key**. This method involves cloning the sample repository.
*   B. **[Google Cloud Vertex AI](#b-google-cloud-vertex-ai)**: Choose this path if you want to use an existing **Google Cloud project** for authentication. This method generates a new, prod-ready project using the [agent-starter-pack](https://goo.gle/agent-starter-pack) including all the deployment scripts required.

---

### A. Google AI Studio

You'll need a **[Google AI Studio API Key](https://aistudio.google.com/app/apikey)**.

#### Step 1: Clone Repository
Clone the repository and `cd` into the project directory.

```bash
git clone https://github.com/google/adk-samples.git
cd adk-samples/python/agents/gemini-fullstack
```

#### Step 2: Set Environment Variables
Create a `.env` file in the `app` folder by running the following command (replace YOUR_AI_STUDIO_API_KEY with your actual API key):

```bash
echo "GOOGLE_GENAI_USE_VERTEXAI=FALSE" >> app/.env
echo "GOOGLE_API_KEY=YOUR_AI_STUDIO_API_KEY" >> app/.env
```

#### Step 3: Install & Run
From the `gemini-fullstack` directory, install dependencies and start the servers.

```bash
make install && make dev
```
Your agent is now running at `http://localhost:5173`.

---

### B. Google Cloud Vertex AI

You'll also need: **[Google Cloud SDK](https://cloud.google.com/sdk/docs/install)** and a **Google Cloud Project** with the **Vertex AI API** enabled.

#### Step 1: Create Project from Template
This command uses the [Agent Starter Pack](https://goo.gle/agent-starter-pack) to create a new directory (`my-fullstack-agent`) with all the necessary code.
```bash
# Create and activate a virtual environment
python -m venv .venv && source .venv/bin/activate # On Windows: .venv\Scripts\activate

# Install the starter pack and create your project
pip install --upgrade agent-starter-pack
agent-starter-pack create my-fullstack-agent -a adk_gemini_fullstack
```
<details>
<summary>⚡️ Alternative: Using uv</summary>

If you have [`uv`](https://github.com/astral-sh/uv) installed, you can create and set up your project with a single command:
```bash
uvx agent-starter-pack create my-fullstack-agent -a adk_gemini_fullstack
```
This command handles creating the project without needing to pre-install the package into a virtual environment.
</details>

You'll be prompted to select a deployment option (Agent Engine or Cloud Run) and verify your Google Cloud credentials.

#### Step 2: Install & Run
Navigate into your **newly created project folder**, then install dependencies and start the servers.
```bash
cd my-fullstack-agent && make install && make dev
```
Your agent is now running at `http://localhost:5173`.

## ☁️ Cloud Deployment
> **Note:** The cloud deployment instructions below apply only if you chose the **Google Cloud Vertex AI** option.

You can quickly deploy your agent to a **development environment** on Google Cloud. You can deploy your latest code at any time with:

```bash
# Replace YOUR_DEV_PROJECT_ID with your actual Google Cloud Project ID
gcloud config set project YOUR_DEV_PROJECT_ID
make backend
```

For robust, **production-ready deployments** with automated CI/CD, please follow the detailed instructions in the **[Agent Starter Pack Development Guide](https://googlecloudplatform.github.io/agent-starter-pack/guide/development-guide.html#b-production-ready-deployment-with-ci-cd)**.

## For Agent Execution Details, see [AGENT_EXECUTION.md](./AGENT_EXECUTION.md)

## Customization

You can modify and extend this agent's behavior by editing the backend code.

*   **Modifying Agent Logic:** The core logic for all sub-agents (planner, researcher, critic, composer) is defined in `app/agent.py`. You can change the prompts, tools, or reasoning steps by modifying the agent definitions here.
*   **Adjusting Research Parameters:** Key parameters, such as the Gemini models used or the number of research loop iterations, can be adjusted in the `ResearchConfiguration` dataclass within `app/config.py`.
*   **Syncing with Frontend:** The frontend UI integrates with the backend through specific agent names that process outputs differently (e.g., research findings vs. final report), update the activity timeline with appropriate titles/icons, and track research metrics like website counts. 
    Important agent names include:
    * `section_researcher` & `enhanced_search_executor` - track websites consulted
    * `report_composer_with_citations` - processes final report
    * `interactive_planner_agent` - updates AI messages during planning
    * `plan_generator` and `section_planner` - used for timeline labels
    
    If you rename agents in `app/agent.py`, you must update their names in the frontend code (`/ui`) to maintain functionality.


## Troubleshooting

If you encounter issues while setting up or running this agent, here are some resources to help you troubleshoot:
- [ADK Documentation](https://google.github.io/adk-docs/): Comprehensive documentation for the Agent Development Kit
- [Vertex AI Authentication Guide](https://cloud.google.com/vertex-ai/docs/authentication): Detailed instructions for setting up authentication
- [Agent Starter Pack Troubleshooting](https://googlecloudplatform.github.io/agent-starter-pack/guide/troubleshooting.html): Common issues


## 🛠️ Technologies Used

### Backend
*   [**Agent Development Kit (ADK)**](https://github.com/google/adk-python): The core framework for building the stateful, multi-turn agent.
*   [**FastAPI**](https://fastapi.tiangolo.com/): High-performance web framework for the backend API.
*   [**Google Gemini**](https://cloud.google.com/vertex-ai/generative-ai/docs): Used for planning, reasoning, search query generation, and final synthesis.

### Frontend
*   [**React**](https://reactjs.org/) (with [Vite](https://vitejs.dev/)): For building the interactive user interface.
*   [**Tailwind CSS**](https://tailwindcss.com/): For utility-first styling.
*   [**Shadcn UI**](https://ui.shadcn.com/): A set of beautifully designed, accessible components.

## Disclaimer

This agent sample is provided for illustrative purposes only. It serves as a basic example of an agent and a foundational starting point for individuals or teams to develop their own agents.

Users are solely responsible for any further development, testing, security hardening, and deployment of agents based on this sample. We recommend thorough review, testing, and the implementation of appropriate safeguards before using any derived agent in a live or critical system.
