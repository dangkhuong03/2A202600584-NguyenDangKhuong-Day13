import time
from app.agent import LabAgent
from app.tracing import langfuse_context

print("Running single request...")
agent = LabAgent()
agent.run(user_id="flush-user", feature="qa", session_id="s99", message="test flush")

print("Flushing Langfuse...")
langfuse_context.flush()
print("Flushed!")
time.sleep(2)
