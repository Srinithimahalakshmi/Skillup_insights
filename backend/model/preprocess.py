def normalize_skills(skills):
    """Lowercase & trim; can be extended later."""
    return [s.strip().lower() for s in skills if s.strip()]
