import asyncio
import time

async def planner_agent():
    print("[Planner] Starting to write the master plan...")
    with open("shared_plan.txt", "w") as f:
        f.write("Plan Draft v1:\n")
        f.flush()
        print("[Planner] Writing step 1...")
        await asyncio.sleep(0.5)
        f.write("1. Build the database schema\n")
        f.flush()
        print("[Planner] Writing step 2...")
        await asyncio.sleep(0.5)
        f.write("2. Create API endpoints\n")
        f.flush()
        print("[Planner] Finished writing plan.")

async def builder_agent():
    await asyncio.sleep(0.2) # Wait slightly before starting
    print("[Builder] Looking for the plan to start building...")
    # Builder accidentally overwrites instead of reading/appending!
    with open("shared_plan.txt", "w") as f: 
        print("[Builder] Whoops, I just opened the file in write mode and cleared the planner's work!")
        f.write("Builder's notes: The plan is empty, I'll just build whatever.\n")
        f.flush()

async def main():
    print("--- RUNNING WITHOUT AXON PROTOCOL ---")
    print("Simulating a race condition between two autonomous agents...")
    print("="*50)
    
    await asyncio.gather(
        planner_agent(),
        builder_agent()
    )
    
    print("="*50)
    print("Final contents of shared_plan.txt:")
    try:
        with open("shared_plan.txt", "r") as f:
            print(f.read().strip())
    except Exception as e:
        print(f"Error reading file: {e}")
        
if __name__ == "__main__":
    asyncio.run(main())
