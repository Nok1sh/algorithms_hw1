from tools.mergesort import MergeSort
from test_alg import universal_test_system
import os
import shutil
from test_for_all_tasks import task17

def merge_files(file1, file2, filename):
    with open(file1, "r") as f1, open(file2, "r") as f2, open(filename, "w") as output:
        line1 = f1.readline()
        line2 = f2.readline()
        
        line1_clean = line1[:-1] if "\n" in line1 else line1
        line2_clean = line2[:-1] if "\n" in line2 else line2
        
        first_line = True
        
        while line1 != "" and line2 != "":
            if line1_clean < line2_clean:
                if not first_line:
                    output.write("\n")
                output.write(line1_clean)
                line1 = f1.readline()
                line1_clean = line1[:-1] if "\n" in line1 else line1
            else:
                if not first_line:
                    output.write("\n")
                output.write(line2_clean)
                line2 = f2.readline()
                line2_clean = line2[:-1] if "\n" in line2 else line2
            
            first_line = False

        while line1 != "":
            if not first_line:
                output.write("\n")
            output.write(line1_clean)
            line1 = f1.readline()
            line1_clean = line1[:-1] if "\n" in line1 else line1
            first_line = False

        while line2 != "":
            if not first_line:
                output.write("\n")
            output.write(line2_clean)
            line2 = f2.readline()
            line2_clean = line2[:-1] if "\n" in line2 else line2
            first_line = False


def func(filename, chunks=100):
    global ind
    chunk_files = []
    number_chunk = 0

    with open(f"{filename}", "r") as file:
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
            filename = f"tests_task17/task17_hw1_temp_files/chunk_{number_chunk}.txt"

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
                filename = f"tests_task17/task17_hw1_temp_files/new_file{count_new_files}.txt"
                merge_files(chunk_files[i], chunk_files[i+1], filename)
                new_chunk_files.append(filename)
                count_new_files += 1

            else:
                new_chunk_files.append(chunk_files[i])

        chunk_files = new_chunk_files

    if chunk_files and os.path.exists(chunk_files[0]):
        
        if os.path.exists(f"tests_task17/results/result{ind}.txt"):
            os.remove(f"tests_task17/results/result{ind}.txt")   
        os.rename(chunk_files[0], f"tests_task17/results/result{ind}.txt")
        ind = ind % count_files
        ind += 1
            

name, solutions, test_cases, ind, count_files = task17()

solutions[name] = func

universal_test_system(solutions, test_cases)

shutil.rmtree("tests_task17/task17_hw1_temp_files") 
os.makedirs("tests_task17/task17_hw1_temp_files")



