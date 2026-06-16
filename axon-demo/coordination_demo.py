import asyncio
import os
from axon import AxonClient

# For local testing against the running CLI server
AXON_PROJECT_ID = os.getenv("AXON_PROJECT_ID", "local_dev")
AXON_API_KEY = os.getenv("AXON_API_KEY", "local_key")
AXON_BASE_URL = os.getenv("AXON_BASE_URL", "http://localhost:8000")

async def planner_agent(client: AxonClient):
    print("[Planner] Requesting lock for 'master-plan'...")
    lock = await client.locks.acquire("master-plan", timeout=10)
    if lock:
        print("[Planner] Lock acquired! Writing the master plan safely...")
        
        # Simulate writing plan by storing it in Axon Memory
        plan_content = "Plan Draft v1:\n1. Build the database schema\n2. Create API endpoints"
        await client.memory.store(
            content=plan_content,
            tags={"type": "plan", "status": "draft"}
        )
        print("[Planner] Plan securely stored in Axon Memory.")
        
        await asyncio.sleep(1.5) # Simulate work
        print("[Planner] Releasing lock...")
        await client.locks.release("master-plan")
    else:
        print("[Planner] Failed to acquire lock!")

async def builder_agent(client: AxonClient):
    await asyncio.sleep(0.2)
    print("[Builder] Attempting to read 'master-plan'...")
    
    # Builder respects the lock
    lock_status = await client.locks.status("master-plan")
    if lock_status and lock_status.is_locked:
        print(f"[Builder] Resource is locked by {lock_status.agent_id}. Waiting...")
        # Simple polling loop
        while lock_status and lock_status.is_locked:
            await asyncio.sleep(0.5)
            lock_status = await client.locks.status("master-plan")
    
    print("[Builder] Lock is free. Fetching the plan from Axon Memory...")
    # Search memory for the plan
    memories = await client.memory.search("Plan Draft", limit=1)
    if memories:
        print("[Builder] Successfully retrieved the plan:")
        print(f"  -> {memories[0].content}")
        print("[Builder] Starting to build following the exact plan.")
    else:
        print("[Builder] No plan found in memory!")

async def main():
    print("--- RUNNING WITH AXON PROTOCOL ---")
    print("Simulating coordinated agents using Axon Locks and Memory...")
    print("="*50)
    
    # Initialize clients for both agents
    planner_client = AxonClient(
        base_url=AXON_BASE_URL,
        api_key=AXON_API_KEY,
        project_id=AXON_PROJECT_ID,
        agent_name="PlannerAgent"
    )
    
    builder_client = AxonClient(
        base_url=AXON_BASE_URL,
        api_key=AXON_API_KEY,
        project_id=AXON_PROJECT_ID,
        agent_name="BuilderAgent"
    )
    
    await asyncio.gather(
        planner_agent(planner_client),
        builder_agent(builder_client)
    )
    
    print("="*50)
    print("Coordination successful!")

if __name__ == "__main__":
    asyncio.run(main())
