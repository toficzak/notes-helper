# notes-helper

## Context

Default work notes directories' tree:
- journal
- knowledge
- tasks
- feedback
- training

## Needs
- script creating a copy of template file with filled current or chosen date
- script calling JIRA instance with given task id and producing based on template task-note in proper directory
- script searching for a pattern in file and replacing occurrences with links to tasks/knowledge pages

## Scripts

### New day script
Assumptions:
- it is executed from journal directory
- template file is in the same journal directory
- template file name is known and hardcoded
- when no data provided - assume today's date
- if date provided - use provided date
  - no validation
- if file already exists - inform and exit
- date-to-replace pattern inside file is known and hardcoded
- date pattern is known and hardcoded as dd.MM.yyyy