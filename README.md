# renpy_tutorials

This repository gathers some of the interesting implementations I came across while developing the game [A Summer with the Shiba Inu](https://store.steampowered.com/app/916030/A_Summer_with_the_Shiba_Inu/).

# Dog troll zoom

I wanted a funny way to zoom into a part of the character sprite I have. This is done without manual cropping, resizing, or flipping the source image - all done with code, and with one single source image.

![Example of troll zoom](/doge_trollzoom/trollzoom_example.gif)

## Hologram overlay

I wanted to do an overlay to emulate a hologram-like image without using Photoshop since I don't have it. Good thing you can do it with some gradients made with [free software paint.net](https://www.getpaint.net/).

![Here's how it looks in-game](/hologram_overlay/hologram_example_ql.jpg)

Using the code snippet in the `.rpy` I applied it to the Ren'Py tutorial image that everyone has seen:

![Image of Eileen with hologram](/hologram_overlay/hologram_example.png)
