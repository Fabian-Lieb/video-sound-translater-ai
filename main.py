"""
main
"""
from download import download_audio
from translator import main_translator

def main():
    """ run main for download,
    converter and translation
    """
    path = download_audio("https://www.youtube.com/watch?v=ORMx45xqWkA")
    result_text = main_translator(path)
    print(result_text)


if __name__ == "__main__":
    main()