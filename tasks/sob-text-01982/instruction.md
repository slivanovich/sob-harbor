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
Puppydog Tales: Rosie & Ruff in "Puppydog Tales" is a British children's television cartoon created by Hilary Hayton, creator of "Crystal Tipps and Alistair".  The show was narrated and scripted by Victoria Wood.  The series was originally broadcast on the BBC in 1992 only running for 13 episodes but was repeated through till 1996.

Ryde or Die Vol. 1: Ryde or Die Vol.  1 is a compilation album from American hip-hop record label Ruff Ryders Entertainment, released on April 27, 1999.

Heichū Monogatari: Tales of Heichū (Heichū monogatari) belongs to the genre of uta monogatari poem tales that emerged in Japanese literature from the mid 10th to the early 11th centuries.  As early as the "Collection of Ten-Thousand Leaves" ("Manyōshū"), a poetry collection completed around 759, there appeared poems introduced by brief prose narrations.  The imperial court began to come alive with poetry from around this time.  People exchanged poetry with one another on topics as diverse as love and politics and religion.  Towards the end of the 9th century it was common for individual poets to keep compilations of their own verse, sometimes explaining in prose the circumstances behind a poem's composition.  The highest honor was to have ones poem selected for inclusion in the "Collection of Ancient and Modern Poetry" (Kokinshū), the first imperial poetry collection, which was completed around 905.  By the middle of the 10th century the idea of a poem paired with a prose narration seems to have taken hold, and "Tales of Ise" (Ise monogatari), "Tales of Heichū", and "Tales of Yamato" (Yamato monogatari) seem to have emerged at about this same time.  Also, the second imperial poetry collection, "Collection of Later Poetry" (Gosenshū), commissioned in 951 and compiled shortly thereafter, has many narrative qualities.  The only extant manuscript of "Tales of Heichū" is a 61-page codex discovered in 1931 that seems to date from the Kamakura Period (1185–1333), some three hundred years after the work's probable date of composition.

Faerie Tale Theatre: Faerie Tale Theatre (also known as Shelley Duvall's Faerie Tale Theatre) is an American award-winning live-action children's anthology television series, starring many famous and well known actors (particularly of the period) including Robin Williams, consisting of 27 episodes retelling 25 classic fairy tales, particularly of The Brothers Grimm, plus the poem The Pied Piper of Hamelin and a special episode called "The Grimm's Party", showcasing the series cast and crew, (including Duvall and Teri Garr), that originally aired on Showtime from September 11, 1982 until November 14, 1987.  Shelley Duvall, who created the series served as narrator, host and executive producer of the program alongside Fred Fuchs, and occasionally starred in episodes.  The series was followed by two other, albeit less successful shorter anthology series "Tall Tales & Legends" (episode 9) which followed the same format as "Faerie Tale Theatre" and focused on classic American folk tales and third series Nightmare Classics (4 episodes, originally planned as 6).  This was one of the first examples of cable original programming, alongside HBO's "Fraggle Rock".

Victoria Wood: Victoria Wood (19 May 1953 – 20 April 2016) was an English comedian, actress, singer and songwriter, screenwriter and director.  Wood wrote and starred in sketches, plays, musicals, films and sitcoms, and her live comedy act was interspersed with her own compositions, which she performed on piano.  Much of her humour was grounded in everyday life and included references to quintessentially "British" activities, attitudes and products.  She was noted for her skills in observing culture and in satirising social classes.

Jigga My Nigga: "Jigga My Nigga" is a single by Jay-Z from the Ruff Ryders Entertainment compilation "Ryde or Die Vol.  1".  It also appeared as a hidden track on Jay-Z's fourth album, "Vol.  3... Life and Times of S. Carter", contained within the final track "Hova Song (Outro)".  Produced by Swizz Beatz, it reached number 28 on the "Billboard" Hot 100.  The song interpolates "Just Me, Just You" by The Counts and "What's My Name? " by Snoop Dogg, using the line "what's my motherfuckin' name?" .  The beat was later remade for "Scenario 2000" by Eve featuring Ruff Ryders.

Ryde or Die Vol. 3: In the &quot;R&quot; We Trust: Ryde or Die Vol.  3: In the "R" We Trust is a compilation album from American hip hop record label Ruff Ryders Entertainment, released on December 18, 2001.  The album was certified Gold by the RIAA in August 2002 (500,000 units).

The Ribbajack: The Ribbajack & Other Curious Yarns is a fantasy book by Brian Jacques, published in 2004.  It was published the same year as the Redwall book (his more known fantasy series) "Rakkety Tam".  There are six tales in this book, all of them like the tales in "Seven Strange and Ghostly Tales", by the same author.  The titles are: "The Ribbajack", "A Smile and a Wave", "The All Ireland Champion Versus the Nye Add", "The Mystery of Huma D'Este", "Miggy Mags and the Malabar Sailor", and "Rosie's Pet."

Katha mitho sarangiko: Katha Mitho Sarangiko ("Sweet Tales of Sarangi", Nepali: कथा मीठो सारंगीको) is a weekly Nepali radio drama produced by BBC Media Action, the charity wing of the BBC.  It was first broadcast in February 2008.  It is improvised and, apart from the linking narration, is recorded entirely on location, mainly in rural communities in Nepal.  The sarangi, mentioned in the title, is a traditional Nepali stringed instrument, played with a bow.  The narrator of the drama is a sarangi player from the Gandharba caste of traditional, itinerant musicians.  The drama comprises a series of tales that the narrator, Prakash Gandharba, tells as he goes about his travels.  The cast varies according to the story being told; if the story is set in a rural community the majority of the roles are played by people from the community who have never acted before.  The cast of story lines set in Kathmandu is predominantly made up of professional actors.  The drama is rich in sound and music.  It has been funded by a three different donors: UNDP, DFID and UNFPA.

Brothers Grimm: The Brothers Grimm ("die Brüder Grimm " or "die Gebrüder Grimm "), Jacob and Wilhelm Grimm, were German academics, philologists, cultural researchers, lexicographers and authors who together collected and published folklore during the 19th century.  They were among the best-known storytellers of folk tales, and popularized stories such as "Cinderella" ("Aschenputtel "), "The Frog Prince" ("Der Froschkönig "), "The Goose-Girl" ("Die Gänsemagd"), "Hansel and Gretel" ("Hänsel und Gretel "), "Rapunzel", "Rumpelstiltskin" ("Rumpelstilzchen "), "Sleeping Beauty" ("Dornröschen "), and "Snow White" ("Schneewittchen ").  Their first collection of folk tales, "Children's and Household Tales" ("Kinder- und Hausmärchen "), was published in 1812.

Question: On what date did the narrator of Rosie & Ruff in Puppydog Tales die?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "narrated_show": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the television show."
        },
        "genre": {
          "type": "string",
          "description": "The genre of the television show."
        }
      },
      "required": [
        "title",
        "genre"
      ],
      "additionalProperties": false
    },
    "narrator_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the narrator."
        },
        "role": {
          "type": "string",
          "description": "The role of the person in the show."
        },
        "birth_date": {
          "type": "string",
          "description": "The birth date of the narrator."
        },
        "death_date": {
          "type": "string",
          "description": "The death date of the narrator."
        }
      },
      "required": [
        "name",
        "role",
        "birth_date",
        "death_date"
      ],
      "additionalProperties": false
    },
    "answer_death_date": {
      "type": "string",
      "description": "The specific date of the narrator's death."
    }
  },
  "required": [
    "narrated_show",
    "narrator_details",
    "answer_death_date"
  ],
  "additionalProperties": false
}
