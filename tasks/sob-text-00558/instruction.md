{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThe Walt Disney Company Italy: The Walt Disney Company Italia S.r.l. (formerly called The Walt Disney Company Italia S.p.A) is The Walt Disney Company's Italian division and one of The Walt Disney Company's European divisions.  The company was founded on 8 May 1938 as Creazioni Walt Disney S.A.I.  The company owns and operates Disney Channel Italy, Disney in English, and more.  Comics are also published by the company as well.\n\nWalt Disney World Swan: The Walt Disney World Swan is a resort hotel designed by architect Michael Graves located between Epcot and Disney's Hollywood Studios behind Disney's BoardWalk Resort and across from its sister resort, the Walt Disney World Dolphin.  The Swan, which opened January 13, 1990 on Disney property, is a joint venture between the Walt Disney Company, Tishman Hotel Corporation, MetLife and Starwood Hotels and Resorts.  The land the resort occupies is owned by the Walt Disney Company, while the buildings themselves are leased by Disney to the Tishman Hotel Corporation and MetLife and operated by Starwood Hotels & Resorts Worldwide under the Westin brand.  The Walt Disney World Swan and Dolphin are a part of the Walt Disney Collection of resorts, because of this they are Disney branded and guests of the resort have access to special Disney benefits available to Disney Resort Hotel guests only.\n\nDisney Comics: Disney Comics was a comic book publishing company operated by The Walt Disney Company which ran from 1990 to 1993.  It was connected with W. D. Publications, Inc., which was a subsidiary of The Walt Disney Company that published \"Disney Comics\" during that time span.  W. D. Publications, Inc. created Disney Comics in 1990 so that The Walt Disney Company would not have to rely on outside publishers such as Gladstone Publishing.  In the USA, Disney only licensed their comic books to other publishers prior to 1990.  Since the demise of the Disney Comics line, Disney has licensed out their properties to various US comics publishers, while continuing to publish comics in the since-defunct magazines \"Disney Adventures\" and \"Disney Adventures Comic Zone\", as well as numerous book projects, and has reentered the periodical comics market through their 2009 purchase of Marvel Entertainment.  Marvel and Disney Publishing began jointly publishing \"Disney/Pixar Presents\" magazine in May 2011 but did not revive the Disney Comics imprint as Boom!  Studios would continue to publish classic Disney character comics.\n\nWalt Disney World Company: Walt Disney World Company was created in 1967 as the company that initially owned and operated Walt Disney World near Orlando, Florida.  The resort opened in 1971 and the land was owned by Walt Disney World Company, Walt Disney Travel Company, and Walt Disney World Hospitality and Recreation Corporation.  In 2009 the name was changed to Walt Disney Parks and Resorts division of The Walt Disney Company.\n\nWalt Disney World Dolphin: The Walt Disney World Dolphin is a resort hotel designed by architect Michael Graves located between Epcot and Disney's Hollywood Studios in the Walt Disney World Resort in Bay Lake, Florida, next to Disney's BoardWalk Resort area.  It opened on June 1, 1990 and is joined to its sister hotel, the Walt Disney World Swan (also designed by Graves) by a palm-tree lined covered walkway crossing a lagoon.  The Walt Disney World Swan and Dolphin is a joint venture between the Walt Disney Company, Tishman Hotel Corporation, MetLife and Starwood Hotels and Resorts.  The land the resort occupies is owned by the Walt Disney Company, while the buildings themselves are leased by Disney to the Tishman Hotel Corporation and MetLife but operated by Starwood Hotels & Resorts Worldwide under the Sheraton Hotels brand.  The Walt Disney World Swan and Dolphin are a part of the Walt Disney Collection of resorts; because of this they are Disney branded and guests of the resort have access to special Disney benefits available to Disney Resort Hotel guests only.\n\nKurt Russell: Kurt Vogel Russell (born March 17, 1951) is an American actor.  He began acting on television in the western series \"The Travels of Jaimie McPheeters\" (1963–64).  In the late 1960s, he signed a ten-year contract with The Walt Disney Company where, according to Robert Osborne, he became the studio's top star of the 1970s.\n\nThe Walt Disney Company France: The Walt Disney Company France, formerly Buena Vista International France, is one of The Walt Disney Company's international divisions and also European divisions.  The Walt Disney Company France is headquartered in Paris, the capital of France.  The company owns and operates French versions of Disney Channel, Disney XD, Playhouse Disney, and Disney Cinemagic (which became Disney Cinema in May of 2015) .  Jean-François Camilleri is head of the company.  The Walt Disney Company France also produces content as well with other media companies.\n\nMandeville-Anthony v. Walt Disney Co.: Mandeville-Anthony v.  The Walt Disney Company, 11-56441 (9th Cir.  2012), is a United States Court of Appeals for the Ninth Circuit case in which the Court evaluated whether defendants Pixar, The Walt Disney Company and Walt Disney Pictures infringed on Jake Mandeville-Anthony's copyrighted works.  Plaintiff Mandeville-Anthony's claim for copyright infringement was first dismissed by the United States District Court for the Central District of California, because the court found that the parties’ works were not substantially similar.  Mandeville-Anthony made copyright infringement claims with regards to his works \"Cookie & Co.\" and \"Cars/Auto-Excess/Cars Chaos\", an animated television show and movie, that he believed Disney copied in order to make their own films, \"Cars\" and \"Cars 2\", both of which were very successful, and animation television show \"Cars Toons: Mater's Tall Tales\".  He also made breach of contract claims stating that he and Disney signed a contract barring Disney from using the ideas contained in his works.  The decision was affirmed by the Court of Appeals.\n\nWalt Disney Pictures: Walt Disney Pictures, Inc. is an American film production company and a subsidiary of Walt Disney Studios, owned by The Walt Disney Company.  The division is based at the Walt Disney Studios in Burbank, California, and is the main producer of live-action feature films within the Walt Disney Studios unit.  It took on its current name in 1983.  Today, in conjunction with the other units of Walt Disney Studios, Walt Disney Pictures is classified as one of Hollywood's \"Big Six\" film studios.  Films produced by Walt Disney Animation Studios and Pixar Animation Studios are also released under this brand.\n\n3000 Miles to Graceland: 3000 Miles to Graceland is a 2001 American action adventure crime film directed, co-produced by Damien Lichtenstein.  The script was written by Richard Recco and Damien Lichtenstein.  It stars Kurt Russell and Kevin Costner with supporting roles Courteney Cox, David Arquette, Bokeem Woodbine, Christian Slater, and Kevin Pollak.  It is a story of theft and betrayal, revolving around a plot to rob the Riviera Casino during a convention of Elvis impersonators.\n\nQuestion: What is the name of the movie lead for the american actor that In the late 1960s signed a ten-year contract with The Walt Disney Company?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the American actor.\"\n    },\n    \"contract_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"company\": {\n          \"type\": \"string\",\n          \"description\": \"The company the actor signed a contract with.\"\n        },\n        \"contract_duration_years\": {\n          \"type\": \"integer\",\n          \"description\": \"The duration of the contract in years.\"\n        },\n        \"contract_start_period\": {\n          \"type\": \"string\",\n          \"description\": \"The period when the contract was signed.\"\n        }\n      },\n      \"required\": [\n        \"company\",\n        \"contract_duration_years\",\n        \"contract_start_period\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"movie_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the movie starring the actor.\"\n    },\n    \"movie_release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the movie.\"\n    }\n  },\n  \"required\": [\n    \"actor_name\",\n    \"contract_details\",\n    \"movie_title\",\n    \"movie_release_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actor_name": {
        "type": "string",
        "description": "The name of the American actor."
      },
      "contract_details": {
        "type": "object",
        "properties": {
          "company": {
            "type": "string",
            "description": "The company the actor signed a contract with."
          },
          "contract_duration_years": {
            "type": "integer",
            "description": "The duration of the contract in years."
          },
          "contract_start_period": {
            "type": "string",
            "description": "The period when the contract was signed."
          }
        },
        "required": [
          "company",
          "contract_duration_years",
          "contract_start_period"
        ],
        "additionalProperties": false
      },
      "movie_title": {
        "type": "string",
        "description": "The title of the movie starring the actor."
      },
      "movie_release_year": {
        "type": "integer",
        "description": "The release year of the movie."
      }
    },
    "required": [
      "actor_name",
      "contract_details",
      "movie_title",
      "movie_release_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
