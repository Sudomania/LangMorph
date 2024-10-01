# LangMorph

LangMorph is a Discord bot designed to facilitate language translation within Discord channels. Users can set their preferred languages and automatically translate messages sent in other languages to their preferred language.

## Features

- **Language Preference**: Users can set their preferred language using a simple command.
- **Automatic Translation**: Messages sent in a different language will be automatically translated to the user's preferred language.
- **Multi-language Support**: The bot uses Google Translate to support a wide range of languages.

## Installation

### Prerequisites

- Python 3.6 or higher
- A Discord bot token
- The following Python packages:
  - `discord.py`
  - `python-dotenv`
  - `googletrans==4.0.0-rc1`
  - `langdetect`

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/Sudomania/LangMorph.git
   cd LangMorph
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory of the project and add your Discord bot token:
   ```bash
   DISCORD_TOKEN=your_bot_token_here
   ```

4. Start the bot:
   ```bash
   python bot.py
   ```

## Usage

- **Set Language**: Users can set their language preference using the command:
  ```
  !setlang <language_code>
  ```
  Example:
  ```
  !setlang es
  ```
  This command sets the user's preferred language to Spanish.

- **Automatic Translation**: After setting the preferred language, any messages sent in a different language will be translated automatically.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [discord.py](https://discordpy.readthedocs.io/en/stable/)
- [Google Translate API](https://cloud.google.com/translate)
- [langdetect](https://github.com/Mojmirs/language-detection)
