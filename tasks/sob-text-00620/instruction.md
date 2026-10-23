{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nHummingbird discography: This page lists the albums recorded by the rock band Hummingbird, which was formed by Bobby Tench and included other former members of The Jeff Beck Group.  All three albums were produced by Ian Samwell.\n\nHummingbird (band): Hummingbird were a British rock band, formed in 1974 by Bobby Tench of The Jeff Beck Group and Streetwalkers fame.  Hummingbird recorded three successful albums, released by A&M using Ian \"Sammy\" Samwell as their record producer.  The original line up included members of the second Jeff Beck Group, vocalist and guitarist Bobby Tench, keyboardist Max Middleton, bassist Clive Chaman, drummer Conrad Isidore and second guitarist Bernie Holland.  At the start of sessions for their first album they were joined by Jeff Beck for a brief period but he did not contribute to the album and left to work on his own project.  After the first album Bernie Holland was replaced by guitarist Robert Ahwai and drummer Bernard \"Pretty\" Purdie replaced Isidore on the next two albums,vocalists Madeline Bell and Liza Strike were brought in to complement the band.  They found success mainly in the United States, also in Europe and Japan.\n\nDarkness Darkness: Darkness Darkness is an album by the former vocalist from The Animals, Eric Burdon.  It was recorded in May 1978 at Roundwood House, County Leix in Ireland, using Ronnie Lane's Mobile Studio.  The album was released by Polydor in 1980.  The line up for \"Darkness Darkness\" included Bobby Tench (Streetwalkers), Brian Robertson (Thin Lizzy, Motörhead), Henry McCullough (Wings) and Mick Weaver (Traffic).  The album was produced by Tony Meehan, who started his career as drummer with The Shadows.\n\nKeep Moving (Andrew Stockdale album): Keep Moving is the debut solo studio album by Australian hard rock musician Andrew Stockdale.  Initially conceived as the third album by Stockdale's band Wolfmother, it was later announced to be a solo album after the disbandment of the group in March 2013.  Recorded by Wolfmother between 2011 and 2013, \"Keep Moving\" was released by Universal in June 2013.\n\nWolfmother: Wolfmother are an Australian hard rock band from Sydney, New South Wales.  Formed in 2000 by vocalist and guitarist Andrew Stockdale, bassist and keyboardist Chris Ross and drummer Myles Heskett, the group currently includes Stockdale, bassist and keyboardist Ian Peres and drummer Hamish Rosser.  Wolfmother released their self-titled debut album \"Wolfmother\" in Australia in 2005 and internationally in 2006.  The album reached number 3 on the Australian Albums Chart and the top 40 in the US and the UK, and has to date sold over 1.5 million copies worldwide.\n\nKeep Moving (EP): Keep Moving is the debut solo extended play (EP) by Australian musician Andrew Stockdale.  Recorded throughout 2012 and 2013 in Byron Bay, the EP features four songs from Stockdale's upcoming debut solo album of the same name.  It was released by Universal on 26 April 2013 in Australia, Germany and Austria, on 28 April in the United Kingdom and the rest of Europe, and on 30 April in the United States.\n\nBobby Tench: Robert Tench also known as Bobby Tench, is a British vocalist, guitarist, sideman, songwriter and arranger.  He is credited on recordings as Bob Tench and Bobby Gass.\n\nAndrew Stockdale: Andrew James Stockdale (born 20 July 1976) is an Australian rock musician, singer and songwriter best known as the lead vocalist, lead guitarist and only mainstay member of the rock band Wolfmother, which formed in 2000.  In 2007, alongside his Wolfmother bandmates, he won 'Songwriter of the Year' at the APRA Awards.  Aside from his work with Wolfmother, Stockdale was featured on the 2010 single \"By the Sword\" by Slash.\n\nCall Me by My Name: Call Me by My Name is the sixth studio album by British soul singer Ruby Turner, released in October 1998.  Turner co-wrote five songs and enlisted the help of rhythm and blues luminaries Bobby Tench, Zoot Money, Stan Webb and Bad Company bassist Boz Burrell.\n\nStratavarious: Stratavarious is an album by Ginger Baker, the drummer from Cream, released by Polydor in 1972.  Baker had many associations with an eclectic mix of musicians brought together under numerous band titles bearing his surname.  \"Stratavarious\" is the only album that was released under the name of \"Ginger Baker\" without other associated names.  The lineup on \"Stratavarious\" included Bobby Tench, vocalist and guitarist from The Jeff Beck Group, who plays guitar under the pseudonym \"Bobby Gass\" and the Nigerian pioneer of Afrobeat, Fela Ransome-Kuti who appeared at concerts with Baker at this time.\n\nQuestion: Do Andrew Stockdale and Bobby Tench have the same nationality ?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_1\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the first person.\"\n        },\n        \"nationality\": {\n          \"type\": \"string\",\n          \"description\": \"The nationality of the first person.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"nationality\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"person_2\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the second person.\"\n        },\n        \"nationality\": {\n          \"type\": \"string\",\n          \"description\": \"The nationality of the second person.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"nationality\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"have_same_nationality\": {\n      \"type\": \"boolean\",\n      \"description\": \"True if both individuals have the same nationality, false otherwise.\"\n    }\n  },\n  \"required\": [\n    \"person_1\",\n    \"person_2\",\n    \"have_same_nationality\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_1": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the first person."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the first person."
          }
        },
        "required": [
          "name",
          "nationality"
        ],
        "additionalProperties": false
      },
      "person_2": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the second person."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the second person."
          }
        },
        "required": [
          "name",
          "nationality"
        ],
        "additionalProperties": false
      },
      "have_same_nationality": {
        "type": "boolean",
        "description": "True if both individuals have the same nationality, false otherwise."
      }
    },
    "required": [
      "person_1",
      "person_2",
      "have_same_nationality"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
