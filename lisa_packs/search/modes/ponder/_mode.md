---
mode_id: ponder
mode_provider_id: lisa-pack-search
start_stage_id: inquire
mode_kind: workflow
require_query: true
routable: true
priority: 8
routing_intent_tags: [analyze, reason, evaluate]
satisfies_intents: [analyze, reason, evaluate]
routing_intent_keywords:
  - question
  - reason
  - analyze
  - explore
  - ponder
  - evaluate
  - consider
  - tradeoff
  - weigh
  - deliberate
  - assess
required_capabilities: [tools, reasoning]
fast_path_patterns:
  - "\\bthink\\s+about\\b"
  - "\\bgo\\s+in\\s+depth\\b"
  - "\\banalyze\\s+(?:this|tradeoffs?)\\b"
  - "\\bevaluate\\s+(?:this|tradeoffs?)\\b"
description: "Exploratory reasoning and forming opinion workflow."
command_pattern: "^(?:/)?(?:ponder)(?:[\\s,:;]+(?P<query>.+))?$"
---
# Ponder Mode

Reason through a specific question, decision, or tradeoff.
Focus on exploring the implications of a single decision or question, and providing a reasoned point of view.

- Build a reasoned point of view from evidence, constraints, and counterarguments.
- Consider and address counterarguments, especially those that are common or intuitive.
- Make uncertainties explicit in the opinion.
- Avoid overgeneralization from limited evidence.
