from mcp.server.fastmcp import FastMCP
import os

mcp = FastMCP("Notes")

Notes = os.path.join(os.path.dirname(__file__), "note.txt")

def EnsureFile():
    if not os.path.exists(Notes):
        with open(Notes, "w") as file:
            file.write(" ")

# Tool to add new message to the notes file   
@mcp.tool()
def AddNote(message: str) -> str:
    """
    Append a message to the notes file
    Args: 
        message {str}: The note content to be added.
    Returns:
        str: Confirmation message indicating the note was added.
    """
    EnsureFile()
    with open(Notes, "a") as file:
        file.write(message + "\n")
    return "Message to added to the notes!"

# Tool to Read the content of the notes
@mcp.tool()
def ReadNote() -> str:
    """
    Read the messages from the notes file
    Args:
        None
    Returns:
        All the contents of the notes file, None if the file is empty  
    """
    EnsureFile()
    with open(Notes, "r") as file:
        content = file.read()
        if content == " ":
            return None
        return content


# Resource to get the new line entry in the notes
@mcp.resource("notes://latest")
def GetLatestNotes():
    """
    Get the latest messages from the notes
    Args:
        None
    Returns:    
        The new message from the notes file, "No notes yet" if the file is empty
    """
    EnsureFile()
    with open(Notes, "r") as file:
        lines = file.readlines()
    return lines[-1].strip() if lines else "No notes yet"

# Prompt to summerize the Notes
@mcp.prompt()
def Summerize():
    """
    Summerizes the entire content in the notes
    Args:
        None
    Returns:
        The Summerized Message, None if the file is empty   
    """
    EnsureFile()
    with open(Notes, "r") as file:
        content = file.read()
    if not content:
        return None
    return f"Summerized content{ content }"
    