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
Scott Hull (musician): Scott Hull (born March 4, 1971) is an American grindcore musician, and the current guitarist and producer for Pig Destroyer, Agoraphobic Nosebleed, and Japanese Torture Comedy Hour.  He has been part of many other projects including the controversial band Anal Cunt (also known as AC or AxCx).  Aside from his music works, he currently works as a government computer specialist.  Hull is noted for his experimental style of guitar playing that incorporates various influences, as well as for his use of eight string and seven string guitars.

Anal Cunt: Anal Cunt, also known as AxCx and A.C., was an American grindcore band that formed in Newton, Massachusetts in 1988.  Since its inception, the band underwent a number of line-up changes.  Known for its grindcore musical style and controversial lyrics, Anal Cunt released eight full-length studio albums in addition to a number of compilations and extended plays.  Anal Cunt disbanded in 2011 after the group's founder and frontman, Seth Putnam, died of a suspected heart attack.

Old Stuff – Part 3: Old Stuff, Part 3 is a compilation album by grindcore band Anal Cunt.  The album contains a demo recorded for a Boston hardcore compilation that was never released (most of these songs were later rerecorded for the album "I Like It When You Die").  It also contains songs from The Raunchous Brothers split 7", songs from various tribute compilations, and other previously unreleased songs.  It was released on CD on July 24, 2008, and on LP in April 2009.  The LP comes with an exclusive poster.  All songs on this album were recorded in the late 1990s.

Seth Putnam: Seth Edward Putnam (May 15, 1968 – June 11, 2011) was an American musician who was the founder of grindcore band Anal Cunt.  He was known for his brutal screaming and lyrics that either shock, offend, or invoke morbid humor.  Throughout his career, Putnam had been involved in many side projects, including backing vocals on Pantera's "The Great Southern Trendkill."

Fuckin' A: Fuckin' A is the eighth and final full-length album by the grindcore band Anal Cunt.  It was released digitally on August 10, 2010, and then physically on January 11, 2011.  The album is intended to be a parody of "cock rock" bands such as Mötley Crüe and Buckcherry and its cover uses the same image as Mötley Crüe's debut album "Too Fast for Love".  Some versions of the CD cover had the umlaut in "Anal" moved to the N, and a completely different font for the album title.

40 More Reasons to Hate Us: 40 More Reasons to Hate Us is the third album by Anal Cunt, recorded after their Japanese Tour in June 1995 and released on March 26, 1996, by Earache Records.  The name of the album reflected the notoriety that the band had achieved due to their controversial song titles and lyrics.

Everyone Should Be Killed: Everyone Should Be Killed is the debut full-length studio album by American grindcore band Anal Cunt, released by Earache Records on May 24, 1994.

Anal Cunt discography: Anal Cunt was an American grindcore band from Newton, Massachusetts.  Formed in 1988, the band released eight studio albums, one live album, five compilation albums, eleven extended plays (EPs) and eight split EPs. Anal Cunt disbanded in 2011 due to the death of frontman Seth Putnam.

Picnic of Love: Picnic of Love is the fifth album by Anal Cunt.  It was released on July 21, 1998.  The album was released as a joke and a parody of love songs, as well as of the band itself.  The album is characterized by the opposite of everything that the band represents.  While the normal Anal Cunt album consists of forty to fifty tracks (most which are under a minute in length), "Picnic of Love" contains only eleven comparably long tracks.  The extreme metal distorted guitars, rapid-fire drumming and loud screaming of earlier Anal Cunt songs is replaced by soft acoustic guitar and vocalist Putnam singing in gentle falsetto.  The most apparent change is the lyrical content: all of the songs are about inoffensive, sweet subjects as opposed to the band's more typical deliberately offensive or provocative material.

Top 40 Hits: Top 40 Hits is the second full-length album by Anal Cunt, released in 1995 on CD and cassette by Earache Records.

Question: When was the frontman of Anal Cunt died?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "frontman_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the frontman."
        },
        "role": {
          "type": "string",
          "description": "The role of the person in the band."
        },
        "birth_date": {
          "type": "string",
          "format": "date",
          "description": "The birth date of the frontman in YYYY-MM-DD format."
        },
        "death_date": {
          "type": "string",
          "format": "date",
          "description": "The death date of the frontman in YYYY-MM-DD format."
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
    "band_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the band."
        },
        "disbandment_year": {
          "type": "integer",
          "description": "The year the band disbanded."
        },
        "disbandment_reason": {
          "type": "string",
          "description": "The reason for the band's disbandment."
        }
      },
      "required": [
        "name",
        "disbandment_year",
        "disbandment_reason"
      ],
      "additionalProperties": false
    },
    "final_answer": {
      "type": "object",
      "properties": {
        "frontman_death_date": {
          "type": "string",
          "format": "date",
          "description": "The specific date of the frontman's death in YYYY-MM-DD format."
        }
      },
      "required": [
        "frontman_death_date"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "frontman_details",
    "band_details",
    "final_answer"
  ],
  "additionalProperties": false
}
