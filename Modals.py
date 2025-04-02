import discord
from discord.ui import Modal, Select, TextInput

class TrainingRequestModal(Modal, title="Training Request"):
    """
    This modal is for requesting training sessions.
    """
    training_type = Select(
        placeholder="Select Training Type",
        options=[
            discord.SelectOption(label="War Training", value="war"),
            discord.SelectOption(label="Raid Training", value="raid"),
            discord.SelectOption(label="Other", value="other"),
        ]
    )

    raid_type = Select(
        placeholder="Select Raid Type",
        options=[
            discord.SelectOption(label="Nol", value="nol"),
            discord.SelectOption(label="Notg", value="notg"),
            discord.SelectOption(label="TNA", value="tna"),
            discord.SelectOption(label="TCC", value="tcc"),
        ],
        disabled=True  # Initially disabled until Raid Training is selected
    )

    other_reason = TextInput(
        label="Please specify",
        placeholder="Enter details...",
        required=False,
        style=discord.TextStyle.paragraph,
        max_length=500
    )

    async def on_submit(self, interaction: discord.Interaction):
        # Enable or disable fields based on the selection
        if self.training_type.values[0] == "raid":
            self.raid_type.disabled = False
            selected_training = f"Raid Training - {self.raid_type.values[0]}"
        elif self.training_type.values[0] == "other":
            selected_training = f"Other - {self.other_reason.value}"
        else:
            selected_training = "War Training"
        
        Thread_Embed = discord.Embed(
            title="Training Request",
            description=f"**Training Type:** {selected_training}\n**Requested by:** {interaction.user.mention}",
        )
        Thread_Embed.set_thumbnail(url=interaction.user.display_avatar.url)
        await interaction.channel.send(embed=Thread_Embed)
        
        await interaction.response.send_message("Your training request has been submitted.", ephemeral=True)

class OtherTrainingModal(discord.ui.Modal, title="Other Training Request"):
    other_reason = discord.ui.TextInput(label="Please specify", placeholder="Enter details...", required=True, max_length=500)
    
    async def on_submit(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Training Request", description=f"**Training Type:** Other - {self.other_reason.value}\n**Requested by:** {interaction.user.mention}")
        embed.set_thumbnail(url=interaction.user.display_avatar.url)
        await interaction.channel.send(embed=embed)
        await interaction.response.send_message("Your training request has been submitted.", ephemeral=True)