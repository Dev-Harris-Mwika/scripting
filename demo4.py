camelot_lines = []
with open(r"C:\Users\Seal\udacity\python\scripting\camelot.txt", "r")  as f:
    for line in f:
        camelot_lines.append(line.strip())
print(camelot_lines)