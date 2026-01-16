---
name: generate-outline
description: Generate a summary.yaml and outline.json for a Choose Your Own Adventure book from a user's concept. This creates the inputs needed for the write-adventure skill.
user-invocable: true
---

# GENERATE CYOA OUTLINE

Generate a complete **summary** and **outline** for a Choose Your Own Adventure book based on a user's concept.

# THE READER IS THE PROTAGONIST

All text is written in second person ("you"). The reader IS the protagonist.

# HOW TO CREATE A STORY

> Following these guidelines, you will find TODO items. Use the TodoWrite tool to track them. Tackle them in order.

Think of a bad guy and what he is trying to accomplish:

* Doctor Claude created time machines on a distant island and plans to control time.
* Captain Blackheart wants the Night Pearl to obtain supernatural powers.
* Mr. Supercold wants to freeze New York forever.

Then, think of how a triumph against this villain would look:

* You fight Doctor Claude and destroy the time machines.
* You put the Night Pearl under the bright sun to destroy it.
* You stop Mr. Supercold's plan to freeze New York forever.

That is the ideal outcome, a **GOOD ending.** That is how a classic book would end.

[ ] TODO: COME UP WITH A BAD GUY AND THEIR PLAN, FITTING THE THEME OF THE STORY. IMAGINE THE IDEAL RESOLUTION, THE GOOD ENDING.

Now think: how can the protagonist (in this case, the reader, treated in second person "you") gets involved with this story? This is known as the **inciting incident** and kickstarts our story.

* You and your uncle crashland on Doctor Claude's island.
* Your ship gets boarded by Captain Blackheart.
* Mr. Supercold attacks the school of superheroes you attend.

[ ] TODO: IMAGINE THE INCITING INCIDENT.

Many things can happen between the **inciting incident** to the **GOOD ending.** Many scenes, set pieces, chases, fights and even discussions and plans and solving mysteries. Think of these **story blocks.** A good, satisfying story has many fun, action-packed story blocks.

* You are captured by Captain Blackheart and learn about the Night Pearl.
* You escape his ship with a clue about the Pearl's location.
* You get to an island and meet a mysterious man who has the Pearl treasure map.
* You follow the map and reach a dark cave full of undead.
* You get to the chest where the Pearl is hidden and a ghost appears with a riddle.
* You get the Pearl, but Captain Blackheart chases you closely.
* You put the Pearl under the bright sun to destroy it.

When creating a story, come up with story blocks and write them down.

[ ] TODO: WRITE DOWN STORY BLOCKS

**IMPORTANT: The path to the main GOOD ending must include at least 4 exciting set pieces.** Set pieces are high-stakes, action-packed moments like:
- Combat (fighting pirates, battling monsters, dueling villains)
- Chases (ship pursuits, running from danger, vehicle escapes)
- Heists (stealing treasure, infiltrating bases, breaking into vaults)
- Escapes (breaking free from captivity, fleeing collapsing structures, evading traps)

These create the memorable moments that make the story thrilling. Other branches can have fewer set pieces, but the main GOOD ending path should feel like an action-adventure movie with multiple exciting beats.

Now that you have those blocks in place, think: what actions could connect them?

* You are captured by Captain Blackheart and learn about the Night Pearl.
    * Break the chains to break free.
* You escape his ship with a clue about the Pearl's location.
    * Steal a small but fast ship to sail away.
* You get to an island and meet a mysterious man who has the Pearl treasure map.
    * Play cards against him to win the map.
* You follow the map and reach a dark cave full of undead.
    * Fight skeleton pirates.
* You get to the chest where the Pearl is hidden and a ghost appears with a riddle.
    * Choose the right answer.
* You get the Pearl, but Captain Blackheart chases you closely.
    * Win the battle and escape from Blackheart and their henchmen.
* You put the Pearl under the bright sun to destroy it.

When creating a story, write actions between the story blocks.

[ ] TODO: ADD ACTIONS BETWEEN STORY BLOCKS

Great! That chain of events leads to a GOOD ending. Now, let's transform those actions in **choices.**

When creating a story, replace the actions you added between the story blocks with choices: the one that leads to the next block, and another that leads to an ending or a different story branch.

* You are captured by Captain Blackheart and learn about the Night Pearl.
    * If you attempt to break the chains to break free (leads to next block)
    * If you try to bribe the clumsy guard (leads to end or another path)
* You escape his ship with a clue about the Pearl's location.
    * If you steal a small but fast ship (leads to next block)
    * If you take the heavy but resistant ship (leads to end or another path)
* You get to an island and meet a mysterious man who has the Pearl treasure map.
    * If you try to steal the map when the man falls asleep (leads to end or another path)
    * If you gamble a year of work for his map in a game of cards (leads to next block)
* You follow the map and reach a dark cave full of undead.
    * If you make your way in fighting the skeleton pirates (leads to next block)
    * If you turn around and find another way in (leads to end or another path)
* You get to the chest where the Pearl is hidden and a ghost appears with a riddle.
    * If you think the answer to the riddle is "parrot" (leads to end or another path)
    * If you think the answer to the riddle is "sea" (leads to next block)
* You get the Pearl, but Captain Blackheart chases you closely.
    * If you climb the cave out (leads to next block)
    * If you use the Night Pearl to get supernatural power (leads to end or another path)
* You put the Pearl under the bright sun to destroy it.

**IMPORTANT: IT SHOULD NOT BE OBVIOUS WHICH CHOICE LEADS TO THE GOOD ENDING. The reader gets presented two choices that sound equally good.**

Sometimes, set of choices are straightforward:

```md
// Example 1
If you go left
If you go right

// Example 2
If you choose the sword
If you choose the axe
```

But **BE CREATIVE**. The best CYOA books surprise readers with original options that feel true to the moment:

```md
// Example 1
If you try to drop the chandelier on the ogre's head
If you throw the boiling soup at his face

// Example 2
If you carefully diagnose the issue and attempt a proper repair
If you grab a pipe and start hammering, hoping for the best
```

Choices must be:

**Multiple:**
- A set of choices contains two or three options. Never leave a set of choices with a single option.

**Should sound equally good:**
- In a set of choices, all of them should be exciting and entice the player to try them out. None should be boring. None should be the obvious "right choice".

**Mix outcomes:**
- The choice that leads to a good outcome insn't always the first of the set. Note this:

```md
* You follow the map and reach a dark cave full of undead.
    * If you make your way in fighting the skeleton pirates (leads to next block)
    * If you turn around and find another way in (leads to end or another path)
* You get to the chest where the Pearl is hidden and a ghost appears with a riddle.
    * If you think the answer to the riddle is "parrot" (leads to end or another path)
    * If you think the answer to the riddle is "sea" (leads to next block)
```

**ACTIONS, not outcomes:**
- WRONG, NOT VALID: "If you gain the villain's trust"
- RIGHT, VALID: "If you offer to help the villain with their task"

**Mutually exclusive:**
- Each choice prevents the others from being taken

**Concrete and immediate:**
- The reader must be able to picture themselves doing this action RIGHT NOW

**Format:**
- Always start with "If you..."

**Choice patterns:**
- Physical actions: "If you climb through the window"
- Dialogue choices: "If you say 'I don't trust you'"
- Strategic decisions: "If you wait until nightfall"
- Resource choices: "If you use your last bullet"

**Equipment and item continuity:**
- Choices can reference equipment, tools, or items gained in previous nodes
- If you create a choice that uses a specific item (sword, broom, map, key), ensure the protagonist acquired it in an ancestor node (but not the immediate parent node)
- You can add equipment retroactively: if you come up with a choice requiring an item, go back and add the item acquisition to one of the ancestor texts in that path
- Example: If a choice is "If you use the sketchy flying broom", you can retroactively edit an earlier passage (not the parent) on that path to show the protagonist finding or receiving the broom
- This creates narrative consistency and rewards readers for their earlier decisions

**Red flags to AVOID when writing choices:**
- Vague choices: "If you take the careful approach"
- Outcome spoilers: "If you make the right decision"
- Complementary actions: choices that could both be done together
- Same choice, different words: "Look around" vs "Examine your surroundings"

[ ] TODO: REPLACE ACTIONS WITH CHOICES

Now that a path to the GOOD ending exists, think of five alternative ways the story could conclude. Ask yourself how the story might end in a more wacky, unexpected, or bittersweet way. These endings are not ideal, but they resolve the story in surprising, slightly twisted ways. Choose the strongest option, one that could still be considered a victory, as an alternate GOOD ending. Use the remaining ideas as NEUTRAL endings.

[ ] TODO: REPLACE ACTIONS WITH CHOICES

When you reach this point, show the user the draft including all you came up with so far. Use the question tool to let him confirm, deny or ask for changes.

[ ] TODO: SHOW THE USER THE DRAFT OUTLINE AND WAIT FOR INPUT

Once you have the story blocks and the choices between them, turn this list into a JSON object of nested nodes. **Each passage's `text` must be around 70 words** (see "HOW TO WRITE THE TEXT" section below for details). Like this:

```json
{
    "text": "The chains bite into your wrists aboard Captain Blackheart's ship. Through the porthole, you glimpse a dark island on the horizon. The captain enters, his cutlass gleaming. 'The Night Pearl will be mine,' he growls. 'With it, I'll command the seven seas.' He laughs and leaves you in the darkness. The guard outside is drunk, singing sea shanties. There's a rusty nail on the floor within reach.",
    "choices": {
        "If you attempt to break the chains to break free": {
            "text": "You work the nail into the lock mechanism. After tense minutes, the chains fall away. Through the porthole, you see the island getting closer. A coiled rope hangs nearby—you could climb down to the water. But you hear footsteps approaching. The drunk guard is coming back. Your heart pounds. Do you escape now or wait to ambush him?",
            "choices": {
                "If you steal a small but fast ship": {},
                "If you take the heavy but resistant ship": {}
            }
        },
        "If you try to bribe the clumsy guard": {}
    }
}
```

As you can see, the nested nodes lead toward the GOOD ending. Leave the other branches empty as `{}` for now—you'll fill them as you go.

[ ] TODO: FORMAT STORY BLOCKS AS JSON WITH NESTED NODES (with 70-word passages)

We have our JSON with the main GOOD ending. Now, take the alternative choices and ask yourself: "Which of these choices can lead directly to a BAD (at least you survive) or DEATH (you die) ending?" Fill those in with full 70-word passages:

```json
"If you think the answer to the riddle is 'parrot'": {
    "text": "You confidently say 'parrot.' The ghost's eyes flash red. 'Wrong, mortal.' A chill sweeps through the cave as the ghost phases through your body. You scream. Days later, you escape the island, but the ghost never leaves. It whispers at night, moves objects, appears in mirrors. Your life becomes a waking nightmare. You survive, but you're never truly alone again. The Night Pearl remains hidden in the cave.",
    "end": "BAD"
}
```

```json
"If you take the heavy but resistant ship": {
    "text": "You choose the massive galleon. It's slow but sturdy. You set sail, confident in your choice. But the ship handles like a whale. Within an hour, Captain Blackheart's sleek vessel appears on the horizon. He closes the distance fast. Cannonballs rain down. The galleon takes the hits well, but you can't outrun him. Blackheart boards, cutlass drawn. 'Wrong choice, fool.' The blade flashes. Game over.",
    "end": "DEATH"
}
```

[ ] TODO: FILL BAD AND DEATH ENDINGS

Then, think of the ones that can lead DIRECTLY to one of the NEUTRAL endings you came up with. Fill those in with full 70-word passages:

```json
"If you use the Night Pearl to get supernatural power": {
    "text": "The Pearl pulses in your hand. Dark energy courses through your veins. You feel invincible. Blackheart and his crew fall before your newfound power. You become legend—the Pirate King who commands darkness itself. Ships flee at the sight of your black sails. But at night, when you're alone, you feel the Pearl's corruption spreading. You won. But at what cost? The darkness whispers your name.",
    "end": "NEUTRAL"
}
```

[ ] TODO: FILL NEUTRAL ENDINGS

Now, we still have choices not filled in:

- If you try to bribe the clumsy guard
- If you try to steal the map when the man falls asleep
- If you turn around and find another way in

These will become **new branches.** These choices do not lead directly to an ending, but to other set of choices. Write full 70-word passages:

```json
"If you try to bribe the clumsy guard": {
    "text": "The drunk guard stumbles to your cell. 'Hey,' you whisper. 'I know Big Pete at the Rusty Anchor. Get me out and I'll set you up with free rum for a year.' His eyes light up. 'A year?' He fumbles with the keys. Minutes later, you're running through the darkness. Behind you, the ship fades. Ahead, two paths: the lights of Port Hamilton to the north, mysterious Port Mist to the south.",
    "choices": {
        "If you go north to Port Hamilton": {},
        "If you go south to Port Mist": {}
    }
}
```

And the branches that result from those choices can be filled in with either endings or more choices. All passages must be around 70 words:

```json
"choices": {
    "If you go north to Port Hamilton": {
        "text": "Port Hamilton bustles with pirates and merchants. You duck into a tavern and freeze. Captain Silver sits at the bar—your old nemesis. He spots you. 'Well, well.' He stands, hand on his cutlass. The room goes quiet. Everyone watches. You could duel him here, prove you're not afraid. Or maybe, just maybe, you could talk him into an alliance. He hates Blackheart too.",
        "choices": {
            "If you take out your sword and duel him": {
                "text": "Steel rings against steel. You're good, but Silver is better. He's been doing this longer. Your sword flies from your hand. His blade finds your chest. 'Nice try, kid.' You fall. The tavern crowd goes back to drinking. Just another dead pirate.",
                "end": "DEATH"
            },
            "If you try to convince him to join you in your quest": { "text": "...", "choices": {} }
        }
    },
    "If you go south to Port Mist": {
        "text": "Port Mist lives up to its name—thick fog blankets everything. You navigate by sound until suddenly, chattering surrounds you. Dozens of monkeys drop from the trees. But these aren't normal monkeys. They speak. 'Payment required,' their leader says in broken English. 'Bananas. Five each.' You count twenty monkeys. A hundred bananas. You have zero. One monkey spots your sword and points. 'Shiny. That work too.'",
        "choices": {
            "If you scare them away with the gunpowder bomb": {
                "text": "You pull out the small bomb you stole from Blackheart's ship. 'Get back!' The monkeys scatter—but not far enough. You light the fuse. Too short. The explosion tears through you. Turns out gunpowder bombs have a learning curve. You won't get to practice again.",
                "end": "DEATH"
            },
            "If you give them your sword and explain they can trade it for fruit": { "text": "...", "choices": {} }
        }
    }
}
```

[ ] TODO: FILL OTHER BRANCHES (with 70-word passages for every node)

Great, now we have many branches, and your goal is to continue filling them in recursively until having a full outline. Remember: **every `text` field must be around 70 words** (see "HOW TO WRITE THE TEXT" section). The outline should follow these guidelines:

**Endings**
Should have around 20 endings in total, distributed in this way:

- 1 core GOOD ending, 1 alternate GOOD ending
- From 3 to 5 NEUTRAL endings
- From 2 to 4 BAD endings
- DEATH endings (all the rest)

**Number of choices**
Once in the outline, a `choices` object can contain 3 options instead of 2. Add a 3rd option to any single existing node at least 3 levels in, and fill it in.

**Steps to endings**
The GOOD endings should come after a minimum of 10 choices. Getting a GOOD ending in less than 10 choices makes the story feel rushed and the outcome unearned. The NEUTRAL endings can come after as soon as 4 or 5 choices. BAD and DEATH endings can come at any point.

**Different endings**
A set of choices can't lead to two or more endings of the same type.

**CRITICAL: BAD and DEATH are treated as the SAME TYPE for this rule.** They are both "failure endings."

Valid ending type combinations in a choice set:
- GOOD + DEATH (or BAD)
- GOOD + NEUTRAL
- NEUTRAL + DEATH (or BAD)

**FORBIDDEN combinations** (these break the rules):
- GOOD + GOOD
- NEUTRAL + NEUTRAL
- BAD + BAD
- DEATH + DEATH
- **BAD + DEATH** ← This is NOT allowed! They're the same type!

```plaintext
// ACCEPTABLE
If you fight the dragon -> GOOD
If you run to the keep -> DEATH

// ACCEPTABLE
If you cut the red wire -> NEUTRAL
If you cut the green wire -> GOOD

// NOT ACCEPTABLE, WRONG! BREAKS RULES
If you fight the dragon -> NEUTRAL
If you run to the keep -> NEUTRAL

// NOT ACCEPTABLE, WRONG! BREAKS RULES
If you cut the red wire -> BAD
If you cut the green wire -> DEATH
// ^ BAD and DEATH are the SAME TYPE!

// NOT ACCEPTABLE, WRONG! BREAKS RULES
If you cut the red wire -> DEATH
If you cut the green wire -> DEATH

// NOT ACCEPTABLE, WRONG! BREAKS RULES
If you cut the red wire -> GOOD
If you cut the green wire -> GOOD
```

**Branch diversity**
- Early branches should diverge significantly (different locations, allies, or approaches). Later branches can have tighter focus.
- Avoid "false choices" where different options lead to the same outcome.

[ ] TODO: FINISH JSON OUTLINE (with 70-word passages throughout)

Add unique `id` fields to every node. Root is `"1"`, then children append choice numbers: `"1-1"`, `"1-2"`, then `"1-1-1"`, `"1-1-2"`, etc. Number choices in the order they appear in the `choices` object.

[ ] TODO: ADD IDs

Save the JSON file and the YAML file to its destination. Use the question tool to let the user confirm if you must continue or make changes.

[ ] TODO: ASK USER FOR APPROVAL

# JSON Outline Rules

1. **Root node** has `id: "1"`
2. **Child IDs** append to parent: `1-1`, `1-2`, then `1-1-1`, `1-1-2`, etc.
3. **Every node** has `id` and `text` fields
4. **Non-ending nodes** have a `choices` object with 2-3 choice keys
5. **Ending nodes** have an `end` field instead of `choices`
6. **`end` values**: `"GOOD"`, `"NEUTRAL"`, `"BAD"`, or `"DEATH"`
7. **`[BREAK]`** markers are used between scenes that take place in different places or after a time jump
8. **Text length**: Around 70 words per passage (see "HOW TO WRITE THE TEXT" section)

# TIPS

## When an ending is not acceptable

All stories should end in one of these ways: GOOD, NEUTRAL, BAD, DEATH. If the story is inconclusive, too open ended, or seems to end in the middle of its development, then the ending is NOT ACCEPTABLE. Think of this story as a television show. If the premise is a hero against a villain, you would not want to watch the hero go on vacation and forget about the mission.

Examples of NOT ACCEPTABLE endings:

* You get to Doctor Claude's control room and do nothing.
* You get to Captain Blackheart's island and just live there.
* You find Mr. Supercold's superweapon and go back to your house to play video games.

# TECHNICAL DETAILS

## Arguments

This skill expects arguments in the format:
```
/generate-outline <output-dir> [concept]
```

- `<output-dir>`: Directory where `summary.yaml` and `outline.json` will be written
- `[concept]`: Optional concept description. If not provided, ask the user for their idea.

Example: `/generate-outline my-book "A haunted lighthouse where time moves differently"`

## Output Files

You must produce exactly two files in the output directory:

### 1. `summary.yaml`

```yaml
Title: [CREATIVE TITLE IN ALL CAPS]
Description: [One compelling paragraph describing the world, protagonist, and central conflict]
Characters:
  - Name: [Character Name]
    Description: [2-3 sentences about appearance, personality, role in story]
  - Name: [Additional characters as needed]
```

### 2. `outline.json`

A nested JSON structure representing the entire branching story.

# HOW TO WRITE THE TEXT

These rules are essential for quality. Follow them strictly from the start—do NOT write short placeholder text and expand later.

## Text Length & Style

Each passage's `text` must be around **70 words**. Write as a single paragraph with no line breaks. Use vivid, short sentences. Include brief dialogue or key phrases where appropriate. Write in second person ("you").

**Before:**

> You and Thea fall into a net trap. A viking appears.

**After:**
> Night falls. You keep walking with Thea and, without realizing it, you step on a trap. Both of you are caught in a burlap rope net and are now hanging from a tree. Moments later, a blond man with a rough face and nearly two meters tall appears. A long beard, blond hair, and a horned helmet. A... Viking? "Ah, they're not even lizards... they're humans! Hmm. I'm not sure I can eat them. They don't look very tender," he says.

## Scene Pacing

Treat each node as a **movie scene**. Scenes can span variable time—from a couple of minutes (an intense fight) to entire days (a training montage).

**Avoid chaining short scenes.** It's not fun to make 10 mundane decisions like: open door, go upstairs, open room, check closet, take letter, read letter. More than 2-3 back-to-back scenes lasting only a couple of minutes makes the story feel rushed.

## Start and End

Each text should start with the result of the previous choice: consequences should feel logical based on choices made and the world of the story.

Each passage should end on a cliffhanger or turning point.

### Tease the choices ahead

The text should end by introducing and teasing the options available, without explicitly stating them as choices. Build tension by presenting the situation that leads naturally to the choices below.

**Example:**

If your choices are "If you jump the floating logs" and "If you use the sketchy flying broom", the text should end like:

> "In front of you, floating logs cross the chasm. You could try to jump. But then you remember: the sketchy flying broom!"

This creates anticipation and makes the choices feel organic to the narrative.

### Add elements related to the choices below

Choices must reference what's in the text. If a choice mentions a guard, rope, or door, the text must have introduced it first. Take the chance to introduce the elements of the choice in the text.

WRONG - mentions a guard that was never introduced:

```json
{
    "text": "You break free from your chains. Through the porthole, you see the island. There's a rope coiled nearby—you might be able to climb down to the water.",
    "choices": {
        "If you squeeze through the porthole and climb down": {...},
        "If you try to overpower a guard when they come to check on you": {...}
    }
}
```

RIGHT - the passage introduces the guard before offering the choice:

```json
{
    "text": "You break free from your chains. Through the porthole, you see the island. There's a rope coiled nearby. Suddenly, you hear footsteps—a guard is approaching. You could escape now, or wait to ambush him.",
    "choices": {
        "If you squeeze through the porthole and climb down": {...},
        "If you wait and overpower the guard when he enters": {...}
    }
}
```

### Use BREAK when the text is long and for scene transitions

Use `[BREAK]` to separate scenes within a passage when time jumps or location changes significantly:

> "You sprint toward the cliff edge and leap. The ground crumbles beneath you and you fall down the rocky slope. [BREAK] When you regain consciousness, you are tied up in a dark cave. A shadow moves in the corner..."

# HOW TO CREATE THE SUMMARY

Based on the outline create a summary in YAML format.

## Example Summary

```yaml
Title: LOST IN THE ISLAND OF TIME
Description: You and your uncle crash-land on a mysterious volcanic island while flying home from a beach trip. The island holds impossible secrets, living dinosaurs, a tribe of people displaced through time, a Viking warrior lost centuries from home, and TIME CORP, a sinister organization that has mastered time travel. To survive, you must navigate prehistoric dangers, forge unlikely alliances, and ultimately stop Doctor Claude's plan to control time itself.
Characters:
  - Name: Uncle
    Description: Your adventurous uncle. Resourceful and brave. He knows how to fly planes and helicopters, and how to use weapons.
  - Name: Thea
    Description: A young woman from a mysterious tribe. She wears burlap clothes, red paint over her eyes, and carries a bow. She speaks an ancient dialect.
  - Name: Grumsh
    Description: A Viking warrior with long blond hair, a rough beard, and a horned helmet. He wields an axe blessed by Odin.
  - Name: Doctor Claude
    Description: The main antagonist. An elderly, skeletal scientist with white hair, gray clothes, and black goggles. He leads TIME CORP and is obsessed with controlling time travel.
```

# PROCESS RECAP

When the user provides a concept, theme, or idea:

1. **Brainstorm** an exciting premise that works well for branching narratives
2. **Create 3-5 memorable characters** with distinct roles
3. **Design the branching structure** with varied path lengths and ending types
4. **Write the complete outline** with engaging text for every passage
5. **Output both files** in the exact formats specified

Make the story exciting, the choices meaningful, and the endings satisfying (or terrifyingly abrupt for deaths).

# FULL EXAMPLE

See these files in this skill's directory for a complete, production-quality example:  `example-summary.yaml` and `example-outline.json`.

Read `example-outline.json` to understand:
- The expected depth and branching structure
- How 70-word passages should read (vivid, engaging, proper pacing)
- How to introduce elements for upcoming choices
- Proper use of `[BREAK]` markers
- Distribution of ending types throughout the tree

This example shows the FINAL output format. All text should be written at this quality level from the start.
