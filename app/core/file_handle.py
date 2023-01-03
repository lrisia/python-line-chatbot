import datetime
import json
import os

class FileHandle:
    """
    """

    DEFAULT_LOG_FILENANE = 'log'
    DEFAULT_ERROR_FILENANE = 'error'
    DEFAULT_LOG_PATH = 'src/logs'
    DEFAULT_ERROR_PATH = 'src/errors'
    DEFAULT_FILE_EXTENSION = 'csv'
    DEFAULT_RECORD_LIMIT = 1000

    def __init__(self, 
        log_path: str=DEFAULT_LOG_PATH,
        error_path: str=DEFAULT_ERROR_PATH,
        log_filename: str=DEFAULT_LOG_FILENANE,
        error_filename: str=DEFAULT_ERROR_FILENANE,
        record_limit: int=DEFAULT_RECORD_LIMIT,
    ) -> None:
        """
        """

        self.log_filename = log_filename + '.' + self.DEFAULT_FILE_EXTENSION
        self.error_filename = error_filename + '.' + self.DEFAULT_FILE_EXTENSION
        self.log_path = log_path
        self.error_path = error_path
        self.record_limit = record_limit

    def __path_check(self, path: str, auto_create: bool=True, type: str="file") -> None:
        isExist = os.path.exists(path)
        if auto_create == False:
            if not isExist: raise FileNotFoundError("File or directory does't exist.")

        try:
            if type == "directory" and not isExist: 
                self.__create_directory(path)
            elif type == "file" and not isExist:
                self.__create_file(path)
        except FileNotFoundError as e:
            raise e

    def __create_directory(self, path: str) -> None:
        if path == "": raise FileNotFoundError("Path cound't be empty.")
        os.mkdir(path)

    def __create_file(self, path: str) -> None:
        if path == "": raise FileNotFoundError("Path cound't be empty.")
        with open(path, 'x') as f:
            f.close()

    def __clean_text(self, text: str) -> str:
        if '\r' in text: text = text.replace('\r', ' ')
        if '\n' in text: text = text.replace('\n', ' ')
        if '  ' in text: text = text.replace('  ', ' ')
        return text

    def __write_file(self, path: str, filename: str, content: str) -> None:
        self.__path_check(path, type="directory")
        __file_count = len([entry for entry in os.listdir(path) if os.path.isfile(os.path.join(path, entry))])
        __filename = filename
        __name, __extension = filename.split('.')
        if __file_count == 0: __filename = f"{__name}{__file_count+1}.{__extension}"
        else: __filename = f"{__name}{__file_count}.{__extension}"
        __path = os.path.join(path, __filename)
        self.__path_check(__path, type="file")

        try:
            __f = open(__path, 'r', encoding='utf-8')
            __last_line =  [i.strip() for i in __f.readlines()][-1]
            __f.close()
            __number = int(__last_line.split(',')[0]) + 1
        except IndexError:
            __number = 1

        if int(__number) == self.record_limit:
            __filename = f"{__name}{__file_count+1}.{__extension}"
            __new_path = os.path.join(path, __filename)
            self.__path_check(__new_path, type="file")

        date = datetime.datetime.now()
        with open(__path, 'a', encoding='utf-8') as f:
            f.write(f'{__number},{date.strftime("%d/%m/%Y:%H:%M:%S")},{content}\n')
            f.close()

    def write_log(self, **logs) -> None:
        result = ""
        for key, value in logs.items():
            result += f"{self.__clean_text(str(value))},"
        result = result[:-1]
        self.__write_file(self.log_path, self.log_filename, result)

    def write_error(self, **errors) -> None:
        result = ""
        for key, value in errors.items():
            result += f"{self.__clean_text(str(value))},"
        result = result[:-1]
        self.__write_file(self.error_path, self.error_filename, result)

    def read_file(self, path: str, extension: str) -> str:
        if not path.endswith(f".{extension}"): path += f".{extension}"
        self.__path_check(path, auto_create=False)
    
        content = ""
        if extension == "json":
            with open(path, 'r', encoding="utf-8") as f:
                content = json.load(f)
                f.close()
        elif extension == "txt":
            with open(path, 'r', encoding='utf-8') as f:
                content = '\n'.join([i.strip() for i in f.readlines()])
                f.close()
        
        return content
