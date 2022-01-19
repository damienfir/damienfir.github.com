---
date: 2021-01-19
title: Devlog #0
---

# Devlog #0

## The game

So I'm developing a puzzle game about teleportation through portals. Yes, it
probably sounds like [something]() you've played before, but this one (probably)
won't have a lot of physics and will be played on a 2D grid.

The game doesn't have a name yet. So I will call it The game for now.

I am not sure what the final look and feel will be, but I'm thinking a semi-open
world where you encounter the puzzle as you explore. My inspiration for the game
were (non-exhaustively):
- Monster's Expedition for its interesting mechanics and
nice look,
- The Witness, because I love that game,
- and obviously Portal

At first, I had the idea of making a game where you can teleport anywhere in
your line of sight. But it turned out to be too hard to make good levels because
the player could only teleport to platforms that are "under" you. Then I tried
switching to a 2D top-down view where the same mechanic applied. However the
teleportation turned to be way too powerful, which made it too hard to design
challenging levels.

So my solution was to merge that idea with Portal's... portals. And also to put
the player on a grid to reduce the degrees of freedom, hence make it easier to
design levels.

More details on the mechanics:

- The player moves on a 2D grid, with a view from above. The goal is to exit the level (the red tile for now).
- The portals are placed on the side of blocks, either movable or not (walls).
- There are doors with buttons to press (with the player or a block standing on
  it).
- There are buttons that deactivates the tunnel (the path between two portals)
  of the same color.
- The player can undo/reset indefinitely to encourage exploration.

By the way, I took a lot of tips from that [series](https://www.youtube.com/watch?v=oCHciE9CYfA) [of](https://www.youtube.com/watch?v=iUi2vMZajco) [video](https://www.youtube.com/watch?v=zsbfkMuaUxs) by Elyot Grant about puzzle design. Highly recommended.

## Development so far

I first developed a prototype in Python (with
[Arcade](https://api.arcade.academy/en/latest/)), which allowed me to explore
different ideas quickly and zero-in on a specific set of mechanics that allows
interesting levels.

![python prototype](/static/content/0-python-prototype.png)

For the rest of the development, I will switch away from Python and use
[Zig](https://ziglang.org/) instead. Why Zig and not something like C++ ?
Because I like to try something new, and Zig is a great compromise between being
low-level and encouraging correctness. Time will tell if it was a wise choice to
start a long-term project with such a young and unstable language. But I'm
hopeful and supportive of Zig's team and their core values.

All the basic mechanics are implemented. It just looks very raw but it will
allow me to work on designing more levels.

## New this week

### Animations

This week I focused on making the game look slightly better by adding some
animations to the movement of the player and the blocks. It makes it easier to
see what is happening, especially when you go through a portal.

The animation is made smooth by using the
[smootherstep](https://en.wikipedia.org/wiki/Smoothstep) function by Ken Perlin.
It is a sigmoid-style easing function that make the animation start slow and end slow.

![animations screencast](/static/content/0-peek-animation.gif)

### Undo/reset

The undo feature makes it easy for the player to explore different solution
without restarting the level if he gets stuck.

My implementation of undo is based on keeping a stack of game state. Appending
to the stack on every move and popping out the last state for undo. Reset is achieved
by taking the first element of the stack.

I can do that since the state is very small, it contains only the player's and
the blocks' positions. We'll see how it evolves.

![undo screencast](/static/content/0-peek-undo.gif)

### Camera view rotation

I have a problem in my game design. Since there are 3D blocks that can have
portals on all sides, there will be some portals that the player can't see. How
do I make them visible to the player ? There are a few solutions:

  - Make the blocks transparent. This might be confusing, it is harder
    to implement, and it severely constrains how the game can look like. You
    basically need glass blocks and glass walls.
  - Make the portals glow, such that you can see them shine on the floor and
    other objects. Again, this might be confusing. It also forces the floor to
    be white.
  - Allow the player to turn the camera. The easiest solution to implement and
    the more flexible one. The problem is that the player can't see the whole
    level at once.

I went with the third solution because it is the easiest to implement, which
allows me to move on to other problems.

![camera rotation screencast](/static/content/0-peek-rotate-camera.gif)


## What's next

I'm planning to design more puzzles to test these mechanics. It is also a great
way of discovering the consequences of these mechanics (often because of bugs).
By discovering these consequences, you can make more interesting levels that
present these consequences to the player. More info in [this video](https://www.youtube.com/watch?v=3BE9y2p01KU) by
Jonathan Blow and Marc ten Bosch.


--

Published on 2021-01-19

[Back home](/)
