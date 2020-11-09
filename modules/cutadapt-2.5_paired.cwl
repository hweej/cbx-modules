#!/usr/bin/env cwl-runner

cwlVersion: v1.1
class: CommandLineTool

requirements:
  - class: DockerRequirement
    #dockerPull: biocontainers/cutadapt:v1.18-1-deb-py3_cv1 # Use v1.18 for now
    dockerPull: kfdrc/cutadapt:latest
  - class: InlineJavascriptRequirement

# baseCommand: ['cutadapt', '--version']
baseCommand: cutadapt

# Singlefile input for now, hold off on glob input
inputs:
  adapterSequence:
    type: string
    inputBinding:
      position: 0
      prefix: -a
  inputFile:
    type: File
    inputBinding:
      position: 3 # Rethink this to use flags instead of positional

outputs: 
  outFile:
    label: modified fastq with removed adapter sequences
    type: File
    outputBinding:
      glob: $(inputs.inputFile.nameroot + "_cutadapt" + inputs.inputFile.nameext)
  # outFile:
  #   type: stdout (will be the clipping metrics file, currently, *cl.stats in impact pipeline)

arguments:
  - position: 2
    prefix: --output
    valueFrom: $(inputs.inputFile.nameroot + "_cutadapt" + inputs.inputFile.nameext)
#stdout: $(inputs.inputFile.basename)

# cutadapt -a AACCGGTT -o output.fastq.gz input.fastq.gz
# command for paired cutadapt with dual indices:
# cutadapt -m 25 -e 0.1 -j 4 -a <R1_adapter>  -A <R2_adapter> -o out.1.fastq -p out.2.fastq in.1.fastq in.2.fastq
