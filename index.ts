
import fs  from 'node:fs'
import path from 'node:path';
import { Client, Collection, IntentsBitField, Emoji, ReactionEmoji, MessageReaction, ActivityType } from 'discord.js';
import { deployCommands } from './deployCommands.js'
import { disses, TOKEN } from './consts.js';

import { fileURLToPath } from 'url'
import { dirname } from 'path'
const __filename = fileURLToPath(import.meta.url)
const __dirname = dirname(__filename)


const client: Client = new Client({ intents: [
	IntentsBitField.Flags.Guilds,
	IntentsBitField.Flags.GuildMessages,
	IntentsBitField.Flags.GuildEmojisAndStickers
] });

client.commands = new Collection();
const commandsPath = path.join(__dirname, 'commands');
const commandFiles = fs.readdirSync(commandsPath).filter(file => file.endsWith('.js'));



for (let file of commandFiles) {
	const filePath = path.join(commandsPath, file);
	const command = await import(filePath);
	client.commands.set(command.data.name, command);
}

client.once('ready', () => {
	//registerSelf(client)
  if(client.user){
    client.user.setActivity("Potato Simulator",{
      type:ActivityType.Playing,
    });
  }
	if(client.readyTimestamp){
    console.log(`Ready at ${new Date(client.readyTimestamp)}`);
  }
	
	deployCommands(client.guilds.cache.map(guild => guild.id),client)
});

client.on('interactionCreate', async interaction => {
	if (!interaction.isCommand()) return;

	const command = client.commands.get(interaction.commandName);

	if (!command) return;

	try {
		await command.execute(interaction);
	} catch (error) {
		console.error(error);
		await interaction.reply({ content: 'There was an error while executing this command!', ephemeral: true });
	}
});

client.on('messageCreate', message => {
	console.log("recived a message")

	if(message.author.id == "790765656571379762"){

		message.react('😡')
		message.reply(disses[Math.floor(Math.random()*disses.length)])
	}

	if(checkforWord(message.content,"balls")){
		message.react('🤨')
	}else if(checkforWord(message.content,"amongus") || checkforWord(message.content,"amogus")){
		message.react('🤢')
	}

});


client.login(TOKEN);

function checkforWord(inp,word){
	return (inp.toLowerCase().replace(/ /g,"").includes(word))
}