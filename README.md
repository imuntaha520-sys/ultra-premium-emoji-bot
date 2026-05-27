# ⭐ ULTRA PREMIUM EMOJI BOT v2.0

> **Your Ultimate Premium Emoji Companion for Telegram**

A powerful, enterprise-grade Telegram bot that converts normal emojis to premium animated emojis, enabling all users to enjoy premium features without a Telegram Premium subscription!

## ✨ Features

### 🎨 Core Features
- **Smart Emoji Conversion** - Convert normal emojis → Premium animated emojis
- **Forward Messages** - Automatically convert forwarded messages
- **Inline Mode** - Use `@bot_username [text]` anywhere
- **Post Creator** - Create beautiful posts with optional media
- **Broadcast System** - Send messages to all users at once

### 🚀 Advanced Features
- ⚡ **Lightning-Fast Processing** - Optimized for speed
- 📊 **Advanced Analytics** - Track conversions and user activity
- 👑 **Complete Admin Panel** - Full bot control without leaving Telegram
- 🎯 **Rate Limiting** - Prevent abuse and protect bot resources
- 💾 **Smart Caching** - Faster responses with intelligent caching
- 🔐 **Security Features** - User verification and ban system
- 🎨 **Beautiful UI** - Colored buttons and premium animations
- 📱 **Mobile Optimized** - Perfect on mobile and desktop

### 🌟 Premium Emojis Available
- ❤️ Hearts & Love (15+ variations)
- 👍 Gestures & Actions
- 🔥 Premium Vibes (fire, stars, sparkles, etc.)
- ✅ Status & Alerts
- 😊 Faces & Emotions
- 🌸 Nature & Animals
- 🎮 Entertainment & Tech
- And many more!

## 🛠️ Technology Stack

- **Language**: Python 3.8+
- **Telegram**: Telethon
- **Database**: MongoDB + Motor (async)
- **Async**: AsyncIO
- **API**: Telegram Bot API

## 📋 Requirements

```bash
pip install telethon>=1.30.0
pip install motor>=3.0.0
pip install pymongo>=4.0.0
pip install python-dotenv>=0.19.0
```

## 🚀 Quick Start

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/ultra-premium-emoji-bot.git
cd ultra-premium-emoji-bot
```

### 2. Setup Environment

Run the interactive setup wizard:
```bash
python setup.py --setup
```

Or manually create `.env`:
```env
API_ID=your_api_id
API_HASH=your_api_hash
TOKEN=your_bot_token
OWNER_ID=your_user_id
MONGO_URI=your_mongodb_uri
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Bot
```bash
python ultra_premium_emoji_bot_v2.py
```

## 📖 Configuration

### Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `API_ID` | Telegram API ID | `33678714` |
| `API_HASH` | Telegram API Hash | `2da8051e6c5d07f62bef903f632d3eef` |
| `TOKEN` | Bot token from @BotFather | `123456789:ABCdef...` |
| `OWNER_ID` | Your Telegram user ID | `8591429820` |
| `MONGO_URI` | MongoDB connection string | `mongodb+srv://...` |

### Getting Credentials

1. **API_ID & API_HASH**: https://my.telegram.org/apps
2. **BOT_TOKEN**: Message @BotFather on Telegram
3. **OWNER_ID**: Message @userinfobot on Telegram
4. **MONGO_URI**: https://www.mongodb.com/cloud/atlas

## 💬 Commands

### User Commands
| Command | Description |
|---------|-------------|
| `/start` | Start the bot |
| `/help` | Show help menu |
| `/post` | Create a premium post |
| `/stats` | View your statistics |

### Admin Commands
| Command | Description |
|---------|-------------|
| `/admin` | Open admin panel |
| `/broadcast` | Send message to all users |
| `/stats` | View bot statistics |
| `/ban [id]` | Ban a user |
| `/unban [id]` | Unban a user |
| `/maintenance` | Toggle maintenance mode |

## 🎯 How to Use

### For Regular Users

1. **Convert Emojis**: Forward any message to the bot
2. **Create Posts**: Use `/post` command
3. **Inline Mode**: Type `@bot_username [your text]` in any chat
4. **Get Stats**: Use `/stats` to view your conversions

### For Admins

1. Open admin panel: `/admin`
2. Manage users, channels, and settings
3. Send broadcasts to all users
4. View detailed statistics

## 🗄️ Database Schema

### Collections

**users**
```json
{
  "user_id": 123456,
  "first_name": "John",
  "username": "johndoe",
  "joined": "2024-01-01",
  "messages_converted": 50,
  "posts_created": 5,
  "is_premium": false
}
```

**channels**
```json
{
  "chat_id": -1001234567,
  "title": "My Channel",
  "username": "mychannel",
  "added_by": 123456,
  "added_at": "2024-01-01"
}
```

**posts**
```json
{
  "user_id": 123456,
  "text": "Hello 👋",
  "media": true,
  "status": "published",
  "channels": 5,
  "created_at": "2024-01-01"
}
```

## 📊 Admin Panel Features

- **User Management**: View, ban, and manage users
- **Channel Management**: Add, remove, and manage channels
- **Broadcasting**: Send messages to all users
- **Statistics**: View detailed bot statistics
- **Settings**: Configure bot behavior
- **Analytics**: Track user activity and conversions

## 🔐 Security

- **Rate Limiting**: Prevents spam and abuse
- **User Banning**: Ban malicious users
- **Admin Verification**: Admin-only commands protected
- **Input Validation**: All inputs validated
- **Error Handling**: Graceful error handling
- **Logging**: Comprehensive activity logging

## ⚙️ Performance Optimization

- **Caching**: Settings and data cached in memory
- **Async Operations**: All I/O operations are async
- **Batch Processing**: Efficient batch operations
- **Connection Pooling**: MongoDB connection pooling
- **Rate Limiting**: Smart rate limiting

## 🚨 Troubleshooting

### Bot Won't Start
```bash
# Check Python version
python --version  # Should be 3.8+

# Check environment variables
echo $API_ID

# Verify dependencies
pip list | grep telethon
```

### MongoDB Connection Failed
```bash
# Check MongoDB URI format
# Should be: mongodb+srv://user:password@cluster.mongodb.net/db

# Test connection
mongo "your_connection_string"
```

### Emojis Not Converting
- Ensure emojis are in `PREMIUM_EMOJI_MAP`
- Check if bot has required permissions
- Verify Telegram account is not restricted

### Admin Commands Not Working
- Verify `OWNER_ID` is correct
- Check if user is added as admin
- Ensure user is not banned

## 📁 Project Structure

```
ultra-premium-emoji-bot/
├── ultra_premium_emoji_bot_v2.py    # Main bot file
├── utilities.py                      # Utilities and helpers
├── config.py                         # Configuration file
├── setup.py                          # Setup wizard
├── requirements.txt                  # Dependencies
├── .env                              # Environment variables
├── README.md                         # This file
└── bot.log                           # Bot logs
```

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 💬 Support

- **Issues**: Report bugs on [GitHub Issues](https://github.com/yourusername/ultra-premium-emoji-bot/issues)
- **Discussions**: Ask questions on [GitHub Discussions](https://github.com/yourusername/ultra-premium-emoji-bot/discussions)
- **Email**: your.email@example.com

## 🌟 Show Your Support

If you like this project, please give it a ⭐ on GitHub!

## 👨‍💻 Author

**Your Name** - [@yourhandle](https://t.me/yourhandle)

---

<div align="center">

**Made with ❤️ for the Telegram Community**

[⬆ Back to Top](#-ultra-premium-emoji-bot-v20)

</div>
