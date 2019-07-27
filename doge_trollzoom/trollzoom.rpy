# The Crop() is so that you don't have to manually crop it. You may need to adjust this with the actual image you use to zoom in on the face, or part of the image you like.
image syd troll_2 = Crop((200, 400, 610, 700), "syd/syd_troll.png") 
image syd troll_1 = Crop((835, 400, 610, 700), im.Flip("syd/syd_troll.png", horizontal=True))

# I usually like to set two versions: One facing left and one facing right - again, all using the same source image "syd/syd_troll.png" and not having to manually crop, resize, or flip it.
image syd troll2 = At("syd troll_2", trollzoom)
image syd troll1 = At("syd troll_1", trollzoom)

init:
    transform trollzoom:
        linear .05 zoom 0.75
        linear .25 zoom 1.25
        linear .25 zoom 1.0
		
# Example of how to use:
# Here, `syd` is your character, `troll1` is the troll zoom facing right, and `center` is a default position in Ren'Py, which you can substitute for the location you want.

show syd troll1 at center

