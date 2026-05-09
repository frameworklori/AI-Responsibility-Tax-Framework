"""AI five-layer economic stack definitions."""


AI_ECONOMIC_STACK = [
    {
        "layer": "energy",
        "description": "Power, cooling, land, water, and energy infrastructure.",
        "public_resource_intensity": "high",
    },
    {
        "layer": "compute",
        "description": "GPUs, TPUs, inference clusters, chips, and compute providers.",
        "public_resource_intensity": "extreme",
    },
    {
        "layer": "foundation_models",
        "description": "Frontier, national, open-source, and aligned model systems.",
        "public_resource_intensity": "high",
    },
    {
        "layer": "platforms",
        "description": "AI operating systems, browsers, search, agents, and cloud platforms.",
        "public_resource_intensity": "extreme",
    },
    {
        "layer": "applications",
        "description": "AI SaaS, enterprise automation, and local productivity systems.",
        "public_resource_intensity": "variable",
    },
]


def get_stack_layers():
    """Return the AI five-layer economic stack."""
    return list(AI_ECONOMIC_STACK)
