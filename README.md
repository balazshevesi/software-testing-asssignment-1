
# Single or Pair-wise Student Assignment

This assignment contains elements that can either be done by a single student or a group of maximum 2 students.

Note that if you are working in a pair, the work should be a team effort. A recommended structure is pair programming where you take turns in implementing test cases and implementation methods. It is not important which student makes the commits to GitHub, but it is important that both students are equally active in the work.

However, **examination of the assignment is done individually**. The grade is also set individually, which means the pair may be given different grades.

This is an **optional** assignment for higher grades [F-A].

First choose either [**A1.a1 (alternative 1)**](https://coursepress.lnu.se/kurser/mjukvarutestning/03-examinations/01-assignment-1-part-1) or **A1.a2 (alternative 2)**. Pass your chosen alternative during lab time, then continue with [**A1 Part 2: Agentic Testing**](https://coursepress.lnu.se/kurser/mjukvarutestning/03-examinations/03-assignment-1-part-2), the PromptLab lab and assessed seminar. You must pass both stages before an A1 grade can be awarded.

# Description

In A1.a2 you study unit-testing frameworks, mocking frameworks, code coverage tools and Test Driven Development in more depth. During this exercise, you will learn automated unit testing using Test Driven Development.

The assignment allows for much freedom in choosing how and what you would like to do, as long as you learn something along the way.

For example, you are to decide the following:

- Language of implementation (For example Java)
- Framework for unit-testing (For example JUnit 4)
- Framework for Mocking (For example Mockito)
- Code coverage tool (For example Code Cover)
- What sort of project you are going to code (For example a dice game)

## Minimum Requirements

There are however some minimum requirements that we want you to achieve. You should see these as guidelines to conduct a project of the right size and type.

In order to get a higher grade you need to show that you have:

### Git Commit History

Made commits to a git repository using a specific pattern that shows that you have worked using TDD (**at least 20 commits**).

Make sure you are working in a **Test Driven Development** manner.

Make a git commit and **PUSH** after each step:

1. **Red:** Write a test that fails. Make a commit with the word `RED` in the commit message.
2. **Green:** Change the implementation so that the test suite succeeds. Make a commit with the word `GREEN`.
3. **Refactor:** Rewrite the code. Make a commit with the word `REFACTOR`.

At some point, do a coverage measurement.

If you make a code coverage measurement, do a commit separately for that named `COVERAGE`. Make sure you save the measurement as a file in your GitHub repository. This could be a text file or a screenshot image.

Note that it's quite common to have around **30–90 cycles (200 commits)**.

### Size and Complexity

Show a project of proper size and complexity that illustrates your proficiency in the techniques.

The important part here is not that you choose some impressive implementation with loads of features, but rather that you understand and use TDD properly.

And remember: don't go into this assignment thinking that you are going to finish the implementation. If you follow TDD properly, you won't.

Our minimum requirements are:

- In the final project, show at least **4 SUT classes with dependencies**. The more classes the better.
- You have used **dependency injection**.
- You needed to **mock or isolate dependencies** so that only bugs in the class under test trigger a failing test and not a bug in other classes.
- **Dynamic object creation** (`new SomeClassOrOther()`) in several (2+) parts of the application (not only as initial setup). Remember to test those too!
- The project has a **UI** (Console, GUI, or Web).

### Understand TDD, Unit Testing, Mocking and Coverage

- Show expertise in the use of the XUnit framework, Mocking framework, and coverage tool.
- Test behaviour using mocks.
- Show the use of different types of mocking.
- Use a code coverage tool.

# Task: Write a Small Project Using TDD

Write a small project and make sure you practice **writing the test first**!

Also, make sure you use **mocking** and **calculate coverage**!

In order to do this, you need to understand TDD first. Most failures on this assignment come from assuming TDD is something it is not.

# During the Examination

## Artifacts That We Want to See During Examination

- Show a programming environment with a project that compiles with **almost 100% unit test coverage** (note that 100% is the goal but sometimes impossible).
- Git commit history that shows that you have worked following **TDD principles (Red, Green, Refactor)**.
- In that project, show examples of how mocking is used to test behaviour and to isolate testing of dependent units.
- Show that you can find code not covered by any test using code coverage.
- Show source code for classes and test classes in Git.

## Study Questions That We Can Ask You During the Examination

The questions are examples of what can be asked during the individual examination.

1. What is a unit?
2. How does TDD differ from standard types of testing?
3. What is an Oracle?
4. How does an oracle know what is right?
5. What might you need to change in the SUT in order to make good use of unit testing, compared to when not doing unit testing?
6. Do all tests need to use asserts?
7. What makes black box testing different from white box testing?
8. Why might we want to use black box testing?
9. What is the purpose of unit testing?
10. What are equivalence partitioning and boundary value analysis?
11. Why do we use TDD? What is its purpose?
12. If multiple tests are broken, which tests are most important to prioritize fixing?
13. Can we always have 100% code coverage?
14. What are the different types of coverage criteria?
15. Why do we use mock objects?
16. What is the difference between a mock, a stub, and a spy?
17. Does 100% coverage mean we are bug-free?
18. Does 100% MCDC coverage mean we are bug-free?
19. Can we prove that we're 100% bug-free?
20. In TDD, why do we go for RED first?

## Examination Procedure

Work on A1.a2 during the lab sessions assigned to your group.

Teaching staff examine you while observing you working on the project tasks during these sessions.

**Showing a finished project or submitting a repository link alone is not sufficient.**

Even if you worked in pairs, the examination is individual.

Kalmar and Växjö campus students attend in person.

Only WP distance students participate online, using the [**course Zoom room**](https://lnu-se.zoom.us/j/65973679221).

**NEW: POST your Git link here:** [**Git Submission Form**](https://forms.gle/1y4C2fwCZzUyA5Ce6)

Follow the lab assessment arrangements explained at the course introduction and posted in your group's Zulip channel.

During the lab assessment, you will show your code and demonstrate proficiency in coding while working on the project tasks.

### Assessment Criteria

During the examination, you will get a **0–4 value** in the following:

| Criterion | Score |
|---|---|
| TDD Usage | 0–4 |
| X-Unit Usage | 0–4 |
| Complexity of the Project | 0–4 |
| Code Coverage | 0–4 |
| Mocking Usage | 0–4 |
| Study Questions | 0–4 |

These values are then weighted into the final grade **E–A**.

### Grading Scale

| Grade | Requirements |
|---|---|
| **A** | All 4s |
| **B** | Some 3s and some 4s |
| **C** | All 3s |
| **D** | Some 2s and some 3+s |
| **E** | All 2s |
