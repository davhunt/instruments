# Contributing to `instruments`

## Overview
Please note our general guidelines for contributing to NDCLab projects [here](https://ndclab.github.io/wiki/docs/contributing.html).

* [Roadmap](#Roadmap)  
* [Directory Structure](#Directory-Structure)  
* [Scripts](#Scripts)
* [Containers](#Containers)  
* [Workflow](#Workflow)  

## Roadmap
Please see the roadmap available on the [README.md](https://github.com/NDCLab/template-tool/blob/main/README.md) file of this repository.

## Directory Structure

```yml
instruments
├── adexi
├── chexi
├── texi
```

### Scripts
The `scripts` directory is the local [package](https://docs.python.org/3/tutorial/modules.html#packages) where Python modules will be written. This ensures that modules are neatly divided according to responsibility, which helps with parallel development and debugging. 

### Container
To ensure reproducibility of results and software, a default docker file is included with this template repository. The respective [README.md](https://github.com/NDCLab/template-tool/tree/main/container) contains a comprehensive guide on how to get started with containerization (special thanks to [Jonhas](https://github.com/Jonhas))!

A step-by-step guide to getting started also included in the following [video](https://www.youtube.com/watch?v=oO8n3y23b6M). 

## Adding Instruments
To add an additional instrument:
1. Create a new directory with the instrument's short name.
2. Upload the published PDF(s) and a REDCamp import .zip that follows the lab's [naming conventions](https://ndclab.github.io/wiki/docs/etiquette/naming-conventions.html#redcap).
3. Add the instrument to the json file with the numerical values for subscale scoring.
4. Add a section to the .ipynb file indicating the appropriate scoring mechanisms for total scores and subscale scores.

## Workflow
Workflow for both internal and external lab members is outlined on the [NDCLab contributing wiki page](https://ndclab.github.io/wiki/docs/contributing.html). 
