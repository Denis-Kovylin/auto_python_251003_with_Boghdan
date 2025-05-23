import csv


def remove_duplicates_csv(file1_path, file2_path, output_path):
    """Об'єднує два CSV-файли, видаляє дублікати рядків та записує результат у новий файл.
        """
    with open(file1_path, "r", encoding="utf-8") as f1:
        reader1 = csv.reader(f1)
        rows1 = list(reader1)

    with open(file2_path, "r", encoding="utf-8") as f2:
        reader2 = csv.reader(f2)
        rows2 = list(reader2)

    header = rows1[0]
    all_rows = rows1[1:] + rows2[1:]
    uniq_rows = list(set(tuple(row) for row in all_rows))

    with open(output_path, "w", newline="", encoding="utf-8") as f_out:
        writer = csv.writer(f_out)
        writer.writerow(header)
        writer.writerows(uniq_rows)

# UPD
