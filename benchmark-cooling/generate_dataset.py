#!/usr/bin/env python3
"""Reproduce the exact 600-row synthetic dataset used in the 2026-11-19 benchmark.
Python standard library only; no real-world observations or confidential inputs.
"""
import csv
import datetime
import hashlib
import pathlib
import random

SEED = 20261119
EXPECTED_SHA256 = "f2e58076228e324bae48237bc10cb585a28aa98265d4ab60bc1a57b841ad1cf4"
OUTPUT = pathlib.Path(__file__).with_name("mira_synthetic_cooling_600.csv")

rng = random.Random(SEED)
ambient, load, coolant, machine, energy = 20.0, 60.0, 100.0, 55.0, 40.0
observations = []
for i in range(800):
    a = 20 + 0.62 * (ambient - 20) + rng.gauss(0, 1.4)
    l = 60 + 0.45 * (load - 60) + rng.gauss(0, 1.3)
    f = 100 + 0.42 * (coolant - 100) + 0.72 * (load - 60) + rng.gauss(0, 1.8)
    m = 55 + 0.46 * (machine - 55) + 0.32 * (load - 60) - 0.38 * (coolant - 100) + 0.35 * (ambient - 20) + rng.gauss(0, 1.1)
    e = 40 + 0.46 * (energy - 40) + 0.28 * (load - 60) + 0.22 * (coolant - 100) + rng.gauss(0, 1.0)
    ambient, load, coolant, machine, energy = a, l, f, m, e
    if i >= 200:
        observations.append((a, l, f, m, e))

start = datetime.datetime(2026, 1, 5, 8)
headers = ["timestamp", "ambient_temp_C", "production_load_pct", "coolant_flow_lpm", "machine_temp_C", "energy_kwh"]
with OUTPUT.open("w", newline="", encoding="utf-8") as target:
    writer = csv.writer(target)
    writer.writerow(headers)
    for i, row in enumerate(observations):
        writer.writerow([(start + datetime.timedelta(minutes=i * 15)).isoformat(timespec="minutes"), *(f"{value:.4f}" for value in row)])
actual = hashlib.sha256(OUTPUT.read_bytes()).hexdigest()
print("Wrote", OUTPUT.name, "rows:", len(observations), "SHA-256:", actual)
if actual != EXPECTED_SHA256:
    raise RuntimeError("Dataset checksum mismatch; check Python environment and generator")
