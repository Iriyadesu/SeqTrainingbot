import discord
from discord.ui import View, Select
from Modals import OtherTrainingModal

class TrainingDropdown(View):
    def __init__(self):
        super().__init__()
        self.add_item(TrainingSelect())

class TrainingSelect(Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="War Training", value="war"),
            discord.SelectOption(label="Raid Training", value="raid"),
            discord.SelectOption(label="Other", value="other"),
        ]
        super().__init__(placeholder="Select Training Type", options=options)

    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "raid":
            raid_options = [
                discord.SelectOption(label="Nol", value="nol"),
                discord.SelectOption(label="Notg", value="notg"),
                discord.SelectOption(label="TNA", value="tna"),
                discord.SelectOption(label="TCC", value="tcc"),
            ]
            view = View()
            view.add_item(Select(placeholder="Select Raid Type", options=raid_options))
            await interaction.response.send_message("Select your Raid Type:", view=view, ephemeral=True)
        elif self.values[0] == "other":
            await interaction.response.send_modal(OtherTrainingModal())
        else:
            embed = discord.Embed(title="Training Request", description=f"**Training Type:** War Training\n**Requested by:** {interaction.user.mention}")
            embed.set_thumbnail(url=interaction.user.display_avatar.url)
            await interaction.channel.send(embed=embed)
            await interaction.response.send_message("Your training request has been submitted.", ephemeral=True)