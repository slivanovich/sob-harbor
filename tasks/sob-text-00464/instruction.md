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
Fanny Mendelssohn: Fanny Mendelssohn (14 November 1805 – 14 May 1847), later Fanny [Cäcilie] Mendelssohn Bartholdy and, after her marriage, Fanny Hensel, was a German pianist and composer.  She composed over 460 pieces of music.  Her compositions include a piano trio and several books of solo piano pieces and songs.  A number of her songs were originally published under her brother, Felix Mendelssohn's, name in his opus 8 and 9 collections.  Her piano works are often in the manner of songs, and many carry the name "Lied ohne Worte" ("Song without Words").  She also wrote, amongst other works for the piano, a cycle of pieces depicting the months of the year, "Das Jahr" ("The Year").  The music was written on coloured sheets of paper, and illustrated by her husband Wilhelm Hensel.  Each piece was also accompanied by a short poem.

Act Without Words II: Act Without Words II is a short mime play by Samuel Beckett, his second (after "Act Without Words I").  Like many of Beckett's works, the piece was originally composed in French ("Acte sans paroles II"), then translated into English by Beckett himself.  Written in the late 1950s it opened at the Calderon Press Institute in Oxford and was directed by John McGrath.  London premiere was directed by Michael Horovitz and performed at the Institute of Contemporary Arts, on 25 January 1960.  The first printing was in "New Departures" 1, Summer 1959.

Act Without Words I: Act Without Words I is a short play by Samuel Beckett.  It is a mime, Beckett's first (followed by "Act Without Words II").  Like many of Beckett's works, the play was originally written in French ("Acte sans paroles I"), being translated into English by Beckett himself.  It was written in 1956 following a request from the dancer Deryk Mendel and first performed on 3 April 1957 at the Royal Court Theatre in London.  On that occasion it followed a performance of "Endgame".  The original music to accompany the performance was written by composer John S. Beckett, Samuel's cousin, who would later collaborate with him on the radio play "Words and Music".

Cantabile: In music, cantabile ] , an Italian word, means literally "singable" or "songlike".  In instrumental music, it is a particular style of playing designed to imitate the human voice.  For 18th-century composers, cantabile is often synonymous with "cantando" (singing), and indicates a measured tempo and flexible, legato playing.  For later composers, particularly in piano music, cantabile is the drawing out of one particular musical line against the accompaniment (compare counterpoint).  Felix Mendelssohn's six books of "Songs Without Words (Lieder ohne Worte)" are short lyrical piano pieces with song-like melodies written between 1829 and 1845.  A modern example is an instrumental by Harry James & His Orchestra, called "Trumpet Blues and Cantabile".

Emanuel Vahl: Emanuel Vahl (Hebrew: עמנואל ואל‎ ‎ ; born in 1938 in Odessa, Ukraine) is a Ukrainian-Israeli composer.  Vahl has composed more than 100 works, including preludes, songs without words, and chamber music.  He taught Harmony and Composition at the Conservatory "Hasadna" in Jerusalem, and now he teaches at the Dance Studio of Jerusalem.  Vahl has been a member of the Union of Israeli Composers and AQUM since 1991.

Moonchild: Songs Without Words: Moonchild: Songs Without Words is an 2006 album by John Zorn featuring performances by Joey Baron, Mike Patton, and Trevor Dunn (sometimes referred to as the "Moonchild Trio").  It was inspired in part by Aleister Crowley, Antonin Artaud and Edgard Varèse.  "Moonchild: Songs Without Words" has been performed internationally by the trio, conducted by John Zorn.

Symphony No. 3 (Milhaud): The Symphony No. 3, Op. 271, sub-titled "Te Deum", is a work for orchestra and chorus by French composer Darius Milhaud.  The piece originated in a 1946 request by Radio France for a Te Deum celebrating the allied victory in World War II.  Instead of confining himself to a setting of the liturgical text, Milhaud delivered a four-movement symphony in which the orchestra plays two movements (I and III) alone.  The chorus joins without words in Movement II; only in the finale is the Latin text of the Te Deum sung.  This symphony is not to be confused with Milhaud's Chamber Symphony No. 3 "Sérénade," op. 71 (1921).

Edgard Varèse: Edgard Victor Achille Charles Varèse (] ; also spelled Edgar Varèse; December 22, 1883 – November 6, 1965) was a French-born composer who spent the greater part of his career in the United States.

Use Your Illusion: Use Your Illusion is a Guns N' Roses compilation album drawing from the "Use Your Illusion I" and "II" albums.  It has only been released in the United States, consisting entirely of songs without profanity (save for one use of "bullshit" on "14 Years").  However, not all songs without profanity were chosen to appear on this compilation, as "So Fine" and "Breakdown" from "Use Your Illusion II" contain no profanity.  The album was primarily sold at Walmart and Kmart, two retail outlets that refused to stock the unedited "Use Your Illusion I" and "II" due to explicit lyrics.

Songs Without Words: Songs Without Words ("Lieder ohne Worte ") is a series of short lyrical piano pieces by the Romantic composer Felix Mendelssohn, written between 1829 and 1845.

Question: Which french composer inspired Moonchild: Songs Without Words?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "album_title": {
      "type": "string",
      "description": "The title of the album in question."
    },
    "inspiration_sources": {
      "type": "array",
      "description": "A list of individuals or entities that inspired the album.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the inspiring individual."
          },
          "role": {
            "type": "string",
            "description": "The role or profession of the inspiring individual (e.g., composer, writer)."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the inspiring individual."
          }
        },
        "required": [
          "name"
        ],
        "additionalProperties": false
      }
    },
    "french_composer_inspiration": {
      "type": "string",
      "description": "The name of the French composer who inspired the album."
    }
  },
  "required": [
    "album_title",
    "inspiration_sources",
    "french_composer_inspiration"
  ],
  "additionalProperties": false
}
