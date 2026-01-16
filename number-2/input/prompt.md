Write a complete Choose Your Own Adventure book with the following rules and constraints.

# General structure:

* The book is written in second person. The reader is the protagonist.
* The story begins on page 1.
* Pages are numbered and not sequential in reading order.
* Each page contains narrative action only.
* Each page must end with either:
  * A list of choices that direct the reader to other numbered pages, or
  * A final “THE END” message.

# Branching and pagination:

* Choices must explicitly reference page numbers, for example:
  * “If you choose to take the train, turn to page 23.”
  * “If you choose to take the plane, turn to page 56.”
* All referenced pages must exist and be fully written.
* Write at least 65 pages in total.
* Include at least 15 distinct endings.
* There must be no orphaned pages. Every page except page 1 must be reachable through at least one choice.
* Leave no gaps in page numbers. Pages 1 through 60 must all be present and contain content.

# Story requirements:

* Use the user’s suggested theme and title if provided.
* Describe action in vivid, sensory detail. Focus on movement, tension, sights, sounds, and emotions.
* Keep the tone engaging, adventurous, and accessible.
* The content must be family friendly and appropriate for young readers.

# Output format:

* Write a markdown file per page, ie `1.md`, `2.md`, etc.
* Link choices to the corresponding page, ie `turn to [page 22](./22.md)`
