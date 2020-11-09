#!/usr/bin/env cwl-runner

cwlVersion: v1.1
class: CommandLineTool

requirements:
  - class: DockerRequirement
    dockerPull: kfdrc/samtools:latest
  - class: InlineJavascriptRequirement

# baseCommand: samtools
baseCommand: ['samtools', '--version']

inputs:
  any_input:
  
# 
outputs:
  anything:
    type: stdout
