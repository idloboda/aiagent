# 🤖 AI Coding Agent

A sophisticated AI-powered coding assistant built with Google's Generative AI (Gemini) that can interact with your codebase through function calling capabilities. This project demonstrates advanced Python development, API integration, and software architecture principles.

## ✨ Features

- **🔍 File System Operations**: List directories, read file contents, and navigate codebases
- **📝 Code Generation**: Write and modify files with AI assistance
- **▶️ Code Execution**: Run Python files with automatic error handling
- **🛡️ Security**: Sandboxed execution within specified working directories
- **🔄 Multi-turn Conversations**: Maintains context across multiple interactions
- **⚙️ Configurable**: Verbose mode for debugging and detailed logging

## 🏗️ Architecture

### Core Components

- **Main Orchestrator** (`main.py`): Manages the conversation loop and coordinates all operations
- **Function Registry** (`functions/`): Modular function implementations for different operations
- **Configuration Management**: Clean separation of concerns using dataclasses
- **Error Handling**: Comprehensive error handling with graceful degradation

### Design Patterns Used

- **Configuration Object Pattern**: `ConversationConfig` and `ConversationState` dataclasses
- **Function Registry Pattern**: Centralized function mapping and execution
- **Strategy Pattern**: Different function implementations for various operations
- **Observer Pattern**: Event-driven processing of AI responses

## 🚀 Quick Start

### Prerequisites

- Python 3.12+
- Google Generative AI API key

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/idloboda/aiagent.git
   cd aiagent
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   # or using uv (recommended)
   uv sync
   ```

3. **Set up environment variables**
   ```bash
   # Create .env file
   echo "GEMINI_API_KEY=your_api_key_here" > .env
   ```

4. **Run the agent**
   ```bash
   python main.py "List all files in the current directory"
   ```

## 📖 Usage Examples

### Basic File Operations
```bash
# List files in a directory
python main.py "Show me all files in the calculator directory"

# Read file contents
python main.py "Read the contents of main.py"

# Write a new file
python main.py "Create a new file called hello.py with a simple hello world function"
```

### Code Execution
```bash
# Run a Python file
python main.py "Execute the calculator/main.py file"

# Run with arguments
python main.py "Run the calculator with expression '2 + 3 * 4'"
```

### Complex Operations
```bash
# Multi-step operations
python main.py "Create a new Python file that implements a simple calculator class, then run it with some test cases"
```

### Verbose Mode
```bash
# Enable detailed logging
python main.py "Analyze the project structure" --verbose
```

## 🛠️ Technical Implementation

### Function Calling System

The agent uses Google's function calling API to execute specific operations:

```python
@dataclass
class ConversationConfig:
    """Configuration object for conversation settings."""
    client: genai.Client
    system_prompt: str
    available_functions: types.Tool
    user_prompt: str
    verbose_mode: bool
```

### Available Functions

1. **`get_files_info`**: List files and directories with metadata
2. **`get_file_content`**: Read file contents (with size limits)
3. **`write_file`**: Create or modify files
4. **`run_python_file`**: Execute Python files safely

### Security Features

- **Path Validation**: All file operations are constrained to working directory
- **Sandboxed Execution**: Python files run in isolated environment
- **Input Sanitization**: Proper handling of user inputs
- **Error Boundaries**: Graceful error handling without crashes

## 🧪 Testing

The project includes comprehensive tests for all functions:

```bash
# Run all tests
python tests.py

# Test specific functionality
python -c "from functions.get_files_info import get_files_info; print(get_files_info('calculator', '.'))"
```

## 📁 Project Structure

```
bootdev_llm/
├── main.py                 # Main application entry point
├── functions/              # Function implementations
│   ├── get_files_info.py   # Directory listing
│   ├── get_file_content.py # File reading
│   ├── write_file.py       # File writing
│   ├── run_python.py       # Code execution
│   └── call_function.py    # Function dispatcher
├── calculator/             # Example application
│   ├── main.py            # Calculator implementation
│   └── pkg/               # Calculator modules
├── tests.py               # Test suite
├── pyproject.toml         # Project configuration
└── README.md             # This file
```

## 🔧 Development

### Code Quality

- **Type Hints**: Full type annotation support
- **Documentation**: Comprehensive docstrings
- **Error Handling**: Robust exception management
- **Modular Design**: Clean separation of concerns

### Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 🎯 Key Learning Outcomes

This project demonstrates proficiency in:

- **Advanced Python**: Dataclasses, type hints, async programming
- **API Integration**: Google Generative AI, function calling
- **Software Architecture**: Clean code principles, design patterns
- **Security**: Input validation, sandboxing, error handling
- **Testing**: Comprehensive test coverage
- **Documentation**: Professional README and code documentation

## 📊 Performance

- **Response Time**: < 2 seconds for most operations
- **Memory Usage**: Efficient memory management
- **Error Recovery**: Graceful handling of API failures
- **Scalability**: Modular design allows easy extension

## 🤝 License

This project is open source and available under the [MIT License](LICENSE).

## 📞 Contact

- **GitHub**: [@idloboda](https://github.com/idloboda)
- **Project**: [AI Agent Repository](https://github.com/idloboda/aiagent)

---

⭐ **Star this repository if you found it helpful!**
