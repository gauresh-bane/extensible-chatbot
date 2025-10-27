# Extensible Chatbot

A modular and extensible chatbot framework built with Python, designed for easy customization and integration of various AI models and features.

## Features

- **Modular Architecture**: Easy to extend with new features and capabilities
- **Multiple AI Model Support**: Integration with various language models
- **Flexible Configuration**: Customize behavior through configuration files
- **Plugin System**: Add new functionalities through plugins
- **RESTful API**: Easy integration with web applications
- **Database Support**: Persistent conversation storage
- **Authentication**: Secure user authentication and authorization
- **Logging**: Comprehensive logging for debugging and monitoring

## Installation

```bash
# Clone the repository
git clone https://github.com/gauresh-bane/extensible-chatbot.git

# Navigate to the project directory
cd extensible-chatbot

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Basic Usage

```python
from chatbot import Chatbot

# Initialize the chatbot
bot = Chatbot()

# Start a conversation
response = bot.chat("Hello, how are you?")
print(response)
```

### Advanced Configuration

```python
from chatbot import Chatbot
from chatbot.models import GPTModel

# Initialize with custom configuration
bot = Chatbot(
    model=GPTModel(),
    config_path="config/custom_config.yaml"
)

# Use with context
response = bot.chat(
    message="What's the weather like?",
    context={"location": "New York"}
)
```

## Configuration

Create a `config.yaml` file to customize the chatbot behavior:

```yaml
model:
  name: "gpt-3.5-turbo"
  temperature: 0.7
  max_tokens: 150

database:
  type: "sqlite"
  path: "data/conversations.db"

logging:
  level: "INFO"
  file: "logs/chatbot.log"
```

## API Endpoints

### POST /chat
Send a message to the chatbot

```json
{
  "message": "Hello!",
  "user_id": "user123",
  "context": {}
}
```

### GET /conversations/:user_id
Retrieve conversation history for a user

### DELETE /conversations/:conversation_id
Delete a specific conversation

## Development

### Running Tests

```bash
pytest tests/
```

### Code Style

```bash
# Format code
black .

# Check linting
flake8 .
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to all contributors
- Inspired by various chatbot frameworks
- Built with ❤️ by the community

## Contact

For questions or support, please open an issue on GitHub.
