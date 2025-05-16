#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Подсчитать количество АЗС (amenity=fuel) по операторам
и вывести список всех названий станций в алфавитном порядке.
"""

import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path
from typing import Dict, Iterator, List, Optional, Tuple


def parse_fuel_elements(osm_path: Path) -> Iterator[Tuple[Optional[str], Optional[str]]]:
    """
    Обходит XML-файл OSM и для каждого <node> или <way> с тегом amenity=fuel
    возвращает кортеж (operator, name). Если тега нет — вернёт (None, None).
    """
    context = ET.iterparse(osm_path, events=("start", "end"))
    _, root = next(context)  # получить корневой элемент
    in_fuel = False
    operator: Optional[str] = None
    name: Optional[str] = None

    for event, elem in context:
        # Когда наткнулись на start-элемент node или way — обнуляем флаги
        if event == "start" and elem.tag in ("node", "way"):
            in_fuel = False
            operator = None
            name = None

        # Ищем теги внутри node/way
        if event == "end" and elem.tag == "tag":
            k = elem.attrib.get("k")
            v = elem.attrib.get("v")
            if k == "amenity" and v == "fuel":
                in_fuel = True
            elif in_fuel and k == "operator":
                operator = v
            elif in_fuel and k == "name":
                name = v

        # Когда закрывается node/way — если это АЗС, отдаём данные
        if event == "end" and elem.tag in ("node", "way"):
            if in_fuel:
                yield (operator, name)
            root.clear()  # очищаем дерево, чтобы не тратить память

    # Конец функции


def main():
    # Пути к файлам (лежать рядом со скриптом)
    files = [Path("16.osm"), Path("16 - 2.osm")]

    # Собираем все (operator, name)
    stations: List[Tuple[str, str]] = []
    for f in files:
        if not f.exists():
            raise FileNotFoundError(f"Файл не найден: {f}")
        for op, nm in parse_fuel_elements(f):
            stations.append((op or "Unknown", nm or ""))

    # Считаем по операторам
    operator_counts: Dict[str, int] = Counter(op for op, _ in stations)

    # Уникальные непустые имена, отсортированные
    names = sorted({nm for _, nm in stations if nm})

    # Вывод
    print("Количество АЗС по фирмам:")
    for op, cnt in operator_counts.items():
        print(f"  {op}: {cnt}")

    print("\nСписок всех АЗС в алфавитном порядке:")
    for nm in names:
        print(f"  {nm}")


if __name__ == "__main__":
    main()