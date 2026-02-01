import turtle
import math
import random
import platform
if platform.system() == "Windows":
	import winsound
t = turtle.Turtle()
t.hideturtle()
VGA_COLORS = [(0,0,0), (0,0,170), (0,170,0), (0,170,170), (170,0,0), (170,0,170), (170,85,0), (170,170,170), (85,85,85), (85,85,255), (85,255,85), (85,255,255), (255,85,85), (255,85,255), (255,255,85)]
turtle.colormode(255)
turtle.bgcolor(255, 255, 255)

# ------ [TR] ------
tr_x = 0
tr_y = 0
def tr_up(): global tr_y; tr_y += 1
def tr_down(): global tr_y; tr_y -= 1
def tr_left(): global tr_x; tr_x -= 1
def tr_right(): global tr_x; tr_x += 1
def tr_reset():
	global tr_z; tr_z = 0
turtle.onkeypress(tr_up, "Up")
turtle.onkeypress(tr_down, "Down")
turtle.onkeypress(tr_left, "Left")
turtle.onkeypress(tr_right, "Right")
turtle.onkeypress(tr_reset, "c")
turtle.onkeypress(tr_reset, "C")

# camera (isometric (30deg))
def proj(x, y, z, cx=0, cy=0, cz=0):
	global scl, xangl, zangl
	x -= cx
	y -= cy
	z -= cz
	# isometric (xangl = 30deg, zangl = 45deg)
	x_rot = x*math.cos(math.radians(zangl))-y*math.sin(math.radians(zangl)) # rotation z axis
	y_rot = x*math.sin(math.radians(zangl))+y*math.cos(math.radians(zangl))
	screen_x = x_rot * scl 					  # depth
	screen_y = (z*math.cos(math.radians(xangl)) - y_rot*math.sin(math.radians(xangl))) * scl
	return screen_x, screen_y

def get_color(c_mode, i, steps):
	gradient = i/steps
	if c_mode == 1: # VGA 15
		return VGA_COLORS[(i//10)%15]
	elif c_mode == 2: # Red-Blue
		r = int(255*(1-gradient))
		g = 0
		b = int(255*gradient)
		return (r, g, b)
	elif c_mode == 3: # Orange-Purple
		r = int(255+(128-255)*gradient)
		g = int(165*(1-gradient))
		b = int(128*gradient)
		return (r, g, b)
	elif c_mode == 4: # Oscilloscope Green
		return (118, 185, 0)
	return (197, 18, 31) # VGA red if broken r

# libraries & safe input
safe_math = {name: getattr(math, name) for name in dir(math) if not name.startswith("_")}
safe_math["pi"] = math.pi
safe_math["e"] = math.e
def make_param_func(expr):
	code_obj = compile(expr, '<string>', 'eval')
	return lambda t, T=0: eval(code_obj, {"__builtins__": {}}, {**safe_math, "t": t, "T": T})

# plot "loop"
def plotparam3d(expr_x, expr_y, expr_z, t_min, t_max, c_mode, steps):
	fx = make_param_func(expr_x)
	fy = make_param_func(expr_y)
	fz = make_param_func(expr_z)
	t.pensize(3)
	t.penup()
	
	for i in range(steps+1):
		t_now = t_min + (t_max - t_min) * i / steps
		color_index = (i // 10) % 15
		t.pencolor(get_color(c_mode, i, steps))
		raw_x = fx(t_now)
		raw_y = fy(t_now)	# <-- 3D coords
		raw_z = fz(t_now)
		screen_x, screen_y = proj(raw_x, raw_y, raw_z) # project to 2D
		if i % 300 == 0:
			freq = int(400 + (raw_z * 100))
			if platform.system() == "Windows":
				winsound.Beep(max(37, freq), 10)
		t.goto(screen_x, screen_y)
		t.pendown()
	turtle.update()

def oscilloscope(cx, cy, cz, t_min, t_max, time_offset, c_mode, steps=200):
	fx = lambda t_val: eval(cx, {"__builtins__": {}}, {**safe_math, "t": t_val, "T": time_offset})
	fy = lambda t_val: eval(cy, {"__builtins__": {}}, {**safe_math, "t": t_val, "T": time_offset})
	fz = lambda t_val: eval(cz, {"__builtins__": {}}, {**safe_math, "t": t_val, "T": time_offset})
	turtle.bgcolor(0, 0, 0)
	t.pensize(4)
	t.penup()
	for i in range(steps+1):
		t_now = t_min + (t_max - t_min)*i /steps
		t.pencolor(get_color(c_mode, i, steps))
		try:
			raw_x = fx(t_now)
			raw_y = fy(t_now)
			raw_z = fz(t_now)
			screen_x, screen_y = proj(raw_x, raw_y, raw_z)
			t.goto(screen_x, screen_y)
			t.pendown()
		except:
			t.penup()
	turtle.update()



# inputs & presets
print("o-----------------------------------------------------o")
print("|       [ I J K   P A R A M E T E R   P L O T ]       |")
print("o-----------------------------------------------------o")
print("                  [ A P P E N D I X ]")
print("           - for the presets: basic programs are on")
print("             the left, preset parametrics")
print("             are on the right")
print("           - camera is locked at (0, 0, 0) * scale")
print("eyes(x,z):   moves the perspective up (-x)")
print("             or sideways (z)")
print("x,y,z(t):    parameteric equations")
print("t(min, max): domain of all parameters,")
print("             lower for performance")
print("scale:       zoom in (+) or out (-), standard = 100")
print("spin:        rotates the camera around the center")
print("             at a certain speed with a ratio")
print("             of 2x / z (causes the rotation")
print("                        not to repeat itself)")
print("o-----------------------------------------------------o")
print("                 to plot yourself -> N")
print("                   [ P R E S E T S ]")
print("  [OC] Oscilloscope      [SR] SpinningRose")
print("  [OS] OrbitalSimulator  [FB] FlyingButterfly")
print("  [IC] InfiniteCanvas    [CP] CircularPolarizer")
print("  [SG] Spirograph        [TD] TumblingDonut")
preset = input("preset (<ACRONYM> / N): ").upper()
if preset == "SR":
	print("o-----------------------------------------------------o")
	print("eyes(x) = 30")
	print("eyes(z) = 45")
	print("x(t) = sin(2t)cos(t)")
	print("y(t) = sin(2t)sin(t)")
	print("z(t) = t/5")
	print("t(min) = -20")
	print("t(max) = 20")
	print("scale = 160")
	print("spin: Y")
	xangl = 30.0
	zangl = 45.0
	ex = "sin(2*t)*cos(t)"
	ey = "sin(2*t)*sin(t)"
	ez = "t/5"
	etmin = -20.0
	etmax = 20.0
	scl = 160.0
	spin_yn = "Y"
	spinv = 2
elif preset == "IC":
	print("o-----------------------------------------------------o")
	print("       Infinite Canvas")
	print("o-----------------------------------------------------o")
	print("[arrow keys] to move, [C] to return to z = 0")
	trvelocity = abs(float(input("speed (small value recommended): ")))
	xangl = -30.0
	zangl = 45.0
	scl = 20.0
	spin_yn = "N"
elif preset == "SG":
	print("o-----------------------------------------------------o")
	print("[H] Hypotrochoids (circle in a circle)")
	print("[P] Polygons (superformulated)")
	print("[R] Rhodonea Curves")
	graphchoice = input("spirochoice (<ACRONYM>): ")
	xangl = -90.0
	zangl = 0.0
	if graphchoice == "H":
		R = float(input("(R) large radius: "))
		r = float(input("(r) small radius: "))
		d = float(input("(d) offset: "))
		ex = f"({R}-{r})*cos(t) + {d}*cos(({R}-{r})*t/{r})"
		ey = f"({R}-{r})*sin(t) - {d}*sin(({R}-{r})*t/{r})"
		ez = input("z(t) ('0' to ignore): ")
		etmin = 0.0
		etmax = 20*math.pi
	elif graphchoice == "P":
		n = float(input("(n) sides: "))
		ex = f"(1/cos((2*asin(sin({n}*t/2)))/{n}))*cos(t)"
		ey = f"(1/cos((2*asin(sin({n}*t/2)))/{n}))*sin(t)"
		ez = input("z(t) ('0' to ignore): ")
		etmin = 0.0
		etmax = 2*math.pi
	elif graphchoice == "R":
		k = float(input("(k) petal constant: "))
		ex = f"cos({k}*t)*cos(t)"
		ey = f"cos({k}*t)*sin(t)"
		ez = input("z(t) ('0' to ignore): ")
		etmin = 0.0
		etmax = 2*math.pi
	else:
		print("InputError")
		ex, ey, ez = "t", "(sin(t))**2", "cos(t)"
		etmin, etmax = -6, 6
	scl = float(input("scale: "))
	spin_yn = input("spin (Y/N): ").upper()
	if spin_yn == "Y":
		spinv = float(input("o--o speed = "))

elif preset == "OS":
	print("o-----------------------------------------------------o")
	print("        QuantumClouds")
	print("o-----------------------------------------------------o")
	qn = int(input("principal (n) [1, 2, ..., 6]: "))
	ql = int(input("azimuthal (l) [0 -> n-1]: "))
	qm = int(input("magnetic (m) [-l -> l]: "))
	if not (qn > 0):
		print("domain error: n > 0")
	elif not (0 <= ql < qn):
		print("domain error: l = [0, n-1]")
	elif not (-ql <= qm <= ql):
		print("domain error: m = [-l, l]")
	else:
		nodes = qn - ql
		xangl = -90
		zangl = 0
		if ql == 0: # S-orbital like ((()))
			ex = f"(cos({nodes}*t))*cos(t)"
			ey = f"(cos({nodes}*t))*sin(t)"
			ez = f"sin({nodes}*t)"
		else: # P, D, F orbitals like angular nodes
			ex = f"cos({ql}*t)*cos({nodes}*t)*cos(t)"
			ey = f"cos({ql}*t)*cos({nodes}*t)*sin(t)"
			ez = f"sin({ql}*t + {qm})"
		# nucleus
		etmin = 0.0
		etmax = 2*math.pi
		scl = 240.0
		spin_yn = "N"
		print("o-----------------------------------------------------o")
		print(f"{qn}{'spdfgh'[ql]}")
elif preset == "OC":
	print("o-----------------------------------------------------o")
	print("            OscCRT")
	print("o-----------------------------------------------------o")
	A = float(input("amplitude (A): "))
	w = float(input("angular freq (ω): "))
	p = float(input("phase shift (φ): "))
	freq_f = w / (2*math.pi)
	wavelength = (2*math.pi) / w
	velocity = freq_f * wavelength
	xangl = -90
	zangl = 0
	ex = "t"
	ey = f"{A}*sin({w}*t + {p} + T)"
	ez = "0"
	etmin = -10
	etmax = 10
	scl = 60.0
	spin_yn = "N"
	print("o-----------------------------------------------------o")
	print(f"    {A}sin({w}t + {p})")
	print(f"(f) frequency:         {freq_f:.2f} Hz")
	print(f"(λ) wavelength:        {wavelength:.2f}")
	print(f"(ω) angular frequency: {w:.2f} rad/s")
	print(f"(v) velocity:          {velocity:.2f}")

elif preset == "FB":
	print("o-----------------------------------------------------o")
	print("eyes(x) = 30")
	print("eyes(z) = 45")
	print("x(t) = sin(t)(e^cos(t) - 2cos(4t) - sin(t/12)^5)")
	print("y(t) = cos(t)(e^cos(t) - 2cos(4t) - sin(t/12)^5)")
	print("z(t) = t/10")
	print("t(min) = 0")
	print("t(max) = 12pi")
	print("scale = 100")
	print("spin: Y")
	xangl = 30.0
	zangl = 45.0
	ex = "sin(t) * (e**cos(t) - 2*cos(4*t) - sin(t/12)**5)"
	ey = "cos(t) * (e**cos(t) - 2*cos(4*t) - sin(t/12)**5)"
	ez = "t/10"
	etmin = 0.0
	etmax = 37.7
	scl = 100.0
	spin_yn = "Y"
	spinv = 1.5
elif preset == "CP":
	print("o-----------------------------------------------------o")
	print("eyes(x) = 0")
	print("eyes(z) = 90")
	print("x(t) = t")
	print("y(t) = Acos(wt)")
	print("z(t) = Asin(wt)")
	print("t(min) = -20")
	print("t(max) = 20")
	print("scale = 60")
	print("spin: Y")
	xangl = 0.0
	zangl = 90.0
	ex = "t"
	ey = "cos(t)"
	ez = "sin(t)"
	etmin = -20.0
	etmax = 20.0
	scl = 60.0
	spin_yn = "Y"
	spinv = 1.5
elif preset == "TD":
	print("o-----------------------------------------------------o")
	print("eyes(x) = 30")
	print("eyes(z) = 45")
	print("x(t) = (3 + cos(18t))(cos(t))")
	print("y(t) = (3 + cos(18t))(sin(t))")
	print("z(t) = sin(18t)")
	print("t(min) = 0")
	print("t(max) = 2pi")
	print("scale = 100")
	print("spin: Y")
	xangl = 30.0
	zangl = 45.0
	ex = "(2+cos(18*t))*cos(t)"
	ey = "(2+cos(18*t))*sin(t)"
	ez = "sin(18*t)"
	etmin = 0.0
	etmax = 2*math.pi
	scl = 100.0
	spin_yn = "Y"
	spinv = 4
else:
	print("o-----------------------------------------------------o")
	print("                  ParametricEquations")
	print("o-----------------------------------------------------o")
	xangl = float(input("eyes(x) = "))
	zangl = float(input("eyes(z) = "))
	ex = input("x(t) = ")
	ey = input("y(t) = ")
	ez = input("z(t) = ")
	etmin = float(input("t(min) = "))
	etmax = float(input("t(max) = "))
	scl = float(input("scale = "))
	spin_yn = input("spin (Y/N): ").upper()
	if spin_yn == "Y":
		spinv = float(input("o--o speed = "))

print("o-----------------------------------------------------o")
print("                    [ C O L O R S ]")
print("  [1] VGA 15")
print("  [2] Red -> Blue")
print("  [3] Orange -> Purple")
print("  [4] OsciGreen")
print("  [5] SimpleRed")
c_mode = int(input("color (1 / 2 / 3 / 4): "))
print("o-----------------------------------------------------o")

# axes kkkkkkkkkk
turtle.pencolor(0, 55, 218)
turtle.tracer(0, 0)
t.pencolor(0, 55, 218)
t.penup(); t.goto(*proj(-6, 0, 0)); t.pendown(); t.goto(*proj(6, 0, 0))
t.penup(); t.goto(*proj(0, -6, 0)); t.pendown(); t.goto(*proj(0, 6, 0))
t.penup(); t.goto(*proj(0, 0, -6)); t.pendown(); t.goto(*proj(0, 0, 6))
t.penup()

if preset == "OC":
	import time
	time_offset = 0
	cx = compile(ex, '<string>', 'eval')
	cy = compile(ey, '<string>', 'eval')
	cz = compile(ez, '<string>', 'eval')
	while True:
		t.clear()
		t.pencolor(30, 30, 30)
		t.penup(); t.goto(*proj(-10, 0, 0)); t.pendown(); t.goto(*proj(10, 0, 0))
		t.penup(); t.goto(*proj(0, -10, 0)); t.pendown(); t.goto(*proj(0, 10, 0))
		oscilloscope(cx, cy, cz, etmin, etmax, time_offset, c_mode)
		time_offset -= 0.2
		turtle.update()
		time.sleep(0.01)
elif preset == "IC":
	import time
	turtle.listen()
	tr_x, tr_y, tr_z = 0, 0, 0
	prev_x, prev_y, prev_z = 0, 0, 0
	t.pensize(3)
	t.speed(0)
	while True:
		tr_z += 0.01*trvelocity
		t.pencolor(get_color(c_mode, int(tr_z*3)%200, 200))
		t.penup()
		t.goto(*proj(prev_x, prev_y, prev_z, 0, 0, 0))
		t.pendown()
		t.goto(*proj(tr_x, tr_y, tr_z, 0, 0, 0))
		prev_x, prev_y, prev_z = tr_x, tr_y, tr_z
		t.dot(5)
		turtle.update()
		time.sleep(0.01)

elif spin_yn == "Y":
	import time
	steps = 350
	while True:
		t.clear()
		zangl += 1*spinv
		xangl += 0.5*spinv
		t.pencolor(0, 55, 218)
		t.penup(); t.goto(*proj(-6, 0, 0)); t.pendown(); t.goto(*proj(6, 0, 0))
		t.penup(); t.goto(*proj(0, -6, 0)); t.pendown(); t.goto(*proj(0, 6, 0))
		t.penup(); t.goto(*proj(0, 0, -6)); t.pendown(); t.goto(*proj(0, 0, 6))
		plotparam3d(ex, ey, ez, etmin, etmax, c_mode, steps)
		turtle.update()
		time.sleep(0.01)
else:
	t.clear()
	steps = 1000
	t.pencolor(0, 55, 218)
	t.penup(); t.goto(*proj(-6, 0, 0)); t.pendown(); t.goto(*proj(6, 0, 0))
	t.penup(); t.goto(*proj(0, -6, 0)); t.pendown(); t.goto(*proj(0, 6, 0))
	t.penup(); t.goto(*proj(0, 0, -6)); t.pendown(); t.goto(*proj(0, 0, 6))
	plotparam3d(ex, ey, ez, etmin, etmax, c_mode, steps)
	turtle.update()
	turtle.done()
