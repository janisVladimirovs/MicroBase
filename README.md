# MicroBase

MicroBase is a small append-only key-value database written in Python.

I created this project mainly to learn Python fundamentals and understand how simple databases work internally, including file storage, command parsing, append-only logs, tombstones, and later indexing and compaction.

## Current Features

- `SET key value`
- `GET key`
- `DELETE key`
- `EXIT`
- Persistent file storage
- Append-only log structure
- Tombstone-based deletion
- Case-insensitive commands
- Skips malformed database entries instead of crashing

## Example

```text
input command: SET name Janis
name added successfully

input command: GET name
Janis

input command: DELETE name
key deleted successfully

input command: GET name
key not found

input command: EXIT


PS: currently it's jsut a bunch of if statements which I will refractor it in the next update