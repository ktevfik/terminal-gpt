# Path to your virtual environment
VENV := openai-env/bin/activate

# Command to activate the virtual environment and run Python script
run:
	/bin/zsh -c "source $(VENV) && python main.py"

# Install dependencies in the virtual environment
install:
	/bin/zsh -c "source $(VENV) && pip install -r requirements.txt"

# Deactivate the virtual environment
deactivate:
	/bin/zsh -c "deactivate"

# Clean up virtual environment and cached files
clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	rm -rf openai-env
