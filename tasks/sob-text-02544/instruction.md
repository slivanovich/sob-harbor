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
The von Trapps: The von Trapps (formerly The von Trapp Children) is a musical group made up of Sofia, Melanie, Amanda and August (formerly Justin) von Trapp, descendants of the Trapp Family Singers.  They are the grandchildren of Werner von Trapp, who was portrayed as Kurt in "The Sound of Music", and the great-grandchildren of Georg Ritter von Trapp and his first wife Agathe Whitehead, and the step-great-grandchildren of Maria von Trapp, Georg's second wife.

Johanna von Trapp: Johanna Karolina (Franziska) von Trapp (7 September 1919 – 25 November 1994) was the sixth child of Georg Ritter von Trapp and his first wife, Agathe (née Whitehead).  She was a member of the Trapp Family Singers, whose lives were the inspiration for the play and film "The Sound of Music".  She was portrayed as the character "Marta".

Rupert von Trapp: Rupert Georg von Trapp, M.D. (1 November 1911 – 22 February 1992) was the firstborn child and eldest son of Georg von Trapp and his first wife, Agatha Whitehead von Trapp.  He was a member of the Trapp Family Singers, whose lives were the inspiration for the play and film "The Sound of Music".  He was portrayed as the character "Friedrich".

Martina von Trapp: Martina von Trapp (17 February 1921 – 25 February 1951) was a member of the Trapp Family Singers and was the seventh child of Georg von Trapp and his first wife, Agatha Whitehead von Trapp.  She was a member of the Trapp Family Singers, whose lives were the inspiration for the play and movie "The Sound of Music".  She was portrayed as the character "Gretl".

Agathe von Trapp: Agathe Johanna Erwina Gobertina von Trapp (12 March 1913 – 28 December 2010) was the eldest daughter of Georg von Trapp and his first wife, Agatha Whitehead von Trapp.  She was also a member of the Trapp Family Singers, whose lives were the inspiration for the play and film "The Sound of Music".  She was portrayed as the character "Liesl".

Maria Franziska von Trapp: Maria Agatha Franziska Gobertina von Trapp (28 September 1914 – 18 February 2014) was the second-oldest daughter of Georg von Trapp and his first wife, Agatha Whitehead von Trapp.  She was a member of the Trapp Family Singers, whose lives inspired the musical and film "The Sound of Music".  She was portrayed as the character "Louisa".  She died at age 99, and was the last surviving sibling portrayed in the film.

Maria von Trapp: Maria Augusta von Trapp (née Kutschera; 26 January 1905 – 28 March 1987), also known as Baroness von Trapp, was the stepmother and matriarch of the Trapp Family Singers.  She wrote "The Story of the Trapp Family Singers" which was published in 1949.  The story served as the inspiration for the 1956 West German film "The Trapp Family", which in turn inspired the Broadway musical "The Sound of Music" (1959) and the 1965 film of the same name.

Werner von Trapp: Werner Ritter von Trapp (21 December 1915 – 11 October 2007) was the second-oldest son of Georg von Trapp and his first wife, Agatha Whitehead von Trapp.  He was a member of the Trapp Family Singers, whose lives were the inspiration for the play and movie "The Sound of Music".  He was portrayed as the character "Kurt".

Hedwig von Trapp: Hedwig Maria Adolphine Gobertina von Trapp (28 July 1917 – 14 September 1972) was the fifth child of Georg von Trapp and his first wife, Agatha Whitehead von Trapp.  She was a member of the Trapp Family Singers, whose lives were the inspiration for the play and movie "The Sound of Music".  She was portrayed as the character "Brigitta".

Edelweiss (song): "Edelweiss" is a show tune from the 1959 Rodgers and Hammerstein musical "The Sound of Music".  It is named after the edelweiss, a white flower found high in the Alps "(Leontopodium alpinum)".  It was created for the 1959 Broadway production of "The Sound of Music" in the role originated by performer Theodore Bikel as a song for the character of Captain Georg Ludwig von Trapp.  In the musical, Captain von Trapp and his family sing this song during the concert near the end of Act II as a statement of Austrian patriotism in the face of the pressure put upon him to join the navy of Nazi Germany following the Anschluss.  It is also Captain von Trapp's subliminal goodbye to his beloved homeland, using the flower as a symbol of his loyalty to Austria.  In the 1965 film adaptation, the song is also sung by the Captain earlier in the film when he rediscovers music with his children.

Question: Warner von Trapp, the grandfather of The von Trapps, was the inspiration for what movie?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the individual mentioned in the question."
    },
    "relationship_to_group": {
      "type": "string",
      "description": "The relationship of the individual to 'The von Trapps' musical group."
    },
    "portrayed_character": {
      "type": "string",
      "description": "The character the individual was portrayed as in the movie."
    },
    "inspired_movie": {
      "type": "string",
      "description": "The name of the movie that the individual's life inspired or in which they were portrayed."
    }
  },
  "required": [
    "person_name",
    "relationship_to_group",
    "portrayed_character",
    "inspired_movie"
  ],
  "additionalProperties": false
}
