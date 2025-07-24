import os
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from .tools.custom_tool import ChromaSearchTool
from typing import List
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

hf_llm = LLM(
    model=os.getenv("MODEL"),
    api_key=os.getenv("HF_TOKEN"),
    provider="huggingface"
)

@CrewBase
class PetloveAgents():
    """PetloveAgents crew"""

    agents: List[BaseAgent]
    tasks: List[Task]


    @agent
    def consultor_vetorial(self) -> Agent:
        return Agent(
            config=self.agents_config['consultor_vetorial'],
            llm=hf_llm
            # verbose=True
        )

    @agent
    def assistente_vendas(self) -> Agent:
        return Agent(
            config=self.agents_config['assistente_vendas'],
            llm=hf_llm
            # verbose=True
        )

    @task
    def recuperar_contexto(self) -> Task:
        return Task(
            config=self.tasks_config['recuperar_contexto'],
            tools=[ChromaSearchTool()]
        )

    @task
    def responder_cliente(self) -> Task:
        return Task(
            config=self.tasks_config['responder_cliente']
        )

    @crew
    def crew(self) -> Crew:
        """Creates the PetloveAgents crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            #verbose=True,
            chat_llm=hf_llm
        )
