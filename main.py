import asyncio
from droidrun import DroidAgent, DroidrunConfig, AgentConfig, AdbTools
from llama_index.llms.google_genai import GoogleGenAI
import os

async def main():

    llm = GoogleGenAI(api_key = os.environ.get("GEMINI_API_KEY"), model="models/gemini-2.5-flash")
    # Initialize the DroidAgent
    droid_agent = DroidAgent(
            goal = """ *Role:* You are a Social Media Marketing Assistant.
*Goal:* Send personalized event invitations to a list of contacts using WhatsApp.
*Context:* You have a list of names in the "Google Sheets" app and need to message them on "WhatsApp".

*Task Workflow:*
1. *Acquire Target:*
   - Open the app "Google Sheets".
   - Tap on the file named "contacts".
   - Locate the next unread name in the list (e.g., Start at Cell A2).
   - if unable to find the cell click on the three dots then search by the cell name.
   - Copy the text of that cell to the clipboard.
   - Action: Store this name in memory as .

2. *Navigate to Platform:*
   - Switch apps to "WhatsApp".
   - Go to the whatsapp home page.
   - Tap the "New Chat" or "Search" icon (magnifying glass) at the top right.

3. *Locate Contact:*
   - Paste the clipboard content into the search bar.
   - Wait 2 seconds for search results to load.
   - Tap the first contact result that matches the name.

4. *Execute Message:*
   - Tap the text input field.
   - Type the following message: "Hey {USER_NAME}, we are hosting the Droidrun DevSprint meetup this weekend. Would love to see you there! 🚀"
   - Tap the "Send" button (paper plane icon).

5. *Loop & Safety:*
   - Wait 5 seconds (to avoid spam detection).
   - Switch back to "Google Sheets".
   - Move to the next cell.
   - Repeat steps 3""",
            config=DroidrunConfig(
            agent=AgentConfig(max_steps=1000)),
            llms = llm,
            tools=AdbTools()
        )
    
    await droid_agent.run()

    
if __name__ == "__main__":
    asyncio.run(main())
