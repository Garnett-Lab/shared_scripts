#!/usr/bin/env python3
# This line specifies the interpreter to be used for executing the script (python3 in this case)
# need to install pip install pyBigWig
import sys, os
import pyBigWig
# Ensure correct usage
if len(sys.argv) < 3:
    print("Usage: ./script.py <ref_ta.tsv> <file.bw>")
    sys.exit(1)

ref_ta_file = sys.argv[1]
bigwig_file = sys.argv[2]

try:
    bw = pyBigWig.open(bigwig_file)
except Exception as e:
    print(f"Error opening BigWig: {e}")
    sys.exit(1)

# Get valid chromosomes from the BigWig header to prevent unnecessary errors
bw_chroms = bw.chroms().keys()

with open(ref_ta_file, "r") as ref_ta_fh:
    for line in ref_ta_fh:
        if '#' in line:
            continue
        parts = line.strip().split("\t")
        if len(parts) < 3:
            continue
            
        chrom, start, end = parts[0], int(parts[1]), int(parts[2])

        # Standardize chromosome naming
        if not chrom.startswith('chr'):
            chrom = f"chr{chrom}"
        
        # Filter out sex/mito chromosomes as per your requirement
        if any(x in chrom for x in ('X', 'Y', 'MT', 'M')):
            continue

        if chrom in bw_chroms:
            try:
                # Get the sum of coverage across the interval
                stats = bw.stats(chrom, start, end, type="sum", exact=True)
                coverage = stats[0] if stats[0] is not None else 0
                
                # Output format: chrom, start, end, total_coverage
                print(f"{chrom}\t{start}\t{end}\t{coverage:.2f}")
            except Exception as e:
                # Print to stderr so it doesn't mess up your redirected output file
                print(f"Error at {chrom}:{start}-{end}: {e}", file=sys.stderr)
        else:
            # Chromosome from BED not found in BigWig file
            print(f"Warning: {chrom} not found in BigWig", file=sys.stderr)

bw.close()

