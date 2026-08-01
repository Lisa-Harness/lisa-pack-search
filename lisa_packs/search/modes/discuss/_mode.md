---
mode_id: discuss
mode_provider_id: lisa-pack-search
start_stage_id: none
mode_kind: chat
routable: true
priority: 5
pre_turn_operation_ids: [discussion_briefing]
routing_intent_tags: [clarify]
satisfies_intents: [clarify]
routing_intent_keywords:
  clarify:
    - clarify
    - not sure
    - need to know
    - what do you mean
    - ask you
    - questions about
    - should i
    - which option
    - ambiguous
    - unclear
    - can you confirm
    - help me decide
allowed_operation_ids: [web_search]
command_pattern: "^(?:/)?discuss(?:[\\s,:;]+(?P<query>.+))?$"
description: "Interactive clarification mode — ask the user questions to avoid making assumptions before proceeding."
---
# Discuss Mode

Discuss the topic for the purposes of seeking clarification.
Ask questions in order to avoid making any assumptions.
Endeavor to gain a full understanding.

When the `<pre-turn-briefing>` is present, use it to inform your view.

Use `web_search` to dig into topics especially when recent information is needed.
