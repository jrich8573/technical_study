# technical_study

An Obsidian vault for technical study and certification prep.

## Contents

| Path | What it is |
|---|---|
| `study/Databricks Data Engineer Associate - 4 Week Plan.md` | 28-day, 1 hour/day plan for the Databricks Certified Data Engineer Associate exam. Starts 2026-11-30, exam target 2026-12-28. |
| `agents/Study Coach.md` | The agent that checks your progress on the plan each morning and texts you a reminder. |
| `agents/study-coach/study_reminder.py` | The script behind the Study Coach. |
| `CLAUDE.md` | Context for Claude when working in this vault. |

## Tracking progress

Each day in the plan is a checkbox line:

```
- [ ] **Day 1 (2026-11-30)** — Topic: details
```

Change `[ ]` to `[x]` once you finish that day. That's the only input the Study Coach reads. Keep the line in this exact format, including the bold `**Day N (YYYY-MM-DD)**` and the em dash (`—`), or the script won't see it.

## Daily reminder

Every day at 8:00 AM, a macOS launch agent runs `study_reminder.py`. The script:

1. Counts the days you've checked off and compares that to the days elapsed since `start_date`.
2. Texts you whether you're on track, ahead or behind, plus the topic of your next unchecked day. It sends through the Messages app, using iMessage first and falling back to SMS.
3. Sends a heads-up the day before the plan starts. Once all 28 days are checked, it sends exam-prep nudges until `exam_target`, and it stops a week after that.

### Commands

Run these from the vault root:

```sh
# Preview today's message without sending it
python3 agents/study-coach/study_reminder.py --dry-run

# Preview the message for a specific date
python3 agents/study-coach/study_reminder.py --dry-run --date=2026-12-05

# Pause the daily reminder
launchctl bootout gui/$(id -u)/com.jasonrich.study-reminder

# Resume the daily reminder
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.jasonrich.study-reminder.plist
```

To change the time, edit `Hour` and `Minute` in `~/Library/LaunchAgents/com.jasonrich.study-reminder.plist`, then pause and resume.

### Logs

- `~/Library/Logs/study-reminder.log`: what the script did each run
- `~/Library/Logs/study-reminder.out.log` and `~/Library/Logs/study-reminder.err.log`: the launch agent's stdout and stderr

## Moving this vault

The script and the launch agent both contain absolute paths to this folder. If you move or rename the vault, update:

- `PLAN` in `agents/study-coach/study_reminder.py`
- the script path in `~/Library/LaunchAgents/com.jasonrich.study-reminder.plist`, then pause and resume the reminder
