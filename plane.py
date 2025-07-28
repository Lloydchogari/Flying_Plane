import turtle
import time
import random

# --- Setup Screen ---
win = turtle.Screen()
win.title("Aviator Game - Realistic Drawn Plane")
win.bgcolor("black")
win.setup(width=1000, height=600)
win.tracer(0)

# --- Draw a more realistic airplane shape ---
def create_realistic_plane():
    drawer = turtle.Turtle()
    drawer.hideturtle()
    drawer.penup()
    drawer.goto(0, 0)
    drawer.begin_poly()

    # Fuselage (main body)
    drawer.goto(-40, 0)
    drawer.pendown()
    drawer.goto(40, 0)      # nose tip/pointer
    drawer.goto(35, 5)
    drawer.goto(-35, 5)     # top body
    drawer.goto(-40, 0)

    # Cockpit
    drawer.penup()
    drawer.goto(20, 5)
    drawer.pendown()
    drawer.goto(15, 12)
    drawer.goto(10, 5)

    # Tail fin
    drawer.penup()
    drawer.goto(-35, 5)
    drawer.pendown()
    drawer.goto(-40, 20)
    drawer.goto(-30, 5)

    # Wings (center)
    drawer.penup()
    drawer.goto(-5, 0)
    drawer.pendown()
    drawer.goto(-25, -15)
    drawer.goto(-15, 0)
    drawer.goto(-5, 0)

    # Rear wing
    drawer.penup()
    drawer.goto(-30, 0)
    drawer.pendown()
    drawer.goto(-45, -8)
    drawer.goto(-25, 0)

    drawer.end_poly()

    # Register shape
    turtle.register_shape("detailed_plane", drawer.get_poly())

create_realistic_plane()

# --- Plane Setup ---
plane = turtle.Turtle()
plane.shape("detailed_plane")
plane.color("white")
plane.penup()
plane.goto(-350, 0)
plane.setheading(95)

# --- Multiplier Display ---
multiplier_text = turtle.Turtle()
multiplier_text.hideturtle()
multiplier_text.penup()
multiplier_text.goto(0, 250)
multiplier_text.color("white")

# --- Game Variables ---
multiplier = 1.00
crash_time = random.uniform(5.0, 15.0)
start_time = time.time()
cashed_out = False
bet = 10.00

# --- Stars Background ---
stars = []

def create_star():
    star = turtle.Turtle()
    star.hideturtle()
    star.shape("circle")
    star.color("white")
    star.penup()
    star.goto(random.randint(-500, 500), random.randint(-250, 250))
    star.shapesize(random.choice([0.1, 0.15, 0.2]))
    stars.append(star)

for _ in range(40):
    create_star()

# --- Cash Out Logic ---
def cash_out():
    global cashed_out
    if not cashed_out:
        earnings = round(bet * multiplier, 2)
        print(f"✅ You cashed out at {multiplier:.2f}x and won ${earnings}!")
        cashed_out = True
        turtle.bye()

win.listen()
win.onkey(cash_out, "space")

# --- Main Game Loop ---
def update():
    global multiplier, cashed_out
    elapsed = time.time() - start_time

    if elapsed >= crash_time:
        if not cashed_out:
            print(f"💥 Plane crashed at {multiplier:.2f}x! You lost your bet of ${bet}.")
        turtle.bye()
        return

    if not cashed_out:
        # Update multiplier
        multiplier += 0.03 + (multiplier * 0.001)

        # Scroll stars left
        for star in stars:
            x, y = star.pos()
            star.goto(x - 5, y)
            if x < -520:
                star.goto(520, random.randint(-250, 250))
            star.showturtle()

        # Display multiplier
        multiplier_text.clear()
        multiplier_text.write(f"Multiplier: {multiplier:.2f}x", align="center", font=("Arial", 24, "bold"))

        win.update()
        win.ontimer(update, 50)

# --- Start Game ---
update()
win.mainloop()
