import os
from dotenv import load_dotenv
from google import genai
import sys
import warnings
from google.genai import types
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_python import schema_run_python_file
from functions.write_file import schema_write_file
from functions.call_function import call_function
from dataclasses import dataclass
from typing import List

# Suppress the specific warning about non-text parts in response
warnings.filterwarnings("ignore", message=".*there are non-text parts in the response.*")

@dataclass
class ConversationConfig:
    """Configuration object for conversation settings."""
    client: genai.Client
    system_prompt: str
    available_functions: types.Tool
    user_prompt: str
    verbose_mode: bool

@dataclass
class ConversationState:
    """State object for conversation data."""
    messages: List[types.Content]
    max_iterations: int = 20

def setup_environment():
    """Initialize environment variables and API client."""
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable not found")
    return genai.Client(api_key=api_key)

def get_system_prompt():
    """Return the system prompt for the AI agent."""
    return """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

def get_available_functions():
    """Return the available function declarations."""
    return types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_run_python_file,
            schema_write_file,
        ]
    )

def parse_command_line_args():
    """Parse and validate command line arguments."""
    try:   
        user_prompt = sys.argv[1]
    except IndexError:
        print('No prompt provided')
        sys.exit(1)
    
    verbose_mode = len(sys.argv) > 2 and sys.argv[2] == '--verbose'
    return user_prompt, verbose_mode

def create_initial_messages(user_prompt):
    """Create the initial message list with user prompt."""
    return [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

def generate_ai_response(config: ConversationConfig, messages: List[types.Content]):
    """Generate a response from the AI model."""
    # Suppress warnings for this specific call
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        return config.client.models.generate_content(
            model='gemini-2.0-flash-001', 
            contents=messages, 
            config=types.GenerateContentConfig(
                system_instruction=config.system_prompt,
                tools=[config.available_functions], 
            )
        )

def process_candidates(response, messages):
    """Process AI response candidates and add to message history."""
    if response.candidates:
        for candidate in response.candidates:
            messages.append(candidate.content)

def process_function_calls(response, config: ConversationConfig, messages: List[types.Content]):
    """Process function calls from the AI response."""
    if not response.function_calls:
        return
    
    for function_call_part in response.function_calls:
        function_result = call_function(function_call_part)
        messages.append(function_result)

        if function_result.parts and function_result.parts[0].function_response.response:
            if config.verbose_mode:
                print(f'User prompt: {config.user_prompt}')
                print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
                print(f'Response tokens: {response.usage_metadata.candidates_token_count}')
        else:
            raise Exception(f"FATAL ____ Error: {function_result.parts[0].function_response}")

def should_continue_conversation(response):
    """Determine if the conversation should continue or end."""
    has_function_calls = response.function_calls is not None and len(response.function_calls) > 0
    return not (response.text and not has_function_calls)

def print_final_response(response):
    """Print the final text response from the AI."""
    if response.text:
        print(response.text)

def run_conversation_loop(config: ConversationConfig, state: ConversationState):
    """Run the main conversation loop with the AI."""
    for iteration in range(state.max_iterations):
        try:
            response = generate_ai_response(config, state.messages)
            
            process_candidates(response, state.messages)
            process_function_calls(response, config, state.messages)
            
            if not should_continue_conversation(response):
                print_final_response(response)
                break
                
        except Exception as e:
            print(f"Try-Except block caught an error: {e}")
            continue

def main():
    """Main function orchestrating the AI coding agent."""
    # Setup
    client = setup_environment()
    system_prompt = get_system_prompt()
    available_functions = get_available_functions()
    
    # Parse arguments
    user_prompt, verbose_mode = parse_command_line_args()
    
    # Create configuration and state objects
    config = ConversationConfig(
        client=client,
        system_prompt=system_prompt,
        available_functions=available_functions,
        user_prompt=user_prompt,
        verbose_mode=verbose_mode
    )
    
    state = ConversationState(
        messages=create_initial_messages(user_prompt)
    )
    
    # Run conversation loop
    run_conversation_loop(config, state)

if __name__ == "__main__":
    main()




