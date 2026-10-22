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
Carol Sklenicka: Carol Sklenicka (born 1948 in San Luis Obispo, California) is an American biographer and essayist best known as the author of "Raymond Carver: A Writer's Life", the first comprehensive biography of short story writer Raymond Carver.

Dana Sawyer: Dana Sawyer was born in Jonesport, Maine in 1951.  He is a full-time professor of religion and philosophy at the Maine College of Art and an adjunct professor in Asian Religions at the Chaplaincy Institute of Maine.  He is the author of numerous published papers and books, including "Aldous Huxley: A Biography", which Laura Huxley described as, "Out of all the biographies written about Aldous, this is the only one he would have actually liked."  In 2014, Sawyer's authorized biography of Huston Smith was published.

Who Are We? (album): Who Are We?  is a 1955 recording of Aldous Huxley giving a lecture at the Vedanta Society of Southern California's Hollywood temple.  The lecture was originally recorded on a wire recorder and digitally transferred to CD.  Huxley was a student of Swami Prabhavananda, who founded the Society.  Along with Christopher Isherwood and other notable disciples of the Swami, Huxley would occasionally give lectures at the society's temples in Hollywood and Santa Barbara.

Elspeth Huxley: Elspeth Joscelin Huxley CBE (née Grant; 23 July 1907 – 10 January 1997) was an author, journalist, broadcaster, magistrate, environmentalist, farmer, and government adviser.  She wrote over 40 books, including her best-known lyrical books, "The Flame Trees of Thika" and "The Mottled Lizard", based on her youth in a coffee farm in British Kenya.  Her husband, Gervas Huxley, was a grandson of Thomas Huxley and a cousin of Aldous Huxley.

Knowledge and Understanding: Knowledge and Understanding is a 1955 recording of Aldous Huxley giving a lecture at the Vedanta Society of Southern California's Hollywood temple.  The lecture was originally recorded on a wire recorder and digitally transferred to CD.  Huxley was a student of Swami Prabhavananda, who founded the Society.  Along with Christopher Isherwood and other notable disciples of the Swami, Huxley would occasionally give lectures at the society's temples in Hollywood and Santa Barbara.

Raymond Carver: Raymond Clevie Carver Jr. (May 25, 1938 – August 2, 1988) was an American short-story writer and poet.  Carver contributed to the revitalization of the American short story during the 1980s.

Huxley on Huxley: Huxley on Huxley is a 2009 documentary directed by Mary Ann Braubach, narrated by Peter Coyote and includes interviews with Laura Huxley, drummer John Densmore (whose band, The Doors, was named after Aldous Huxley’s 1954 book, The Doors of Perception), spiritual leader Ram Dass, Esalen co-founder Michael Murphy, artist Don Bachardy, philosopher Huston Smith and actor Nick Nolte, star of the adaptation of Aldous Huxley's 1955 novel "The Genius and the Goddess".  The film features archival footage of Aldous Huxley, Timothy Leary, Mike Wallace, and Igor Stravinsky, and photographs from Laura and Aldous Huxley’s personal collection, as well as other historical archives.

Aldous Huxley: Aldous Leonard Huxley ( ; 26 July 1894 – 22 November 1963) was an English writer, novelist, philosopher, and prominent member of the Huxley family.  He graduated from Balliol College at the University of Oxford with a first-class honours in English literature.

After Many a Summer: After Many a Summer (1939) is a novel by Aldous Huxley that tells the story of a Hollywood millionaire who fears his impending death.  It was published in the United States as After Many a Summer Dies the Swan.  Written soon after Huxley left England and settled in California, the novel is Huxley's examination of American culture, particularly what he saw as its narcissism, superficiality, and obsession with youth.  This satire also raises philosophical and social issues, some of which would later take the forefront in Huxley's final novel "Island".  The novel's title is taken from Tennyson's poem "Tithonus", about a figure in Greek mythology to whom Aurora gave eternal life but not eternal youth.  The book was awarded the 1939 James Tait Black Memorial Prize for fiction.

Between Heaven and Hell (novel): Between Heaven and Hell: A Dialog Somewhere Beyond Death with John F. Kennedy, C. S. Lewis, & Aldous Huxley is a novel by Peter Kreeft about U.S. President John F. Kennedy, and authors C. S. Lewis ("The Chronicles of Narnia") and Aldous Huxley ("Brave New World") meeting in Purgatory and engaging in a philosophical discussion on faith.  It was inspired by the fact that all three men died on the same day: November 22, 1963.  We see from the three points of view: Kennedy's "modern Christian" view, Lewis's "conservative Christian" or "mere Christian" view, and Huxley's "Orientalized Christian" view.  The book progresses as Lewis and Kennedy discuss Jesus' being God incarnate, to Lewis and Huxley discussing whether or not Jesus was a deity or "just a good person."

Question: Who has more scope of profession, Aldous Huxley or Raymond Carver?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_with_broader_scope": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of the person with the broader scope of profession."
        },
        "professions": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of professions held by this person."
        },
        "profession_count": {
          "type": "integer",
          "description": "The total number of distinct professions for this person."
        }
      },
      "required": [
        "name",
        "professions",
        "profession_count"
      ],
      "additionalProperties": false
    },
    "person_with_narrower_scope": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of the person with the narrower scope of profession."
        },
        "professions": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of professions held by this person."
        },
        "profession_count": {
          "type": "integer",
          "description": "The total number of distinct professions for this person."
        }
      },
      "required": [
        "name",
        "professions",
        "profession_count"
      ],
      "additionalProperties": false
    },
    "comparison_result": {
      "type": "string",
      "description": "States which person has a broader scope of profession."
    }
  },
  "required": [
    "person_with_broader_scope",
    "person_with_narrower_scope",
    "comparison_result"
  ],
  "additionalProperties": false
}
