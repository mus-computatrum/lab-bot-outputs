import subprocess
for d in ['20200513_Mouse_PatchSeq_Release_count.v2', '20200625_patchseq_metadata_mouse']:
    result = subprocess.run(['find', f'/data/gouwens2020-patchseq/transcriptome/{d}', '-type', 'f'], 
                           capture_output=True, text=True)
    print(result.stdout)