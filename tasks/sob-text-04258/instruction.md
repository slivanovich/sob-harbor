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
The Best of Isaac Asimov: The Best of Isaac Asimov (Sphere, 1973) is a collection of twelve science fiction short stories by American writer Isaac Asimov.  It begins with a short introduction (six pages in the Doubleday hardcover edition) giving various details on the stories, such as how they came to be written, or what significance merits their inclusion in a "best of" collection, as well as some of Dr. Asimov's thoughts on a best of collection itself.  The stories included are two of his early works, two of his late works (post-1960), and eight from the 1950s, which he refers to as his "golden decade" in the introduction.  Except for the last story in the book, "Mirror Image", none of the stories are related to his "Robot" and "Foundation" series, while a few ("The Last Question", "The Dead Past", and "Anniversary") mention the Multivac computer.

Marooned off Vesta: "Marooned off Vesta" is a science fiction short story by American writer Isaac Asimov.  It was the third story written by him, and the first to be published.  Written in July 1938 when Asimov was 18, it was rejected by "Astounding Science Fiction" in August, then accepted in October by "Amazing Stories", appearing in the March 1939 issue.  Asimov first included it in his 1968 story collection "Asimov's Mysteries", and subsequently in the 1973 collection "The Best of Isaac Asimov".

Time Pussy: "Time Pussy" is an early science fiction short story by American writer Isaac Asimov.  It was the third of three stories Asimov wrote for John W. Campbell for a new category of science fiction tall tales in "Astounding Science Fiction" called "Probability Zero".  Campbell rejected the first two stories, "Big Game" and "First Law", since they were not what he was looking for, but he accepted "Time Pussy", albeit unenthusiastically.  Campbell also wanted to run the story under a pseudonym, since he wanted to encourage new writers to write "Probability Zero" stories.  Asimov agreed, and chose the name George E. Dale at random.  The story appeared pseudonymously in the April 1942 issue of "Astounding" and was reprinted under Asimov's name in the 1972 collection "The Early Asimov".

Robot Dreams: Robot Dreams (1986) is a collection of science fiction short stories by Isaac Asimov, illustrated by Ralph McQuarrie.  The title story is about Susan Calvin's discovery of a robot with rather disturbing dreams.  It was written specifically for this volume and inspired by the McQuarrie cover illustration.  All of the other stories had previously appeared in various other Asimov collections.  Four of the stories are robot stories, while five are Multivac stories.

The Billiard Ball: "The Billiard Ball" is a science fiction short story by American author Isaac Asimov, written in September 1966 and first published in the March 1967 issue of "If".  It appeared in Asimov's 1968 collection "Asimov's Mysteries", in his 1973 collection "The Best of Isaac Asimov", in his 1986 collection "Robot Dreams" and in "The Complete Stories, Vol.  2".

For the Birds (short story): "For the Birds" is a science fiction short story by Isaac Asimov.  The editor of a proposed fashion magazine wanted a science fiction story about a clothing designer.  Asimov agreed, and wrote the story in November 1978.  It was accepted, but the proposed magazine never appeared, and Asimov sold the story to "Asimov's Science Fiction".  "For the Birds" was published in the May 1980 issue of "Asimov's", and was reprinted in the 1983 collection "The Winds of Change and Other Stories".  The story was one of three Asimov wrote in the late 1970s set among a series of O'Neill-type space habitats.

Wizards (Asimov anthology): Wizards is an anthology of themed fantasy and science fiction short stories on the subject of wizards edited by Isaac Asimov, Martin H. Greenberg and Charles G. Waugh.  The first volume in their Isaac Asimov's Magical Worlds of Fantasy series, it was first published in paperback by Signet/New American Library in October 1983.  It was later gathered together with "Witches", the second book in the series, into the omnibus hardcover collection "Isaac Asimov's Magical Worlds of Fantasy: Witches & Wizards" (1985).

Ralph McQuarrie: Ralph Angus McQuarrie (June 13, 1929 – March 3, 2012) was an American conceptual designer and illustrator.  His career included work on the original "Star Wars" trilogy, the original "Battlestar Galactica" television series, the film "E.T. the Extra-Terrestrial", and the film "Cocoon", for which he won an Academy Award.

Witches (anthology): Witches is an anthology of themed fantasy and science fiction short stories on the subject of witches edited by Isaac Asimov, Martin H. Greenberg and Charles G. Waugh as the second volume in their Isaac Asimov's Magical Worlds of Fantasy series.  It was first published in paperback by Signet/New American Library in April 1984.  It was later gathered together with "Wizards", the first book in the series, into the omnibus hardcover collection "Isaac Asimov's Magical Worlds of Fantasy: Witches & Wizards" (1985).

The Last Question: "The Last Question" is a science fiction short story by American writer Isaac Asimov.  It first appeared in the November 1956 issue of "Science Fiction Quarterly" and was anthologized in the collections "Nine Tomorrows" (1959), "The Best of Isaac Asimov" (1973), "Robot Dreams" (1986), the retrospective "Opus 100" (1969), and in "Isaac Asimov: The Complete Stories, Vol.  1" (1990).  It was Asimov's favorite short story of his own authorship, and is one of a loosely connected series of stories concerning a fictional computer called Multivac.  The story overlaps science fiction, theology, and philosophy.

Question: Which collection of science fiction short stories by Isaac Asimov was illustrated by an American conceptual designer and illustrator who won an Academy Award for the film "Cocoon?"

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "collection_name": {
      "type": "string",
      "description": "The name of the science fiction short story collection."
    },
    "illustrator": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the illustrator."
        },
        "profession": {
          "type": "string",
          "description": "The profession of the illustrator."
        },
        "award_details": {
          "type": "object",
          "properties": {
            "award_name": {
              "type": "string",
              "description": "The name of the award won by the illustrator."
            },
            "award_for_film": {
              "type": "string",
              "description": "The film for which the award was won."
            }
          },
          "required": [
            "award_name",
            "award_for_film"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "name",
        "profession",
        "award_details"
      ],
      "additionalProperties": false
    },
    "illustration_role": {
      "type": "string",
      "description": "Describes the illustrator's role for the collection."
    }
  },
  "required": [
    "collection_name",
    "illustrator",
    "illustration_role"
  ],
  "additionalProperties": false
}
