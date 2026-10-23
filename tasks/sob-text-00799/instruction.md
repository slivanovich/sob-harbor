{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nRunnin' Wild (Airbourne album): Runnin' Wild is the debut album by the Australian hard rock band Airbourne.  The album was released on 23 June 2007 by the record label EMI and debuted on the ARIA album chart at #21.  It debuted at #62 on the UK Album Chart.\n\nFinal Conversation of Kings: Final Conversation of Kings is the third studio album by Australian hard rock band The Butterfly Effect.  It was released on September 20, 2008.  The album was the band's first foray into a more progressive rock sound, and the last to feature vocalist Clint Boge.  The album's first single, \"Window and the Watcher\", was released on a few weeks prior to the album's release on September 6, 2008.  \"Final Conversation\" and \"In These Hands\" were also later released as singles.  The album was generally well-received, debuting at no. 3 on the Australian Music Charts and receiving positive reviews from critics, who praised the more progressive nature of the album's sound.\n\nToo Much, Too Young, Too Fast: \"Too Much, Too Young, Too Fast\" is the 2nd single from \"Runnin' Wild\" by the Australian hard rock band Airbourne.  It is one of the band's most famous songs.\n\nNo Guts No Glory (Airbourne album): No Guts.  No Glory.  is the second studio album by the Australian hard rock band Airbourne and the follow-up to their 2007 debut \"Runnin' Wild\".  The album was released on 8 March 2010, in Europe, Canada, Japan and Australia and on 20 April 2010 in the US.\n\nAC/DC: AC/DC are an Australian hard rock band, formed in Sydney in 1973 by brothers Malcolm and Angus Young.  A hard rock/blues rock band, they have also been considered a heavy metal band, although they have always dubbed their music simply \"rock and roll\".\n\nNo Way But the Hard Way: \"No Way But The Hard Way\" is the 1st single from \"No Guts.  No Glory. \" by the Australian hard rock band Airbourne.\n\nRunnin' Wild (Airbourne song): \"Runnin' Wild\" is the 1st single from the album \"Runnin' Wild\" by the Australian hard rock band Airbourne.\n\nBlack Dog Barking: Black Dog Barking is the third studio album by the Australian hard rock band Airbourne and the follow-up to their 2010 album \"No Guts.  No Glory. \" The album was released in Europe and Australia on 20 May 2013, and worldwide on 21 May 2013.\n\nAirbourne (band): Airbourne is an Australian hard rock band formed in Warrnambool in 2003.\n\nNew Christs: The New Christs are an Australian hard rock band formed in 1980 by founding mainstay, Rob Younger, on lead vocals.  Younger was the lead singer in the punk rockers, Radio Birdman, and in other hard rock groups, New Race, Bad Music, the Other Side, Nanker Phelge and Deep Reduction.  The New Christs line-up since 2011 is Younger with Jim Dickson on bass guitar, Dave Kettley on guitar, Paul Larsen on drums and Brent Williams on guitar and keyboards.  Over their career the group have issued five studio albums, \"Distemper\" (1989), \"Lower Yourself\" (1997), \"We Got This!\"  (2002), \"Gloria\" (2009) and \"Incantations\" (2014).  Three former members have died: Stevie Plunder in January 1996, Mark Wilkinson in December 2012 and Christian Houllemare in June 2014.\n\nQuestion: Black Dog Barking is the third studio album by the Australian hard rock band Airbourne, an Australian hard rock band formed in Warrnambool in which year?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"band_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the band.\"\n    },\n    \"formation_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the band was formed.\"\n    },\n    \"origin_city\": {\n      \"type\": \"string\",\n      \"description\": \"The city where the band was formed.\"\n    },\n    \"genre\": {\n      \"type\": \"string\",\n      \"description\": \"The primary genre of the band.\"\n    }\n  },\n  \"required\": [\n    \"band_name\",\n    \"formation_year\",\n    \"origin_city\",\n    \"genre\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "band_name": {
        "type": "string",
        "description": "The name of the band."
      },
      "formation_year": {
        "type": "integer",
        "description": "The year the band was formed."
      },
      "origin_city": {
        "type": "string",
        "description": "The city where the band was formed."
      },
      "genre": {
        "type": "string",
        "description": "The primary genre of the band."
      }
    },
    "required": [
      "band_name",
      "formation_year",
      "origin_city",
      "genre"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
