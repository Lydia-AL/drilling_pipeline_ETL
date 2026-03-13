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

def add_contact_info(dm: Dict[str, Any]) -> Dict[str, Any]:
    """Ensure contact_information key exists."""
    if "contact_information" not in dm or not isinstance(dm["contact_information"], dict):
        dm["contact_information"] = {
            "operator_company": None,
            "contact_person": None,
            "phone": None,
            "email": None,
        }
    return dm

def format_machine_id(dm: Dict[str, Any]) -> Dict[str, Any]:
    """Normalize machine id to format 'DM-XXX'."""
    raw_key = "machine_id" if "machine_id" in dm else "machine_ID" if "machine_ID" in dm else None
    if not raw_key:
        return dm
    raw = dm[raw_key]
    if "-" in raw:
        prefix, num = raw.split("-", 1)
        if num.isdigit():
            dm["machine_id"] = f"{prefix}-{num.zfill(3)}"
            if raw_key == "machine_ID":
                del dm["machine_ID"]
    return dm

def format_machine_id(dm: Dict[str, Any]) -> Dict[str, Any]:
    """Normalize machine_id and reorder keys."""
    raw_key = "machine_id" if "machine_id" in dm else "machine_ID" if "machine_ID" in dm else None
    if not raw_key:
        return dm
    raw = dm[raw_key]
    if "-" in raw:
        prefix, num = raw.split("-", 1)
        if num.isdigit():
            dm["machine_id"] = f"{prefix}-{num.zfill(3)}"
            if raw_key == "machine_ID":
                del dm["machine_ID"]
            reordered = {"machine_id": dm["machine_id"]}
            for k, v in dm.items():
                if k != "machine_id":
                    reordered[k] = v
            return reordered
    dm["machine_id"] = raw
    if raw_key == "machine_ID":
        del dm["machine_ID"]
    return dm
