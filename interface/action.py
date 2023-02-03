def speed_knots(callsign: str, speed: float) -> dict:
    """
    Create a speed control action with units of knots.
    """
    return {"callsign": callsign, "kind": "speed", "subkind": "knots", "value": speed}


def speed_mach(callsign: str, speed: float) -> dict:
    """
    Create a speed control action with units of Mach number.
    """
    return {"callsign": callsign, "kind": "speed", "subkind": "mach", "value": speed}


def level_absolute(callsign: str, flight_level: int) -> dict:
    """
    Create an absolute flight level control action.
    """
    return {
        "callsign": callsign,
        "kind": "flight_level",
        "subkind": "absolute",
        "value": flight_level,
    }


def level_relative(callsign: str, flight_level: int) -> dict:
    """
    Create a relative flight level control action.
    """
    return {
        "callsign": callsign,
        "kind": "flight_level",
        "subkind": "relative",
        "value": flight_level,
    }


def heading_absolute(callsign: str, heading: int) -> dict:
    """
    Create an absolute heading control action.
    """
    return {
        "callsign": callsign,
        "kind": "heading",
        "subkind": "absolute",
        "value": heading,
    }


def heading_relative(callsign: str, heading: int) -> dict:
    """
    Create a relative heading control action.
    """
    return {
        "callsign": callsign,
        "kind": "heading",
        "subkind": "absolute",
        "value": heading,
    }


def navigate_direct(callsign: str, fix_id: str) -> dict:
    """
    Create a navigation control action.
    """
    return {
        "callsign": callsign,
        "kind": "navigate",
        "subkind": "direct",
        "value": fix_id,
    }


def comms_in(callsign: str) -> dict:
    """
    Create an incoming comms control action.
    """
    return {
        "callsign": callsign,
        "kind": "comms",
        "subkind": "in",
    }


def comms_out(callsign: str) -> dict:
    """
    Create an outgoing comms control action.
    """
    return {
        "callsign": callsign,
        "kind": "comms",
        "subkind": "out",
    }
