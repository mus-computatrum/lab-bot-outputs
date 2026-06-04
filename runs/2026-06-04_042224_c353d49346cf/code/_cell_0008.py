# Check how metadata IDs match count matrix column IDs
print("Metadata transcriptomics_sample_id samples:")
print(meta['transcriptomics_sample_id'].head(10).tolist())

# Count matrix header sample
import subprocess
header = subprocess.run(['head', '-1', 
    '/data/gouwens2020-patchseq/transcriptome/20200513_Mouse_PatchSeq_Release_count.v2/20200513_Mouse_PatchSeq_Release_count.v2.csv'],
    capture_output=True, text=True).stdout
cols = header.strip().split(',')
print("\nCount matrix column samples (first 5):", cols[1:6])
print("Total columns:", len(cols))