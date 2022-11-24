import * as dotenv from 'dotenv' 
dotenv.config()

import fs from 'node:fs';
import path from 'node:path';



import { REST, Routes } from 'discord.js';
import { TOKEN } from './consts.js';
import ping from "./commands/ping.js"


export async function deployCommands(guildIds,clientIds){


ping.data
	

const commands:string[] = [];
// Grab all the command files from the commands directory you created earlier
const commandFiles = fs.readdirSync('./commands').filter(file => file.endsWith('.js'));

// Grab the SlashCommandBuilder#toJSON() output of each command's data for deployment
for (const file of commandFiles) {
	const command = (await import(`./commands/${file}`))
	commands.push(command.data.toJSON());
}

// Construct and prepare an instance of the REST module
const rest = new REST({ version: '10' }).setToken(TOKEN);

// and deploy your commands!

	try {
		console.log(`Started refreshing ${commands.length} application (/) commands.`);

		// The put method is used to fully refresh all commands in the guild with the current set
		const data = await rest.put(
			Routes.applicationGuildCommands(clientIds, guildIds),
			{ body: commands },
		);
		//@ts-ignore
		console.log(`Successfully reloaded ${data.length} application (/) commands.`);
	} catch (error) {
		// And of course, make sure you catch and log any errors!
		console.error(error);
	}


}


