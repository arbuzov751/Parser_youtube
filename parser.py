from pytube import YouTube
import csv
import glob


def csv_dict_reader(file_obj):
    """
    Read a CSV file using csv.DictReader
    """
    reader = csv.DictReader(file_obj, delimiter=';')
    for line in reader:
        print(line["url"])
        print(line["directory_name"])
        direct = line["directory_name"]
        files_in_direct = glob.glob(f"{direct}\*.*")
        try:
            yt = YouTube(line["url"]).streams.first()
            file_name = yt.title
            ext = yt.mime_type.split('/')[1]

            file_name = file_name.replace(".", "")
            file_name = file_name.replace(":", "")

            file_name = direct + "\\" + file_name + "." + ext
            if file_name not in files_in_direct:
                yt.download(f'{line["directory_name"]}')
        except:
            pass
            # Нужно ли делать перезапись файла, чтоб пользователь увидел ошибку?
            # line["directory_name"] = "Невозможно скачать файл!"


if __name__ == "__main__":
    with open("videos_for_parsing.csv", "r+", encoding='utf-8') as f_obj:
        csv_dict_reader(f_obj)
