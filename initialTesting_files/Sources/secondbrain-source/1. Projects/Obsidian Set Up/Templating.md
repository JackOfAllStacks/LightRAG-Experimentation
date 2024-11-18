---
date: 2024-09-07
time: 21:00
last_edited: 2024-09-16 18:05
tags:
  - projElement
  - vaultProject
aliases: 
Project: "[[Project - Setting Up Obsidian]]"
Area: "[[Obsidian]]"
Status: In Progress
Deadline: 2024-09-18
DateCompleted: 
---
# Templating
I want to make templates for all the different areas of my [[Obsidian]] vault in order to automate everything as much as I can, and provide the most ease of access. I want a [[Root Template]] that a note created in my vault will use by default if it is created in an area that hasn't been assigned a template.

I can use icons from the icons library using (:Li) to put icons in notes instead of just the side folders.
This will be great for organising the [[obsidian]] brain and making things look better.

I have just gotten the [[Linter Plugin]] to help with the templating process. The [[Linter Plugin]] is being used to update the "last_edited" property in the YAML frontmatter of all notes.

## Directories in Need of Templates
### Top Level Directories in Vault in Need of Templates
- [x] [[Root Template]] for [[Root Directory]] ✅ 2024-09-16
- [x] [[1. Project Folder Script Template]] for [[Project Directory]] ✅ 2024-09-16
- [x] [[1. Project Template]] for [[Project Directory]] ✅ 2024-09-16
- [x] [[1. ProjElement Template]] for [[Project Directory]] ✅ 2024-09-16
- [x] [[2. Area Template]] for [[Area Directory]] ✅ 2024-09-16
- [x] [[3. Resource Template]] for [[Resource Directory]] ✅ 2024-09-16
- [x] [[99. Meta template]] for [[Meta Directory]] ✅ 2024-09-16

### Resource Directories in Need of Templates
- [ ] [[Account Template]] for [[Accounts Directory]]
- [ ] [[Book Template]] for [[Book Directory]]
- [ ] [[Person Template]] for [[People Directory]]
- [ ] [[Recipe Template]] for [[Recipes Directory]]
- [ ] [[Place Template]] for [[Places Directory]]
- [ ] [[Clothes Template]] for [[Clothes Directory]]
- [ ] [[Services Template]] for [[Services Directory]]
- [ ] [[Health Template]] for [[Health Directory]]

### Journal Directories in Need of Templates
- [ ] [[1. Daily Template]] for [[Daily Note Directory]]
- [ ] [[2. Weekly Template]] for [[Weekly Note Directory]]
- [ ] [[3. Monthly Template]] for [[Monthly Note Directory]]
- [ ] [[4. Quarterly Template]] for [[Quarterly Note Directory]]
- [ ] [[5. Yearly Template]] for [[Yearly Note Directory]]
- [ ] [[Dream Journal Template]] for [[Dream Journal Directory]]
- [ ] [[Magick Diary Template]] for [[Magickal Diary Directory]]

## Initial Thoughts from First Draft
I need templates made so that every note I create will be created with all the necessary components it will need straight away without faffing about. These necessities are different depending on the area the template is made for, but we will start general
- Metadata and [[tags]] that are relevant to the note, and useful for creating dataview queries
- Potentially [[tags]] not as # tag, but as a note, so that as my network of notes builds, there is a larger topic note which has all of the notes using it as a tag connected to it. As the tag note gets bigger, I can turn that note into an index or a MOC (Map of Content) where the note links to all the other notes that reference it
- References. A part at the bottom of a note for references, that can link to other notes, books, videos, url's and links
- The time and date the note was created
- Heading taken from the title of the note
