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
Hala Strana: Hala Strana (Bulgarian for "salt beach") is the name of a recording project of American musician Steven R. Smith.  Smith began recording under the name in 2002 as an outlet which allowed him to explore the traditional music of Eastern Europe more fully than possible with his solo work.  Although numerous musicians have contributed to the project, including Glenn Donaldson, Loren Chasse, and Darren Ankenman, most Hala Strana recordings are solo productions.  His recordings have included such diverse instruments as hurdy-gurdy, bouzouki, harmonium, spike fiddles, bul bul tarang, the optigan keyboard, xaphoon, and field recordings.  Hala Strana’s releases have featured arrangements of traditional music from Hungary, Romania, Croatia, Albania, Ukraine and Bulgaria as well as original music influenced by the music of these areas.  Hala Strana has recorded for a number of independent labels such as Soft Abuse, Last Visible Dog, Jewelled Antler, and Emperor Jones.

Boscoe Holder: Boscoe Holder (16 July 1921 – 21 April 2007), born Arthur Aldwyn Holder in Port of Spain, Trinidad and Tobago, was Trinidad and Tobago's leading contemporary painter, who also had a celebrated international career spanning six decades as a designer and visual artist, dancer, choreographer and musician.  In 1948 he married the dancer Sheila Davis Clarke, daughter of radio personality Kathleen Davis (a.k.a. "Aunty Kay"), and their son Christian was born the following year.  Christian Holder eventually became a leading dancer with the Joffrey Ballet and an artist in his own right.  Living in London, England, during the 1950s and 1960s, Boscoe Holder has been credited with introducing limbo dancing and steel-pan playing to Britain, performing on British television and radio, in variety and nightclubs, in films, and at well-known theatres in the West End.  His company also danced for Queen Elizabeth II at her coronation in 1953, and, in two years later, at Windsor Castle.

The Emperor Jones (1933 film): The Emperor Jones is a 1933 American pre-Code film adaptation of the Eugene O'Neill play of the same title, was made outside of the Hollywood studio system, financed with private money from neophyte wealthy producers, and directed by iconoclast Dudley Murphy, who had sought O'Neill's permission to film the play since its 1924 production in New York.  He cast Paul Robeson in his first film role, Dudley Digges, Frank H. Wilson, and Fredi Washington.  The screenplay was written by DuBose Heyward and filmed at Kaufman Astoria Studios with the beach scene shot at Jones beach Long Beach, New York.  Robeson starred in the O'Neill play on stage, both in the United States and England, a role that had helped launch his career.

Charles Sidney Gilpin: Charles Sidney Gilpin (November 20, 1878 – May 6, 1930) was one of the most highly regarded stage actors of the 1920s.  He played in critical debuts in New York City: the 1919 premier of John Drinkwater’s "Abraham Lincoln" and the lead role of Brutus Jones in the 1920 premier of Eugene O'Neill's "The Emperor Jones", also touring with the play.  In 1920 he was the first black American to receive the Drama League of New York's annual award as one of the 10 people who had done the most that year for American theater.

Tallahassee (album): Tallahassee is the seventh studio album by the Mountain Goats.  It was the band's second new album to be released in 2002, and it marked quite a few changes.  First of all, after releasing records (and cassettes) on small record labels such as Shrimper, Ajax, and Emperor Jones, "Tallahassee" was the first Mountain Goats album to be released on a widely known independent label, the British alternative rock label 4AD.  It was also the first Mountain Goats album to have an official single released, for the song "See America Right."

The Emperor Jones (1953 film): The Emperor Jones was a 1953 BBC Television production of the Eugene O'Neill play of the same title, and transmitted live on 7 July that year.  It was adapted and directed by Alvin Rakoff (uncredited), starring Gordon Heath in the title role, with music by Billy Shalanki and choreography by Boscoe Holder.  The production was not recorded, and is now lost.  As summarised in "The Radio Times", "The action of the play takes place on an island in the West Indies as yet not fully exploited by Western civilisation."

The Emperor Jones (opera): The Emperor Jones is an opera in two acts with a prologue and interlude composed by Louis Gruenberg to an English-language libretto adapted by the composer from Eugene O'Neill's 1920 play, "The Emperor Jones".  It premiered on January 7, 1933, at the Metropolitan Opera in New York City with Lawrence Tibbett in the title role.  Set on an unnamed island in the West Indies, the opera tells the story of African American Brutus Jones, a former Pullman porter and ex-convict who escaped to the island, set himself up as its tyrannical "Emperor", and became rich by exploiting the natives.  The natives start a revolt against him, and as he tries to escape through the jungle, he is haunted by visions of his past life and the man he had murdered.  As the natives close in, he commits suicide using the silver bullet which he had worn around his neck as a good-luck charm.  With a score that incorporates elements of jazz and negro spirituals, "The Emperor Jones" was the eleventh American opera to premiere at the Met, and has continued to be performed into the 21st century, albeit rarely.

Trumans Water (album): Trumans Water is a 2001 album by Trumans Water.  The CD version (released by Emperor Jones) has a slightly different track list than the LP (released in the UK by Delboy Records in March 2002).

The Emperor Jones (1955 film): The Emperor Jones is a 1955 film adaptation of the Eugene O'Neill play of the same title produced by the "Kraft Television Theatre" anthology series starring Ossie Davis in the title role.

The Emperor Jones: The Emperor Jones is a 1920 play by American dramatist Eugene O'Neill that tells the tale of Brutus Jones, a resourceful, self-assured African American and a former Pullman porter, who kills another black man in a dice game, is jailed, and later escapes to a small, backward Caribbean island where he sets himself up as emperor.  The play recounts his story in flashbacks as Brutus makes his way through the jungle in an attempt to escape former subjects who have rebelled against him.

Question: In what year was the choreographer of "The Emperor Jones" born?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "choreographer": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "birth_year": {
          "type": "integer"
        },
        "death_year": {
          "type": "integer"
        },
        "primary_roles": {
          "type": "array",
          "items": {
            "type": "string"
          }
        }
      },
      "required": [
        "name",
        "birth_year",
        "primary_roles"
      ],
      "additionalProperties": false
    },
    "production_identified": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string"
        },
        "year": {
          "type": "integer"
        },
        "media_type": {
          "type": "string"
        }
      },
      "required": [
        "title",
        "year",
        "media_type"
      ],
      "additionalProperties": false
    },
    "choreographer_birth_year": {
      "type": "integer"
    }
  },
  "required": [
    "choreographer",
    "production_identified",
    "choreographer_birth_year"
  ],
  "additionalProperties": false
}
