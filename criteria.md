# Acceptance criteria — The Unofficial Guide

Five criteria that say what "working" means for this system, written in week 1
**before** any results existed.

An acceptance criterion names a target: a number, a count, a rate, or something
a person could plainly observe. *"Retrieval works"* is an opinion. *"For at
least 4 of my 5 test questions, the top results include a chunk containing the
answer"* is a criterion.

Under each one, write a sentence or two on **why that target** and not a
stricter or looser one. A reason that says something about your corpus or your
pipeline earns credit; *"80% seemed reasonable"* does not.

> Missing your own targets next week costs you nothing. Setting a target so
> easy you can't miss it does.

---

## 1. Retrieved chunks contain the answer

For at least 4 of my 5 test questions, the retrieved chunks include one that
contains the answer.

**Why this target:**
 One of my questions is about a topic only two documents mention, so
     I expect that one to be hard.

---

## 2. Every answer names a source

Every answer the system produces names at least one source document.

**Why this target:**
 The source document makes it so that the answers are coming from actual sources and not being hallucinated by the AI 

---

## 3. The relevance gate stops out-of-corpus questions

When I ask a question my documents clearly don't cover, the relevance gate
stops it and the system returns "I don't have enough information about that" —
in at least 4 of 5 tries.



**Why this target:**
This is so the AI does not hallucinate and give wrong information to the incoming student. 
---

## 4. Something about your chunks

for at least four of the five chunks, the chunk reads as a complete thought and no sentence gets cut off or shortened. 


**Why this target:**

Because a chunk that is complete and readable is more likely to have a better sound answer compared to something more cut off. If it reads as a complete thought, the incoming student is more likely to follow through with it and not be confused. 

---

## 5. Correct Source Attrbiution  

at least four of 5 answers, the systems names the correct source that supports the answer as well as a citation, showing where in the document it answered 


**Why this target:**
 The correct answer often depends on which document is being cited, so if the system can point to the correct source, it will make sure that the advice being given out is cited and correct. 


---

<!-- ─────────────────────────────────────────────────────────────────────────
     WEEK 2 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath it, like this:

         ## 1. Retrieved chunks contain the answer

         For at least 4 of my 5 test questions, the retrieved chunks include
         one that contains the answer.

         **Why this target:** ...

         > **Revised in week 2:** For at least 4 of 5 questions, the top three
         > results contain the answer.
         >
         > **Why revised:** I couldn't judge "the chunks include one that
         > contains the answer" the same way twice — I scored two questions
         > differently on Monday than on Wednesday. The new version is
         > something I can actually check.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "I said 4 of 5 but got 2 of 5, so 2 of 5 is more realistic."

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.

     The whole reason the originals stay visible is so someone can see what you
     said before you knew the answer.
     ───────────────────────────────────────────────────────────────────────── -->
