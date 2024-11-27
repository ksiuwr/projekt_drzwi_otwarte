import { spawn } from 'child_process';
import { PermissionFlagsBits, SlashCommandBuilder } from 'discord.js';

export default {
  cooldown: 6,
  data: new SlashCommandBuilder()
    .setName('adddooruser')
    .setDescription('Dodaje nowego użytkownika do zamka w KSI.')
    .setDefaultMemberPermissions(PermissionFlagsBits.BanMembers)
    .addStringOption(option =>
      option.setName('name').setDescription('Imię').setRequired(true).setMaxLength(50)
    )
    .addStringOption(option =>
      option.setName('surname').setDescription('Nazwisko').setRequired(true).setMaxLength(50)
    ),
  async execute(interaction) {
    const name = interaction.options.getString('name').replace(/\W/g, '');
    const surname = interaction.options.getString('surname').replace(/\W/g, '');
    const child = spawn('python3', [process.env.DOOR_HOME + 'Kod/adder.py', name, surname], {
      cwd: process.env.DOOR_HOME,
      stdio: 'inherit'
    });
    //child.stdout.setEncoding('utf8');
    //child.stdout.on('data', function(data) {
    //Here is where the output goes
    //	console.log('stdout: ' + data);
    await interaction.reply('Dodawanie nowego użytkownika...');
    //});
  }
};
