from bedrock_agentcore.runtime import BedrockAgentCoreApp
from strands import Agent
from strands.models import BedrockModel
from strands_tools import calculator

# 1. Initialize the AgentCore App container
app = BedrockAgentCoreApp()

# 2. Define the model (Amazon Nova 2 Lite)
model = BedrockModel(model_id="us.amazon.nova-2-lite-v1:0")

# 3. Define a concise, explicit system prompt
SYSTEM_PROMPT = """You are WanderBot, the official AI travel assistant for Horizon Travel.
When asked to calculate costs, points, durations, or any numeric value,
always use the calculator tool for accuracy."""

# 4. Define the entrypoint handler
@app.entrypoint
async def invoke(payload: dict, context=None):
    user_message = payload.get("message", "Hello!")
    
    # Create a fresh agent for each request
    agent = Agent(
        model=model,
        system_prompt=SYSTEM_PROMPT,
        tools=[calculator],
    )
    
    # Return the agent's response
    return agent(user_message)

# 5. Run the app locally
if __name__ == "__main__":
    app.run()
