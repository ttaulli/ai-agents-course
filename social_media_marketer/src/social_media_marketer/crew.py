from crewai import Crew
from config.agents import researcher, writer, editor
from config.tasks import trend_analysis, content_creation, content_review

crew = Crew(
    agents=[researcher, writer, editor],
    tasks=[trend_analysis, content_creation, content_review]
)

