"""Inline SVG icons. Stroked 24x24 paths unless noted."""

_STROKE = (
    '<svg viewBox="0 0 24 24" aria-hidden="true" stroke-linecap="round" '
    'stroke-linejoin="round">{}</svg>'
)

_PATHS = {
    "stethoscope":
        '<path d="M6 3v5a4 4 0 0 0 8 0V3"/><path d="M4 3h3M13 3h3"/>'
        '<path d="M10 12v3a5 5 0 0 0 10 0v-1"/><circle cx="20" cy="10" r="2"/>',
    "womens":
        '<circle cx="12" cy="8" r="5"/><path d="M12 13v8M9 18h6"/>',
    "mens":
        '<circle cx="10" cy="14" r="5"/><path d="M15 9l6-6M16 3h5v5"/>',
    "shield":
        '<path d="M12 3l7 3v6c0 4.2-2.9 7.7-7 9-4.1-1.3-7-4.8-7-9V6z"/>'
        '<path d="M9.5 12l1.8 1.8 3.4-3.6"/>',
    "pulse":
        '<path d="M3 12h4l2.5-6 4 12L16 12h5"/>',
    "mind":
        '<path d="M15.5 4A5.5 5.5 0 0 0 10 9.5V20h5.5a5.5 5.5 0 0 0 0-11"/>'
        '<path d="M10 9.5A4.5 4.5 0 1 0 5.5 14H10"/>',
    "plus":
        '<path d="M12 5v14M5 12h14"/>',
    "signal":
        '<path d="M4 18v-4M9 18v-8M14 18V7M19 18V4"/>',
    "clock":
        '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.2 2"/>',
    "wallet":
        '<path d="M3 7.5A2.5 2.5 0 0 1 5.5 5H18v3"/>'
        '<path d="M3 7.5V17a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-6a2 2 0 0 0-2-2H5.5"/>'
        '<circle cx="17" cy="13" r="1.1"/>',
    "network":
        '<circle cx="12" cy="5" r="2.4"/><circle cx="5" cy="18" r="2.4"/>'
        '<circle cx="19" cy="18" r="2.4"/><path d="M10.6 7L6.4 15.9M13.4 7l4.2 8.9M7.4 18h9.2"/>',
    "lock":
        '<rect x="4.5" y="10" width="15" height="10" rx="2.2"/>'
        '<path d="M8 10V7.5a4 4 0 0 1 8 0V10"/>',
    "device":
        '<rect x="7" y="2.5" width="10" height="19" rx="2.4"/><path d="M11 18.6h2"/>',
    "heart":
        '<path d="M12 20s-7-4.4-7-9.2A3.8 3.8 0 0 1 12 8a3.8 3.8 0 0 1 7 2.8C19 15.6 12 20 12 20z"/>',
    "user":
        '<circle cx="12" cy="8.5" r="4"/><path d="M4.5 20c1.4-3.7 4.2-5.5 7.5-5.5s6.1 1.8 7.5 5.5"/>',
    "pin":
        '<path d="M12 21s7-5.6 7-11a7 7 0 1 0-14 0c0 5.4 7 11 7 11z"/><circle cx="12" cy="10" r="2.6"/>',
}

# Filled icons for buttons and floating actions.
_FILLED = {
    "phone":
        '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 '
        '6.6 6.6l2.2-2.2a1 1 0 0 1 1-.24 11.4 11.4 0 0 0 3.6.58 1 1 0 0 1 1 1V20a1 1 0 0 '
        '1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1 11.4 11.4 0 0 0 .58 3.6 1 '
        '1 0 0 1-.25 1z"/></svg>',
    "whatsapp":
        '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15L2 22l5.2-1.4A10 '
        '10 0 1 0 12 2m0 1.8a8.2 8.2 0 1 1-4.2 15.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 0 1 12 '
        '3.8m-3.3 4c-.2 0-.5.1-.7.4-.2.3-.9.9-.9 2.1s.9 2.4 1 2.6c.1.2 1.7 2.7 4.2 3.7 2 .8 2.5.7 '
        '2.9.6.4 0 1.4-.6 1.6-1.1.2-.6.2-1 .1-1.1l-.6-.3-1.5-.7c-.2-.1-.4-.1-.5.1l-.7.9c-.1.2-.3.2-.5.1a6.8 '
        '6.8 0 0 1-2-1.2 7.4 7.4 0 0 1-1.4-1.7c-.1-.3 0-.4.1-.5l.4-.5.3-.5v-.4l-.7-1.7c-.2-.4-.4-.4-.5-.4z"/></svg>',
    "mail":
        '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 5h18a1 1 0 0 1 1 1v12a1 1 0 0 '
        '1-1 1H3a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1m1.6 2L12 12.2 19.4 7z"/></svg>',
    "menu":
        '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 6h18v2H3zM3 11h18v2H3zM3 16h18v2H3z"/></svg>',
    "arrow":
        '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M13.2 5.6 19.6 12l-6.4 6.4-1.4-1.4 4-4H4.4v-2h11.4l-4-4z"/></svg>',
}


def icon(name):
    """Return the inline SVG for `name`, or an empty string if unknown."""
    if name in _FILLED:
        return _FILLED[name]
    if name in _PATHS:
        return _STROKE.format(_PATHS[name])
    return ""
