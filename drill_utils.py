# drill_utils.py
from typing import Dict, Any, List

EXPECTED_KEYS: List[str] = [
    "machine_id",
    "machine_ID",
    "name",
    "location",
    "status",
    "specifications",
    "last_maintenance_date",
    "next_maintenance_due",
    "contact_information",
]

def remove_useless_data(dm: Dict[str, Any]) -> Dict[str, Any]:
    """Return a new dict keeping only EXPECTED_KEYS (if present)."""
    return {k: v for k, v in dm.items() if k in EXPECTED_KEYS}

def convert_miles_to_meters(dm: Dict[str, Any]) -> Dict[str, Any]:
    """Convert depth_capacity_miles and drilling_speed_miles_per_day to meters."""
    specs = dm.get("specifications", {})
    if "depth_capacity_miles" in specs:
        specs["depth_capacity_meters"] = specs["depth_capacity_miles"] * 1609
        del specs["depth_capacity_miles"]
    if "drilling_speed_miles_per_day" in specs:
        specs["drilling_speed_meters_per_day"] = specs["drilling_speed_miles_per_day"] * 1609
        del specs["drilling_speed_miles_per_day"]
    dm["specifications"] = specs
    return dm

def convert_dates(dm: Dict[str, Any]) -> Dict[str, Any]:
    """Normalize date strings to DD/MM/YYYY."""
    def to_dd_mm_yyyy(s: str) -> str:
        if "-" in s:
            parts = s.split("-")
            if len(parts) == 3:
                if len(parts[0]) == 4:  # YYYY-MM-DD
                    return f"{parts[2]}/{parts[1]}/{parts[0]}"
                return "/".join(parts)
        if "/" in s:
            return s
        return s
    if "last_maintenance_date" in dm:
        dm["last_maintenance_date"] = to_dd_mm_yyyy(dm["last_maintenance_date"])
    if "next_maintenance_due" in dm:
        dm["next_maintenance_due"] = to_dd_mm_yyyy(dm["next_maintenance_due"])
    return dm