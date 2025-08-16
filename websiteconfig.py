
# Website Configuration
class WebsiteConfig:
    # Bot Information
    PROJECT_NAME = "Rabbit"
    DESCRIPTION = "A powerful Discord bot with moderation, tickets, and AI features."
    BOT_LOGO = "https://images-ext-1.discordapp.net/external/dtLGVUIYHH5_n6W96XRxVc1JNURxyAmQzxta6zVk1dI/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1346766976038731826/29d42641ac2416fc989a79f03a269345.png?format=webp&quality=lossless&width=411&height=411"
    
    # Server Information
    DOMAIN = "your-bot-domain.com"
    IP_ADDRESS = "0.0.0.0"
    PORT = 3000
    
    # Discord Links
    BOT_INVITE_URL = "https://discordapp.com/oauth2/authorize?client_id=1379011148434899026&scope=bot%20applications.commands&permissions=268561646"
    SUPPORT_SERVER_URL = "https://discord.gg/sifarish"
    TOPGG_VOTE_URL = "https://top.gg/bot/1379011148434899026/vote"
    
    # Owner Information
    OWNER = {
        'username': 'majestic.ego',
        'display_name': '!!    Majestic',
        'user_id': '1374976078556303453',
        'avatar': 'https://cdn.discordapp.com/avatars/1374976078556303453/90963b1929f2ac49875ec3259e9fc6cb.png?size=1024'
    }
    
    # Discord Webhook for Contact Form
    CONTACT_WEBHOOK_URL = "https://discord.com/api/webhooks/1405892605274751018/gb3CcBmknoQl7pUKwMzFlhjTRLQWQy7FYdJbkOPt7JlOPbQZsfqa06qhnH0Rehh7eFLb"
    
    # Commands Configuration
    PREFIX_COMMANDS = {
        'Automod Commands': ['automod', 'automod anti message spam enable/disable', 'automod anti mention spam enable/disable', 'automod anti toxicity enable/disable', 'automod config', 'automod reset', 'modlog', 'antinuke'],
        'Moderation Commands': ['timeout <user>', 'untimeout <user>', 'clear bots', 'clear humans', 'clear embeds', 'clear files', 'clear mentions', 'clear pins', 'ban <user>', 'unban <user>', 'kick <user>', 'hide <channel>', 'unhide <channel>', 'lock <channel>', 'unlock <channel>', 'nuke', 'purge', 'voice', 'voice muteall', 'voice unmuteall', 'voice deafenall', 'voice undeafenall', 'voice mute <user>', 'voice unmute <user>', 'voice deafen <user>', 'voice undeafen <user>'],
        'Giveaway Commands': ['gcreate', 'reroll', 'end'],
        'Utility Commands': ['help', 'invite', 'ping', 'prefix', 'support', 'uptime', 'userinfo', 'serverinfo', 'avatar user', 'botinfo', 'afk', 'report', 'roles', 'vote', 'reactionrole', 'autoreact'],
        'Sticky Message Commands': ['stickyadd', 'stickyremove'],
        'Vanity Commands': ['vanity set', 'vanity remove', 'vanity list']
    }
    
    SLASH_COMMANDS = {
        'Welcome Commands': ['/welcome setup', '/welcome variable', '/welcome test'],
        'Ticket Commands': ['/ticket-panel', '/ticket close'],
        'AI Commands': ['/imagine', '/ask'],
    }
