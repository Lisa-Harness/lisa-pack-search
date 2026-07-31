---
mode_id: read
mode_provider_id: lisa-pack-search
start_stage_id: none
mode_kind: chat
require_query: true
routable: true
priority: 6
routing_intent_tags: [read]
satisfies_intents: [read]
routing_intent_keywords:
  read:
    - read documents
    - read files
    - read text files
allowed_tool_ids: [read_file, list_files]
command_pattern: "^(?:/)?read[\\s,:;]+(?P<query>.+)$"
description: "Read mode for reading documents, files, and text files."
fast_path_patterns:
  - "^(?:read|review)\\b"
---
# Read Mode

Read for comprehension and analysis unless the user explicitly asks you to read for a different purpose.
