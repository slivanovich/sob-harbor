Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
Mitya's Love: Mitya's Love (Митина любовь, "Mi′tina Lyubo′v") is a short novel by a Nobel Prize-winning Russian author Ivan Bunin written in 1924 and first published in books XXIII and XXIV of the "Sovremennye Zapiski" Paris-based literary journal in 1925.  It also featured in (and gave the title to) a compilation of novelets and short stories published the same year in France.

Thug Notes: Thug Notes is an American educational web series that summarizes and analyzes various literary works in a comedic manner.  "Thug Notes" first aired on June 3, 2013, on YouTube, with the pilot episode centered on "Crime and Punishment".  The host of the series is Sparky Sweets, Ph.D., portrayed by actor and comedian Greg Edwards.

Demons (Dostoyevsky novel): Demons (Russian: Бесы , "Bésy") is a novel by Fyodor Dostoyevsky, first published in the journal "The Russian Messenger" in 1871–2.  It is considered one of the four masterworks written by Dostoyevsky after his return from Siberian exile, along with "Crime and Punishment" (1866), "The Idiot" (1869) and "The Brothers Karamazov" (1880).  "Demons" is a social and political satire, a psychological drama, and large scale tragedy.  Joyce Carol Oates has described it as "Dostoevsky's most confused and violent novel, and his most satisfactorily 'tragic' work."  According to Ronald Hingley, it is Dostoyevsky's "greatest onslaught on Nihilism", and "one of humanity's most impressive achievements—perhaps even its supreme achievement—in the art of prose fiction."

The Brothers Karamazov: The Brothers Karamazov (Russian: Бра́тья Карама́зовы , "Brat'ya Karamazovy", ] ), also translated as The Karamazov Brothers, is the final novel by the Russian author Fyodor Dostoyevsky.  Dostoyevsky spent nearly two years writing "The Brothers Karamazov", which was published as a serial in "The Russian Messenger" from January 1879 to November 1880.  The author died less than four months after its publication.

The Cossacks (novel): The Cossacks (Russian: Казаки ["Kazaki"]) is a short novel by Leo Tolstoy, published in 1863 in the popular literary magazine "The Russian Messenger".  It was originally called "Young Manhood".  Both Ivan Turgenev and the Nobel prize-winning Russian writer Ivan Bunin gave the work great praise, Turgenev calling it his favorite work by Tolstoy.  Tolstoy began work on the story in August 1853.  In August 1857, after having reread the "Iliad", he vowed to completely rewrite "The Cossacks".  In February 1862, after having lost badly at cards he finished the novel to help pay his debts.  The novel was published in 1863, the same year his first child was born.

The Time: Night: The Time: Night (Russian: Время ночь ) is a novella by Russian author Lyudmila Petrushevskaya.  It was originally published in Russian in the literary journal "Novy Mir" in 1992 and translated into English by Sally Laird in 1994.  In 1992 it was shortlisted for the Russian Booker Prize.

The Princess (Maykov poem): The Princess (Russian: Княжна , Knyazhna) is a poem by Apollon Maykov first published in the January 1878 issue of "The Russian Messenger".  It told the story of a young Russian girl belonging to a noble family who joined a group of radical youth fighting against the repressive state.  The poem, condemned by the Russian literary left of the time, in retrospect is seen as a strong political statement attacking both the corrupt political system of mid-19th-century Russia, based on serfdom and the violent methods of undermining it, as professed by the 'nihilistic' youth of the time.

At Daggers Drawn (novel): At Daggers Drawn (Russian: На ножах ) is an anti-nihilist novel by Nikolai Leskov, first published in 1870 (issues 10-12) and 1871 (issues 1-8, 10) by "The Russian Messenger".  In November 1871 the novel was released as a separate book.  The novel's original text has been severely edited by the magazine's staff.

Crime and Punishment: Crime and Punishment (Russian: Преступлéние и наказáние , "Prestupleniye i nakazaniye"; ] ) is a novel by the Russian author Fyodor Dostoyevsky.  It was first published in the literary journal "The Russian Messenger" in twelve monthly installments during 1866.  Later, it was published in a single volume.  It is the second of Dostoyevsky's full-length novels following his return from 5 years of exile in Siberia.  "Crime and Punishment" is considered the first great novel of his "mature" period of writing.

The Idiot: The Idiot (Russian: Идио́т , "Idiot") is a novel by the 19th-century Russian author Fyodor Dostoyevsky.  It was first published serially in the journal "The Russian Messenger" in 1868–9.

Question: Which novel by a Russian author was first published in the literary journal "The Russian Messenger" and was used by  American educational web series Thug Notes, which had their pilot episode centered on it?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "final_answer_novel_title": {
      "type": "string",
      "description": "The title of the novel that matches all criteria."
    },
    "novel_information": {
      "type": "object",
      "description": "Details about the identified novel.",
      "properties": {
        "title": {
          "type": "string",
          "description": "The full title of the novel."
        },
        "author": {
          "type": "string",
          "description": "The author of the novel."
        },
        "author_nationality": {
          "type": "string",
          "description": "The nationality of the novel's author."
        },
        "first_publication_details": {
          "type": "object",
          "description": "Information about the novel's initial publication.",
          "properties": {
            "journal_name": {
              "type": "string",
              "description": "The name of the literary journal where the novel was first published."
            },
            "year": {
              "type": "integer",
              "description": "The year the novel was first published."
            }
          },
          "required": [
            "journal_name",
            "year"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "title",
        "author",
        "author_nationality",
        "first_publication_details"
      ],
      "additionalProperties": false
    },
    "thug_notes_information": {
      "type": "object",
      "description": "Details about the 'Thug Notes' episode related to the novel.",
      "properties": {
        "series_name": {
          "type": "string",
          "description": "The name of the educational web series."
        },
        "episode_type": {
          "type": "string",
          "description": "The type of episode (e.g., 'pilot')."
        },
        "air_date": {
          "type": "string",
          "description": "The date the episode first aired."
        },
        "host": {
          "type": "string",
          "description": "The host of the 'Thug Notes' series."
        }
      },
      "required": [
        "series_name",
        "episode_type",
        "air_date",
        "host"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "final_answer_novel_title",
    "novel_information",
    "thug_notes_information"
  ],
  "additionalProperties": false
}
