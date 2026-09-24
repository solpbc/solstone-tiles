---
name: solstone-memory
description: Answer questions about the owner's own past (what they said, heard or planned, and who someone is) from their journal. Use whenever a question is about the owner's life, conversations, people or plans.
---

# The owner's journal

The journal tools only read the owner's journal.

1. Start with `search`, using a few plain keywords (names, topics), not a whole sentence.
2. Before answering, read the best hit with `fetch`, passing the `reference` that search returned.
3. For "who is X", search for the name and read what the hits say about them.
4. Search does not cover raw transcripts. When the owner names a day, call `list_transcripts` with that day as `YYYYMMDD`, then `get_transcript` with a segment's `reference` to read what was said.
5. Answer from what the journal says, and name the day it came from.
6. When a tool result says nothing matched, believe it. Try one other wording at most, then tell the owner nothing turned up in what they've let Tiles see. Do not list or read transcripts one by one to be sure.
7. If the journal tools are missing, tell the owner to type `/mcp-auth solstone__journal` in the chat to connect Tiles to their journal.
8. Never fill a gap with a guess, and never put anything from the journal into a web search.
