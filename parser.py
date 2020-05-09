from pytube import YouTube
import csv


def csv_dict_reader(file_obj):
    """
    Read a CSV file using csv.DictReader
    """
    reader = csv.DictReader(file_obj, delimiter=';')
    for line in reader:
        print(line["url"])
        print(line["file_name"])
        YouTube(line["url"]).streams.first().download(f'download_videos/{line["file_name"]}')


if __name__ == "__main__":
    with open("videos_for_parsing.csv", "r", encoding='utf-8') as f_obj:
        csv_dict_reader(f_obj)
