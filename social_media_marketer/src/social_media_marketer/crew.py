from crewai import Agent, Crew, Process, Task
from langchain_openai import ChatOpenAI
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class SocialMediaMarketer():
    """Social Media Marketing Crew that generates engaging social media posts"""

    agents: List[BaseAgent]
    tasks: List[Task]
    
    # Configure a more powerful OpenAI model
    llm = ChatOpenAI(model="gpt-4", temperature=0.7)
    
    @agent
    def trend_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['trend_analyst'],
            verbose=True,
            llm=self.llm
        )

    @agent
    def content_creator(self) -> Agent:
        return Agent(
            config=self.agents_config['content_creator'],
            verbose=True,
            llm=self.llm
        )

    @agent
    def engagement_optimizer(self) -> Agent:
        return Agent(
            config=self.agents_config['engagement_optimizer'],
            verbose=True,
            llm=self.llm
        )

    @task
    def analyze_trends_task(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_trends_task'],
            output_file='trend_analysis.md'
        )

    @task
    def create_posts_task(self) -> Task:
        return Task(
            config=self.tasks_config['create_posts_task'],
            output_file='social_media_posts.md'
        )

    @task
    def optimize_posts_task(self) -> Task:
        return Task(
            config=self.tasks_config['optimize_posts_task'],
            output_file='optimized_social_media_posts.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Social Media Marketing crew with three specialized agents"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
