
import fs  from 'node:fs/promises'
import path from 'node:path';
import { Client, Collection, IntentsBitField, ActivityType, Events } from 'discord.js';
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
const commandFiles = (await fs.readdir("./build/commands")).filter(file => file.endsWith('.js'));

// Grab all the command files from the commands directory you created earlier
console.log(`found ${commandFiles.length} command files`)


for (const file of commandFiles) {

	const command = (await import(`./commands/${file}`)).default;
	// Set a new item in the Collection with the key as the command name and the value as the exported module
	if ('data' in command && 'execute' in command) {
		client.commands.set(command.data.name, command);
	} else {
		console.log(`[WARNING] The command is missing a required "data" or "execute" property.`);
	}
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
});

client.on(Events.InteractionCreate, async interaction => {
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

client.on(Events.MessageCreate, message => {
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

function checkforWord(inp:string,word:string){
	return (inp.toLowerCase().replace(/ /g,"").includes(word))
}