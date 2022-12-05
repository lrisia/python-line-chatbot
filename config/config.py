import json

class Config:
    """Handle config container file"""

    DEFAULT_FILE_PATH = ''
    DEFAULT_FILENANE = 'config'
    DEFAULT_FILE_EXTENSION = 'json'
    
    def __init__(self, key: str,
        path: str=DEFAULT_FILE_PATH,
        filename: str=DEFAULT_FILENANE, 
        extension: str=DEFAULT_FILE_EXTENSION
    ) -> None:
        """__init__ method
        
        Args:
            key: Key to config in file
            path: Path to config container file. Defaults to DEFAULT_FILENANE
            filename: Config container file name. Defaults to DEFAULT_FILE_PATH
            extension: Config contanier file extension. Defaults to DEFAULT_FILE_EXTENSION.
        """

        self.key = key
        self.filename = filename
        self.path = path
        self.extension = extension
        self.content = self.__read()

    def __read(self) -> dict:
        """Read config in file and return in dict

        Returns:
            dict: Content in config file
        """

        file_path = f'{self.path}{self.filename}.{self.extension}'
        content = dict()

        if self.extension == "json":
            with open(file_path, encoding='utf8') as f:
                content = json.load(f)
                f.close
        return content[self.key]

    def get(self, *key: str) -> any:
        """Get value from config file
        
        Args:
            *key: Key to access value in dict, can be multivalue

        Returns:
            any: Value in config file
        """

        content = self.content

        for i in key:
            content = content[i]
        return content

    def get_all(self) -> dict:
        """Get all value in config file in dict format
        
        Returns:
            dict: All content in config file
        """

        return self.content
