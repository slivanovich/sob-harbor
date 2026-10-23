{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nKenneth Williams: Fantabulosa!: Kenneth Williams: Fantabulosa!  is a 2006 BBC Four television play starring Michael Sheen as the English comic actor Kenneth Williams, based on Williams' own diaries.  Cheryl Campbell plays Williams's beloved mother, Lou.\n\nRound the Horne: Round the Horne is a BBC Radio comedy programme that was transmitted in four series of weekly episodes from 1965 until 1968.  The series was created by Barry Took and Marty Feldman, with others contributing to later series after Feldman returned to performing, and starred Kenneth Horne, with Kenneth Williams, Hugh Paddick, Betty Marsden and Bill Pertwee.  The show's announcer was Douglas Smith and from time to time he took part in the sketches.  It had musical interludes by close harmony singing group the Fraser Hayes Four, and accompaniment by the big band of Edwin Braden (\"the great, 'airy fool\" according to Kenneth Williams), known as Edwin Braden and the Hornblowers.  The band was actually the BBC Radio Orchestra but was never billed as such.  In the fourth series, all the musical duties were performed by the smaller Max Harris Group.  Took and the cast had worked on the predecessor series \"Beyond Our Ken\".  The name is a pun on the nautical phrase for sailing around Cape Horn.\n\nMichael McCorkell: Colonel Sir Michael McCorkell (3 May 1925 – 13 November 2006) was an Ulster soldier and British public servant, emulating the high level of British public service of successive generations of the McCorkell family, being Lord Lieutenant of County Londonderry for 25 years.  His uncle, Sir Dudley McCorkell, had also been Lord Lieutenant of County Londonderry.\n\nTamotsu Yatō: Tamotsu Yato (矢頭 保 , Yatō Tamotsu , 1928(?)  – May 1973) was a Japanese photographer and occasional actor responsible for pioneering Japanese homoerotic photography and creating iconic black-and-white images of the Japanese male.  He was a friend and collaborator of the writer Yukio Mishima and the film critic Donald Richie, as well as a long-term romantic partner of Meredith Weatherby, an expatriate American publisher and translator of Mishima's works into English.  Yato completed three volumes of photography.\n\nHugh Paddick: Hugh William Paddick (22 August 1915 – 9 November 2000) was an English actor, whose most notable role was in the 1960s BBC radio show \"Round the Horne\", in sketches such as \"Charles and Fiona\" (as Charles) and \"Julian and Sandy\" (as Julian).  Both he and Kenneth Williams are largely responsible for introducing the underground language polari to the British public.\n\nWilliam Sharp (homeopath): William Sharp (1805–1896) was an English surgeon and physician.  Sharp is credited with first advocating the establishment of local museums in Britain and for putting science on the curricula of British public schools.  He was the first science teacher in a British public school and an early advocate of homoeopathy.\n\nJulian and Sandy: Julian and Sandy were characters on the BBC radio comedy programme \"Round the Horne\" from 1965 to 1968 and were played by Hugh Paddick and Kenneth Williams respectively, with scripts written by Barry Took and Marty Feldman.  According to a BBC Radio 4 programme on the characters, they were named after the writers Sandy Wilson and Julian Slade.\n\nCarry On Sergeant: Carry On Sergeant is a 1958 comedy film about National Service starring William Hartnell, Bob Monkhouse and Eric Barker; it is the first in the series of \"Carry On\" films, with 31 entries.  The film was based on a play \"The Bull Boys\" by R. F. Delderfield and was adapted into a script by Norman Hudis with John Antrobus contributing additional material and replacing the conscripted ballet dancers of the novel into a married couple.  It was directed by Gerald Thomas and produced by Peter Rogers, a partnership which would last until 1978.  Actors in this film, who went on to be part of the regular team in the series, were Kenneth Williams, Charles Hawtrey, Hattie Jacques, Kenneth Connor and Terry Scott.  The first public screening was on 1 August 1958 at Screen One, in London and it went on general cinema release across British cinemas on 15 August 1958.  The soundtrack music was played by the Band of the Coldstream Guards, conducted by the composer.\n\nBeyond Our Ken: Beyond Our Ken (1958–1964) is a radio comedy programme, the predecessor to \"Round the Horne\" (1965–1968).  Both programmes starred Kenneth Horne, Kenneth Williams, Hugh Paddick, Betty Marsden and Bill Pertwee, with announcer Douglas Smith.  Musical accompaniment was provided by the BBC Revue Orchestra.  The name is a pun on Kenneth Horne's name and the (now mainly Northern English and Scots) word \"\", meaning \"knowledge or perception\".\n\nCastaway 2007: Castaway 2007 was a follow-up to the BBC series \"Castaway 2000\" in which a group of people from the British public are \"castaway\" on a remote island.  While in the 2000 series 36 men, women and children moved to a remote Scottish island for a year, this series featured 15 men and women from the British public who were moved to a New Zealand island for three months.  The basic premise of a group of volunteers living as a community in a remote location remains, however this time the BBC promised an \"exotic location, on the other side of the world\".  Another change since Castaway 2000, was that the castaways were voted off the island one-by-one, in a manner similar to other reality series like \"Big Brother\".\n\nQuestion: The actor responsible for introducing the underground language polari to the British public, starred with Kenneth Williams in what show from 1965 to 1968?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actor who helped introduce the language.\"\n    },\n    \"co_star_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the co-star mentioned in the question.\"\n    },\n    \"language_introduced\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the underground language introduced to the public.\"\n    },\n    \"show_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"show_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the radio show.\"\n        },\n        \"transmission_start_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The start year of the show's transmission.\"\n        },\n        \"transmission_end_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The end year of the show's transmission.\"\n        }\n      },\n      \"required\": [\n        \"show_name\",\n        \"transmission_start_year\",\n        \"transmission_end_year\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"actor_name\",\n    \"co_star_name\",\n    \"language_introduced\",\n    \"show_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actor_name": {
        "type": "string",
        "description": "The name of the actor who helped introduce the language."
      },
      "co_star_name": {
        "type": "string",
        "description": "The name of the co-star mentioned in the question."
      },
      "language_introduced": {
        "type": "string",
        "description": "The name of the underground language introduced to the public."
      },
      "show_details": {
        "type": "object",
        "properties": {
          "show_name": {
            "type": "string",
            "description": "The name of the radio show."
          },
          "transmission_start_year": {
            "type": "integer",
            "description": "The start year of the show's transmission."
          },
          "transmission_end_year": {
            "type": "integer",
            "description": "The end year of the show's transmission."
          }
        },
        "required": [
          "show_name",
          "transmission_start_year",
          "transmission_end_year"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "actor_name",
      "co_star_name",
      "language_introduced",
      "show_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
