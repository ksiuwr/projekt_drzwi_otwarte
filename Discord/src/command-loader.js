import { readdirSync } from 'node:fs';
import { join } from 'node:path';

async function* loadCommands() {
  const __dirname = import.meta.dirname;
  const foldersPath = join(__dirname, 'commands');
  const commandFolders = readdirSync(foldersPath);

  for (const folder of commandFolders) {
    const commandsPath = join(foldersPath, folder);
    const commandFiles = readdirSync(commandsPath).filter(file => file.endsWith('.js'));
    for (const file of commandFiles) {
      const filePath = join(commandsPath, file);
      const command = (await import(filePath)).default;
      if ('data' in command && 'execute' in command) {
        console.log(`Loaded command ${command.data.name}`);
        yield command;
      } else {
        console.log(
          `[WARNING] The command at ${filePath} is missing a required "data" or "execute" property.`
        );
      }
    }
  }
}

export default loadCommands;
