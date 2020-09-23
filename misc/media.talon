(volume|media)  up: key(volup)
(volume|media)  down: key(voldown)
set (volume|media) <number>: user.media_set_volume(number)
(volume|media) mute: key(mute)
media next: key(next)
media last: key(prev) 
# TODO: key(play) doesn't work
media (play | pause): key(play)
