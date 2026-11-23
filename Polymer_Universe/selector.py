"""Decision logic for the Polyverse polymer requirement selector."""

# The fifth scenario is the printer-guide peer-testing challenge.
REQUIREMENTS = {
    "1": {
        "title": "Lightweight, strong reinforcement for a laptop bag",
        "polymer": "Kevlar",
        "reason": "Kevlar has a high strength-to-weight ratio, making it suitable for lightweight reinforcement.",
        "icon": "🎒",
        "tag": "Strength + low weight",
    },
    "2": {
        "title": "A conducting coating for a sensor",
        "polymer": "Polyaniline (PANI)",
        "reason": "In a suitable doped form, polyaniline can conduct electricity and is useful in sensor coatings.",
        "icon": "📟",
        "tag": "Electrical conductivity",
    },
    "3": {
        "title": "Disposable packaging intended for industrial composting",
        "polymer": "Polylactic Acid (PLA)",
        "reason": "Suitable PLA grades can biodegrade under controlled industrial composting conditions.",
        "icon": "🥡",
        "tag": "Industrial composting",
    },
    "4": {
        "title": "A low-friction surface for a sliding component",
        "polymer": "PTFE",
        "reason": "PTFE has a very low coefficient of friction, helping surfaces slide smoothly.",
        "icon": "⚙️",
        "tag": "Low friction",
    },
    "5": {
        "title": "A small guide inside a printer must let a moving part slide smoothly",
        "polymer": "PTFE",
        "reason": "PTFE's low coefficient of friction makes it a suitable candidate for a smooth-sliding printer guide.",
        "icon": "🖨️",
        "tag": "Peer-testing challenge",
    },
}


def get_recommendation(choice):
    """Return a recommendation for a valid numbered choice, else None.

    The input is converted to text and whitespace is removed so values such as
    1, "1" and " 1 " all behave consistently.
    """
    return REQUIREMENTS.get(str(choice).strip())


# Application Finder: examples supplied for the project presentation.
APPLICATION_KEYWORDS = {
    "Sensors": "Polyaniline (PANI)",
    "Water bottles": "PET",
    "Laptop bags": "Kevlar",
    "Biodegradable food packaging": "Polylactic Acid (PLA)",
    "Printer sliding components": "PTFE",
    "Bullet-resistant protective clothing": "Kevlar",
    "Rechargeable battery electrodes": "Polyaniline (PANI)",
    "Non-stick cookware": "PTFE",
    "Polyester clothing": "PET",
    "Biomedical sutures": "Polylactic Acid (PLA)",
    "Food packaging trays": "PET",
    "Corrosion-resistant coatings": "Polyaniline (PANI)",
    "Aerospace reinforcement": "Kevlar",
    "Chemical-resistant seals and gaskets": "PTFE",
}

# If an application phrase is not recognised, the user can search by a
# material requirement/property instead.
PROPERTY_MATCHES = {
    "Lightweight and strong reinforcement": "Kevlar",
    "Conductive coatings and sensors": "Polyaniline (PANI)",
    "Biodegradable packaging": "Polylactic Acid (PLA)",
    "Low-friction sliding components": "PTFE",
    "Bullet-resistant protective materials": "Kevlar",
    "Rechargeable battery electrodes": "Polyaniline (PANI)",
    "Biomedical sutures": "Polylactic Acid (PLA)",
    "Non-stick coatings": "PTFE",
}


def find_application_matches(application):
    """Return application matches, preferring the longest matching phrase."""
    query = (application or "").strip().casefold()
    if not query:
        return []
    matches = []
    for phrase, polymer in APPLICATION_KEYWORDS.items():
        if phrase.casefold() in query or query in phrase.casefold():
            matches.append((phrase, polymer, len(phrase)))
    matches.sort(key=lambda item: item[2], reverse=True)
    return matches


def find_property_matches(description):
    """Return property-based matches when no application keyword is found."""
    query = (description or "").strip().casefold()
    if not query:
        return []
    matches = []
    for phrase, polymer in PROPERTY_MATCHES.items():
        if phrase.casefold() in query or query in phrase.casefold():
            matches.append((phrase, polymer, len(phrase)))
    matches.sort(key=lambda item: item[2], reverse=True)
    return matches
