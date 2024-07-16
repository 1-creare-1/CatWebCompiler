globals = [
    {
        "name": "log",
        "id": 0,
        "args": 1,
        "types": ["string"],
    },
    {
        "name": "warn",
        "id": 1,
        "args": 1,
        "types": ["string"],
    },
    {
        "name": "error",
        "id": 2,
        "args": 1,
        "types": ["string"],
    },



    {
        "name": "wait",
        "id": 3,
        "args": 1,
        "types": ["number"],
    },

    {
        "name": "redirect",
        "id": 4,
        "args": 1,
        "extra": {"href": True},
        "types": ["string"],
    },



    {
        "name": "play",
        "id": 5,
        "args": 1,
        "types": ["number"],
    },
    {
        "name": "play_l",
        "id": 26,
        "args": 1,
        "types": ["number"],
    },
    {
        "name": "volume",
        "id": 6,
        "args": 1,
        "types": ["number"],
    },
    {
        "name": "stopall",
        "id": 7,
        "args": 0
    },
    {
        "name": "pauseall",
        "id": 28,
        "args": 0
    },
    {
        "name": "resumeall",
        "id": 29,
        "args": 0
    },


    {
        "name": "hide",
        "id": 8,
        "args": 1,
        "types": ["object"],
    },
    {
        "name": "show",
        "id": 9,
        "types": ["object"],
        "args": 1
    },
    {
        "name": "configure",
        "id": 31,
        "args": 3,
        "types": ["string", "object", "any"],
    }
]

def get_global(name):
    for g in globals:
        if g['name'] == name:
            return g