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
Sub Sub: Sub Sub were an English dance act from Handforth, Cheshire composed of Jimi Goodwin and twin brothers Andy and Jez Williams.

The Worst of Black Box Recorder: The Worst of Black Box Recorder is a 2001 album by Black Box Recorder, whose members include Luke Haines, Sarah Nixey and John Moore.  It is a compilation of B-sides from the singles of "England Made Me" and "The Facts Of Life".

Jimi Goodwin: Jimi Goodwin (born Jamie Francis Alexander Goodwin 28 May 1970 in Manchester) is the bassist, vocalist and guitarist for Doves.  Before their incarnation as Doves, the three members were in a house music group, Sub Sub.

From Every Sphere: From Every Sphere is the second album by British singer-songwriter Ed Harcourt, released in 2003.  Heavenly Records labelmate Jimi Goodwin of Doves plays tambourine on the first single "All of Your Days Will Be Blessed."

Odludek: Odludek is the debut solo album by Jimi Goodwin, released on Heavenly Recordings on 24 March 2014.  The album follows a few years after his band, Doves, announced they were taking an "indefinite hiatus."  The word "odludek" is a Polish word, meaning "pilgrim" or "loner."  Goodwin wrote and played almost everything on "Odludek" himself, with only a handful of guest musicians, including Elbow frontman Guy Garvey and former Dungen member Fredrik Bjorling, and the album was recorded and co-produced with Dan Austin at a studio in the Forest of Dean across 18 months.  Goodwin said, "Initially I wanted to have loads of guests on it.  Maybe I wasn't trusting my own instincts because I'd collaborated in a band for such a long time, but that idea soon went out the window.  Very quickly I decided I wanted to get my Prince head on and play everything.  I became very protective of it.  There was no-one steering me.  I made it myself and paid for it myself, and that was very free and liberating."

Sarah Nixey: Sarah Anne Nixey (born 21 December 1973 in Dorset, England) is a British singer songwriter, best known as the vocalist in Black Box Recorder.  Her debut solo album, "Sing, Memory", was released on 19 February 2007, followed by "Brave Tin Soldiers", released on 9 May 2011.  Nixey currently lives in London with her husband, music producer Jimmy Hogarth, whom she married in late 2010 and has one son, Reuben (born late 2007) and a daughter, Lola (born late 2012).  Nixey has a daughter, Ava (born 2001) from her previous marriage with John Moore.

Sing, Memory: Sing, Memory is the debut album from British Black Box Recorder vocalist, Sarah Nixey.  Recorded in London, and produced by James Banbury, the album is split into two halves, "Sing" and "Memory".  The title is probably a reference to Vladimir Nabokov's autobiography, "Speak, Memory".  It was released in the UK on February 19, 2007.

England Made Me (album): England Made Me is the debut studio album by English indie rock band Black Box Recorder, whose members include Luke Haines, Sarah Nixey and John Moore, released in July 1998 via Chrysalis Records.

Mathematics (Cherry Ghost song): "Mathematics" is the debut single from Manchester band Cherry Ghost.  It was released as a digital download on March 26, 2007 and on CD and 7" vinyl on April 9, 2007.  It went to #57 on the UK singles chart.  "Mathematics" acquired the title "song of the week" on BBC Radio 2 in early 2007, and Zane Lowe of BBC Radio 1 declared the song "the hottest record in the world" in February 2007.  Jimi Goodwin of Doves plays bass and drums on the single.  The B-side "Junebug" is a Sparklehorse cover.

People Help the People: "People Help the People" is the second single taken from Cherry Ghost's début album, "Thirst for Romance".  It was made available to download on 11 June 2007, and followed two weeks later on CD and 7" vinyl.  The band played the song live on "Later... with Jools Holland" on 24 November 2006.  Jimi Goodwin of the band Doves plays drums on the single.  "People Help the People" peaked the UK Singles Chart at #27.  The song was also a hit in Italy.

Question: What do Jimi Goodwin and Sarah Nixey have in common?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "common_role": {
      "type": "string",
      "description": "The specific role that both individuals share."
    },
    "individuals_involved": {
      "type": "array",
      "description": "Details about each individual involved in the commonality.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the individual."
          },
          "primary_group": {
            "type": "string",
            "description": "The primary group or band the individual is associated with for this role."
          }
        },
        "required": [
          "name",
          "primary_group"
        ],
        "additionalProperties": false
      }
    },
    "reasoning": {
      "type": "string",
      "description": "An explanation of how the common role was identified from the context."
    }
  },
  "required": [
    "common_role",
    "individuals_involved",
    "reasoning"
  ],
  "additionalProperties": false
}
