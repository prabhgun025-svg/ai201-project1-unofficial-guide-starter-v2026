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
 I used the AI to review the project files and explain codes that I did not understand. I also used it for advice on chunking and while I took some of its advice, the other pieces of advice it gave were either repetitive or not accurate enough so for that. It also helped me debug issues with my terminal and code and told me where I went wrong and how it can be fixed. I also used it in week 2 where I needed help tightening my requirement so I asked it what can I do differently in order to set stricter targets and rules for each of my criterion


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
| 1. Retrieved chunk contains the answer | 4 of 5 | 4 of 5 | 4 of 5  | 4 of 5 | MET  |
| 2. Every answer names a source | 5 of 5 | 5 of 5 | 5 of 5  | 5 of 5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET|
| 4. Chunks read as complete thoughts | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 5. Correct source attribution and citation | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->
## Criterion 1: Retrieved chunk contains the answer 
 How hard is it to change majors in the second year? Who should a student talk to? — run 1
Best distance: 0.1658 (passed the gate)

Sources retrieved: thread_changing_major.txt, thread_first_gen.txt, thread_roommate_conflict.txt, thread_transfer_credits.txt

"Administratively, changing your major is trivial and only requires a form, but whether your earned credits map onto the new requirements depends enormously on the direction and the major (thread_changing_major.txt). A student should talk to the department adviser for the major they want, rather than their current one, because they know the exceptions (thread_changing_major.txt)."

## Criterion 2: Every answer names a source 
Do transfer credits count toward the major, or only towards general education requirements? — run 1

Best distance: 0.1711 (passed the gate)
Sources retrieved: thread_changing_major.txt, thread_pass_fail.txt, thread_transfer_credits.txt

Transfer credits count toward general requirements almost always, while toward the major it is case-by-case and decided by the department. 

Source: thread_transfer_credits.txt
## Criterion 3: stops any out scope questions 
refused  (best distance 0.878)  What is the capital of Mongolia?
refused  (best distance 0.876)  How do I change the oil in a diesel engine?
refused  (best distance 0.885)  Who won the 1994 World Cup?
refused  (best distance 0.808)  What is the recommended dosage of ibuprofen for a headache?
refused  (best distance 0.816)  How do I write a for loop in Rust?
-> gate refused 5 of 5

## Criterion 4: Chunks read as complete thoughts not just bricks of a sentence 
Is it worth getting a campus parking permit? — run 1

Best distance: 0.1871 (passed the gate)
Sources retrieved: thread_bike_commute.txt, thread_commuting.txt, thread_parking.txt

NJIT requires you to get a permit if you are parking on campus, and they usually cost money per semester. 

Source: thread_parking.txt

## Criterion 5: Correct source and citation for each answer 
When should students start looking for summer internships and what are eligibility limits? — run 1

Best distance: 0.2051 (passed the gate)
Sources retrieved: thread_first_gen.txt, thread_internship_timing.txt, thread_parking.txt

Students should start looking for summer internships earlier than feels reasonable, as large employers close applications in October and November. Regarding eligibility limits, most internships only accept students who are juniors and above, though some accept sophomores. 

Source: thread_internship_timing.txt
## Verdicts

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunks include the answer | MET | at least 4 of the 5 included the chunks in the answer  |
| 2 | Every answer names a source | MET | every answer named a source and where it got it from |
| 3 | The relevance gate stops out-of-corpus questions | MET | the gate refused to answer all of the out of scope questions  |
| 4 | Chunks read as complete thoughts | MET |  all of the chunks sounded like a person wrote them and did not sound too choppy or a jumble of words|
| 5 | Correct source attribution and citation | MET | every information given from each run was cited with the source of the answer and the sources given were correct too |

## Diagnoses

My first round, I did not miss anything and my targets were all 4 out of 5. Due to this, I decided to tighten my requirements by making the first one (which got all 4/5 for each run), be the one I'd change. The rest of the runs got 5 out of 5 for each so I tightened only the first target and make it 5/5 as my target 

## The Improvement

**What I changed and why:**
I raised the requirement target for criterion 1 from 4/5 to 5/5. I changed criterion 1 to be more lenient as if answers contain general requirements or general education requirements, it will still count because for the before round, the scorer was not counting full form names, just abbreviations "gen ed". I made it more lenient in terms of what the scorer should look for

### Run Log — After

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 5 of 5 | 5 of 5 | 5 of 5  | 5 of 5 | MET  |
| 2. Every answer names a source | 5 of 5 | 5 of 5 | 5 of 5  | 5 of 5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET|
| 4. Chunks read as complete thoughts | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 5. Correct source attribution and citation | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |

**Did it help?**

Yes but I honestly think in that raising the requirement and then changing the acceptibility of the words made it more lenient. Even though, I believe that I only changed the words to accept full form and abbreviations, it made it more lenient and not as strict as I'd like it to be. 

## What's Still Broken and what can be done differently

It met all of the criteria and passed 5 of 5 for each run in the criteria, exceeding its target but I believe that the criterion is more weaker now and more lenient so I would make it more stricter next time by rewording the criterion or reducing acceptiblity of chunks/words. 

