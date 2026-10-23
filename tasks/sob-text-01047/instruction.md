{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSinbad (TV series): Sinbad is an action-adventure fantasy family saga television series that was broadcast on Sky1 from 8 July 2012, consisting of 12 episodes.  It was produced by Impossible Pictures, the same company who made \"Walking with Dinosaurs\" and \"Primeval\".  The series stars Elliot Knight as the titular hero, Sinbad.\n\nOnce Upon a Time (TV series): Once Upon a Time is an American fantasy drama television series that premiered on October 23, 2011, on ABC.  The show takes place in the fictional seaside town of Storybrooke, Maine, whose residents are characters from various fairy tales transported to the \"real world\" town and robbed of their original memories by a powerful curse.\n\nBWF Super Series: The BWF Super Series, launched on December 14, 2006 and implemented in 2007, is a series of elite badminton tournaments, sanctioned by Badminton World Federation (BWF).  Since 2011, the Super Series includes two levels of tournament, Super Series Premier and Super Series.  A season of Super Series features twelve tournaments around the world, including five of them classified as Super Series Premier.  Super Series Premier tournament offers higher ranking point and higher minimum total prize money.  Top eight players/pairs in each discipline in Super Series standings are invited to the Super Series Finals held at the year end.\n\nSrikanth Kidambi: Srikanth Kidambi is an Indian badminton player.  He shot to prominence by defeating Olympic Champion Lin Dan in 2014 China Open Super Series Premier by 21–19 21–17 in the final round, thus becoming the first Indian to win a Super Series Premier Men's title.  He trains at the Gopichand Badminton Academy, Hyderabad and is supported by the GoSports Foundation, Bangalore.  He is also sponsored by Li-Ning.\n\nTanongsak Saensomboonsuk: Tanongsak Saensomboonsuk (;born 13 October 1990) is a Thai male badminton player.  He won his first career Super Series Premier title by winning the Denmark Open on 23 October 2016, becoming the first Thai to win a men's singles title in a Super Series Premier tournament.  He studies a bachelor in business administration at Siam University.\n\n2017 All England Super Series Premier: The 2017 All England Super Series Premier is the first Super Series tournament of the 2017 BWF Super Series.  The tournament took place in Birmingham, England, from March 7–12, 2017, and had a total purse of $600,000.\n\nLee Chong Wei career statistics: This is a list of the main career statistics of Malaysian professional badminton player, Lee Chong Wei.  To date, Lee has won sixty three singles titles, including eleven Super Series Premier titles, twenty-eight Super Series titles, and four Super Series Finals titles.  He is the first men's singles player to win at least once in different Super Series Premier titles.  He is also a Silver medalist at the 2008 Summer Olympics, 2012 Summer Olympics and the 2016 Summer Olympics.  He is the runner-up at the 2011 BWF World Championships, 2013 BWF World Championships and 2015 BWF World Championships.  His achievement as the runner-up at the 2014 BWF World Championships was canceled due to doping violations.  Following that matter, he served an 8-month suspension from international competitions.\n\n2011 Korea Open Super Series Premier: The 2011 Korea Open Super Series Premier was the second tournament of the 2011 BWF Super Series.  It was the first competition under the new format where a select group of Super Series events were elevated to premier status.  The tournament was held in Seoul, South Korea from 25–30 January 2011 and had a total purse of $1,200,000.\n\nElliot Knight: Elliot Knight is a British actor.  He is known for his role as Sinbad in the British television series \"Sinbad\".  He portrayed Merlin on the American fantasy television series \"Once Upon a Time\".\n\nWayne Knight: Wayne Elliot Knight (born August 7, 1955) is an American actor and comedian.  He is known for playing Newman in the TV sitcom \"Seinfeld\" (1992–1998) and Officer Don Orville in \"3rd Rock from the Sun\" (1996–2001).  His other roles include Dennis Nedry in \"Jurassic Park\", Stan Podolak in \"Space Jam\" (1996), Al McWhiggin in \"Toy Story 2\" (1999), Tantor in \"Tarzan\" (1999), the Giraffe in \"Bee Movie\" (2007), Zack Mallozzi in \"Rat Race\" (2001), Dojo in Xiaolin Showdown (2003–2006), Mr. Blik in \"Catscratch\" (2005–2007), Microchip in \"\" (2008) and Haskell Lutz in \"The Exes\" (2011–2015).\n\nQuestion: What year did the series premier that starred Elliot Knight as Merlin?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"series_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the television series.\"\n    },\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actor who played the character.\"\n    },\n    \"character_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the character played by the actor.\"\n    },\n    \"premiere_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the television series premiered.\"\n    }\n  },\n  \"required\": [\n    \"series_name\",\n    \"actor_name\",\n    \"character_name\",\n    \"premiere_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "series_name": {
        "type": "string",
        "description": "The name of the television series."
      },
      "actor_name": {
        "type": "string",
        "description": "The name of the actor who played the character."
      },
      "character_name": {
        "type": "string",
        "description": "The name of the character played by the actor."
      },
      "premiere_year": {
        "type": "integer",
        "description": "The year the television series premiered."
      }
    },
    "required": [
      "series_name",
      "actor_name",
      "character_name",
      "premiere_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
