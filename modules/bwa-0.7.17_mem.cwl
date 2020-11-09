#!/usr/bin/env cwl-runner

cwlVersion: v1.1
class: CommandLineTool

requirements:
  - class: DockerRequirement
    dockerPull: biocontainers/bwa:v0.7.17_cv1
  - class: InlineJavascriptRequirement

baseCommand: ['bwa', 'mem']

inputs:
  reference_genome:
    type: File
  read_group_header: 
    type: string
    '@RG\\tID:%s\\tLB:%s\\tSM:%s\\tPL:Illumina\\tPU:%s\\tCN:DMP_MSKCC'
  fastq_input:
  
outputs:


# 1. make index of the reference genome in fasta format
# 2. Perform alignment

# bwa mem usage
# bwa mem index_prefix [input_reads.fastq|input_reads_pair_1.fastq input_reads_pair_2.fastq] [options]

# bwa index ref.fa
# bwa mem ref.fa reads.fq > aln-se.sam
# bwa mem ref.fa read1.fq read2.fq > aln-pe.sam

# "bwa mem \
# -t 4 
# -PM 
# -R '@RG\\tID:{baseName}\\tLB:{tid}\\tSM:{sample_id}\\tPL:Illumina\\tPU:{barcode}\\tCN:DMP_MSKCC' 
# {ref}  {in1}  {in2} ".format(
#   baseName, tid, sampleId, barcode, 
#   self.__propObj.getBWAHGRef(), inputFile1, inputFile2)
