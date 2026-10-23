{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nGreatest Hits Tour (Björk): The Greatest Hits Tour was the fifth worldwide concert tour by Icelandic musician Björk.  It was launched in support of the release of her \"Greatest Hits\" album, her box set \"Family Tree\", and to coincide with the release of her \"Live Box\" collection.  The tour was supposed to take place one year earlier, but it was delayed as Björk gave birth to her daughter.  The first dates of the tour were announced just two months after the birth.  The tour kicked off with two shows in London on May 24, 2003, and ended with a rescheduled performance in Toronto on September 3, 2003.  The tour visited Europe, Asia and North America with 28 shows in total.  Björk wore outfits and creations from Jeremy Scott, Alexander McQueen and Shoplifter.\n\nHunter (Björk song): \"Hunter\" is a song by Icelandic musician Björk from her 1997 album \"Homogenic\".  The lyrics of \"Hunter\" explore the pressure Björk felt to write music after realising the workforce that depended on her, following the success she found as a solo artist with her previous studio albums.  The song was first performed at the 1997 Tibetan Freedom Concert and later included with the online promotional release of \"Homogenic\"; the track was subsequently released as the third single for the album as three different CD releases in October 1998.  A collaborative effort between Björk and Mark Bell, \"Hunter\" features a dark combination of strings and layered synths, a militaristic electronic beat, and enigmatic lyrics about the heading towards a mission.\n\nAll Neon Like: \"All Neon Like\" is a song by Icelandic musician Björk.  The song was written by Björk and produced by the singer and British producer Mark Bell for Björk's fourth studio album, Homogenic (1997).\n\nVespertine: Vespertine is the fourth solo album by Icelandic musician Björk, released on 27 August 2001, on One Little Indian Records.  It was recorded at locations in Spain, Iceland, and the United States in 2000; production began during the filming of \"Dancer in the Dark\", which was characterized by conflict between the singer and director Lars von Trier. \" Björk\", a self-titled coffee table book containing photographs of the singer throughout her career, was released simultaneously with the album.  \"Vespertine\"' s sound reflected Björk's newly found interest in the music of artists such as Opiate and Console, who were also enlisted as producers.\n\nAlexander McQueen: Lee Alexander McQueen, CBE (17 March 1969 – 11 February 2010) was a British fashion designer and couturier.  He is known for having worked as chief designer at Givenchy from 1996 to 2001 and for founding his own Alexander McQueen label.  His achievements in fashion earned him four British Designer of the Year awards (1996, 1997, 2001 and 2003), as well as the CFDA's International Designer of the Year award in 2003.  McQueen committed suicide in 2010, at the age of forty, at his home in Mayfair, London.\n\nJulien Macdonald: Julien Macdonald OBE (born 19 March 1971 in Merthyr Tydfil) is a Welsh fashion designer who has appeared as judge on the television programme, \"Britain & Ireland's Next Top Model\".  In 2001, he was named \"British Fashion Designer of the Year\", and on 15 March 2001, was appointed as chief designer at Givenchy (Alexander McQueen's successor).  His \"atelier\" is at Old Burlington Street, London.\n\nAlexander McQueen (brand): Alexander McQueen brand was founded by designer Alexander McQueen in 1992.  It was the suggestion of Isabella Blow that McQueen use his middle name for the label.  The house's early collections developed its reputation for controversy and shock tactics (earning the title \"l'enfant terrible\" and \"the hooligan of English fashion\"), with trousers aptly named \"bumsters\" and a collection entitled \"Highland Rape\".  Alexander McQueen staged lavish and unconventional runway shows, such as a recreation of a shipwreck for his Spring 2003 collection, Spring 2005's human chess game, and the Fall 2006 show, \"Widows of Culloden\", which featured a life-sized hologram of supermodel Kate Moss dressed in yards of rippling fabric.  In total, McQueen designed 36 collections for his London label, including his MA graduate collection.\n\nHomogenic: Homogenic is the third international solo album by Icelandic musician Björk, released in September 1997.  Produced by Björk, Mark Bell, Guy Sigsworth, Howie B and Markus Dravs, it was released on One Little Indian Records.  The music of \"Homogenic\" was a new style for Björk, focusing on similar-sounding music combining electronic beats and string instruments with songs in tribute to her native country Iceland.  \"Homogenic\" was originally to be produced in her home in London, but was later recorded in Spain.  \"Homogenic\" marked the first of several production collaborations between Björk and Mark Bell, whom Björk would cite as a major influence on her musical career.  The album peaked at number twenty-eight on the \"Billboard\" 200, and at number four on the UK Albums Chart.\n\nPluto (song): \"Pluto\" is a song by Icelandic musician Björk.  The song was written and produced by Björk and British producer Mark Bell for Björk's fourth studio album, \"Homogenic\" (1997).\n\nInside Björk: Inside Björk is an official DVD released by Björk on 23 August 2003.  The DVD contains a 2002 documentary outlining the career of Björk, from her early work in Icelandic bands, to joining The Sugarcubes to her solo work up to 2002.  The documentary gives viewers a personal view into her private thoughts, views and motivations.  \"Inside Björk\" also features interviews with Sean Penn, Lars von Trier, Thom Yorke, Beck, RZA, Elton John, Missy Elliott, the late Alexander McQueen and more on their thoughts of Björk and her impact on music and culture.  The documentary coincided with the release of the \"Greatest Hits\" album, and had previously been seen on some television networks at the end of 2002.  It was commissioned by One Little Indian to make up for the fact that Björk was beginning to do fewer interviews than had been previous.  Two small new live performances are included in the documentary, \"Generous Palmstroke\" performed with Zeena Parkins and an organ version of \"The Anchor Song\" played in an Icelandic church.\n\nQuestion: Who is known for having worked as chief designer at Givenchy from 1996 to 2001 and for founding his own Alexander McQueen label, who's work was worn by Icelandic musician Björk? \n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"designer_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the fashion designer.\"\n    },\n    \"career_roles\": {\n      \"type\": \"array\",\n      \"description\": \"Key roles and achievements of the designer's career.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"role_type\": {\n            \"type\": \"string\",\n            \"description\": \"Type of role, e.g., 'Chief Designer', 'Founder'.\"\n          },\n          \"organization\": {\n            \"type\": \"string\",\n            \"description\": \"The company or label associated with the role.\"\n          },\n          \"start_year\": {\n            \"type\": \"integer\",\n            \"description\": \"The start year of the role or founding.\"\n          },\n          \"end_year\": {\n            \"type\": \"integer\",\n            \"description\": \"The end year of the role (if applicable).\"\n          }\n        },\n        \"required\": [\n          \"role_type\",\n          \"organization\",\n          \"start_year\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"artist_who_wore_designs\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"artist_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the musician who wore the designer's creations.\"\n        },\n        \"event_context\": {\n          \"type\": \"string\",\n          \"description\": \"The context or event where the designs were worn.\"\n        }\n      },\n      \"required\": [\n        \"artist_name\",\n        \"event_context\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"designer_name\",\n    \"career_roles\",\n    \"artist_who_wore_designs\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "designer_name": {
        "type": "string",
        "description": "The full name of the fashion designer."
      },
      "career_roles": {
        "type": "array",
        "description": "Key roles and achievements of the designer's career.",
        "items": {
          "type": "object",
          "properties": {
            "role_type": {
              "type": "string",
              "description": "Type of role, e.g., 'Chief Designer', 'Founder'."
            },
            "organization": {
              "type": "string",
              "description": "The company or label associated with the role."
            },
            "start_year": {
              "type": "integer",
              "description": "The start year of the role or founding."
            },
            "end_year": {
              "type": "integer",
              "description": "The end year of the role (if applicable)."
            }
          },
          "required": [
            "role_type",
            "organization",
            "start_year"
          ],
          "additionalProperties": false
        }
      },
      "artist_who_wore_designs": {
        "type": "object",
        "properties": {
          "artist_name": {
            "type": "string",
            "description": "The name of the musician who wore the designer's creations."
          },
          "event_context": {
            "type": "string",
            "description": "The context or event where the designs were worn."
          }
        },
        "required": [
          "artist_name",
          "event_context"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "designer_name",
      "career_roles",
      "artist_who_wore_designs"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
