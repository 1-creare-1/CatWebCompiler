globals = [
    {
        "name": "log",
        "id": 0,
        "args": 1
    },
    {
        "name": "warn",
        "id": 1,
        "args": 1
    },
    {
        "name": "error",
        "id": 2,
        "args": 1
    },



    {
        "name": "wait",
        "id": 3,
        "args": 1
    },

    {
        "name": "redirect",
        "id": 4,
        "args": 1,
        "extra": {"href": True}
    },



    {
        "name": "play",
        "id": 5,
        "args": 1
    },
    {
        "name": "play_l",
        "id": 26,
        "args": 1
    },
    {
        "name": "volume",
        "id": 6,
        "args": 1
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
        "args": 1
    },


    {
        "name": "hide",
        "id": 8,
        "args": 1
    },
    {
        "name": "show",
        "id": 9,
        "args": 1
    },
    {
        "name": "configure",
        "id": 31,
        "args": 3
    }
]

def get_global(name):
    for g in globals:
        if g['name'] == name:
            return g