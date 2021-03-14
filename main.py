def on_on_overlap(sprite, otherSprite):
    info.change_score_by(-1)
    mySprite.start_effect(effects.fire, 200)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.player, on_on_overlap)

projectile: Sprite = None
mySprite: Sprite = None
info.start_countdown(90)
tiles.set_tilemap(tilemap("""
    level1
"""))
mySprite = sprites.create(img("""
        . . . . . . f f f f . . . . . . 
            . . . . f f f 2 2 f f f . . . . 
            . . . f f f 2 2 2 2 f f f . . . 
            . . f f f e e e e e e f f f . . 
            . . f f e 2 2 2 2 2 2 e e f . . 
            . . f e 2 f f f f f f 2 e f . . 
            . . f f f f e e e e f f f f . . 
            . f f e f b f 4 4 f b f e f f . 
            . f e e 4 1 f d d f 1 4 e e f . 
            . . f e e d d d d d d e e f . . 
            . . . f e e 4 4 4 4 e e f . . . 
            . . e 4 f 2 2 2 2 2 2 f 4 e . . 
            . . 4 d f 2 2 2 2 2 2 f d 4 . . 
            . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
            . . . . . f f f f f f . . . . . 
            . . . . . f f . . f f . . . . .
    """),
    SpriteKind.player)
mySprite2 = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.projectile)
controller.move_sprite(mySprite, 50, 50)
mySprite.set_stay_in_screen(True)

def on_update_interval():
    global projectile
    projectile = sprites.create_projectile_from_side(img("""
            ........................
                    ........................
                    ........................
                    ........................
                    ..........ffff..........
                    ........ff1111ff........
                    .......fb111111bf.......
                    .......fd1111111f.......
                    ......fdd1111111df......
                    ......fddd111111df......
                    ......fdddddd111df......
                    ......fbddddbfd1df......
                    ......fcbbbdcfddbf......
                    .......fcbb11111f.......
                    ........fffff1b1f.......
                    ........fb111cfbf.......
                    ........ffb1b1ff........
                    ......f.fffbfbf.........
                    ......ffffffff..........
                    .......fffff............
                    ........................
                    ........................
                    ........................
                    ........................
        """),
        randint(-100, 100),
        randint(-100, 100))
game.on_update_interval(1000, on_update_interval)
