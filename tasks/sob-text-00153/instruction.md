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
Fred Ball (producer): Fred Ball is a record producer and songwriter living in London.  He is originally from Fredrikstad in Norway.  Fred moved to the UK when he formed his solo project "Pleasure".  The debut album was hailed as The Sunday Times’ favourite debut of the year.  It featured artists such as Justine Frischmann, Ed Harcourt and Dr. Fink.  "Pleasure" launched the start of Fred¹s songwriting and production career.

Suede discography: The discography of the English alternative rock band Suede consists of seven studio albums, three compilation albums, five video albums and over twenty singles. Suede were formed in 1989 by singer Brett Anderson, bassist Mat Osman and guitarist Justine Frischmann.  Guitarist Bernard Butler later joined after the group responded to an ad in the "Melody Maker".  The group played as a four-piece with a drum machine until drummer Simon Gilbert joined.  Frischmann left before the group released any material.

Love and Poison (book): Love and Poison is the official biography of the English alternative rock band Suede.  The book, written by long-time band associate David Barnett, reveals the real stories behind singer Brett Anderson's battle with drugs, his relationship with Elastica's Justine Frischmann and the subsequent feud with Blur after she started stepping out with Damon Albarn.

Stutter (Elastica song): "Stutter" is a song by the Britpop group Elastica and was written by lead singer Justine Frischmann.  It was originally released as a single in 1993 and then included on the band's 1995 self-titled debut album.  The single, which received positive reviews from critics, charted in the US and Canada.

Galang (song): "Galang" is a song by British musician M.I.A. from her debut album "Arular".  It was released on Showbiz Records in 2003 as her first single, which pressed 500 vinyl copies, gaining immediate international recognition via radio airplay, fashion shows, club rotations and internet filesharing.  "Galang" was re-released on 1 November 2004 via XL Recordings as the second single from the album released by the label and was released for a third time as "Galang '05" on 11 October 2005 by the label and in the US by Interscope Records.  It is written by Maya "M.I.A." Arulpragasam, Justine Frischmann, Ross Orton and Steve Mackey.  It first appeared on M.I.A.'s six song demo tape in 2003, her official MySpace account on 9 June 2004 and was later reworked slightly by Orton and Mackey who received production credit for the song.  "Galang" was the second song M.I.A. wrote on her Roland MC-505, intending for the piece to be performed by Frischmann's band Elastica.  Inspired by her experiences and observations of life in London, M.I.A. wrote the song to encourage her friends in the band to continue to make music.  However, after cowriting the song, Frischmann convinced M.I.A. to record "Galang" herself, complimenting the piece's lyrical narrative and music direction.

Pleasure (Norwegian band): Pleasure is a Norwegian funky pop band, led by Fred Ball.  One single was released in 2003, "Don't Look The Other Way", which featured Justine Frischmann (former lead singer for Elastica) on vocals.

No Distance Left to Run: "No Distance Left to Run" is a song by Blur.  It is on their 1999 album "13" and was also released as the third and final single from the album, reaching number 14 in the UK Singles Chart.  It is widely understood to refer to Blur vocalist Damon Albarn's split from long-term partner Justine Frischmann.

Justine Frischmann: Justine Elinor Frischmann (born 16 September 1969) is an English artist and former musician, best known for being the lead singer of the Britpop band Elastica.  She is now pursuing a career as a painter.

M. Shadows: Matthew Charles Sanders (born July 31, 1981), better known as M. Shadows, is an American singer, songwriter, and musician.  He is best known as the lead vocalist, songwriter, and a founding member of the American heavy metal band Avenged Sevenfold.  In 2017, he was voted 3rd in the list of Top 25 Greatest Modern Frontmen by Ultimate Guitar.

Arular: Arular is the debut studio album by English recording artist M.I.A..  It was released on 22 March 2005 in the United States, and one month later in the United Kingdom, with a slightly different track listing.  In 2004, the album's release was preceded by two singles and a mixtape.  M.I.A. wrote or co-wrote all the songs on the album and created the basic backing tracks using a Roland MC-505 sequencer/drum machine given to her by long-time friend Justine Frischmann.  Collaborators included Switch, Diplo, Richard X, Ant Whiting and Greg "Wizard" Fleming.  The album's title is the political code name used by her father, Arul Pragasam, during his involvement with Sri Lankan Tamil militant groups, and themes of conflict and revolution feature heavily in the lyrics and artwork.  Musically, the album incorporates styles that range from hip hop and electroclash to funk carioca and punk rock.

Question: Which musician is older, M. Shadows or Justine Frischmann?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "musician_comparison": {
      "type": "object",
      "properties": {
        "musician_1": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "The name of the first musician."
            },
            "birth_year": {
              "type": "integer",
              "description": "The birth year of the first musician."
            }
          },
          "required": [
            "name",
            "birth_year"
          ],
          "additionalProperties": false
        },
        "musician_2": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "The name of the second musician."
            },
            "birth_year": {
              "type": "integer",
              "description": "The birth year of the second musician."
            }
          },
          "required": [
            "name",
            "birth_year"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "musician_1",
        "musician_2"
      ],
      "additionalProperties": false
    },
    "older_musician_name": {
      "type": "string",
      "description": "The name of the musician who is older."
    },
    "age_difference_years": {
      "type": "integer",
      "description": "The difference in birth years between the two musicians."
    }
  },
  "required": [
    "musician_comparison",
    "older_musician_name",
    "age_difference_years"
  ],
  "additionalProperties": false
}
