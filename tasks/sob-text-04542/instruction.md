{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nJonathan Kellerman: Jonathan Kellerman (born August 9, 1949) is an American psychologist, and Edgar and Anthony Award-winning author of numerous bestselling suspense novels.\n\nJesse Kellerman: Jesse Oren Kellerman (born September 1, 1978) is an American novelist and playwright.  He has published the novels: \"Sunstroke\" (2006), \"Trouble\" (2007), \"The Genius\" (2008), \"The Executor\" (2010), \"I'll Catch You\" (2012), and with his father, Jonathan Kellerman, \"The Golem of Hollywood\" (2014).  For his play, \"Things Beyond Our Control\" (2004) he was honored with a Princess Grace Award, which recognizes emerging talent in theater, dance, and film in the U.S.\n\nBlood Test (novel): Blood Test is the second novel by Jonathan Kellerman, published in 1986.  It is told from the first-person point of view of Dr. Alex Delaware, a child psychologist who is Kellerman's main character in the majority of his novels.  The novel also includes Delaware's best friend, LAPD Detective, Milo Sturgis.\n\nSurvival of the Fittest (novel): Survival of the Fittest is the thirteenth novel by Jonathan Kellerman and is told through the first person point of view of Kellerman's main character, Dr. Alex Delaware.  LAPD Detective Milo Sturgis has asked Alex to help him with another whodunit.  It reached number two in the New York Times Best Seller list for paperbacks.\n\nVoices of Our Nation Arts Foundation: Voices of Our Nations Arts Foundation (VONA) is a written arts organization that was founded in 1999 by Pulitzer-prize winning author Junot Diaz, along with award winning author Elmaz Abinader, Víctor Díaz and Diem Jones in order to provide emerging writers of color with workshops and mentoring by established writers of color.  Since its founding, over 2,000 aspiring writers from around the world have been involved in their programs.\n\nThe Two of Us (play): The Two of Us is a 1970 play by British playwright Michael Frayn.  It consists of four one-act plays for two actors and is Frayn's first published play.\n\nAlex Delaware: Alex Delaware is a literary character created by Jonathan Kellerman.  The Alex Delaware detective series begins with \"When the Bough Breaks\", published in 1985.  Delaware appears in 32 of Kellerman's popular murder mysteries.  Kellerman sets the series in Los Angeles.  Delaware is a forensic psychologist; although Kellerman writes a back story in which Delaware practiced as a child psychologist.\n\nWhen the Bough Breaks (1986 film): When the Bough Breaks is a 1986 television film directed by Waris Hussein and starring Ted Danson.  The screenplay by Phil Penningroth was adapted from a 1985 novel by Jonathan Kellerman, also titled \"When the Bough Breaks\".  Danson, who also co-produced, plays the crime-solving forensic psychologist Alex Delaware, a character who appears in a series of novels by Kellerman.\n\nNoises Off: Noises Off is a 1982 play by the English playwright Michael Frayn.  The idea for it came in 1970, when Frayn was watching from the wings a performance of \"The Two of Us\", a farce that he had written for Lynn Redgrave.  He said, \"It was funnier from behind than in front, and I thought that one day I must write a farce from behind.\"  The prototype, a short-lived one-act play called \"Exits\", was written and performed in 1977.  At the request of his associate, Michael Codron, Frayn expanded this into what would become \"Noises Off\".  It takes its title from the theatrical stage direction indicating sounds coming from offstage.\n\nMichael Frayn: Michael Frayn, FRSL ( ; born 8 September 1933) is an English playwright and novelist.  He is best known as the author of the farce \"Noises Off\" and the dramas \"Copenhagen\" and \"Democracy\".  His novels, such as \"Towards the End of the Morning\", \"Headlong\" and \"Spies\", have also been critical and commercial successes, making him one of the handful of writers in the English language to succeed in both drama and prose fiction.  He has also written philosophical works, such as \"The Human Touch: Our Part in the Creation of the Universe\" (2006).\n\nQuestion: Which man an Edgar and Anthony Award winning author, Michael Frayn or Jonathan Kellerman?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"award_winning_author\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the author who won the specified awards.\"\n    },\n    \"awards_won\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of the specific awards won by the author.\"\n    },\n    \"author_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"nationality\": {\n          \"type\": \"string\",\n          \"description\": \"The nationality of the award-winning author.\"\n        },\n        \"profession\": {\n          \"type\": \"string\",\n          \"description\": \"The primary profession of the award-winning author.\"\n        }\n      },\n      \"required\": [\n        \"nationality\",\n        \"profession\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"other_author_mentioned\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the other author mentioned in the question who did not win these specific awards.\"\n    }\n  },\n  \"required\": [\n    \"award_winning_author\",\n    \"awards_won\",\n    \"author_details\",\n    \"other_author_mentioned\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "award_winning_author": {
        "type": "string",
        "description": "The name of the author who won the specified awards."
      },
      "awards_won": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of the specific awards won by the author."
      },
      "author_details": {
        "type": "object",
        "properties": {
          "nationality": {
            "type": "string",
            "description": "The nationality of the award-winning author."
          },
          "profession": {
            "type": "string",
            "description": "The primary profession of the award-winning author."
          }
        },
        "required": [
          "nationality",
          "profession"
        ],
        "additionalProperties": false
      },
      "other_author_mentioned": {
        "type": "string",
        "description": "The name of the other author mentioned in the question who did not win these specific awards."
      }
    },
    "required": [
      "award_winning_author",
      "awards_won",
      "author_details",
      "other_author_mentioned"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
