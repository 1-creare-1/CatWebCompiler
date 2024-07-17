# Catweb Compiler
Code compiler for roblox game [Cat Web](https://www.roblox.com/games/16855862021)
The game uses a block-based coding language. Luckly its possible to import code via json so I've made this compiler which coverts a basic text based language into cat web's json format.

## Basic Docs
### Global Functions
#### Debuging
- `log(message: string);` Prints white text
- `warn(message: string);` Prints orange text
- `error(message: string);` Prints red text

#### Control
- `wait(seconds: number);` Waits `seconds` seconds
- `redirect(url: string);` Redirects user to `url`

#### Audio
- `play(audio_id: number);` Plays audio with id `id`
- `play_l(audio_id: number);` Plays audio with id `id` on loop
- `volume(volume: number);` Sets global volume to `volume`
- `stopall();` Stops all playing audio
- `pauseall();` Pauses all playing audio
- `resumeall();` Resumes any paused audio

#### Display
- `hide(id: number);` Hides element with global id `id`<
- `show(id: number);` Shows element with global id `id`
- `configure(property: string, id: number, value: any);` Sets property `property` to `value` on element with global id `id`

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

### Variables
Variable support is still in progress however the basics work.
- `x = 10;` Create variable `x` with value `10`
- `y = x + 2;` Create variable `y` with value as result of expression `x + 2` (Support for longer expressions not implemented yet)
- `log("{x}");` Log variable `x` to console. Support for `log(x);` not implemented yet.
- `log("The value of x is: {x}");` String works!

## Notes
- There is a limit of 500 actions per second. `wait(seconds: number)` can be used to slow down your code to stay below this limit.
- The developer of cat web has incorrectly utilized the roblox filter resulting in very harsh code tagging.

## Todo
- [x] Variables
- [ ] Conditionals
- [x] Loops
- [ ] Functions (Cat web doesn't have functions, this will be a compiler time macro-like thing)