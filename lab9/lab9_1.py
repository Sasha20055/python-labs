#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Фильтрация слушателей по баллам и дате завершения теста.

Скрипт:
 1. Читает любые CSV с произвольным масштабом оценки (10 или 100).
 2. Для каждой строки динамически находит столбец с оценкой по вхождению "Оценка"
    и столбец с датой по вхождению "Завершено".
 3. Парсит русские даты формата "12 мая 2017 10:09" и "01 Май 2017".
 4. Фильтрует по порогу и диапазону дат, выводит в алфавитном порядке.
"""

import csv
import argparse
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any, Iterator

# Поддерживаем оба падежа названий месяцев
_MONTHS: Dict[str, int] = {
    **{m + "я": i for m, i in zip(
        ["январ", "феврал", "март", "апрел", "ма", "июн", "июл", "август", "сентябр", "октябр", "ноябр", "декабр"],
        range(1,13)
    )},
    **{m: i for m, i in zip(
        ["январь","февраль","март","апрель","май","июнь","июль","август","сентябрь","октябрь","ноябрь","декабрь"],
        range(1,13)
    )}
}

def parse_russian_datetime(s: str) -> datetime:
    """
    "12 мая 2017 10:09" или "12 Май 2017 10:09" или "01 мая 2017" → datetime
    """
    parts = s.strip().split()
    if len(parts) == 3:
        parts.append("00:00")
    if len(parts) != 4:
        raise ValueError(f"Неверный формат даты: {s!r}")
    day = int(parts[0])
    month = _MONTHS.get(parts[1].lower())
    if not month:
        raise ValueError(f"Неизвестный месяц: {parts[1]!r}")
    year = int(parts[2])
    hour, minute = map(int, parts[3].split(":"))
    return datetime(year, month, day, hour, minute)

def read_all_rows(files: List[Path]) -> Iterator[Dict[str, Any]]:
    """Итерируем по всем строкам всех CSV-файлов."""
    for p in files:
        with p.open(encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                yield row

def filter_listeners(
        rows: Iterator[Dict[str, Any]],
        min_score: float,
        start_dt: datetime,
        end_dt: datetime
) -> List[Dict[str, Any]]:
    """
    Для каждой строки:
     - находим key_score (подстрока "Оценка")
     - находим key_date  (подстрока "Завершено")
     - парсим и фильтруем
    """
    passed = []
    for row in rows:
        # определяем колонки для этой строки
        score_key = next((k for k in row if "Оценка" in k), None)
        date_key  = next((k for k in row if "Завершено" in k), None)
        if not score_key or not date_key:
            continue

        # парсим и проверяем балл
        raw = row[score_key].replace(",", ".")
        try:
            score = float(raw)
        except ValueError:
            continue
        if score < min_score:
            continue

        # парсим и проверяем дату
        try:
            dt = parse_russian_datetime(row[date_key])
        except ValueError:
            continue
        if not (start_dt <= dt <= end_dt):
            continue

        # если всё ок — сохраняем нужные поля
        passed.append({
            "Фамилия": row.get("Фамилия", "").strip(),
            "Имя":     row.get("Имя", "").strip(),
            "score":   score,
            "date":    row[date_key].strip(),
        })

    return passed

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--files", nargs="+", type=Path, required=True,
        help="CSV-файлы (например: \"16 - 1.csv\" \"16 - 2.csv\")"
    )
    parser.add_argument(
        "--min-score", type=float, required=True,
        help="Минимальная оценка в тех же единицах, что и в CSV"
    )
    parser.add_argument(
        "--start-date", type=str, required=True,
        help="Дата начала диапазона (DD Mon YYYY)"
    )
    parser.add_argument(
        "--end-date", type=str, required=True,
        help="Дата конца диапазона (DD Mon YYYY)"
    )
    args = parser.parse_args()

    dt_start = parse_russian_datetime(f"{args.start_date} 00:00")
    dt_end   = parse_russian_datetime(f"{args.end_date} 23:59")

    rows = read_all_rows(args.files)
    passed = filter_listeners(rows, args.min_score, dt_start, dt_end)

    # Сортируем и выводим
    passed.sort(key=lambda x: (x["Фамилия"], x["Имя"]))
    print("Отобранные слушатели:")
    for r in passed:
        print(f'{r["Фамилия"]} {r["Имя"]} — {r["score"]} балл(ов), завершено {r["date"]}')

if __name__ == "__main__":
    main()


"""
python3 lab9_1.py \
     --files "16 - 1.csv" "16 - 2.csv" \
     --min-score 60 \
     --start-date "01 Май 2017" \
     --end-date   "31 Май 2017"
"""