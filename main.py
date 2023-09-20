from decouple import config
from azure_recognizer import AzureRecognizer

def main():
    KEY = config("KEY")
    ENDPOINT = config("ENDPOINT")
    PATH_PDF = config("PATH_PDF")
    azure_recognizer = AzureRecognizer(KEY, ENDPOINT)
    content: str = azure_recognizer.process_file_content(PATH_PDF)
    print(content)

if __name__ == "__main__":
    main()
