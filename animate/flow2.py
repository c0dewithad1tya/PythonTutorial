from manim import *

class CPPOnlineValueChain(Scene):
    def construct(self):
        # Define colors for each participant
        colors = {
            "Customer": "#FF9999",
            "UX": "#99FF99",
            "Domain API": "#9999FF",
            "MicroValidator": "#FFFF99",
            "FTM": "#FF99FF",
            "Services": "#99FFFF"
        }

        # Create participant boxes
        customer = RoundedRectangle(corner_radius=0.5, height=1, width=2).set_fill(colors["Customer"], opacity=0.8)
        ux = RoundedRectangle(corner_radius=0.5, height=1, width=2).set_fill(colors["UX"], opacity=0.8)
        domain_api = RoundedRectangle(corner_radius=0.5, height=1, width=2).set_fill(colors["Domain API"], opacity=0.8)
        microvalidator = RoundedRectangle(corner_radius=0.5, height=1, width=2).set_fill(colors["MicroValidator"], opacity=0.8)
        ftm = RoundedRectangle(corner_radius=0.5, height=1, width=2).set_fill(colors["FTM"], opacity=0.8)

        # Position participants
        customer.to_edge(LEFT)
        ux.next_to(customer, RIGHT, buff=1.5)
        domain_api.next_to(ux, RIGHT, buff=1.5)
        microvalidator.next_to(domain_api, RIGHT, buff=1.5)
        ftm.next_to(microvalidator, RIGHT, buff=1.5)

        # Add labels
        labels = VGroup(*[Text(name, font_size=24).next_to(box, UP, buff=0.2) for name, box in zip(colors.keys(), [customer, ux, domain_api, microvalidator, ftm])])

        # Create services
        services = VGroup(*[Circle(radius=0.2, color=colors["Services"]) for _ in range(8)])
        services.arrange_in_grid(rows=2, cols=4, buff=0.5)
        services.next_to(microvalidator, DOWN, buff=1)

        # Add shadows and glow
        for box in [customer, ux, domain_api, microvalidator, ftm]:
            box.set_shadow(opacity=0.5)
            box.set_gloss(opacity=0.2)

        # Animate the value chain
        self.play(FadeIn(VGroup(customer, ux, domain_api, microvalidator, ftm, labels, services)))

        # Step 1: Customer to UX
        arrow1 = Arrow(customer.get_right(), ux.get_left(), buff=0.1, color=WHITE)
        self.play(GrowArrow(arrow1))

        # Step 2: UX to Domain API
        arrow2 = Arrow(ux.get_right(), domain_api.get_left(), buff=0.1, color=WHITE)
        self.play(GrowArrow(arrow2))

        # Step 3: Domain API to MicroValidator
        arrow3 = Arrow(domain_api.get_right(), microvalidator.get_left(), buff=0.1, color=WHITE)
        self.play(GrowArrow(arrow3))

        # Step 4: MicroValidator to Services
        arrows4 = VGroup(*[Arrow(microvalidator.get_bottom(), service.get_top(), buff=0.1, color=WHITE) for service in services])
        self.play(LaggedStart(*[GrowArrow(arrow) for arrow in arrows4], lag_ratio=0.1))

        # Step 5: MicroValidator to Domain API
        arrow5 = Arrow(microvalidator.get_left(), domain_api.get_right(), buff=0.1, color=WHITE).shift(UP * 0.2)
        self.play(GrowArrow(arrow5))

        # Step 5 (parallel): Domain API to FTM
        arrow6 = Arrow(domain_api.get_right(), ftm.get_left(), buff=0.1, color=WHITE).shift(DOWN * 0.2)
        self.play(GrowArrow(arrow6))

        # Step 6-8: FTM processes
        ftm_steps = VGroup(
            Text("1. Mapping", font_size=20),
            Text("2. Validation", font_size=20),
            Text("3. Wait for approval", font_size=20)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(ftm, DOWN, buff=0.5)

        self.play(Write(ftm_steps[0]))
        self.wait(0.5)
        self.play(Write(ftm_steps[1]))
        self.wait(0.5)
        self.play(Write(ftm_steps[2]))

        self.wait(2)
