---
date: 2024-08-16
time: 15:44
last_edited: 2024-09-16 16:48
tags:
  - area
aliases: 
Links: "[[My Areas]]"
---
# Books to Get
```dataview
table without id
file.link as Title, Author, Fiction, Owned
from "3. Resources" and #book
where Owned = "false"
sort file.name asc
```

# Books Owned
```dataview
table without id
file.link as Title, Author, Fiction, Owned
from "3. Resources" and #book 
where Owned = "true"
sort file.name asc
```

# Fiction
```dataview
table without id
file.link as Title, Author, Fiction, Genre, Pages
from "3. Resources" and #book and [[Fiction]]
sort file.name asc
```

# Non Fiction
```dataview
table without id
file.link as Title, Author, Fiction, Genre, Pages
from "3. Resources" and #book and [[Non-fiction]]
sort file.name asc
```

# Reading
```dataview
table without id
file.link as Title, Author, Fiction, Genre, Pages
from "3. Resources" and #book
where ReadingStatus = "Reading"
sort file.name asc
```

# To Read
```dataview
table without id
file.link as Title, Author, Fiction, Genre, Pages
from "3. Resources" and #book
where ReadingStatus = "To Read"
sort file.name asc
```

# Read
```dataview
table without id
file.link as Title, Author, Fiction, Genre, Pages, Rating
from "3. Resources" and #book
where ReadingStatus = "Read"
sort file.name asc
```
