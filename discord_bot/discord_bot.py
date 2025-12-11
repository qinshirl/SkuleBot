# discord_bot.py
import os

import httpx
import discord
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
SKULEBOT_API_URL = os.getenv("SKULEBOT_API_URL", "http://127.0.0.1:8000/chat")
GUILD_ID = None


class SkuleBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)

        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        """
        Called by discord.py when the bot logs in.
        We sync slash commands here.
        """
        if GUILD_ID:
            guild = discord.Object(id=int(GUILD_ID))
            self.tree.copy_global_to(guild=guild)
            await self.tree.sync(guild=guild)
            print(f"Synced commands to guild {GUILD_ID}")
        else:
            await self.tree.sync()
            print("Synced global commands")


client = SkuleBot()


@client.tree.command(
    name="skule",
    description="Ask the SkuleBot course assistant a question",
)
@app_commands.describe(query="Your question about UofT Engineering courses/exams")
async def skule(
    interaction: discord.Interaction,
    query: str,
):
    """Slash command handler for /skule."""

    await interaction.response.defer(thinking=True)

    try:
        async with httpx.AsyncClient(timeout=60.0) as http_client:
            resp = await http_client.post(
                SKULEBOT_API_URL,
                json={"message": query},
            )
            resp.raise_for_status()
            data = resp.json()
            reply_text = data.get("reply", "I couldn't parse a reply from the backend.")
    except Exception as e:
        print("Error talking to backend:", e)
        reply_text = "Oops, something went wrong talking to SkuleBot's brain."

    # Discord has a 2000-char limit; be safe and chunk
    if len(reply_text) <= 2000:
        await interaction.followup.send(reply_text)
    else:
        for i in range(0, len(reply_text), 1900):
            await interaction.followup.send(reply_text[i : i + 1900])


def main():
    if not DISCORD_TOKEN:
        raise RuntimeError("DISCORD_BOT_TOKEN is not set in .env")
    client.run(DISCORD_TOKEN)


if __name__ == "__main__":
    main()
