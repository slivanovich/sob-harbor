{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nPaul King (chief executive): Paul King (born May 26, 1984) is a technology innovator and entrepreneur.  He is the founder and chief executive officer of Hercules Networks, as well as a member of the board.  Prior to Hercules Networks, King was a founding partner at G.C. Media, Inc.  Earlier in his career he was the founder and C.E.O. of International Sales Team Realty.  King expanded International Sales Team Realty by developing Chase Mortgage Center and New Wave Title Company.\n\nWale Adebanwi: Professor Wale Adebanwi, (born 1969), is a Nigerian - born first Black African Rhodes Professor at Oxford University\n\nList of Lab Rats characters: \"Lab Rats\", also known as \"Lab Rats: Bionic Island\" for its fourth season, is an American television sitcom that premiered on February 27, 2012, on Disney XD.  It focuses on the life of teenager Leo Dooley, whose mother, Tasha, marries billionaire genius Donald Davenport.  He meets Adam, Bree, and Chase, three bionic superhumans, with whom he develops an immediate friendship.  It should be noted that the names of the Lab Rats imply that they were originally known as subjects A, B, C and D. Adam was born first, then Bree, then Chase, and finally Daniel.\n\nLiar (Fake Shark – Real Zombie! album): Liar is the third album by Vancouver indie band Fake Shark – Real Zombie! .  It was released on February 14, 2013.  The album is a bit of direction change for the band, and the first with label, Light Organ Records.  Guests include Care Failure of the band Die Mannequin, Jimmy Urine of Mindless Self Indulgence, Steve Bays of Hot Hot Heat, and Henry Rollins.\n\nJimmy Urine: James Euringer (born September 7, 1969), known professionally as Jimmy Urine, is an American singer, songwriter, and musician.  He is best known as the lead singer and programmer of electropunk band Mindless Self Indulgence.\n\nDespoina: In Greek mythology, Despoina, Despoena or Despoine, was the daughter of Demeter and Poseidon and sister of Arion.  She was the goddess of mysteries of Arcadian cults worshipped under the title \"Despoina\", \"the mistress\" alongside her mother Demeter, one of the goddesses of the Eleusinian mysteries.  Her real name could not be revealed to anyone except those initiated to her mysteries.  Pausanias spoke of Demeter as having two daughters; Kore being born first, then later Despoina.  With Zeus being the father of Kore, and Poseidon as the father of Despoina.  Pausanias made it clear that Kore is Persephone, though he wouldn't reveal Despoina's proper name.\n\nThe Left Rights (album): The Left Rights is the self-titled debut album by the Mindless Self Indulgence side project featuring members Little Jimmy Urine and Steve, Righ? .  The album also contains a video of Mindless Self Indulgence performing \"Panty Shot\" live at CBGBs in New York City.\n\nPaddington (film): Paddington is a 2014 comedy film directed by Paul King, written by King and Hamish McColl and produced by David Heyman.  Based on \"Paddington Bear\" by Michael Bond, the film stars Ben Whishaw as the voice of the title character, along with Hugh Bonneville, Sally Hawkins, Julie Walters, Jim Broadbent, Peter Capaldi and Nicole Kidman in live-action roles.  The film was co-produced by the French company StudioCanal and the British company Heyday Films.  It was released in the United Kingdom on 28 November 2014 and grossed $265.3 million worldwide on a €38.5 million budget.  Among several honours, King was nominated for the BAFTA Award for Best Adapted Screenplay and both he and Heyman were nominated for the BAFTA Award for Best British Film.  A sequel, \"Paddington 2\", is scheduled to be released in 2017.\n\nAugustine of Canterbury: Augustine of Canterbury (born first third of the 6th century – died probably 26 May 604) was a Catholic Benedictine monk who became the first Archbishop of Canterbury in the year 597.  He is considered the \"Apostle to the English\" and a founder of the Catholic Church in England.\n\nPaul King (VJ): Paul King (born 20 November 1960) is a British-Irish singer, musician, VJ and TV presenter.\n\nQuestion: Who was born first, Paul King or Jimmy Urine?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_1_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the first person being compared.\"\n    },\n    \"person_1_birth_date\": {\n      \"type\": \"string\",\n      \"description\": \"The birth date of the first person.\"\n    },\n    \"person_2_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the second person being compared.\"\n    },\n    \"person_2_birth_date\": {\n      \"type\": \"string\",\n      \"description\": \"The birth date of the second person.\"\n    },\n    \"earlier_born_person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person who was born first.\"\n    },\n    \"earlier_born_person_birth_date\": {\n      \"type\": \"string\",\n      \"description\": \"The birth date of the person who was born first.\"\n    }\n  },\n  \"required\": [\n    \"person_1_name\",\n    \"person_1_birth_date\",\n    \"person_2_name\",\n    \"person_2_birth_date\",\n    \"earlier_born_person_name\",\n    \"earlier_born_person_birth_date\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_1_name": {
        "type": "string",
        "description": "The name of the first person being compared."
      },
      "person_1_birth_date": {
        "type": "string",
        "description": "The birth date of the first person."
      },
      "person_2_name": {
        "type": "string",
        "description": "The name of the second person being compared."
      },
      "person_2_birth_date": {
        "type": "string",
        "description": "The birth date of the second person."
      },
      "earlier_born_person_name": {
        "type": "string",
        "description": "The name of the person who was born first."
      },
      "earlier_born_person_birth_date": {
        "type": "string",
        "description": "The birth date of the person who was born first."
      }
    },
    "required": [
      "person_1_name",
      "person_1_birth_date",
      "person_2_name",
      "person_2_birth_date",
      "earlier_born_person_name",
      "earlier_born_person_birth_date"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
