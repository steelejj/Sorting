COMMAND=$1

if [ "$COMMAND" = "--interactive" ]; then
    docker run -it --rm -v "$(pwd)/app:/app" sorting /bin/bash
elif [ "$COMMAND" = "--test" ]; then
    docker run --rm -v $(pwd):/app -w /app sorting pytest tests/
else
    echo "Invalid command. Use '--interactive' or '--test'."
fi

