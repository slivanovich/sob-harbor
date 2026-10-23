{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMike Tyson vs. Buster Douglas: Mike Tyson vs. Buster Douglas, billed as \"Tyson Is Back!\" , was a historic boxing match that occurred at the Tokyo Dome in Tokyo, Japan on February 11, 1990, in which then undefeated, undisputed heavyweight champion Mike Tyson lost via knockout to the 42–1 underdog Buster Douglas.  The fight is widely considered one of the biggest upsets in sports history.\n\nBuster Douglas: James \"Buster\" Douglas (born April 7, 1960) is an American former professional boxer who competed from 1981 to 1990, and 1996 to 1999.  He is best known for his stunning upset of Mike Tyson on February 11, 1990 in Tokyo to win the undisputed heavyweight title.  At the time Tyson was undefeated and considered to be the best boxer in the world, as well as one of the most feared heavyweight champions in history due to his domination of the division over the previous three years.  The only casino to make odds for the fight (all others declining to do so as they considered the fight such a foregone conclusion) had Douglas as a 42-to-1 underdog for the fight, making his victory, in commentator Jim Lampley's words, \"The biggest upset in the history of heavyweight championship fights.\"  Douglas held the title for eight months and two weeks, losing on October 25, 1990 to Evander Holyfield via third-round knockout, in his only title defense.\n\nMike Tyson vs. Evander Holyfield: Mike Tyson vs. Evander Holyfield, billed as \"Finally\", was a professional boxing match fought between Evander Holyfield and Mike Tyson for the World Boxing Association heavyweight championship on November 9, 1996 at the MGM Grand Garden Arena in Paradise, Nevada.  The bout was Tyson's first defense of the WBA title that he had won from Bruce Seldon on September 7 of that year.\n\nEvander Holyfield vs. Mike Tyson II: Evander Holyfield vs. Mike Tyson II, billed as \"The Sound and the Fury\" and afterwards infamously referred to as \"The Bite Fight\", was a professional boxing match contested on June 28, 1997 for the WBA Heavyweight Championship.  It achieved notoriety as one of the most bizarre fights in boxing history, after Tyson bit off part of Holyfield's ear.  Tyson was disqualified from the match and lost his boxing license, though it was later reinstated.\n\nEvander Holyfield vs. Riddick Bowe: Evander Holyfield vs. Riddick Bowe was a professional boxing match that took place on November 13, 1992 in Las Vegas, Nevada.  The fight was contested for the undisputed world heavyweight championship, which consisted of the WBA, WBC, IBF and Lineal championships.\n\nRiddick Bowe vs. Evander Holyfield II: Riddick Bowe vs. Evander Holyfield II, billed as \"Repeat or Revenge\", was a professional boxing match that took place on November 6, 1993 for the WBA, IBF and \"Lineal\" Heavyweight championships.\n\nThe Mirage: The Mirage is a 3,044 room Polynesian-themed resort and casino resort located on the Las Vegas Strip in Paradise, Nevada, United States.  The resort was built by developer Steve Wynn and is currently owned and operated by MGM Resorts International.\n\nRiddick Bowe vs. Evander Holyfield III: Riddick Bowe vs. Evander Holyfield III, billed as \"The Final Chapter\", was a professional boxing match contested on November 4, 1995.  The non-title match marked the third and final fight in the Bowe–Holyfield trilogy.\n\nRiddick Bowe vs. Jesse Ferguson: Riddick Bowe vs. Jesse Ferguson, billed as \"The Heavyweight Debate\", was a professional boxing match contested on May 22, 1993, for the WBA and \"Lineal\" Heavyweight championships.  The fight took place in RFK Stadium in Washington, DC, was Bowe's second defense of the title he had won from Evander Holyfield in November 1992, and was the main event of a card that included a fight between Roy Jones, Jr. and Bernard Hopkins for the vacant IBF middleweight championship, which Jones won.\n\nBuster Douglas vs. Evander Holyfield: Buster Douglas vs Evander Holyfield, billed as \"The Moment of Truth\", was a professional boxing match contested on October 25, 1990 for the WBA, WBC, IBF, \"The Ring\" and lineal Heavyweight championships.  The bout took place at The Mirage in Paradise, Nevada, USA and saw Douglas making the first defense of the titles he won from Mike Tyson in February 1990.\n\nQuestion: Who built the place where Buster Douglas vs Evander Holyfield took place?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"fight_event\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the boxing match.\"\n        },\n        \"date\": {\n          \"type\": \"string\",\n          \"description\": \"The date the fight took place.\"\n        },\n        \"venue\": {\n          \"type\": \"object\",\n          \"properties\": {\n            \"name\": {\n              \"type\": \"string\",\n              \"description\": \"The name of the venue where the fight occurred.\"\n            },\n            \"location\": {\n              \"type\": \"string\",\n              \"description\": \"The location of the venue.\"\n            }\n          },\n          \"required\": [\n            \"name\",\n            \"location\"\n          ],\n          \"additionalProperties\": false\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"date\",\n        \"venue\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"venue_builder\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the person or entity who built the venue.\"\n        },\n        \"role\": {\n          \"type\": \"string\",\n          \"description\": \"The role of the builder (e.g., developer).\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"role\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"final_answer\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person who built the venue.\"\n    }\n  },\n  \"required\": [\n    \"fight_event\",\n    \"venue_builder\",\n    \"final_answer\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "fight_event": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the boxing match."
          },
          "date": {
            "type": "string",
            "description": "The date the fight took place."
          },
          "venue": {
            "type": "object",
            "properties": {
              "name": {
                "type": "string",
                "description": "The name of the venue where the fight occurred."
              },
              "location": {
                "type": "string",
                "description": "The location of the venue."
              }
            },
            "required": [
              "name",
              "location"
            ],
            "additionalProperties": false
          }
        },
        "required": [
          "name",
          "date",
          "venue"
        ],
        "additionalProperties": false
      },
      "venue_builder": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the person or entity who built the venue."
          },
          "role": {
            "type": "string",
            "description": "The role of the builder (e.g., developer)."
          }
        },
        "required": [
          "name",
          "role"
        ],
        "additionalProperties": false
      },
      "final_answer": {
        "type": "string",
        "description": "The name of the person who built the venue."
      }
    },
    "required": [
      "fight_event",
      "venue_builder",
      "final_answer"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
