import { spawn } from 'child_process';
import { SlashCommandBuilder } from 'discord.js';

export default {
  cooldown: 6,
  data: new SlashCommandBuilder()
    .setName('openthedoor')
    .setDescription('Otwiera zamek do drzwi w KSI.'),
  async execute(interaction) {
    const cmd = spawn('python3', [process.env.DOOR_HOME + '/Kod/open_the_door.py']);
    cmd.stdout.on('data', data => {
      console.log(`stdout: ${data}`);
    });

    cmd.stderr.on('data', data => {
      console.log(`stderr: ${data}`);
    });

    cmd.on('error', error => {
      console.log(`error: ${error.message}`);
    });

    cmd.on('close', code => {
      console.log(`child process exited with code ${code}`);
    });
    await interaction.reply({ content: 'Drzwi otwarte!', ephemeral: false });
  }
};