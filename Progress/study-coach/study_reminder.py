#!/usr/bin/env python3
"""Daily study-progress check + text reminder for the Databricks DE Associate plan.

Reads the plan's checkboxes, compares completed days to where you should be,
and texts today's task via the macOS Messages app.
Usage: study_reminder.py [--dry-run]
"""
import datetime as dt
import re
import subprocess
import sys
from pathlib import Path

PHONE = "+17576467569"
PLAN = Path("/Users/jasonrich/technical_study/study/Databricks Data Engineer Associate - 4 Week Plan.md")
LOG = Path.home() / "Library/Logs/study-reminder.log"
TOTAL_DAYS = 28

DAY_RE = re.compile(r"^- \[( |x|X)\] \*\*Day (\d+) \((\d{4}-\d{2}-\d{2})\)\*\* — (.+)$")


def parse_plan(text):
    meta = dict(re.findall(r"^(start_date|exam_target): (\S+)$", text, re.M))
    days = []
    for line in text.splitlines():
        m = DAY_RE.match(line.strip())
        if m:
            done, num, date, task = m.groups()
            topic = re.sub(r"[*`]", "", task).split(":")[0].split(" — ")[0].strip()
            days.append({"done": done.lower() == "x", "num": int(num),
                         "date": dt.date.fromisoformat(date), "topic": topic[:110]})
    return meta, days


def build_message(today, meta, days):
    start = dt.date.fromisoformat(meta["start_date"])
    exam = dt.date.fromisoformat(meta["exam_target"])
    done = sum(d["done"] for d in days)
    day_idx = (today - start).days + 1

    if day_idx < 0:
        return None  # more than a day before the plan starts: stay quiet
    if day_idx == 0:
        return (f"📚 Databricks DE Associate plan starts tomorrow ({start:%a %b %d}). "
                f"Day 1: {days[0]['topic']}. Block out 1 hour!")
    if done == TOTAL_DAYS:
        if today <= exam:
            return f"🎯 All 28 days done! Exam target {exam:%b %d}. Do a light 1-hour review today and you're set."
        return None
    if day_idx > TOTAL_DAYS and today > exam + dt.timedelta(days=7):
        return None  # plan over; stop nagging

    expected_before_today = min(day_idx - 1, TOTAL_DAYS)
    behind = expected_before_today - done
    nxt = next(d for d in days if not d["done"])
    if behind <= 0:
        status = "✅ on track" if behind == 0 else f"🚀 {-behind} day(s) ahead"
    else:
        status = f"⚠️ {behind} day(s) behind"

    header = f"📚 Databricks DE Associate — Day {min(day_idx, TOTAL_DAYS)}/28"
    if day_idx > TOTAL_DAYS:
        header = f"📚 Databricks DE Associate — plan window ended, {TOTAL_DAYS - done} day(s) left"
    return (f"{header}\nProgress: {done}/28 ({status})\n"
            f"Up next: Day {nxt['num']} — {nxt['topic']}\n"
            f"Study for 1 hour today, then check it off in Obsidian.")


def send_text(msg):
    script = '''
on run {targetNumber, msgText}
    tell application "Messages"
        try
            set svc to 1st account whose service type = iMessage
            send msgText to participant targetNumber of svc
        on error
            set svc to 1st account whose service type = SMS
            send msgText to participant targetNumber of svc
        end try
    end tell
end run
'''
    subprocess.run(["osascript", "-e", script, PHONE, msg], check=True,
                   capture_output=True, text=True)


def log(line):
    LOG.parent.mkdir(parents=True, exist_ok=True)
    with LOG.open("a") as f:
        f.write(f"{dt.datetime.now():%Y-%m-%d %H:%M} {line}\n")


def main():
    dry = "--dry-run" in sys.argv
    today = dt.date.today()
    for a in sys.argv:
        if a.startswith("--date="):
            today = dt.date.fromisoformat(a.split("=", 1)[1])
    meta, days = parse_plan(PLAN.read_text())
    msg = build_message(today, meta, days)
    if msg is None:
        log("no message today")
        print("(no message today)")
        return
    print(msg)
    if dry:
        return
    try:
        send_text(msg)
        log("sent: " + msg.replace("\n", " | "))
    except subprocess.CalledProcessError as e:
        log("SEND FAILED: " + (e.stderr or str(e)).strip())
        raise


if __name__ == "__main__":
    main()
