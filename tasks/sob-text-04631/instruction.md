{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMatty Mullins: Matty Mullins (born July 3, 1988) is an American rock musician.  He is the lead vocalist of Dallas-based metalcore band Memphis May Fire.\n\nSleepwalking (Memphis May Fire album): Sleepwalking is the debut full-length studio album by American metalcore band Memphis May Fire.  The album was released through Trustkill Records on July 21, 2009.  This album is the first album to feature lead vocalist Matty Mullins after former lead vocalist Chase Ryan left the band in 2008.  Scheduled to be released summer 2008, the release got delayed because of the line-up change.  Mullins has described the album as \"a new breed of rock 'n' roll\" and musically it has \"more aggressive guitar work and noticeably more melodic, but still retains that southern swagger.\"\n\nMatty Mullins (album): Matty Mullins is the first full-length album by American rock musician Matty Mullins which was released September 23, 2014 by Rise Records.\n\nFeel (Sleeping with Sirens album): Feel is the third album by American post-hardcore band Sleeping with Sirens was released by June 4, 2013.  This is the last album released on Rise.  The first single, \"Low\", was released on April 23, 2013.  The second single, \"Alone\", featuring rapper MGK, was released on May 21, 2013.  The album also features guest appearances by Fronz (Attila), Matty Mullins (Memphis May Fire) and Shayley Bourget (Dayshell, ex-Of Mice & Men).  The entire album was produced by Cameron Mizell who had produced their debut album.  On May 26, 2013 the entire album was streamed on the Rise Records YouTube channel.\n\nThe Spring: The Spring is a 1989 independent movie, not available in video, about archaeologists Andy (Dack Rambo) and Matty (Gedde Watanabe), who discover a diary written by a member of Ponce de León's exploration party, which they believe can lead them to the Fountain of Youth.  They go to Florida to retrace De León's steps, but the secret of their quest gets out and they are pursued by a millionaire with plans to make money from the spring and a voodoo acolyte hoping to find immortality.  Andy's investigations bring him in contact with Dyanne (Shari Shattuck), an artist living near the search area, who seems to be holding back knowledge of the spring.\n\nAndy Kuntz: Andy Kuntz is a German Progressive Metal singer best known for his work with the band Vanden Plas.  In addition to his work with Vanden Plas he has also participated in a production of the musical Jesus Christ Superstar.\n\nCactus Choir (band): Cactus Choir was an American country music group from San Francisco, California composed of Marty Atkinson (vocals), Gary Hooker (guitar), Dave Ristrim (steel guitar), Tim Hensley (banjo), Shane Hicks (keyboards), Cal Ball (bass) and Eric Nelson (drums).  The group's self-titled debut album was released by Curb/Universal on March 24, 1998.  Jesse Mullins of \"American Cowboy\" gave the album a favorable review, writing that the musicians \"come from varied musical backgrounds but have blended their talents well.\"  Mullins compared their \"wistful harmonies\" to Restless Heart and Blackhawk.\n\nRomeo's Daughter: Romeo's Daughter are a British AOR, contemporary and mainstream rock band featuring Leigh Matty, Craig Joiner and Anthony Mitman.  The band released two albums in 1988 and 1993 respectively.  The band then reformed in 2009 and have toured extensively, as well as releasing new material: a live EP of past hits and an album of new material \"Rapture\" in 2012.  and \"Spin\" in 2015.  The current line up is Leigh Matty, Craig Joiner, Ed Poole and Andy Welsford.\n\nAmerican Satan: American Satan is an upcoming American thriller film written by Ash Avildsen and Matty Beckerman.  It is set to be released in theaters on Friday the 13th of October.  and features rock artists Andy Biersack, Ben Bruce, and Drake Bell.  (Andy Biersack's singing vocals to be played by Remington Leith).  It also stars Denise Richards, Malcolm McDowell, Booboo Stewart, and Tori Black.\n\nSemantic Saturation: Semantic Saturation is a three-member American progressive rock-metal band, composed of Shant Hagopian, Virgil Donati and Ric Fierabracci, with guests; Derek Sherinian and Andy Kuntz.  The band recorded its debut album \"Solipsistic\" in 2012 and released it in early 2013.\n\nQuestion: Are both Matty Mullins and Andy Kuntz.from the same country?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_1\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\"\n        },\n        \"country_of_origin\": {\n          \"type\": \"string\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"country_of_origin\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"person_2\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\"\n        },\n        \"country_of_origin\": {\n          \"type\": \"string\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"country_of_origin\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"are_from_same_country\": {\n      \"type\": \"boolean\"\n    }\n  },\n  \"required\": [\n    \"person_1\",\n    \"person_2\",\n    \"are_from_same_country\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_1": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "country_of_origin": {
            "type": "string"
          }
        },
        "required": [
          "name",
          "country_of_origin"
        ],
        "additionalProperties": false
      },
      "person_2": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "country_of_origin": {
            "type": "string"
          }
        },
        "required": [
          "name",
          "country_of_origin"
        ],
        "additionalProperties": false
      },
      "are_from_same_country": {
        "type": "boolean"
      }
    },
    "required": [
      "person_1",
      "person_2",
      "are_from_same_country"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
