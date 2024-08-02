![instagram dm bot](https://github.com/user-attachments/assets/6166fdd6-36df-4bf2-a882-de680af84e66)
# Instagram DM Bot 🤖📩

Welcome to the **Instagram DM Bot**! This script automatically sends a Direct Message (DM) to users who comment a specific keyword on a specified Instagram video post. Using the `instagrapi` library, it interacts with Instagram and the `python-dotenv` library to manage environment variables securely.

## ✨ Features

- **Login**: Securely logs into your Instagram account.
- **Monitor Comments**: Tracks comments on a specific Instagram video URL.
- **Keyword Detection**: Triggers action when a comment contains a specific keyword.
- **Send DM**: Sends a predefined message directly to the user who commented.

## 🗂️ Files

- **`main.py`**: The main script that executes the bot.
- **`requirements.txt`**: Lists the dependencies required to run the bot.
- **`config.env.example`**: Example configuration file for environment variables.

## 🚀 Setup Instructions

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/Dexiikk/instagram-dm-bot.git
   ```

2. **Install Dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**:
   - Copy the `config.env.example` file to `.env`:
     ```sh
     cp config.env.example .env
     ```
   - Edit the `.env` file to include your Instagram credentials, video URL, keyword, and message.

4. **Run the Bot**:
   ```sh
   python main.py
   ```

## ⚠️ Important Notes

- **Security**: Keep your `.env` file private as it contains sensitive information. 🔒
- **Instagram Policy**: Follow Instagram's guidelines to avoid account suspension due to automation. 🚫
- **Customization**: Modify the keyword and message in the `.env` file as needed. ✍️

## 📧 Contact

For any questions or issues, feel free to open an issue in the repository or reach out to us.

Happy automating! 🚀
