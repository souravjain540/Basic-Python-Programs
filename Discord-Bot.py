# A Discord Bot example using hikari and lightbulb libraries instead of discord.py
# Author: https://github.com/IQExotic/
# Feel free to use this code in your own projects, or contribute to this file.

# Import the libraries we need
import hikari
import lightbulb

# Set the token variable to make your bot work
token = "Yor_Bot_Token_Here"

# Setup the Bot and give it "intents" to be able to interact with the server.
### MAKE SURE TO ENABLE SERVER MEMBERS INTENT IN THE DISCORD DEVELOPER PORTAL ###
bot = lightbulb.BotApp(
    token=token,
    intents=hikari.Intents.ALL_UNPRIVILEGED
    | hikari.Intents.MESSAGE_CONTENT
    | hikari.Intents.GUILD_MEMBERS,
)


@bot.command()
# The option for the command to choose a user. This can be removed if you don't need it.
@lightbulb.option("user", "who to say hello to", type=hikari.OptionType.USER, required=True)
# What your Command is called and what it does
@lightbulb.command("hey", "say Hello.")
@lightbulb.implements(lightbulb.SlashCommand)
async def hey(event: lightbulb.SlashContext) -> None:
    user = event.options.user  # The user that was chosen with the option
    await event.interaction.create_initial_response(
        content=f"Hey {user.mention}",
        flags=64,
        response_type=hikari.ResponseType.MESSAGE_CREATE
    )  # Create an ephemeral response to the command where it mentions the user.


@bot.command()
# What your Command is called and what it does
@lightbulb.command("ping", "sends a pong back.")
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(event: lightbulb.SlashContext) -> None:
    # Create a response to the command but not ephemeral
    await event.respond("Pong!")


bot.run()
