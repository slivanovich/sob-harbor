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
World Shut Your Mouth (song): "World Shut Your Mouth" is a song by the English singer-songwriter Julian Cope.  It is the first single released in support of his third album "Saint Julian".  The title of the song is the same as Cope's first solo album, "World Shut Your Mouth".

Saint Julian (album): Saint Julian is the third solo album by Julian Cope.  It has a very strong pop sound, compared to other Cope releases, and spawned several of his best known tracks (including "World Shut Your Mouth" and "Trampolene", which were both hit singles).

The Four Seasons (band): The Four Seasons is an American rock and pop band that became internationally successful in the 1960s and 1970s.  The Vocal Group Hall of Fame has stated that the group was the most popular rock band before the Beatles.  Since 1970, they have also been known at times as Frankie Valli and the Four Seasons.  In 1960, the group known as the Four Lovers evolved into the Four Seasons, with Frankie Valli as the lead singer, Bob Gaudio (formerly of the Royal Teens) on keyboards and tenor vocals, Tommy DeVito on lead guitar and baritone vocals, and Nick Massi on electric bass and bass vocals.

Julian Cope: Julian David Cope (born 21 October 1957) is an English musician, author, antiquarian, musicologist, poet and cultural commentator.  Originally coming to prominence in 1978 as the singer and songwriter in Liverpool post-punk band the Teardrop Explodes, he has followed a solo career since 1983 and worked on musical side projects such as Queen Elizabeth, Brain Donor and Black Sheep.

Thighpaulsandra: Thighpaulsandra (Tim Lewis) is a Welsh experimental musician and multi-instrumentalist known mostly for performing on synthesizers and keyboards.  As Tim Lewis, he began his career working with Julian Cope.  A collaboration with Cope in 1993 followed, as the experimental duo Queen Elizabeth.  This project completed just the two albums, "Queen Elizabeth" (ESP Records 1994) and "Elizabeth Vagina" (Head Heritage 1997), each containing extremely long spacey tracks of between 20–47 minutes in duration.  In 1997, former Cope guitarist Mike Mooney invited Lewis to fill for the departing Kate Radley on a Spiritualized tour, where he remained until early 2008.  In 1999 he also became a member of the experimental band Coil.  He has subsequently released several solo albums.

Peggy Suicide: Peggy Suicide is the seventh album by Julian Cope.  It is generally seen as the beginning of Cope's trademark sound and approach, and as a turning-point for Cope as a maturing artist.

Rite²: Rite² is an ambient music album by Julian Cope, released in 1997.  It is technically Cope’s fourteenth solo album, but is also the follow-up to the earlier album "Rite" (released in 1992 and credited to "Julian Cope & Donald Ross Skinner") and is the second in the "Rite" series.

Jehovahkill: Jehovahkill is the eighth album by Julian Cope, released in 1992.  After the critical success of "Peggy Suicide" (1991), Cope's idea for "Jehovakill" was to incorporate a krautrock attitude into his music.  He began recording the album with musicians Rooster Cosby and Donald Ross Skinner, while co-producing it with the latter.  The sessions yielded what Cope considered to be his most sonically experimental material to date.  Originally titleing the record "Julian H. Cope", he sent an eleven track version to Island Records, who initially rejected its release, but relentfully gave Cope extra recording sessions for the album.  During the extra sessions, in which six extra songs were recorded, the album became harder and was retitled "Jehovahkill".

Floored Genius: Floored Genius - The Best of Julian Cope and The Teardrop Explodes 1979-91 is a compilation album by Julian Cope, released in 1992, combining Cope's work with The Teardrop Explodes and his early solo work.

Love Peace &amp; Fuck: Love Peace & Fuck is the 2001 debut album by Julian Cope side project Brain Donor, released on Impresario records as a double LP.  It was written, produced and directed by Cope along with long term collaborator Thighpaulsandra.  The album was recorded by the power pop trio of Cope, lead guitarist Doggen Foster and drummer Kevin Bales, both formerly of Spiritualized.  Cope plays bass, a role he had not assumed since The Teardrop Explodes in the late 1970s.

Question: Are The Four Seasons and Julian Cope the same nationality?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "question_asked": {
      "type": "string",
      "description": "The original question posed."
    },
    "entity_1": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "Name of the first entity."
        },
        "nationality": {
          "type": "string",
          "description": "Nationality of the first entity."
        }
      },
      "required": [
        "name",
        "nationality"
      ],
      "additionalProperties": false
    },
    "entity_2": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "Name of the second entity."
        },
        "nationality": {
          "type": "string",
          "description": "Nationality of the second entity."
        }
      },
      "required": [
        "name",
        "nationality"
      ],
      "additionalProperties": false
    },
    "are_same_nationality": {
      "type": "boolean",
      "description": "True if both entities share the same nationality, false otherwise."
    }
  },
  "required": [
    "question_asked",
    "entity_1",
    "entity_2",
    "are_same_nationality"
  ],
  "additionalProperties": false
}
