#!/usr/bin/python3

if __name__ == "__main__":
    import importlib.util

    # Load the compiled module hidden_4.pyc
    spec = importlib.util.spec_from_file_location("hidden_4", "hidden_4.pyc")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Get all names defined in the module
    names = dir(module)

    # Filter out names that start with "__"
    filtered_names = [name for name in names if not name.startswith("__")]

    # Print the filtered names in alphabetical order
    for name in sorted(filtered_names):
        print(name)

