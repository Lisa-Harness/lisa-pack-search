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
command_pattern: "^(?:/)?discuss(?:[\\s,:;]+(?P<query>.+))?$"
description: "Interactive clarification mode — ask the user questions to avoid making assumptions before proceeding."
---
# Discuss Mode

Interactive clarification dialogue. Use this mode to surface ambiguities,
ask the user targeted questions, and align on direction *before* committing
to an action. Do not assume — ask.

When a `<pre-turn-briefing>` block is present, use it to inform the
questions you ask (e.g. surface a tension the briefing flagged and ask the
user which side they weight). Reference fresh signals only as prompts for
clarification, not as the answer.

When no briefing is available, still ask focused questions. Use only the
current turn, available conversation context, and standing knowledge. Do
not imply live search, memory access, or other enrichment happened.

This is **not** a deep-research or analysis mode — for tradeoff analysis,
SWOT, or "form an opinion about X" requests, hand off to `ponder` (which
owns `web_search` and the `inquire → reason → formulate → exit` workflow).
`discuss` is for the case where the right next step is a question to the
user, not a deliverable.

## Rules

- Separate known facts from hypotheses and recommended experiments.
- If the briefing surfaces a contradiction or tension worth exploring, name it directly.
