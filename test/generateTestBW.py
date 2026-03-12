
#!/usr/bin/env python3
# This line specifies the interpreter to be used for executing the script (python3 in this case)
# need to install pip install pyBigWig
import pyBigWig

# 1. Create the file
bw = pyBigWig.open("test.bw", "w")

# 2. Add Header (Chromosomes and their total lengths)
# Note: chr18 is now correctly sized
bw.addHeader([("chr1", 248956422), ("chr2", 242193529), ("chr18", 80373285)], maxZooms=0)

# 3. Prepare sorted data
# Format: (Chrom, Start, End, Value)
data = [
    # chr1 entries
    ("chr1", 3985539, 3985593, 1445.0),
    ("chr1", 3986092, 3986158, 1604.0),
    ("chr1", 4834947, 4834972, 451.0),
    ("chr1", 4932074, 4932105, 781.0),
    ("chr1", 7398193, 7398238, 718.0),
    ("chr1", 10997255, 10997298, 1495.0),
    ("chr1", 11967597, 11967659, 2219.0),
    ("chr1", 13091584, 13091602, 605.0), # Removed duplicate/overlap for simplicity
    ("chr1", 13091602, 13091609, 230.0),
    ("chr1", 17175906, 17175954, 1109.0),
    # chr2 entries
    ("chr2", 474242, 474302, 1560.0),
    ("chr2", 1005806, 1005875, 1519.0),
    ("chr2", 2109875, 2109924, 743.0),
    ("chr2", 2782811, 2782860, 990.0),
    ("chr2", 3153311, 3153360, 1174.0),
    ("chr2", 4118682, 4118726, 701.0),
    ("chr2", 4290402, 4290433, 565.0),
    ("chr2", 4403280, 4403323, 1209.0),
    ("chr2", 4563951, 4563986, 648.0),
    ("chr2", 4948833, 4948907, 1518.0),
    # chr18 entries
    ("chr18", 41186829, 41186856, 792.0)
]

# Extract lists for addEntries
chroms = [x[0] for x in data]
starts = [x[1] for x in data]
ends = [x[2] for x in data]
values = [x[3] for x in data]

# 4. Write to file
bw.addEntries(chroms, starts, ends=ends, values=values)

# 5. Always close to flush the buffer
bw.close()
print("test.bw created successfully.")
