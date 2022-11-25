import { REST, Routes } from 'discord.js';
import { CLIENTID, TOKEN } from './consts.js';
import fs from 'node:fs/promises';

const commands = [];
// Grab all the command files from the commands directory you created earlier
const commandFiles = (await fs.readdir('./build/commands')).filter(file => file.endsWith('.js'));

console.log(`found ${commandFiles.length} command files`)


// Grab the SlashCommandBuilder#toJSON() output of each command's data for deployment
for (const file of commandFiles) {
	const command = await import(`./commands/${file}`);
	commands.push(command.default.data.toJSON());
}

// Construct and prepare an instance of the REST module
const rest = new REST({ version: '10' }).setToken(TOKEN);

// and deploy your commands!
(async () => {
	try {
		

		// The put method is used to fully refresh all commands in the guild with the current set
		const data = await rest.put(
			Routes.applicationCommands(CLIENTID ),
			{ body: commands },
		);
		//@ts-ignore
		console.log(`Successfully reloaded ${data.length} application (/) commands.`);
	} catch (error) {
		// And of course, make sure you catch and log any errors!
		console.error(error);
	}
})();


