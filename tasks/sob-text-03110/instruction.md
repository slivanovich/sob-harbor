{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nKasabian: Kasabian ( ) are an English rock band formed in Leicester in 1997.  The band's original members consisted of vocalist Tom Meighan, guitarist and vocalist Sergio Pizzorno, guitarist Chris Karloff, and bassist Chris Edwards.  The band's line-up was completed by drummer Ian Matthews in 2004 after a string of session drummers.  Karloff left the band in 2006 and founded a new band called Black Onassis.  Jay Mehler joined as touring lead guitarist in 2006.  Mehler left the band for Liam Gallagher's Beady Eye in 2013, to be replaced by Tim Carter.  In 2010 and 2014, Kasabian won the Q Awards for 'Best Act in the World Today', while they were also named \"Best Live Act\" at the 2014 Q Awards and the 2007 NME Awards.  The band's music is often described as \"indie rock\", but Pizzorno has said he \"hates indie bands\" and does not feel Kasabian fit into that category.\n\nThe Sabres of Paradise: The Sabres of Paradise were a British experimental group formed in London, England in 1992.  Although their roots were in the acid house scene, they later produced more dub-inspired work.  Andrew Weatherall formed the group with engineers Jagz Kooner and Gary Burns and became responsible for the Sabresonic warehouse raves.  Keith \"Radioactive Man\" Tenniswood joined the group after meeting Jagz at Phil Perry's Full Circle club, Sabres dissolved in 1995.  Weatherall went on to form Two Lone Swordsmen with Keith Tenniswood while Kooner and Burns carried on working with The Aloof, and Jagz has also kept a consistent remix and production career.  His remix \"My Beautiful Friend\" for The Charlatans was groundbreaking and it inspired Eddie Temple Morris, a DJ at the X FM radio station, to form a show dedicated to remixes.  Kooner also worked with Oasis, Garbage, Massive Attack, Kasabian and Primal Scream.\n\nOutcrowd: Outcrowd was a punk, alternative rock trio band formed in Lexington Park, Maryland in 1986 (then later by relocation to NYC/NJ) by Todd Morse (guitars & vocals), Todd Friend (drums) and Gene Booth (bass).  Outcrowd performed frequently around the Washington D.C, New York City, Baltimore, Philadelphia, New England & other East Coast scenes, opening for and performing with bands such as The Ramones, Fugazi, Government Issue, Scream, Soulside, Circle Jerks, Murphy's Law, Dead Milkmen, Verbal Assault, Token Entry, Black Train Jack, McRad, Gorilla Biscuits, Sick of It All, Killing Time, American Standard, Shudder to Think, Jawbox, Gray Matter, Images, Swiz, The Icemen, Dr. Know (band) & The Goops.\n\nJawbox: Jawbox was an American alternative rock band from Washington, D.C., United States.  Its original members were J. Robbins (vocals, guitar), Kim Coletta (bass guitar) and Adam Wade (drums).  Bill Barbot (vocals, guitar) and Zach Barocas (drums) later joined the group, with Barocas replacing Wade.\n\nNME Awards 2012: The NME Awards 2012 were held in London, England, on 29 February 2012, at the Brixton Academy and was hosted by English comedian Jack Whitehall.  The nominations were announced exclusively on Zane Lowe's BBC Radio 1 show on 30 January 2012.  Arctic Monkeys had seven nominations, followed by Kasabian, who went on to win best British Band, Lana Del Rey and Muse with three apiece.\n\nNeil Bedford (photographer): Neil Bedford (born December 13, 1981, Bradford, England) is a British photographer, known for his work in advertising and being the official Kasabian photographer.\n\nBen Kealey: Ben Kealey is the touring keyboardist for the rock band Kasabian.  He was born in Leicester, England.\n\nQuestion: Are Kasabian and Jawbox both from England?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"bands_compared\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"band_name\": {\n            \"type\": \"string\"\n          },\n          \"country_of_origin\": {\n            \"type\": \"string\"\n          }\n        },\n        \"required\": [\n          \"band_name\",\n          \"country_of_origin\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"all_bands_from_england\": {\n      \"type\": \"boolean\",\n      \"description\": \"True if all bands in the comparison are from England, false otherwise.\"\n    },\n    \"final_answer\": {\n      \"type\": \"string\",\n      \"description\": \"The direct answer to the question.\"\n    }\n  },\n  \"required\": [\n    \"bands_compared\",\n    \"all_bands_from_england\",\n    \"final_answer\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "bands_compared": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "band_name": {
              "type": "string"
            },
            "country_of_origin": {
              "type": "string"
            }
          },
          "required": [
            "band_name",
            "country_of_origin"
          ],
          "additionalProperties": false
        }
      },
      "all_bands_from_england": {
        "type": "boolean",
        "description": "True if all bands in the comparison are from England, false otherwise."
      },
      "final_answer": {
        "type": "string",
        "description": "The direct answer to the question."
      }
    },
    "required": [
      "bands_compared",
      "all_bands_from_england",
      "final_answer"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
