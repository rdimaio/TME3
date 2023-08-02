import sys
from .json_graph_extractor import JsonGraphExtractor

def main():
    correct_usage = "python -m json_graph_extractor [relative_path_to_file]"

    if len(sys.argv) != 2:
        print(f"Too many arguments. Correct usage:\n{correct_usage}")
        return

    json_filename = sys.argv[1]

    try:
        jge = JsonGraphExtractor(json_filename)
    except FileNotFoundError:
        print(f"Error: file {json_filename} not found")
        return
    except OSError:
        print(f"Error while accessing file {json_filename}")
        return

    print(jge.dict_to_graph())
    return

if __name__ == '__main__':
    main()