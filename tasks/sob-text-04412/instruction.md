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
Giovacchino Forzano: Giovacchino Forzano (] ; 19 November 1884 – 28 October 1970) was an Italian playwright, librettist, stage director, and film director.  A resourceful writer, he authored numerous popular plays and produced opera librettos for most of the major Italian composers of the early twentieth century, including the librettos for Giacomo Puccini's "Suor Angelica" and "Gianni Schicchi".

O mio babbino caro: "O mio babbino caro " ("Oh My Beloved Father") is a soprano aria from the opera "Gianni Schicchi" (1918) by Giacomo Puccini to a libretto by Giovacchino Forzano.  It is sung by Lauretta after tensions between her father Schicchi and the family of Rinuccio, the boy she loves, have reached a breaking point that threatens to separate her from Rinuccio.  It provides an interlude expressing lyrical simplicity and single-hearted love in contrast with the atmosphere of hypocrisy, jealousy, double-dealing, and feuding in the medieval Florence of Puccini's only comedy.  It provides the only set-piece in the through-composed opera.

Marie Tiffany: Marie Berg Tiffany (July 8, 1881 - April 12, 1948) was an American operatic soprano.  She was a member of the Metropolitan Opera in Manhattan, New York City from 1916 to 1928; making a total of 208 appearances at the Met during her career.  She created roles in several world premieres at the Met and was notably the only performer to appear in all three one act operas at the premiere of Giacomo Puccini's "Il Trittico" in 1918.

Suor Angelica: Suor Angelica (Sister Angelica) is an opera in one act by Giacomo Puccini to an original Italian libretto by Giovacchino Forzano.  It is the second opera of the trio of operas known as "Il trittico" ("Triptych").  It received its world premiere at the Metropolitan Opera on December 14, 1918.

Giuseppe De Luca: Giuseppe De Luca (25 December 1876 – 26 August 1950), was an Italian baritone who achieved his greatest triumphs at the Metropolitan Opera in New York City.  He notably created roles in the world premieres of two operas by Giacomo Puccini: Sharpless in "Madama Butterfly" (at La Scala, Milan, 1904) and the title role in "Gianni Schicchi" (Metropolitan Opera, 1918).

Gianni Schicchi discography: This is a list of the recordings of Gianni Schicchi, the third of a group of three one-act operas by Giacomo Puccini collectively known as "Il trittico"; the other operas are "Il tabarro" and "Suor Angelica".  The three were premiered at the Metropolitan Opera on 14 December 1918, and for the next three years were always played together.  After 1921, however, Puccini agreed that the operas could be performed separately. " Gianni Schicchi" became the most popular and most frequently performed of the three, often paired with other works such as Maurice Ravel's "L'heure espagnole" and Richard Strauss's "Salome".

Anna Nechaeva: Anna Nechaeva is Russian soprano singer who was born in Saratov and used attend its Conservatory in 1996.  Later she was offered to perform the role of "Tatiana" in "Eugene Onegin" at the Saint Petersburg Conservatory and by 2003 became a soloist at the Saint Petersburg Opera where she continued her original role as well as other title roles in Giacomo Puccini's "Gianni Schicchi", Madama Butterfly, and "Suor Angelica".  From 2008 to 2011 she became a soloist at the Mikhaylovsky Theatre where she performed roles of "Nedda" in "Pagliacci" and "Rachel" in "The Jews" as well as the title roles of "Rusalka" and of course "Tatiana" in "Eugene Onegin".  In 2012, she made her first public appearance with Bolshoi Theatre where she sang in "The Enchantress" portraying "Nastasya" becoming soloist there the same year.  After her debut, she performed such roles as "Iolanta" in an opera of the same name as well as "Liu" in "Turandot" and "Yaroslavna" in "Prince Igor".

Il trittico: Il trittico ("The Triptych") is the title of a collection of three one-act operas, "Il tabarro", "Suor Angelica", and "Gianni Schicchi", by Giacomo Puccini.  The work received its world premiere at the Metropolitan Opera on 14 December 1918.

Gianni Schicchi: Gianni Schicchi (] ) is a comic opera in one act by Giacomo Puccini to an Italian libretto by Giovacchino Forzano, composed in 1917–18.  The libretto is based on an incident mentioned in Dante's "Divine Comedy".  The work is the third and final part of Puccini's "Il trittico" (The Triptych)—three one-act operas with contrasting themes, originally written to be presented together.  Although it continues to be performed with one or both of the other "trittico" operas, "Gianni Schicchi" is now more frequently staged either alone or with short operas by other composers.  The aria "O mio babbino caro" is one of Puccini's best known, and one of the most popular arias in opera.

Il tabarro: Il tabarro (The Cloak) is an opera in one act by Giacomo Puccini to an Italian libretto by Giuseppe Adami, based on Didier Gold's play "La houppelande".  It is the first of the trio of operas known as "Il trittico".  The first performance was given on 14 December 1918 at the Metropolitan Opera in New York City.

Question: What is the name of the soprano aria from the opera "Gianni Schicchi" (1918), the third and and final part of Giacomo Puccini's "Il trittico"?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "aria_name": {
      "type": "string",
      "description": "The name of the soprano aria."
    },
    "opera_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the opera from which the aria originates."
        },
        "composer": {
          "type": "string",
          "description": "The composer of the opera."
        },
        "librettist": {
          "type": "string",
          "description": "The librettist of the opera."
        },
        "premiere_year": {
          "type": "integer",
          "description": "The year the opera premiered."
        }
      },
      "required": [
        "title",
        "composer",
        "librettist",
        "premiere_year"
      ],
      "additionalProperties": false
    },
    "collection_details": {
      "type": "object",
      "properties": {
        "collection_title": {
          "type": "string",
          "description": "The title of the collection of operas to which this opera belongs."
        },
        "part_number": {
          "type": "integer",
          "description": "The sequential number of the opera within its collection."
        },
        "total_parts": {
          "type": "integer",
          "description": "The total number of operas in the collection."
        }
      },
      "required": [
        "collection_title",
        "part_number",
        "total_parts"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "aria_name",
    "opera_details",
    "collection_details"
  ],
  "additionalProperties": false
}
