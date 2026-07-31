---
mode_id: search
mode_provider_id: lisa-pack-search
start_stage_id: none
mode_kind: action
artifact_type: search_results
routable: true
routing_intent_tags: [research]
satisfies_intents: [research]
routing_intent_keywords:
  research:
    - search
    - latest
    - recent
    - current
    - news
    - update
    - today
fast_path_patterns:
  - "^(?:search(?:\\s+the\\s+web)?|web\\s+search|look\\s+up|find\\s+(?:recent|latest|current)|what(?:'s|\\s+is)\\s+(?:the\\s+)?(?:latest|new)|latest\\s+(?:news|updates?)\\s+(?:on|for)?|recent\\s+(?:news|updates?)\\s+(?:on|for)?)\\b"
require_query: true
entry_operation_ids: [web_search]
required_capabilities: [tools]
command_pattern: "^(?:/)?search[\\s,:;]+(?P<query>.+)$"
description: "Web search mode."
---
# Search Mode

Provide a detailed and reasoned interpretation of the results.
