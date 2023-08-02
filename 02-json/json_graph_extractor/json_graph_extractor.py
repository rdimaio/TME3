import json

class JsonGraphExtractor:
    def __init__(self, json_filename: str):
        """
        Class constructor for JsonGraphExtractor

        Parameters:
            json_filename: str
                String representing the filename of the JSON file to extract the graph from
        """

        self.json_filename = json_filename
        self.json_dict = self.json_to_dict()

    def json_to_dict(self) -> dict:
        """
        Convert data from a JSON file to a dict

        Returns:
            dict
                Dict representing the JSON data
        """
        with open(self.json_filename) as json_file:
            return json.load(json_file)

    def _get_key_and_values(self, key: str, indentation_level: int) -> str:
        """
        Return the string of a key, and recursively of all its values and their values

        Parameters:
            key: str
                Key to access the dictionary with
            indentation_level: int
                Indentation level of the current key
        
        Returns:
            str
                String composed of the key, and recursively of all its values and their values
        """
        out_str = " " * indentation_level + f"- {key}\n"
        if key in self.json_dict:
            for value in self.json_dict[key]:
                out_str += self._get_key_and_values(value, indentation_level+1)
        return out_str

    def dict_to_graph(self) -> str:
        """
        Return the JSON data as a string representing a graph.

        Returns:
            str
                String representing the dict as a graph.
        """
        out_str = ""
        for key, value_list in self.json_dict.items():
            out_str += self._get_key_and_values(key, 0)
        return out_str