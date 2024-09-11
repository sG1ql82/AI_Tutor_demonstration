import pickle
from quantitativeSkill import quantitativeSkill

qSkill1= quantitativeSkill(title = "Factoring algebraic expressions by common factor", 
                           
                            prompt = """ Generate 5 questions which test the skill of factoring an algebraic expression by common factor. All questions should be single
                                        step and not involve factoring quadratics or similar polynomials. Some examples are given below delimited by square brackets with answers. 
                                        [Factorize x^2y^3 - 2xy^4 answer: xy^3(x - 2y)], [Factorize 3a^2bc + 6ab^2c + 9abc^2 answer: 3abc(a + b + c)] 
                                        """,
                            numeric = False
                           )

qSkill2 = quantitativeSkill(title = "Evaluating derivatives of polynomials", 
                           prompt = """ Generate 5 questions that test the skill of evaluating the derivative of a polynomial at a specific value. Each problem should involve first finding the derivative of the given polynomial and then substituting a specific value to calculate the numeric value of the derivative at that point. The answer should be the numeric value of the derivative evaluated at the given point, not just the derivative expression.

                                    Here are two examples:

                                    1. If f(x) = x^2 + 3x + 2, evaluate f'(-1). 
                                    2. If y = x^4 - 2x^3 + 7x - 5, evaluate dy/dx at x = 3. 

                                    Please generate problems similar to these examples, where the final answer is the derivative evaluated at a specific point.
                                    """,
                            numeric = True
                           )

qSkill3 = quantitativeSkill(title = "Using conservation of momentum in one dimension", 
                           prompt = """ Generate 5 questions that involve solving for the velocity or mass of an object using conservation of momentum. Each problem should involve finding one unknown mass or velocity, and only involve motion along one axis.
                                    The use of conservation of energy should NOT be required for any of these problems.

                                    Here are two examples:

                                    1. Two ice skaters, Skater A and Skater B, are initially at rest on a frictionless ice surface. 
                                    Skater A (mass = 70 kg) pushes Skater B (mass = 50 kg) so that Skater B moves to the right with a velocity of 3 m/s. 
                                    What is the velocity of Skater A after the push?

                                    2. A 0.5 kg ball is moving to the right at 4 m/s and collides head-on with another ball moving to the left at 3 m/s. After the collision, the first ball rebounds to the left with a velocity of 2 m/s, 
                                    while the second ball continues moving to the left at 1 m/s. Assuming no external forces act on the system, what is the mass of the second ball?

                                    Please generate problems similar to these examples, where the final answer is a number. All numeric answers should be in SI units.
                                    """,
                            numeric = True
                           )

qSkill4 = quantitativeSkill(title = "Solving 2 step linear equations", 
                           prompt = """ Generate 5 questions that involve solving two step linear equations. Each problem should involve two steps, one involving adding or subtracting a term
                                    from both sides, and one involving dividing both sides by some constant.

                                    Here are two examples:

                                    1. Solve the equation 2x + 3 = 9

                                    2. Solve the equation 7x - 8 = 20

                                    Please generate problems similar to these examples, where the final answer is a number.
                                    """,
                            numeric = True
                           )


qSkill5 = quantitativeSkill(title = "Identifying major chords in music", 
                           prompt = """ 
    `                               Generate 5 questions which involve identifying the 1st, 4th and 5th chords in a major key. Present the chord on a stave
                                    with the key signature for the respective key.
                                    """,
                            numeric = False
                           )



def setUpSkill(filename, skill: quantitativeSkill):
    skill.generateExplanation()
    skill.setUse4o(False)

    print(skill.getExplanation())
    skill.generateQuestionBank()
    print(skill)
    print(skill.getQuestionBank())

    with open(filename, 'wb') as f:
        pickle.dump(skill, f)