Find uncompleted items from all my daily notes and move them into today's note

## TODO

- [ ] MVP
    - [ ] list all daily notes files
    - [ ] read all daily notes and parse (AST)
    - [ ] extract all uncompleted tasks per section
    - [ ] extract non tasks paragraps after ## Jewelry section
    - [ ] find today's note
    - [ ] append extracted tasks into today's note
    - [ ] remove extracted lines from parsed notes
    - [ ] implement caching, do not process specific files, use platformdirs to
      store state file
    - [ ] Nuitka compiling

## Requirements

- [ ] use argsparse
- [ ] argument (or enviroment varible) to set working directory
- [ ] argument (date pattern) to find today's note
- [ ] process files only once
- [ ] log which files was processed
- [ ] enabled files backup by default
