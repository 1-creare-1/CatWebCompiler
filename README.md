# Catweb Compiler
Code compiler for roblox game [Cat Web](https://www.roblox.com/games/16855862021)
The game uses a block-based coding language. Luckly its possible to import code via json so I've made this compiler which coverts a basic text based language into cat web's json format.

## Basic Docs
### Global Functions
`log(message: string);` Prints white text<br>
`warn(message: string);` Prints orange text<br>
`error(message: string);` Prints red text<br>

`wait(seconds: number);` Waits `seconds` seconds<br>

`redirect(url: string);` Redirects user to `url`<br>

`play(audio_id: number);` Plays audio with id `id`<br>
`play_l(audio_id: number);` Plays audio with id `id` on loop<br>
`volume(volume: number);` Sets global volume to `volume`<br>
`stopall();` Stops all playing audio<br>
`pauseall();` Pauses all playing audio<br>
`resumeall();` Resumes any paused audio<br>

`hide(id: number);` Hides element with global id `id`<br>
`show(id: number);` Shows element with global id `id`<br>
`configure(property: string, id: number, value: any);` Sets property `property` to `value` on element with global id `id`<br>

### Loops
Loop forever
```
loop {
    log("hi");
}
```
Loop n times
```
loop(n: number) {
    log("hi");
}
```

## Notes
- There is a limit of 500 actions per second. `wait(seconds: number)` can be used to slow down your code to stay below this limit.

## Todo
- [ ] Variables
- [ ] Conditionals
- [x] Loops
- [ ] Functions (Cat web doesn't have functions, this will be a compiler time macro-like thing)