# Tools

The `ludo-tools` plugin (Mac) and `ludo-tools-windows` plugin (Windows) add two tools Claude can call. Both need [Node.js](https://nodejs.org) and install automatically with the plugin.

## chrome

A Chrome window Claude controls: open pages, click, type, scroll, read, take screenshots, check the console and network, and measure page speed. Use it to test and debug websites you build, or to read pages a plain web fetch can't.

Lab settings, already applied:
- **Throwaway profile** (`--isolated`): a fresh browser every time. Your real Chrome logins, cookies and history are never touched.
- **Smaller screenshots** (JPEG, max 1280px wide): the same information for a fraction of your usage limit.
- **1280x800 window**, a standard laptop size.
- **No usage statistics** sent to Google, and page speed checks stay local.

Try: *"Open my site at localhost:3000, check it at phone width, and list anything broken."*

## docs

Up-to-date documentation and code examples for coding libraries and frameworks. Claude's training has a cutoff; this closes the gap.

Try: *"Use the docs tool to check the current way to set up a Next.js app, then do it."*

## Claude in Chrome (optional, separate)

Anthropic's own Chrome extension lets Claude use **your** Chrome, including sites you're logged in to. It's what `/ludo:scrape` uses for logged-in pages. Setup is in the scrape skill, or:

1. Install "Claude" by Anthropic from the [Chrome Web Store](https://chromewebstore.google.com/detail/claude/fcoeoabgfenejglbffodgkkbkcdhcgfn).
2. Start Claude Code with `claude --chrome`.
3. `/chrome` should say Status: Enabled.
