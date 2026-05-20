# MCP / Connectivity Security Reference

Load when adding any MCP server configuration or external connectivity component to
the harness. Required before writing any connectivity configuration.

> **Authorization Requirement**: Do not add any MCP component in either Active or
> Passive governance mode without explicit user authorization. Adding MCP expands
> agent capability boundaries and may break security guardrails. When MCP is desired,
> present the User Confirmation Template in this file and obtain explicit approval
> before proceeding.

---

## Pre-Creation Risk Assessment

Answer all questions before proceeding. If any answer is "unsure", ask the user before
continuing.

1. **Scope**: What specific tools or resources does the agent need? List each one.
2. **Access pattern**: Read-only, read-write, or execute? Justify each level.
3. **Data sensitivity**: Can this server access credentials, PII, or internal data?
4. **Blast radius**: If this server is compromised or misconfigured, what is exposed?
5. **Confirmation obtained**: Has the user explicitly confirmed they want this
   connection? (Required — do not proceed without it.)

---

## Minimal Capability Principle

Grant only what is needed for the declared task. Do not configure:

- Wildcard tool access (e.g., `tools: "*"` or `resources: "**"`)
- Speculative access to resources not referenced in the declared task
- Write or execute access where read-only suffices
- Persistent credentials when ephemeral tokens are available

Every capability in an MCP config must map to a specific, named, current task.

---

## MCP Config Security Template

Apply this structure to every MCP server entry:

```json
{
  "mcpServers": {
    "<server-name>": {
      "command": "<executable>",
      "args": ["<arg1>", "<arg2>"],
      "env": {
        "API_KEY": "$ENV_VAR_NAME"
      },
      "_comment": "<why this server exists, what it accesses, confirmed by user on YYYY-MM-DD>"
    }
  }
}
```

**Forbidden in MCP configs:**
- Inline credentials, tokens, or passwords — use `$ENV_VAR_NAME` references only
- Broad filesystem paths (`/`, `~`, `../`) — scope to the minimum required directory
- Servers that execute arbitrary shell commands without explicit scope restriction
- Server entries without a `_comment` documenting purpose and confirmation reference

---

## User Confirmation Template

Present this to the user before creating any MCP component:

```
Proposed MCP server: <server-name>
Access type:         <read | read-write | execute>
Resources accessed:  <specific files, APIs, directories, or external services>
Why needed:          <what agent task this enables>

Confirm? [yes / no / modify]
```

Record the confirmation reference (PR number, commit hash, or date) in the `_comment`
field of the resulting config.

---

## Pre-Commit Checklist

- [ ] User explicitly confirmed — reference documented in config comment
- [ ] No inline credentials — environment variable references only
- [ ] Tool and resource list is minimal: nothing speculative or for future use
- [ ] Each capability maps to a named, current task
- [ ] Blast radius is understood and acceptable to the user
- [ ] Any file containing secrets is listed in `.gitignore` or equivalent
- [ ] `_comment` field present on every server entry
