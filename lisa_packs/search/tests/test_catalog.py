"""Tests for the search pack's catalog discovery.

Verifies that the ``lisa-content`` server discovers the web_search tool
and the research operations from the search pack's content root, and
that the pack ships no mode content (modes were removed in 336a73f).
"""

from __future__ import annotations

import json

from sdk.content import (
    build_tool_catalog_json,
    resolve_mode_roots,
    resolve_tool_roots,
)
from lisa_packs.search import get_content_root


def test_web_search_tool_discovered() -> None:
    """The web_search tool is discovered from the pack's tools/ directory."""
    roots = resolve_tool_roots([get_content_root()])
    assert roots, "No tools/ directory found in search pack"

    catalog_json = build_tool_catalog_json(roots)
    catalog = json.loads(catalog_json)

    assert "web_search" in catalog
    tool = catalog["web_search"]
    assert tool["tool_id"] == "web_search"
    assert tool["description"]
    assert tool["module_path"]
    assert tool["module_path"].startswith("lisa_packs.search.tools.")


def test_search_pack_has_no_mode_content() -> None:
    """The pack no longer ships mode content.

    discuss/ponder/search modes were removed in commit 336a73f ("refactor:
    remove discuss, ponder, and search modes to streamline functionality");
    the pack now contributes tools and research operations only. The mode
    catalog scan must therefore find no ``modes/`` directory here.
    """
    roots = resolve_mode_roots([get_content_root()])
    assert roots == [], f"unexpected mode roots: {roots}"


def test_search_pack_models_importable() -> None:
    """The pack's response models are importable via the new module path."""
    from lisa_packs.search.models import WebSearchResponse, WebSearchResult
    from lisa_packs.search.operations.research.web_research import WebSearchStructuredOutput
    from lisa_packs.search.operations.research.discussion_briefing import (
        DiscussionBriefingStructuredOutput,
    )

    assert WebSearchResponse is not None
    assert WebSearchResult is not None
    assert WebSearchStructuredOutput is not None
    assert DiscussionBriefingStructuredOutput is not None
