import { spawnSync } from 'child_process';
import { AttachmentBuilder, PermissionFlagsBits, SlashCommandBuilder } from 'discord.js';

export default {
  cooldown: 6,
  data: new SlashCommandBuilder()
    .setName('getregisteredcards')
    .setDescription('Pobiera listę zarejestrowanych kart.')
    .setDefaultMemberPermissions(PermissionFlagsBits.BanMembers),
  async execute(interaction) {
    await interaction.deferReply('Sprawdzam...');
    const child = spawnSync(process.env.DOOR_HOME + 'Skrypty/get-registered-cards.sh', [], {
      cwd: process.env.DOOR_HOME,
      stdio: 'pipe',
      encoding: 'utf-8'
    });
    console.log(child.output);
    //console.log(child.stdio);
    let atc = new AttachmentBuilder(Buffer.from(child.output[1]), { name: 'cards.txt' });
    interaction.editReply({ files: [atc] });
    //interaction.editReply(child.output[1]);
    //await new Promise( (resolve) => {
    //    await child.on('close', resolve);
    //}).then(await interaction.reply(child.stdout));
    //child.stdout.setEncoding('utf8');
    //child.stdout.on('data', function(data) {
    //Here is where the output goes
    //	console.log('stdout: ' + data);
    //await interaction.reply('Pobieram listę kart...');
    //});
  }
};
