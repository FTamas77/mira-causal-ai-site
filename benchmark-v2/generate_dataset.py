#!/usr/bin/env python3
"""Exactly reproduce the blind industrial cooling benchmark v2 CSV (900 rows).
The dataset and model are synthetic. Uses only the Python standard library.
"""
import csv
import datetime as dt
import hashlib
import pathlib
import random

SEED = 20261119
EXPECTED_SHA256 = "22eac3fc04f0577df3af126d5537c628018213e1dcfd35cef5f304b2aeb5d13a"
OUTPUT = pathlib.Path(__file__).with_name("mira_blind_cooling_v2_900.csv")
rng = random.Random(SEED)
a, l, f, m, e, v = 20.0, 60.0, 100.0, 55.0, 40.0, 8.0
start = dt.datetime(2026, 1, 12, 8, 0)

with OUTPUT.open("w", newline="", encoding="utf-8") as stream:
    writer = csv.writer(stream)
    writer.writerow([
        "timestamp", "ambient_temp_C", "production_load_pct",
        "coolant_flow_lpm", "machine_temp_C", "energy_kwh", "vibration_mm_s",
    ])
    for i in range(250 + 900):
        aa = 20 + 0.62 * (a - 20) + rng.gauss(0, 1.25)
        ll = 60 + 0.55 * (l - 60) + rng.gauss(0, 1.4)
        ff = 100 + 0.38 * (f - 100) + 1.20 * (l - 60) + 0.85 * (m - 55) + rng.gauss(0, 1.1)
        mm = 55 + 0.50 * (m - 55) + 0.56 * (l - 60) - 0.55 * (f - 100) + 0.26 * (a - 20) + rng.gauss(0, 0.85)
        ee = 40 + 0.36 * (e - 40) + 0.38 * (l - 60) + 0.25 * (f - 100) + rng.gauss(0, 0.9)
        vv = 8 + 0.42 * (v - 8) + 0.44 * (m - 55) + 0.22 * (l - 60) + rng.gauss(0, 0.75)
        a, l, f, m, e, v = aa, ll, ff, mm, ee, vv
        if i >= 250:
            timestamp = (start + dt.timedelta(minutes=(i - 250) * 15)).isoformat(timespec="minutes")
            writer.writerow([timestamp, *(f"{value:.4f}" for value in (a, l, f, m, e, v))])

actual = hashlib.sha256(OUTPUT.read_bytes()).hexdigest()
print(f"{OUTPUT.name}: 900 synthetic rows, SHA-256 {actual}")
if actual != EXPECTED_SHA256:
    raise RuntimeError("Byte-level checksum mismatch: generator/environment differs")
