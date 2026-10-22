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
Mechanize: Mechanize is the seventh studio album by American heavy metal band Fear Factory.  It is the only album to feature Gene Hoglan on drums and the first since 2001's "Digimortal" to include original guitarist and founding member Dino Cazares, who rejoined the band after a reconciliation with lead vocalist Burton C. Bell, in April 2009.  The album was produced by Rhys Fulber, who had not produced or been involved with a Fear Factory album since "Archetype".  The album has received mostly positive reviews from fans and music critics, being praised for its very aggressive and heavy sound.  In its first week of release, the album sold 10,000 copies.

Clark Brown: Clark Ernst Brown is the vocalist for GZR.  He took over from Burton C. Bell, who had guested on "Plastic Planet" (1995) and has remained since.  Clark is also the vocalist for SYMATIC, a Hardcore Metal band out of Massachusetts.

Shock (Fear Factory song): "Shock" is a song by American heavy metal band Fear Factory.  It was the lead single from their 1998 album "Obsolete" and the first track on the album.  Its music was composed by guitarist Dino Cazares and drummer Raymond Herrera.  The lyrics were written by vocalist Burton C. Bell.  The introduction of a concept album, "Shock" introduces its protagonist, a political prisoner known only as Edgecrusher, who declares his personal mission to destroy the totalitarian society in which he lives.

Demanufacture (album): Demanufacture is the second studio album by American industrial metal band Fear Factory, released on June 13, 1995 by Roadrunner Records.  Burton C. Bell wrote a majority of the lyrics and Dino Cazares wrote all the music.  This is the band's first album with their classic line-up adding new bassist Christian Olde Wolbers.  Although credited as Fear Factory's official bassist, Christian Olde Wolbers only played live.  Many regard it as the band's best album and a heavy metal classic.  The album was certified Gold in Australia by ARIA and Silver in the UK by the BPI.

Descent (song): "Descent" is a single by American heavy metal band Fear Factory from their album "Obsolete".  It was the third single released and the fifth track on the album.  The music was composed by guitarist Dino Cazares and drummer Raymond Herrera, with lyrics by Burton C. Bell.  In the storyline of "Obsolete's" concept, "Descent" expresses the despair felt by the album's protagonist, the dissident Edgecrusher, as he rests briefly on his flight from the pursuing forces of Securitron.  He questions the worth of his personal mission; in the end, he decides to continue his fight against his oppressors.

Digimortal (album): Digimortal is the fourth studio album by American industrial metal band Fear Factory, released on April 24, 2001 by Roadrunner Records.  It is a concept album and a sequel to "Obsolete", their previous album (which was a continuation to "Demanufacture") and the final part of a trilogy.  This was the band's last album before officially breaking up in March 2002.  Although "Digimortal" was not a commercial success, this was not given as reason for the band's breakup, instead citing frontman Burton C. Bell's desire to "form a band that's more indie-rock-oriented."  Fear Factory would officially reform in 2003, however, to begin work on their next album, "Archetype".  "Digimortal" was the last to feature founding guitarist/songwriter Dino Cazares for eight years until his return to the band in 2009.

Yoon Chae-kyung: Yoon Chae-kyung (born July 7, 1996), is a South Korean singer and actress.  She originally debuted in 2012 as a member of Japan-based South Korean girl-group Puretty under DSP Media.  She is also known as a contestant of "Kara Project" (2014) and "Produce 101" (2016).

Burton C. Bell: Burton Christopher Bell (born February 19, 1969) is an American musician and vocalist.  Bell is best known as co-founder and frontman of the metal band Fear Factory.  His singing style mixes clean and shouted vocals with death growls.

Plastic Planet: Plastic Planet is an album by GZR (known at the time as g//z/r), a Heavy metal band featuring Geezer Butler of Black Sabbath.  The album features Fear Factory vocalist Burton C. Bell.

City of Fire (band): City of Fire is a groove metal band from Canada, formed in 2008.  Members include vocalist Burton C. Bell of Fear Factory, bassist Byron Stroud from Fear Factory, Strapping Young Lad and Zimmers Hole, and drummer Bob Wagner of Econoline Crush.  City of Fire has so far released a self-titled album, issued in Australia in April 2010 and worldwide in August.  The second pressing of the album contained additional "bonus tracks", one of which was a cover of the T-Rex song "Children of the Revolution".  Several poorly recorded sample portions of their songs were uploaded on the band's MySpace page throughout 2009, often accompanied with video (consisting mostly of studio footage).

Question: Yoon Chae-kyung and Burton C. Bell, have similar occupations?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_1_name": {
      "type": "string",
      "description": "The name of the first person mentioned."
    },
    "person_1_occupations": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of occupations for the first person."
    },
    "person_2_name": {
      "type": "string",
      "description": "The name of the second person mentioned."
    },
    "person_2_occupations": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of occupations for the second person."
    },
    "occupations_similar": {
      "type": "boolean",
      "description": "True if their occupations are similar, false otherwise."
    }
  },
  "required": [
    "person_1_name",
    "person_1_occupations",
    "person_2_name",
    "person_2_occupations",
    "occupations_similar"
  ],
  "additionalProperties": false
}
