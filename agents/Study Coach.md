---
role: Study Coach
schedule: daily 08:00 (launchd)
tags: [agent, study, databricks]
---

# Study Coach

Checks progress on [[Databricks Data Engineer Associate - 4 Week Plan]] every morning and texts Jason a reminder to study for 1 hour.

## What it does
1. Reads the plan's `- [ ] **Day N (date)**` checkboxes.
2. Compares days checked off vs. days elapsed since `start_date` → *on track / ahead / behind*.
3. Texts (iMessage, SMS fallback) the progress and the next unchecked day's topic.
4. Day before start: heads-up text. After all 28 days are checked: exam-prep nudge until `exam_target`, then stops. Goes quiet a week after the exam target.

## How to track progress
Check off each day in the plan (`- [x]`). That's the only input.

## Files
- Script: `agents/study-coach/study_reminder.py` (`--dry-run`, `--date=YYYY-MM-DD` for testing)
- Schedule: `~/Library/LaunchAgents/com.jasonrich.study-reminder.plist`
- Log: `~/Library/Logs/study-reminder.log`

## Manage
- Preview today's text: `python3 agents/study-coach/study_reminder.py --dry-run`
- Pause: `launchctl bootout gui/$(id -u)/com.jasonrich.study-reminder`
- Resume: `launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.jasonrich.study-reminder.plist`
- Change time: edit `Hour`/`Minute` in the plist, then pause + resume.
