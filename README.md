# 📒 Notes Manager with FastMCP

This project uses **FastMCP** to create a simple Notes management system.  
It provides tools, resources, and prompts to add, read, and manage notes through the MCP protocol.

---

## ✅ Features

### 1️⃣ AddNote Tool
Adds a new message to `note.txt`.

**Usage:**
```python
AddNote("Your message here")
```

---

### 2️⃣ ReadNote Tool
Reads **all messages** from `note.txt`.  
Returns `None` if the file is empty.

**Usage:**
```python
ReadNote()
```

---

### 3️⃣ GetLatestNotes Resource
Fetches **only the latest note** from `note.txt`.  
Returns `"No notes yet"` if the file is empty.

**Usage:**
```python
GetLatestNotes()
```

---

### 4️⃣ Summerize Prompt
Generates a simple summary of all notes in the file.  
Returns `None` if the file is empty.

**Usage:**
```python
Summerize()
```

---

## ⚙️ How It Works

- Checks if `note.txt` exists; creates it if it doesn’t.
- Appends each new note line by line.
- Provides MCP-compatible tools, resources, and prompts.
- All data is stored in `note.txt` in the same directory as the script.

---

## 📂 File

- **File Name:** `note.txt`  
- **Location:** Same directory as your Python script.

---

## 🚀 Requirements

- `fastmcp` module (`FastMCP` from `mcp.server.fastmcp`)
- Standard Python `os` module

---

## 📝 Example

```python
from mcp.server.fastmcp import FastMCP
import os

mcp = FastMCP("Notes")

# Add a note
AddNote("Remember to buy milk.")

# Read all notes
print(ReadNote())

# Get the latest note
print(GetLatestNotes())

# Summarize notes
print(Summerize())
```

---

**Happy Note Taking! 📚✨**
