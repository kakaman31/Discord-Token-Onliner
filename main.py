const fs = require('fs');

const Discord = require('discord.js');

const tokens = fs.readFileSync('tokens.txt', 'utf-8').replace(/\r|\x22/gi, '').split('\n');

const items = ['Minecraft', 'Valorant', 'CS:GO', 'Among Us', 'Rocket League', 'TikTok', 'YouTube', 'Visual Code Studio', 'GitHub', 'TurkHackTeam.org', 'Apex Legends', 'Pubg Mobile', 'Pubg Mobile Lite', 'Pubg Mobile Korean', 'Fire Fire', 'Minecraft', 'Minecraft Java', 'Minecraft PE', 'THT: raunchytve', '7/24 Online', 'Google'];


class Bot {

  constructor(token, items) {

    this.token = token;

    this.items = items;

    this.client = new Discord.Client({ disableEveryone: true });

  }

  start() {

    this.client.on('ready', () => {

      console.log(`[${this.client.user.tag}] Başarılı bir şekilde giriş yapıldı. `);

      this.updateActivity();

    });

    this.client.login(this.token)

      .catch(error => console.error(`[${this.client.user.tag}] Giriş yaparken bir hata oluştu: ${error.message}`));

  }

  updateActivity() {

    setInterval(() => {

      const activity = this.items[Math.floor(Math.random() * this.items.length)];

      this.client.user.setActivity(activity, { type: 'PLAYING' });

    }, 300000); // Her 5 dakikada bir aktivite güncellenir.

  }

}

process.title = `Raunchy Onliner! [Birden fazla hesap] Toplam hesap sayısı: ${tokens.length}`;

console.log('Raunchy Onliner!n/[Birden fazla hesap]');

console.log(`Toplam hesap sayısı: ${tokens.length}`);

tokens.forEach((token, index) => {

  const bot = new Bot(token, []);

  bot.start();

});

