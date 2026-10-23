{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nList of Only Fools and Horses episodes: The following is an episode list for the BBC One sitcom \"Only Fools and Horses\".  The show was first broadcast in the United Kingdom on BBC One on 8 September 1981.  It ran for seven series and sixteen Christmas Specials until 25 December 2003, when the final episode was broadcast.  In total, 64 regular episodes of \"Only Fools and Horses\", all written by John Sullivan, were produced.  All are now available on both Region 2 and Region 1 DVD.\n\nRock &amp; Chips: Rock & Chips is a British television comedy-drama and a prequel to the sitcom \"Only Fools and Horses\".  Set in 1960s Peckham, it focuses primarily on the lives of Del Trotter, Freddie Robdal and Joan and Reg Trotter.  Nicholas Lyndhurst, who played Rodney in \"Only Fools and Horses\", plays Robdal alongside James Buckley (Del Boy), Kellie Bright (Joan), Shaun Dingwall (Reg) and Phil Daniels (Grandad).  The Shazam Productions and BBC co-production was written by \"Only Fools and Horses\" creator John Sullivan, directed by Dewi Humphreys and produced by Gareth Gwenlan.\n\nWorld Heavyweight Championship (Zero1): The World Heavyweight Championship is a professional wrestling world heavyweight championship in the Japanese promotion Pro Wrestling Zero1.  It is one of Zero1's top two singles titles, along with the NWA United National Heavyweight Championship.  It was first introduced on December 15, 2007 when Zero1 ended their relationship with the AWA Superstars of Wrestling.  The Superstars of Wrestling champion at the time, Masato Tanaka, was then recognized as the first Zero1 World Heavyweight Champion.  To this day, Zero1 continues to use the AWA title belt, which reads \"AWA World Heavyweight Wrestling Champion\", to represent the World Heavyweight Championship.  There have been a total of 14 recognized champions who have had a combined 21 official reigns.\n\nKenneth MacDonald (English actor): Kenneth MacDonald (20 November 1950 – 6 August 2001) was an English actor who was best known for the parts of Gunner Nobby Clark in \"It Ain't Half Hot Mum\" and Mike Fisher in \"Only Fools and Horses\".\n\nBill MacDonald (wrestler): William \"Bill\" MacDonald (c.1920/1921 – 1964) was a Scottish heavyweight wrestling champion.  He was the father of actor Kenneth MacDonald (1950-2001).  Kenneth was most famous for playing the role of Mike Fisher in the British sitcom \"Only Fools and Horses\" (1981-2003).\n\nThe Green Green Grass: The Green Green Grass is a BBC television sitcom, created and initially written by John Sullivan, produced by Shazam Productions for the BBC.  It is a sequel/spin-off of the long running sitcom \"Only Fools and Horses\" and stars John Challis, Sue Holderness and Jack Doolan.  Four series and three Christmas specials were originally broadcast on BBC One between 2005 and 2009.\n\nOnly Fools and Horses: Only Fools and Horses is a British television sitcom created and written by John Sullivan.  Seven series were originally broadcast on BBC One in the United Kingdom from 1981 to 1991, with sixteen sporadic Christmas specials aired until the end of the show in 2003.  Episodes are regularly repeated on UKTV comedy channel Gold, Yesterday and occasionally repeated on BBC One.\n\nNickolaus Hirschl: Nickolaus \"Mickey\" Hirschl (March 20, 1906 – October 10, 1991) was an Austrian Olympic-medal-winning wrestler, European Heavyweight Wrestling Champion, and for 10 years held the title of Austrian Heavyweight Wrestling Champion.  He was also an Austrian Shotput and Discus Junior Champion, Austrian Heavyweight Weightlifting Junior Champion, and for seven years the Austrian Pentathlon Champion.\n\nList of The Vicar of Dibley episodes: \"The Vicar of Dibley\" is a British sitcom which premiered on BBC One on 10 November, 1994.  From 1994 to 1998, two series and two specials had been produced and broadcast.  No further series were produced.  Following this, a number of specials were broadcast.  Over the seasonal period between Christmas 1999 and early 2000, four specials aired.  This collection of specials are often referred to as the third series, however, it was not produced as an official series.  Another four specials were aired between 2004/2005 and 2006/2007.  The series ended on 1 January 2007.  This was, however, followed by three short Comic Relief episodes, aired on 16 March 2007, 15 March 2013 and 13 March 2015.  In all, 20 episodes and six shorter Comic Relief specials have been produced.\n\nSport Relief 2014 Special: The Sport Relief special, also referred to as \"Beckham in Peckham\" was an edition of the BBC sit-com, \"Only Fools and Horses\", recorded as part of the \"Sport Relief 2014\" appeal.  It was screened on 21 March 2014.  Actors David Jason and Nicholas Lyndhurst reprised their roles as Del Boy and Rodney in the sketch written by Jim Sullivan and Dan Sullivan, which included previously unused material written by their father John Sullivan, who created and wrote every episode of the series.  David Beckham guest starred.  Beckham was also the person that got in touch with Jim Sullivan, the son of the late \"Only Fools and Horses\" creator John Sullivan about doing something for \"Sport Relief 2014\".\n\nQuestion: William \"Bill\" MacDonald, was a Scottish heavyweight wrestling champion, and was the father of actor Kenneth MacDonald, who was most famous for playing the role of Mike Fisher in the British sitcom \"Only Fools and Horses\", a British television sitcom created and written by John Sullivan, with sixteen sporadic Christmas specials aired, until the end of the show in which year?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"sitcom_information\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the British television sitcom.\"\n        },\n        \"creator\": {\n          \"type\": \"string\",\n          \"description\": \"The creator and writer of the sitcom.\"\n        },\n        \"final_broadcast_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the final episode of the sitcom was broadcast.\"\n        },\n        \"number_of_christmas_specials\": {\n          \"type\": \"integer\",\n          \"description\": \"The total number of Christmas specials aired for the sitcom.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"creator\",\n        \"final_broadcast_year\",\n        \"number_of_christmas_specials\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"actor_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the actor.\"\n        },\n        \"role_in_sitcom\": {\n          \"type\": \"string\",\n          \"description\": \"The character played by the actor in the sitcom.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"role_in_sitcom\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"actor_parent_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the actor's parent.\"\n        },\n        \"profession\": {\n          \"type\": \"string\",\n          \"description\": \"The profession of the actor's parent.\"\n        },\n        \"relationship_to_actor\": {\n          \"type\": \"string\",\n          \"description\": \"The family relationship of this person to the actor.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"profession\",\n        \"relationship_to_actor\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"sitcom_information\",\n    \"actor_details\",\n    \"actor_parent_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "sitcom_information": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the British television sitcom."
          },
          "creator": {
            "type": "string",
            "description": "The creator and writer of the sitcom."
          },
          "final_broadcast_year": {
            "type": "integer",
            "description": "The year the final episode of the sitcom was broadcast."
          },
          "number_of_christmas_specials": {
            "type": "integer",
            "description": "The total number of Christmas specials aired for the sitcom."
          }
        },
        "required": [
          "title",
          "creator",
          "final_broadcast_year",
          "number_of_christmas_specials"
        ],
        "additionalProperties": false
      },
      "actor_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the actor."
          },
          "role_in_sitcom": {
            "type": "string",
            "description": "The character played by the actor in the sitcom."
          }
        },
        "required": [
          "name",
          "role_in_sitcom"
        ],
        "additionalProperties": false
      },
      "actor_parent_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the actor's parent."
          },
          "profession": {
            "type": "string",
            "description": "The profession of the actor's parent."
          },
          "relationship_to_actor": {
            "type": "string",
            "description": "The family relationship of this person to the actor."
          }
        },
        "required": [
          "name",
          "profession",
          "relationship_to_actor"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "sitcom_information",
      "actor_details",
      "actor_parent_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
