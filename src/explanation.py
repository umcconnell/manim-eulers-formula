from manim import *
from typing import List, Tuple, Union

from .config import BACKGROUND_COLOR, TEXT_COLOR

config.background_color = BACKGROUND_COLOR


class Explanation(Scene):
    def construct(self):
        exp_sigma = MathTex(
            r"e^{x} = \sum_{k=0}^{\infty} \frac{x^k}{k!}", color=TEXT_COLOR)
        self.play(Write(exp_sigma))
        self.wait(2)

        exp_sum, exp_sum_substituted = self.substitute_exp_sum(
            exp_sigma=exp_sigma)
        self.wait()

        exp_sum_expanded = self.expand_exp_sum_substituted(
            exp_sum=exp_sum, exp_sum_substituted=exp_sum_substituted)
        self.wait()

        real_part, imag_part = self.extract_real_imag_parts(
            ref_sum=exp_sum_expanded,
            real_part_idxs=[1, slice(5, 7), slice(9, 11)],
            imag_part_idxs=[slice(3, 5), slice(7, 9)]
        )
        self.wait(3)

        self.play(FadeOut(exp_sum, exp_sum_expanded,
                  real_part, imag_part, shift=DOWN))
        self.wait()

        self.show_eulers_identity()
        self.wait(2)

    def substitute_exp_sum(self, exp_sigma: Mobject) -> Tuple[Mobject, Mobject]:
        exp_sum = [
            r"1 +", r"x", r"+ {", r"x", "^2 \over 2}", r" + {", r"x",
            r"^3 \over 6}", r" + {", r"x", r"^4 \over 24} + \dots"
        ]
        exp_sum_substituted = [el.replace("x", "(i t \pi)") for el in exp_sum]
        exp_sum_substituted[0] = r"z = " + exp_sum_substituted[0]

        exp_sum = MathTex(
            *exp_sum, color=TEXT_COLOR).next_to(exp_sigma, 2*DOWN)
        exp_sum_substituted = MathTex(*exp_sum_substituted, color=TEXT_COLOR)

        self.play(Write(exp_sum))
        self.wait(2)

        self.play(FadeOut(exp_sigma, shift=UP), exp_sum.animate.to_edge(UP))

        return exp_sum, exp_sum_substituted

    def expand_exp_sum_substituted(self, exp_sum: Mobject, exp_sum_substituted: Mobject) -> Mobject:
        exp_sum_copy = exp_sum.copy()
        self.play(exp_sum_copy.animate.shift(2*DOWN))
        self.wait()

        exp_sum_copy.set_color_by_tex("x", ORANGE)
        self.wait()

        exp_sum_substituted.set_color_by_tex("(i t \pi)", ORANGE)
        exp_sum_substituted.align_to(exp_sum_copy, UP)
        self.play(TransformMatchingTex(
            exp_sum_copy, exp_sum_substituted, run_time=2))
        self.wait()

        exp_sum_substituted_expanded = MathTex(*[
            r"z = 1 +", r"i", r"~t \pi + ", r"i^2", r"~{", r"(t \pi)^2", r" \over 2} + ",
            r"i^3", r"~{", r"(t \pi)^3", r" \over 6} + ", r"i^4", r"~{", r"(t \pi)^4",
            r" \over 24} + \dots"
        ], color=TEXT_COLOR).align_to(exp_sum_substituted, UP)

        self.play(TransformMatchingShapes(
            exp_sum_substituted, exp_sum_substituted_expanded))
        self.wait()

        for i in [1, 3, 7, 11]:
            exp_sum_substituted_expanded[i].set_color(ORANGE)

        self.wait(2)

        exp_sum_substituted_expanded2 = MathTex(*[
            r"z = ", r"1", r" + ", r"i", r"~t \pi", r"-", r" { (t \pi)^2 \over 2}",
            r" - i", r"~{ (t \pi)^3 \over 6}", r" + ", r"{ (t \pi)^4 \over 24}", r" + \dots"
        ], color=TEXT_COLOR).align_to(exp_sum_substituted, UP)

        exp_sum_color_idxs = [3, 5, 7, 9]

        for i in exp_sum_color_idxs:
            exp_sum_substituted_expanded2[i].set_color(ORANGE)

        self.play(TransformMatchingShapes(
            exp_sum_substituted_expanded, exp_sum_substituted_expanded2))
        self.wait(2)

        for i in exp_sum_color_idxs:
            exp_sum_substituted_expanded2[i].set_color(TEXT_COLOR)

        return exp_sum_substituted_expanded2

    def extract_real_imag_parts(self, ref_sum: Mobject,
                                real_part_idxs: List[Union[int, slice]],
                                imag_part_idxs: List[Union[int, slice]]
                                ) -> Tuple[Mobject, Mobject]:
        frameboxes_real = [
            SurroundingRectangle(ref_sum[i], buff=0.2, color=ORANGE)
            for i in real_part_idxs
        ]
        frameboxes_imag = [
            SurroundingRectangle(ref_sum[i], buff=0.2, color=ORANGE)
            for i in imag_part_idxs
        ]

        # Real Part
        real_part = VGroup(
            MathTex(r"\cos(t \pi) =", color=TEXT_COLOR),
            MathTex(r"\mathfrak{Re}(z) = ", color=TEXT_COLOR),
            MathTex(
                r"1 - { (t \pi)^2 \over 2 } + { (t \pi)^4 \over 24} - \dots", color=TEXT_COLOR)
        ).arrange(RIGHT).next_to(ref_sum, 2.5*DOWN)

        self.play(LaggedStart(*[Create(box)
                  for box in frameboxes_real], lag_ratio=0.2))
        self.play(Write(real_part[1:]))
        self.wait()
        self.remove(*frameboxes_real)

        # Imag Part
        imag_part = VGroup(
            MathTex(r"\sin(t \pi) =", color=TEXT_COLOR),
            MathTex(r"\mathfrak{Im}(z) = ", color=TEXT_COLOR),
            MathTex(r"t \pi - { (t \pi)^3 \over 6 } + \dots", color=TEXT_COLOR)
        ).arrange(RIGHT).align_to(real_part, LEFT + UP).shift(1.5*DOWN)

        self.play(LaggedStart(*[Create(box)
                  for box in frameboxes_imag], lag_ratio=0.2))
        self.play(Write(imag_part[1:]))
        self.wait()
        self.remove(*frameboxes_imag)

        self.play(Write(real_part[0]))
        self.play(Write(imag_part[0]))

        return real_part, imag_part

    def show_eulers_identity(self):
        eulers_identity = MathTex(
            r"e^{i t \pi} = \cos(t \pi) + i \sin(t \pi)", color=TEXT_COLOR)

        self.play(Write(eulers_identity))
        self.wait()

        eulers_identity_text = Text(
            "Euler's formula", color=TEXT_COLOR).next_to(eulers_identity, 3*UP)
        eulers_identity_box = SurroundingRectangle(
            eulers_identity, buff=0.3, color=ORANGE)
        self.play(Create(eulers_identity_box))
        self.wait()
        self.play(Write(eulers_identity_text))
