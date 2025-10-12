from tools.mergesort import MergeSort
import os


def merge_files(file1, file2, filename):
    with open(file1, "r") as file1, open(file2, "r") as file2, open(filename, "w") as output_file:
        line_file1 = file1.readline()
        line_file2 = file2.readline()
        lines = []

        while line_file1 != "" and line_file2 != "":
            if line_file1 < line_file2:
                lines.append(line_file1)
                line_file1 = file1.readline()
            else:
                lines.append(line_file2)
                line_file2 = file2.readline()

        while line_file1 != "":
            lines.append(line_file1)
            line_file1 = file1.readline()
        
        while line_file2 != "":
            lines.append(line_file2)
            line_file2 = file2.readline()
        
        for i in range(len(lines)-1):
            if "\n" in lines[i]:
                output_file.write(lines[i])
            else:
                output_file.write(lines[i] + "\n")

        if "\n" in lines[-1]:
            output_file.write(lines[-1][:-1])
        else:
            output_file.write(lines[-1])
        del lines


def func(chunks=2):
    chunk_files = []
    number_chunk = 0

    with open("test.txt", "r") as file:
        while True:
            lines = []
            for _ in range(chunks):
                line = file.readline()
                if "\n" in line:
                    line = line[:-1]
                if line == "":
                    break
                lines.append(line)

            if not lines:
                break
            lines = MergeSort.merge(lines)
            filename = f"task17_hw1_temp_files/chunk_{number_chunk}.txt"

            with open(filename, "w") as chunk_file:
                for i in range(len(lines)-1):
                    chunk_file.write(lines[i] + "\n")
                chunk_file.write(lines[-1])
            
            chunk_files.append(filename)
            number_chunk += 1

    count_new_files = 0
    while len(chunk_files) > 1:

        new_chunk_files = []
        

        for i in range(0, len(chunk_files), 2):
            if i + 1 < len(chunk_files):
                print(count_new_files)
                filename = f"task17_hw1_temp_files/new_file{count_new_files}.txt"
                print(filename)
                merge_files(chunk_files[i], chunk_files[i+1], filename)
                new_chunk_files.append(filename)
                count_new_files += 1

            else:
                new_chunk_files.append(chunk_files[i])

        chunk_files = new_chunk_files

    if chunk_files and os.path.exists(chunk_files[0]):
        if os.path.exists("result.txt"):
            os.remove("result.txt")
        os.rename(chunk_files[0], "result.txt")
            

func()

