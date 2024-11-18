---
date: 2024-09-14
time: 12:57
last_edited: 2024-09-16 14:36
tags:
  - projElement
  - vaultProject
  - vaultOrganisation
aliases:
  - 1. Projects
Project: "[[Project - Setting Up Obsidian]]"
Area: "[[Obsidian]]"
Status: Complete
Deadline: 2024-09-16
DateCompleted: 2024-09-16
---
# 1. Projects
This is the [[PARA Method - Project|Project (PARA)]] directory, following the structure of the [[PARA Method]].

## Project Creation Methodology
Right now we are going with the approach of using the [[Projects Plugin]] to manage and create projects. In the **Project Directory** I will create a **Project - Note** outlining the initial thoughts for a project, and then a new folder for the [[Projects Plugin]] to use to store all notes relevant to the project. This allows for all **elements** that are temporary and exclusively relevant to this project only to be held within a folder that can be moved to [[Archive Directory|6. Archives]] when the project is complete. Any notes that are created during this process that aren't exclusively relevant to the project will be created in the [[Resource Directory]] as they might be relevant at a later date and will be better never being moved to [[Archive Directory|6. Archives]].

## [[Templating]] For Projects
The process of [[Templating]] for **Projects** at this stage requires 3 separate templates. The [[1. Project Folder Script Template]] is the first script that runs and determines whether the note being created is within the initial **1. Projects** directory or a subfolder within **1. Projects**. If the note is created in the top level directory, then that means the note is a **Project - Note**, intended to first outline the initial ideas for the project and should use the [[1. Project Template]]. If the note is created within a subfolder of the **Project Directory** then that means a folder has already been created for the **project elements** to be contained within, and any notes created within are **project elements** and should then use the [[1. ProjElement Template]].

First the [[1. Project Folder Script Template]] runs to check the location of the note being created.
If the note is a **Project - Note** it will use the [[1. Project Template]].
If the note is a **ProjElement** of a larger **Project** it will use the [[1. ProjElement Template]].

### Elements of the [[1. Project Template]]
- YAML Frontmatter
	- Date and Time of note creation
	- Last edited date
	- [[Tags]]
	- Aliases
	- Links (A link to [[My Projects]])
	- Area
	- Status (Brainstorming/Outlining, Todo, In progress, Complete)
	- Deadline
	- Date completed
- Title
- Areas
- Resources
- ProjElements

### Elements of the [[1. ProjElement Template]]
- YAML Frontmatter
	- Date and Time of note creation
	- Last edited date
	- [[Tags]]
	- Aliases
	- Project (A link to the [[PARA Method - Project|Project (PARA)]] this is an element of)
	- Area
	- Status (Brainstorming/Outlining, Todo, In progress, Complete)
	- Deadline
	- Date completed
- Title
