![cover](/cover.png)

# CAN CLAUDE CODE WRITE A (GOOD) CHOOSE YOUR OWN ADVENTURE BOOK?

## Intro

What can we say about AI?

---

1. AI can predict the 3D structure of proteins, a breakthrough recognized with a Nobel Prize, helping us understand how diseases develop (Nobel Prize in Chemistry 2024).
2. Using AI models for speech to text and text to speech helps people with disabilities communicate and access information.
3. AI helps us break language barriers with live translation or captioning
4. AI supports scientific research by analyzing massive datasets
5. AI helps detect diseases earlier by analyzing medical images like X-rays, MRIs, and CT scans with high accuracy

---

At the same time...

1. You can use AI to generate slop
2. Or fake news, with fake images and fake videos, with fake comments of fake users upvoted by an army of more fake users
3. With AI a scammer can clone your voice, call your grandma and ask her for money
4. Or your government can use AI for face recognition and mass surveillance
5. Or a friend of yours can use ChatGPT as a therapist
6. Or a mega corporation can use AI to generate an awful Christmas commercial

---

AI can be all of that at the same time. Saying “AI is great” or “AI sucks” is a blanket statement.

It's like saying "internet videos are bad" because you see a YouTuber make a silly prank video, when you have Laracast which also counts as "internet videos" and I think we all learned from it.

In summary, talking about AI is complicated.

And there's a lot of AI news. The AI news cycle is exhausting. There are many awesome things coming up all the time, don't get me wrong.

But tell me if you find yourself in this situation: a friend sends you a link about something AI related and you reply "ohh cool". What do you mean by cool? This is awful. So we have this rule: if you share something, add your take.

"Disney invest about $1 billion in OpenAI as part of a broader three-year partnership that includes licensing over 200 characters from Disney, Pixar, Marvel, and Star Wars for use in OpenAI’s generative AI tools like Sora"

---

There are many controversial, unnerving questions regarding AI:

- Will AI take all our jobs?
- Is the AI market a bubble?
- Will we get general superintelligence?
- Will it rise like Skynet to destroy us all?

# OUR GOAL FOR TODAY

And today we will answer none of them. Instead, we will focus on a much more important question:

**CAN CLAUDE CODE WRITE A (GOOD) CHOOSE YOUR OWN ADVENTURE BOOK?**

That is all we care about today. Can we say, “I want a choose your own adventure book about Zombies at Laracon,” and get one of these?

That is our mission for today.

But to start answering this question, we need to go back to the distant year of 2022.

What was the first thing you generated on ChatGPT?

One of my first tasks for ChatGPT was creating a poem about Bistolfi, my friend’s DnD character.

“Bistolfi is the greatest hero of them all.”

It worked like magic. But once you understand how LLMs work, it seems less magical. And that is a good thing.

You see, generative AI is like a slot machine. But a rigged slot machine.

It predicts what the next word will be.

```
Bistolfi is the greatest…

Potato? 1%
Warrior? 14%
Hero? 90%
```

What gives these words their weights? The training data.

Even if the model has never seen “Bistolfi” before, the phrase structure is very familiar. “X is the greatest … of them all” is a strong pattern in the training data.

The model treats “Bistolfi” as a variable plugged into a known template. Once that template is recognized, the next words are driven by how that structure usually continues, not by facts about Bistolfi.

ChatGPT does not know about my friend’s character.

It's all about patterns and context.

**THIS IS AN OVERSIMPLIFICATION,** but helps us understand.

# AI CODING

And this is the perfect segue to talk about coding with AI. Because code is just text. A different kind of text, but text nonetheless.

If we have:

```js
const customers = [
  { name: "Bob", active: true },
  { name: "Alice", active: false }
];

const activeCustomers =
```

The LLM can predict the rest:

```js
const activeCustomers = customers.filter(customer => customer.active);
```

The moment this happened, it was over for us. Game over, guys. Let’s master a different skill. Programmers are basically extinct. It was fun while it lasted. Goodbye!!

Whether we like it or not, we are in the era of AI-assisted coding.

We have Copilot, Cursor, Windsurf, and who knows how many other VS Code forks. And of course, we have the man of the hour: Claude Code.

This tool was released by Anthropic in February 2025, so it is not even a year old yet.

This tool is not another editor, it doesn't have a GUI, because it lives in your terminal.

Let me show you:

Here I showcase Claude Code and test:

```md
[x] it can take a simple prompt
[x] it can edit files
[x] it can connect with your editor
[x] it can execute cli commands
[x] it can add a feature
[x] it can solve a repo issue
[x] show models
[x] show usage
[x] show context
    [x] be mindful of MCPs!
```

So, Claude Code is great. But the question remains:

_CAN IT WRITE A BOOK? AND MORE SPECIFICALLY, A CHOOSE YOUR OWN ADVENTURE BOOK?_

# CHOOSE YOUR OWN ADVENTURE BOOKS

And this is my favorite part of the talk because we're gonna dive into the world of CHOOSE YOUR OWN ADVENTURE

I love these books!

_AN AFTERNOON..._

I was bored. I wanted a CYOA book but didn't have any at home, and I have Claude Code. I prompted it to create one... and it was terrible.

- Characters that disappear
- Equipment that you get or lose randomly
- Branches that lead nowhere
- Abrupt endings
- Terrible pacing
- Really dumb choices
    - Two equivalent choices
    - Two choices that you can do at the same time

It was the worst! But at the same time it was kinda cool.

That marked the start of my quest: making Claude Code write an actual good book.

## ATTEMPT NUMBER 1: VIBE YOUR OWN ADVENTURE

Model: Sonnet

**OSIRIS STATION**

```
STRUCTURE: 1/10
PROSE: 1/10
CHOICES: 1/10
FUN FACTOR: 10/10
```

# ATTEMPT NUMBER 2: PLAN YOUR OWN ADVENTURE

Model: Opus

I have to admit, Opus does a pretty good job in terms of structure... or so I thought.

It has a some good endings, finding either the treasure or a map to it. A couple of neutral endings, you find something else. And on page 70 it even has the courage of saying:

"Sometimes the journey is just as valuable as the destination."

The treasure are the friends we made along the way!

BUT WAIT, on page 49 I choose to grab a crowbar and... I get to page 66 and read:

```md
You grab the crowbar (or try the combination, or grab treasure from the flooding chamber—paths converge here). With determination, you work at the lock or door or situation before you.
```

Even tho at first glance the branching makes sense, if you look closely, you'll notice that many choices lead to the same end:

[page 66](./number-2/output/66.md)

```
You grab the crowbar (or try the combination, or grab treasure from the flooding chamber—paths converge here). With determination, you work at the lock or door or situation before you.
```

[page 65](./number-2/output/65.md)

```
Beyond the iron door (or in the storage area, or at the cairn—depending on your path), you find yourself in a carefully prepared treasure chamber. The room is dry and has been protected from the elements.
```

_YOU CHEATER!!_

And what is lacking is DEATH. There isn't a single DEATH ending. And CYOA is famous for having DEATH endings!

Another big problem: if we ask for changes, we can fill up the context. Content quality will degrade.

**TREASURE HUNT**

```
STRUCTURE: 8/10 (no, 4/10)!
PROSE: 4/10
CHOICES: 8/10
FUN FACTOR: 3/10
```

# ATTEMPT NUMBER 3: CLAUDE YOUR OWN ADVENTURE

We need something better. This doesn't qualify as a good CYOA book.

Let's go overboard. Let's go full in. Let's show those vibe-coders that we programmers never see the light of day.

What we need is an OUTLINE.

A CYOA book is essentially a branching structure, and when I think of it I think of JSON. What if we have an outline like this...?

**LOST IN THE ISLAND OF TIME**

```
STRUCTURE: 8/10
PROSE: 7/10
CHOICES: 9/10
FUN FACTOR: 8/10
```

# ATTEMPT NUMBER 3: CLAUDE YOUR OWN ADVENTURE 2

**YOU ARE A WIZARD**

```
STRUCTURE: 8/10
PROSE: 6/10
CHOICES: 8/10
FUN FACTOR: 7/10
```
