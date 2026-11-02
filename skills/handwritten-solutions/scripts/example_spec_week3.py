# Handwritten solutions spec: 11 Methods Exam Revision Homework Week 3
# grid index -> list of parts (one list of lines per part column). \tick = one mark.
SOL = {
 0: [  # Q1 write as a^k
   [r"\sqrt[3]{7} = 7^{\frac{1}{3}} \tick"],
   [r"\sqrt{125} = \sqrt{5^3}", r"= 5^{\frac{3}{2}} \tick"],
   [r"\frac{1}{9\sqrt{3}} = \frac{1}{3^2 \times 3^{\frac{1}{2}}}", r"= \frac{1}{3^{\frac{5}{2}}} = 3^{-\frac{5}{2}} \tick"],
 ],
 1: [  # Q2 simplify / evaluate
   [r"\frac{16x^{12}}{8x^5}", r"= 2x^7 \tick"],
   [r"(\sqrt[3]{27})^2 = 3^2", r"= 9 \tick"],
   [r"\frac{1}{16^{\frac{3}{4}}} = \frac{1}{(\sqrt[4]{16})^3}", r"= \frac{1}{2^3} = \frac{1}{8} \tick"],
 ],
 2: [  # Q3 surds
   [r"\sqrt{25 \times 3} - 2\sqrt{4 \times 3}", r"= 5\sqrt{3} - 4\sqrt{3} \tick", r"= \sqrt{3} \tick"],
   [r"\frac{6}{\sqrt{3} - 1} \times \frac{(\sqrt{3} + 1)}{(\sqrt{3} + 1)}", r"= \frac{6\sqrt{3} + 6}{3 - 1} \tick", r"= 3\sqrt{3} + 3 \tick"],
 ],
 3: [  # Q4 factorise
   [r"(5^x)^2 - 5^x", r"= 5^x(5^x - 1) \tick"],
   [r"2^n \times 2^3 + 2^n", r"= 2^n(2^3 + 1) = 9(2^n) \tick"],
 ],
 4: [  # Q5 expand
   [r"(2^x + 3)(2^x + 3)", r"= 2^{2x} + 3(2^x) + 3(2^x) + 9 \tick", r"= 2^{2x} + 6(2^x) + 9 \tick"],
 ],
 5: [  # Q6 convert
   [r"150 \times \frac{\pi}{180} = \frac{5\pi}{6} \tick"],
   [r"\frac{4\pi}{5} \times \frac{180}{\pi} = 144\deg \tick"],
 ],
 6: [  # Q7 derivative: index form first, then n x coefficient x^(n-1)
   [r"f(x) = 4x^3 - 6x^{-2} + 5x^{\frac{1}{2}} \tick",
    r"f'(x) = 3 \times 4x^{3-1} - 2 \times -6x^{-2-1} + \frac{1}{2} \times 5x^{\frac{1}{2}-1}",
    r"= 12x^2 + 12x^{-3} + \frac{5}{2}x^{-\frac{1}{2}} \tick",
    r"= 12x^2 + \frac{12}{x^3} + \frac{5}{2\sqrt{x}} \tick"],
 ],
 7: [  # Q8a average rate of change
   [r"V(0) = 200 \quad V(10) = 400",
    r"ROC = \frac{V(10) - V(0)}{10 - 0} = \frac{400 - 200}{10} = 20 L/min \tick"],
 ],
 8: [  # Q8b instantaneous rate
   [r"V'(t) = 30 - 2t \tick", r"V'(10) = 30 - 2(10) = 10 L/min \tick"],
 ],
 9: [  # Q8c maximum
   [r"V'(t) = 0 \quad 30 - 2t = 0", r"t = 15 \tick", "@sign + 15 -", r"max V(15) = 200 + 30(15) - 15^2 = 425 L \tick"],
 ],
 10: [ # Q9 tangent: y = f'(a)(x - a) + f(a)
   [r"f(2) = 2^3 - 4(2) + 1 = 1",
    r"f'(x) = 3x^2 - 4 \tick",
    r"f'(2) = 3(2)^2 - 4 = 8 \tick",
    r"y = f'(a)(x - a) + f(a)",
    r"y = 8(x - 2) + 1",
    r"= 8x - 15 \tick"],
 ],
 11: [ # Q10 sector: A = 1/2 theta r^2, l = theta r
   [r"A = \frac{1}{2}\theta r^2",
    r"30 = \frac{1}{2}(1.2)r^2 \tick",
    r"r^2 = 50 \quad r = \sqrt{50} = 7.07 cm \tick",
    r"P = 2r + r\theta = 3.2\sqrt{50}",
    r"= 22.63 cm \tick"],
 ],
 12: [ # challenge
   [r"2^{30} = (2^3)^{10} = 8^{10} \quad 3^{20} = (3^2)^{10} = 9^{10}",
    r"9^{10} \gt 8^{10} so 3^{20} is larger"],
 ],
}
