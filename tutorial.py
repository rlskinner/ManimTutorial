from manim import *

class axes(Scene):
    def construct(self):
        axs = Axes(x_range=(-1, 10), y_range=(-1, 10), x_length=13, y_length=5, tips=False).add_coordinates().set_color(BLUE)
        x = axs.get_x_axis_label("XX")
        y = axs.get_y_axis_label("YY")
        self.play(Write(axs), Write(x), Write(y))

        self.wait(3)



class axes1(Scene):
    def construct(self):
        axes = Axes(x_range=(-20, 20), y_range=(-15, 15))
        tri = Triangle().scale(0.3)
        tri.move_to(axes.c2p(-7, 10))

        self.play(Write(axes))
        self.play(Write(tri))
        self.wait()

        dot = Dot(color=RED)
        self.play(Create(dot))
        self.play(dot.animate.move_to(axes.c2p(7, -10)))

        self.wait(5)






class ValueCheckers(Scene):
    def construct(self):
        t1 = ValueTracker(10)

        number = always_redraw(lambda: DecimalNumber(t1.get_value(), num_decimal_places=0))

        self.play(Write(number))
        self.play(t1.animate.set_value(30), run_time=5)
        self.wait(5)


        








class textAndArrays(Scene):
    def construct(self):
        t = Tex("Hello ", "there ", "d", "o", "g")
        t[2].color = RED
        t[3].color = ORANGE
        t[4].color = YELLOW

        self.play(Write(t[2:5]))
        self.play(Write(t[0:2]))
        
        self.play(t[0].animate.to_edge(UL, buff=1), t[1].animate.to_edge(UR, buff=1))

        self.play(t[2].animate.move_to([0, 2, 0]), t[3].animate.move_to([0, 0, 0]), t[4].animate.move_to([0, -2, 0]))

        r = Rectangle(height=1, width=1).move_to(t[2].get_center())
        c = Circle(radius=0.5).move_to(t[3].get_center())
        p = RegularPolygon(5).move_to(t[4].get_center()).scale(0.5)
        self.play(SpinInFromNothing(r), Write(c), SpinInFromNothing(p))

        rcp = VGroup(r, c, p)
        self.play(Rotate(rcp, 3*PI))

        tp = VGroup(t[2], p)
        tr = VGroup(t[4], r)
        self.play(Swap(tr, tp))
        
        grp = VGroup(t, rcp)
        # internal error if I use Text() ???
        b = Tex("Bye")
        self.play(Transform(grp, b))

        self.wait(5)


class demo(Scene):
    def construct(self):
        c = Circle(radius=0.5, stroke_width=10, fill_opacity=0.3, color=RED)
        r = SurroundingRectangle(c, color=BLUE, corner_radius=0.1)
        t = Text("Manim").next_to(r, UP, buff=0.5)

        self.play(Write(NumberPlane()))
        
        self.play(Write(c), DrawBorderThenFill(r), Write(t))
        
        cr = VGroup(c, r)
        
        self.play(t.animate.move_to([-4, 0, 0]), cr.animate.move_to([4, 0, 0]))
        
        a = always_redraw(lambda: Line(start=cr.get_left(), end=t.get_right(), buff=0.4).add_tip(tip_shape=StealthTip).add_tip(tip_shape=StealthTip, at_start=True))
        self.play(Write(a))

        self.play(Indicate(t, 1.5, color=ORANGE))
        self.play(Rotate(r, angle=PI/2), ScaleInPlace(c, 2.0))
        self.play(cr.animate.move_to([0, 0, 0]))

        self.play(FadeOut(a), FadeOut(t), run_time=.25)
        self.play(ShrinkToCenter(r), ScaleInPlace(c, 30))
        self.play(FadeOut(c))

        self.wait(5)