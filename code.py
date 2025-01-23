import os
import google.generativeai as genai

genai.configure(api_key=["AIzaSyAooNcS_-7pgX0JbX4rAc3p1pr5ryHJUOQ"])

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash-exp",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "Teach me a lesson on quadratic equations. Assume I know absolutely nothing about it.",
      ],
    },
    {
      "role": "model",
      "parts": [
        "## Quadratic Equations: A Beginner&#39;s Guide\n\nImagine you&#39;re throwing a ball up in the air. It goes up, reaches a peak, and then falls back down. The path it takes can be described by a **quadratic equation**. Let&#39;s explore what that means:\n\n**1. What is a Quadratic Equation?**\n\nIt&#39;s an equation that looks like this: **ax² + bx + c = 0**. Don&#39;t be intimidated by the symbols! Let&#39;s break it down:\n\n* **x**: This represents an unknown value, like the time it takes for the ball to reach the ground.\n* **a, b, c**: These are numbers, like the initial speed of the ball, its starting height, and the effect of gravity.\n* **²**: This means &quot;squared,&quot; or multiplied by itself. For example, x² is the same as x times x.\n\n**2. Why are they called &quot;Quadratic&quot;?**\n\nThe word &quot;quadratic&quot; comes from &quot;quad,&quot; which means &quot;square.&quot; The highest power of x in the equation is 2, hence the name.\n\n**3. What do they tell us?**\n\nQuadratic equations help us solve problems where things change in a non-linear way, like the ball&#39;s trajectory. Solving the equation means finding the values of x that make the equation true. These values are called **roots** or **solutions**.\n\n**4. How do we solve them?**\n\nThere are different ways to solve quadratic equations:\n\n* **Factoring**: This involves rewriting the equation as a product of two simpler expressions.\n* **Quadratic Formula**: This is a powerful formula that can solve any quadratic equation. It looks scary, but it&#39;s just a recipe for finding the roots.\n* **Graphing**: You can plot the equation on a graph and see where it crosses the x-axis. Those points are the solutions.\n\n**5. Why are they important?**\n\nQuadratic equations have applications in various fields:\n\n* **Physics**: Calculating the motion of objects, like our ball example.\n* **Engineering**: Designing bridges, buildings, and other structures.\n* **Finance**: Predicting market trends and making investment decisions.\n* **Computer Science**: Used in algorithms and computer graphics.\n\n**6. Let&#39;s see an example:**\n\nImagine the equation describing the ball&#39;s height is: **h = -5t² + 20t + 10**. Here, h is the height and t is the time. Solving this equation will tell us when the ball hits the ground (h = 0). We can use the quadratic formula or graph the equation to find the solutions.\n\nThis is just a basic introduction to quadratic equations. There&#39;s much more to learn, but hopefully, this gives you a starting point to explore further!\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "Give me an equation to solve and test my knowledge, Don't give answers just yet. ",
      ],
    },
    {
      "role": "model",
      "parts": [
        "**Solve the following quadratic equation:**\n\n**x² - 5x + 6 = 0**\n\nRemember, the solutions are the values of x that make the equation true. You can use any method you like, such as factoring, the quadratic formula, or graphing. Good luck! \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "x=0 and x=10",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Unfortunately, x = 0 and x = 10 are not solutions to the equation x² - 5x + 6 = 0. \n\nLet&#39;s check:\n\n* For x = 0: (0)² - 5(0) + 6 = 6 ≠ 0\n* For x = 10: (10)² - 5(10) + 6 = 56 ≠ 0\n\nAs you can see, neither value makes the equation true. \n\nTry using another method like factoring or the quadratic formula to find the correct solutions. \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "Provide a detailed method to solve it",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Okay, let's break down how to solve the quadratic equation **x² - 5x + 6 = 0** in detail, using two common methods:\n\n**Method 1: Factoring**\n\n1. **Understanding Factoring:** Factoring involves rewriting the quadratic expression as a product of two linear expressions (expressions with 'x' to the power of 1). We are looking for two numbers that:\n    * Multiply to give the constant term (c), which is 6 in this case.\n    * Add to give the coefficient of the 'x' term (b), which is -5 in this case.\n\n2. **Finding the Numbers:**\n    * Let's think of pairs of numbers that multiply to 6:\n        * 1 and 6\n        * 2 and 3\n        * -1 and -6\n        * -2 and -3\n    * Out of these, the pair -2 and -3 adds up to -5.\n\n3. **Rewriting the Equation:** We can now rewrite the equation like this:\n    (x - 2)(x - 3) = 0\n    * Notice how if you were to expand this, you'd get back to x² - 5x + 6.\n\n4. **Solving for x:** For the product of two terms to equal zero, at least one of the terms *must* be zero.  So we have two possibilities:\n    * x - 2 = 0  \n    * x - 3 = 0\n\n5. **Finding the Solutions:**\n    * Solving x - 2 = 0, we get x = 2\n    * Solving x - 3 = 0, we get x = 3\n\n**Therefore, the solutions to the equation x² - 5x + 6 = 0 are x = 2 and x = 3.**\n\n**Method 2: Quadratic Formula**\n\n1. **The Quadratic Formula:** The quadratic formula is a general formula that can solve *any* quadratic equation in the form ax² + bx + c = 0. It is given by:\n   x = (-b ± √(b² - 4ac)) / 2a\n\n2. **Identifying a, b, and c:** In our equation, x² - 5x + 6 = 0:\n   * a = 1 (the coefficient of x²)\n   * b = -5 (the coefficient of x)\n   * c = 6 (the constant term)\n\n3. **Plugging the Values into the Formula:** Substituting these values into the formula, we get:\n   x = (-(-5) ± √((-5)² - 4 * 1 * 6)) / (2 * 1)\n\n4. **Simplifying:** Let's simplify the expression step-by-step:\n   * x = (5 ± √(25 - 24)) / 2\n   * x = (5 ± √1) / 2\n   * x = (5 ± 1) / 2\n\n5. **Finding the Two Solutions:** Now we have two possibilities, one with '+' and the other with '-':\n   * x = (5 + 1) / 2 = 6 / 2 = 3\n   * x = (5 - 1) / 2 = 4 / 2 = 2\n\n**Again, we find that the solutions to the equation x² - 5x + 6 = 0 are x = 2 and x = 3.**\n\n**Key Takeaways:**\n\n* Both factoring and the quadratic formula are valid ways to solve quadratic equations.\n* Factoring works best when the solutions are whole numbers or simple fractions.\n* The quadratic formula is more versatile and can solve any quadratic equation, even if the solutions are irrational or complex numbers.\n* Always double-check your answers by plugging them back into the original equation to make sure they satisfy it.\n\nI hope this detailed explanation helps! Feel free to ask if you have any more questions.\n",
      ],
    },
  ]
)

response = chat_session.send_message("INSERT_INPUT_HERE")

print(response.text)RE")

print(response.text)
