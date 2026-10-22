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
Mind Your Manners (Pearl Jam song): "Mind Your Manners" is a song by the American alternative rock band Pearl Jam.  It was released on July 11, 2013 as a digital download as the lead single from their tenth studio album "Lightning Bolt".  Writing for "The Globe and Mail", Brad Wheeler said the song was "lean, swift and punishing".  Pearl Jam guitarist Mike McCready said "It's my attempt to try to make a really hard edge-type Dead Kennedys-sounding song".  Singer Eddie Vedder's lyrics criticize organized religion, which Vedder considers hypocritical for their intolerance and "so many of the things which have come out of those organizations– like the abuse of children and then its cover-up."

Love Boat Captain: "Love Boat Captain" is a song by the American rock band Pearl Jam.  Featuring lyrics written by vocalist Eddie Vedder and music co-written by Vedder and keyboardist Boom Gaspar, "Love Boat Captain" was released on February 18, 2003 as a single from the band's seventh studio album, "Riot Act" (2002).

Light Years (Pearl Jam song): "Light Years" is a song by the American rock band Pearl Jam.  Featuring lyrics written by vocalist Eddie Vedder and music co-written by Vedder and guitarists Mike McCready and Stone Gossard, "Light Years" was released on July 18, 2000 as the second and final single from the band's sixth studio album, "Binaural" (2000).  The song peaked at number 17 on the "Billboard" Mainstream Rock Tracks chart.  The song was included on Pearl Jam's 2004 greatest hits album, "rearviewmirror (Greatest Hits 1991–2003)".

Water on the Road: Water on the Road is a film released on DVD and Blu-ray by American singer and Pearl Jam frontman Eddie Vedder.  It documents Vedder's 2008 solo tour, during which he performed Pearl Jam songs, numerous covers, and solo works including songs from the "Into the Wild Soundtrack".  The film features mostly performances from two shows Vedder performed on August 16 and 17, 2008, at Warner Theatre in Washington, D.C. It was released on May 31, 2011.

Hi! School: Love On: Hi!  School: Love On (Korean: 하이스쿨: 러브온 ) is a 2014 South Korean television series starring Kim Sae-ron, Nam Woo-hyun and Lee Sung-yeol of the band Infinite.  It aired on KBS2 from July 11 to December 19, 2014 on Fridays at 20:55 for 20 episodes.

Nam Woo-hyun: Nam Woo-hyun (Hangul: 남우현 ; Hanja: 南優賢 ; born February 8, 1991), commonly known by his mononym Woohyun, is a South Korean singer and actor with the boy band Infinite.  In 2016 he released a solo album.

Oceans (Pearl Jam song): "Oceans" is a song by the American rock band Pearl Jam.  Featuring lyrics written by vocalist Eddie Vedder and music co-written by Vedder, guitarist Stone Gossard, and bassist Jeff Ament, "Oceans" was released in 1992 as the fourth single from the band's debut album, "Ten" (1991).  Remixed versions of the song can be found on the "Even Flow" single and the 2009 "Ten" reissue.

Jeremy (song): "Jeremy" is a song by the American rock band Pearl Jam, with lyrics written by vocalist Eddie Vedder and music written by bassist Jeff Ament.  "Jeremy" was released in 1992 as the third single from Pearl Jam's debut album "Ten" (1991).  The song was inspired by a newspaper article Vedder read about a high school student who shot himself in front of his English class on January 8, 1991.  It reached the number five spot on both the Mainstream and Modern Rock "Billboard" charts.  It did not originally chart on the regular "Billboard" Hot 100 singles chart since it was not released as a commercial single in the US at the time, but a re-release in July 1995 brought it up to number 79.

Black (Pearl Jam song): "Black" is a power ballad by the American rock band Pearl Jam.  The song is the fifth track on the band's debut album, "Ten" (1991).  Featuring lyrics written by vocalist Eddie Vedder and music written by guitarist Stone Gossard, "Black" is said to be about first relationships, though Vedder showed strong emotion while performing the song live in early years.  (In relationship with Beth Liebling from 1983-2000) Notably, Vedder now renders the added lyric "We belong together" as "I've been healed" or "We didn't belong together" indicating his moving on from the relationship and being content with how it ended.

Eddie Vedder: Eddie Vedder (born Edward Louis Severson; December 23, 1964) is an American musician, singer and songwriter best known as a member of the rock band Pearl Jam, with whom he performs lead vocals and is one of three guitarists.  He is known for his powerful baritone vocals.  He also appeared as a guest vocalist in Temple of the Dog, the one-off tribute band dedicated to the late singer Andrew Wood.

Question: Was Nam Woo-hyun or Eddie Vedder born first?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_a": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "birth_date": {
          "type": "string",
          "format": "date"
        },
        "birth_year": {
          "type": "integer"
        }
      },
      "required": [
        "name",
        "birth_date",
        "birth_year"
      ],
      "additionalProperties": false
    },
    "person_b": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "birth_date": {
          "type": "string",
          "format": "date"
        },
        "birth_year": {
          "type": "integer"
        }
      },
      "required": [
        "name",
        "birth_date",
        "birth_year"
      ],
      "additionalProperties": false
    },
    "comparison_result": {
      "type": "object",
      "properties": {
        "born_first_name": {
          "type": "string"
        },
        "born_first_year": {
          "type": "integer"
        },
        "born_second_name": {
          "type": "string"
        },
        "born_second_year": {
          "type": "integer"
        }
      },
      "required": [
        "born_first_name",
        "born_first_year",
        "born_second_name",
        "born_second_year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "person_a",
    "person_b",
    "comparison_result"
  ],
  "additionalProperties": false
}
