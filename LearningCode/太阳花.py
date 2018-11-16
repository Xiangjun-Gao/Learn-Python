import turtle as t
t.color('blue','violet')
t.speed(200)
t.begin_fill()
while True:
    t.fd(200)
    t.left(170)
    if abs(t.pos())<1:
        break
t.end_fill()
t.done()