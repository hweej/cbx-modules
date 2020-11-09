WIP:POC: Repo to show that we can switch from using perl modules over to using cwl modules instead.

Instructions
After cloning this repository, users should first install all requirements by installing Pipenv on their machine. Please reference the Makefile. 

1) make

2) make activate

Update test_data_files submodule
cd tests/data
git fetch
git pull

To do:

- [ ] Make initial cwl tools
 - cutadapt
 - fastp
 - bwa
 - samtools
 - abra
- [ ] combine intial tools into a bam generation workflow
 - run locally with test data
 - run on lsf cluster with test data
- [x] Gather test_data 
 - T/N from CLIN 20200040 (case has mutations, copy number, fusion and CH). 
 - include a second pair and controls (NTC, PoolNormal, PoolTumor, BloodPoolNormal)
 - make downsampled versions of the fastqs for testing locally

User Requirements:
    FASTQS -> bams
    Use CWL/DSL
    Use toil
    Test on LSF
    Use singularity
    Project structure


### Tools
Merge/Trim
    CUTADAPT 
    fastqc
    bamqc
Bam Generation
    SAMTOOLS
    ABRA
    BWA - mem, etc...
    GATK - BQSR ( think about it )

There are two ideas that are starting to form here.
1) Pluggable modules
    a. Community Modules + MSKCC ClinBx in-house modules
    b. Separate ability for development and testing
2) Cookie-cutter pattern
    a. Separate pipeline development
    b. Separate pipeline requirements
