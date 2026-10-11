# The AI agency skill

An AI automation agency that runs inside Claude Code. Five agents, one command. Free, MIT, no signup, no API key.

Made by **Alex Chen** ([@nocodealex](https://instagram.com/nocodealex)), an AI creator who builds free Claude Code skills. Full guide: [chen.media](https://chen.media).

An AI agency used to mean a team on payroll: one person for outreach, one for sales calls, one to build, one to
answer clients. `/agency` gives each of those jobs to an agent inside Claude, and they hand work to each other.

| command | the agent | what it does |
| --- | --- | --- |
| `/agency setup` | | interviews you once: your offer, who you sell to, your price, your voice |
| `/agency outbound leads.csv` | outbound | a personal first email for every business on your list, ready to send from your own email |
| `/agency sales prep acme` | sales | a one-page call plan: questions, objections, price, the next step |
| `/agency sales live call.txt` | sales | coaches you during the call, one line at a time, from any live transcript file |
| `/agency build acme` | workflow | writes the proposal, then builds the automation with a README and a test |
| `/agency support` | customer service | sorts client emails and drafts every reply in your voice |
| `/agency night` | night shift | works through `.agency/queue.md` while your computer stays on |
| `/agency status` | | what's waiting on you |

**Nothing is sent without your yes.** Outbound writes the emails and a mail-merge file; you send them from your own
email, at a pace your provider allows. Support drafts replies; you send them. The night shift never sends email.

Everything lives in `.agency/` in the folder you run it in.

## Install

Paste this into Claude Code:

```
https://github.com/alexyc9381/agency-skill
Install this skill, then run /agency setup.
```

Or as a plugin:

```
/plugin marketplace add alexyc9381/agency-skill
/plugin install agency-skill@agency-skill
```

Or copy `skills/agency` into `~/.claude/skills/`. Open a new Claude Code session afterwards.

## Good to know

- Live call coaching needs a transcription app that writes the call to a text file as you talk. The agent reads
  that file every 10 seconds.
- The night shift runs only while your computer is on and awake (on a Mac, run `caffeinate -i` in another window),
  and every job counts toward your Claude plan's usage.
- Cold email has rules (CAN-SPAM in the US, GDPR in Europe). Every email says who it's from and how to opt out, and
  `.agency/DO-NOT-CONTACT.md` is checked before anything is written.
- It is not made by Anthropic.

Run the tests with:

```bash
python3 -m unittest discover -s tests
```

## Making a video or post about this?

Go ahead. Credit it like this, in your caption or description:

```text
/agency skill by Alex Chen (@nocodealex): github.com/alexyc9381/agency-skill
```

Tag [@nocodealex](https://instagram.com/nocodealex) so I can see it. Every file the skill writes already ends with
the same credit, so leave it in the shot.

Writing about it or citing it in a paper? Use **Cite this repository** in the sidebar on GitHub.
