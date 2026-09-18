# The Unofficial Guide

Prabhgun kaur - Advice_threads 

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none, because the grader can't
> read it.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Week 1

## What This Does

   For this unofficial guide, I picked the corpus on campus advice. With this corpus, the system answers questions on general advice that students may need such as parking, meal plans, textbooks, etc. It will go through advices that every first year student might need or may be asking. 

## Chunking Strategy

**Chunk size:**
**Overlap:**

For the advice threads corpus, I split it on the reply arkers so each reply become its own chunk. The replies answer the question directly and standalone. I did it so that every chunk contains some answerable content and utilized the AI to make sure that every single of those chunks can be understood even if the reader did not read anything before or after it.
for the city guides corpus, I made it so that each section is its own topic 
for campus life, I split the paragraphs and made them all one or two sentences to make sure they fit in chunks  
This was my strategy to make sure that there is no overlap between the corpuses 

## Sample Chunks

**Chunk 1** — source: `thread_bike_commute.txt#0` — produced by: `chunker.py::split_documents`

```
--- reply 1 (14 votes) ---
Yeah. Cuts an 18 minute walk to about 6. The thing nobody mentions is storage — covered bike parking exists and is full by 9am at all three.
```

**Chunk 2** — source: `thread_first_year_regret.txt#0` — produced by: `chunker.py::split_documents`

```
--- reply 1 (41 votes) ---
That the add/drop deadline and the withdrawal deadline are different dates. There is a set period for withdrawal refunds before you cannot anymore
```

**Chunk 3** — source: `thread_internship_timing.txt#0` — produced by: `chunker.py::split_documents`

```
Earlier than feels reasonable. Large employers close applications in October and November for the following summer. Smaller and local places hire in February and March, so if you missed autumn you have not missed everything. Most internships only accept junior and above but some accept sophomores
```

**Chunk 4** — source: `thread_pass_fail.txt#0` — produced by: `chunker.py::split_documents`

```
NJIT does not offer pass/fail unless there are specific circumstances (such as covid or hurricanes). There are SOME one credit/0 credit courses where there is pass/fail such as Co-op, first Year seminar, or physical education courses
```

**Chunk 5** — source: `thread_roommate_conflict.txt#2` — produced by: `chunker.py::split_documents`

```
--- reply 3 (33 votes) ---
Write down specifics before the meeting. 'It's not working' is hard to act on; 'guests four nights a week past 2am' is not.
```

## Sample Answer

**Question:**
When should I apply for internships? 
**Answer:**
(best distance 0.216, cutoff 0.6)

You should start looking earlier than feels reasonable. Large employers close applications in October and November for the following summer, while smaller and local places hire in February and March. 

Source: thread_internship_timing.txt

Sources retrieved: thread_changing_major.txt, thread_first_gen.txt, thread_first_year_regret.txt, thread_internship_timing.txt
```
```
## Sample Answer for Out_of_scope 

**Question** 
What is the capital of France?
**Answer**
(best distance 0.907, cutoff 0.6)

I don't have enough information about that.
**My relevance cutoff:**

The gap between in-corpus and out-of-scope questions is clear. All 5 in-corpus questions scored 0.09–0.38 (well below 0.6). All 5 out-of-scope questions scored 0.78–0.91 (well above 0.6). The cutoff of 0.6 sits in the middle of the gap and correctly gates all out-of-scope questions while allowing all in-corpus ones through.

| Question | In corpus? | Best distance |
|---|---|---|
| How important is a parking permit? | Yes | 0.200 |
| Is a bike commute worth it? | Yes | 0.185 |
| What do you wish you'd known in first year? | Yes | 0.093 |
| How do I handle group projects? | Yes | 0.385 |
| What are the best study spots? | Yes | 0.234 |
| What is the capital of France? | No | 0.907 |
| How do I fix my car? | No | 0.784 |
| What is quantum computing? | No | 0.870 |
| How do I cook a steak? | No | 0.818 |
| What is the history of ancient Rome? | No | 0.880 |

## How I Used AI


     I used the AI to review the project files and explain codes that I did not understand. I also used it for advice on chunking and while I took some of its advice, the other pieces of advice it gave were either repetitive or not accurate enough so for that. It also helped me debug issues with my terminal and code and told me where I went wrong and how it can be fixed. 

---

# Week 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     week 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     week — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |
| 4 |  |  |  |
| 5 |  |  |  |

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

## The Improvement

**What I changed:**

**Why I picked it:**

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
