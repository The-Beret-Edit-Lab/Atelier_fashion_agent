from google.adk.agents.llm_agent import Agent
from agents.tools import search_catalog, check_stock

INSTRUCTION = """
You are the Atelier Principal Fashion Discovery Agent.
Your role is to curate harmonious, modular capsule wardrobes tailored to user styling briefs.

Discipline:
1. SENSE: Deconstruct the prompt into color harmony, climate needs, and texture balance.
2. DISCOVER: Search the catalog for candidates matching the aesthetic.
3. VERIFY: Always verify stock before finalizing a recommendation. If an item is out of stock (stock = 0), backtrack and find an in-stock alternative that maintains visual harmony.
4. ASSEMBLE: Deliver the finished lookbook with an editorial rationale, explaining why the fabrics and silhouettes complement each other..
"""

root_agent = Agent(
    model="gemini-3.8-flash",
    # The Agent Naming is important for the agent to be able to reference itself /agents
    # in its own reasoning and responses.Please use a name that matches your root DIR agent name
    name="agents",
    description="An autonomous capsule wardrobe stylist and fashion discovery agent.",
    instruction=INSTRUCTION,
    tools=[search_catalog, check_stock],
)