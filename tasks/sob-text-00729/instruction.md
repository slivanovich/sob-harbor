{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nAnthony Joshua: As of May 2017, Joshua is ranked as the world's best heavyweight by the Transnational Boxing Rankings Board and BoxRec, and second best by \"The Ring\".  His knockout-to-win ratio stands at 100%.  Joshua is the second British boxer, after James DeGale, to win both a gold medal at the Olympics and a world title by a major professional sanctioning body, as well as being the first British heavyweight to do so.  He is also the second boxer, after Joe Frazier, to win a world heavyweight title whilst still reigning as Olympic champion at the top weight.\n\nJoshua Buatsi: Joshua Buatsi (born 14 March 1993) is a Ghanaian-born British boxer who competed and won a Bronze Medal at the 2016 Summer Olympics held in Rio de Janeiro, Brazil, in the light heavyweight division.  He turned professional on 5 June 2017, signing with Matchroom.  He is managed by world heavyweight champion Anthony Joshua.\n\nGary Cornish: Gary Cornish (born April 10, 1987) is a Scottish professional boxer.  Cornish has had 24 fights and lost his undefeated record in the ring to Anthony Joshua in a bout on September 12, 2015 in what was Cornish's first Commonwealth title attempt.\n\nOrthodox stance: In combat sports such as boxing, an orthodox stance is one in which the boxer places his left foot farther in front of the right foot, thus having his weaker side closer to the opponent.  As it favors the stronger, dominant side—often the right side, see laterality—the orthodox stance is the most common stance in boxing.  It is mostly used by right-handed boxers.  Many boxing champions—such as Jack Johnson, Anthony Joshua, Marco Antonio Barrera, Rocky Marciano, Ingmar Johansson, Roberto Durán, Floyd Mayweather Jr., Muhammad Ali, Amir Khan, Peter Buckley, Johnny Tapia, Mike Tyson, Larry Holmes, Lennox Lewis, and Wladimir Klitschko —fought in an orthodox stance.\n\nDominic Breazeale: Dominic Breazeale (born August 24, 1985) is an American professional boxer and one of the division's most popular top contenders.  As an amateur he fought at super heavyweight and was the number one rated U.S. amateur boxer in the division.  Breazeale is best known for his 2016 IBF world heavyweight title defeat to current champion Anthony Joshua in London.\n\nAnthony Joshua vs. Wladimir Klitschko: Anthony Joshua vs. Wladimir Klitschko was a professional boxing match contested between Anthony Joshua and Wladimir Klitschko.  The event took place on 29 April 2017 at Wembley Stadium in London, England, with Joshua's IBF and the vacant WBA (Super) and IBO heavyweight titles on the line.  Joshua won the match via technical knockout in the 11th round.  Klitschko announced his retirement from boxing a few months after the fight.\n\nAustralia at the 2010 Winter Paralympics: At the 2010 Winter paralympics in Vancouver, British Columbia, Canada Australia sent ever of 11 competitors to compete against 42 other nations with a total of 502 competitors making these olympics the largest ever with only 39 countries competing at Torino in 2006.  Of these other nations, 2010 was the first winter paralympics for Argentina, Bosnia & Herzegovina, Romania, Russian Federation, and Serbia.  The delegation also consisted of 3 sighted guides and 17 support staff.  This was the largest delegation Australia had sent to a Winter Paralympics.  Australia has competed at every winter Paralympics, with a history of five athletes that are known to have participated in both the Summer and Winter Paralympic Games between 1960 and 2010: Peter Richards (athletics, snooker, and cross-country skiing), Kyrra Grunnsund, Anthony Bonaccurso, Michael Milton and Dominic Monypenny.  Of these athletes, Dominic Monypenny was the only one to compete at the 2010 games.  Nine out of the 11 athletes prior to the 2010 winter Paralympics had recorded top 10 finishes in Paralympic, world cup or world championship competition in their class, in the lead-up to the games.\n\nDominic Anthony: Dominic Anthony Hughes (born 14 March 1997), commonly known by his stage name Dominic Anthony, is an English magician from Boothstown, Salford.\n\nRoberto Cammarelle: Roberto Cammarelle (born 30 July 1980) is an Italian boxer, best known for winning the World Amateur Boxing Championships in 2007 (Chicago) and 2009 (Milan) as a super heavyweight and a gold medal at the 2008 Olympic Games in Beijing.  He won a silver medal in 2012 London Olympics Games, losing to Anthony Joshua, by a contested jury's decision that was unsuccessfully appealed.\n\nAnthony Shaffer (writer): Anthony Joshua Shaffer (15 May 19266 November 2001) was an English playwright, screenwriter, novelist, barrister and advertising executive.\n\nQuestion: what does Dominic Breazeale and Anthony Joshua have in common?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"common_profession\": {\n      \"type\": \"string\",\n      \"description\": \"The profession shared by both individuals.\"\n    },\n    \"individuals_involved\": {\n      \"type\": \"array\",\n      \"description\": \"Details about the individuals involved.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the individual.\"\n          },\n          \"nationality\": {\n            \"type\": \"string\",\n            \"description\": \"The nationality of the individual.\"\n          }\n        },\n        \"required\": [\n          \"name\",\n          \"nationality\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"shared_event\": {\n      \"type\": \"object\",\n      \"description\": \"A specific event in which both individuals participated.\",\n      \"properties\": {\n        \"event_type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of event.\"\n        },\n        \"participants\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"The names of the participants in the event.\"\n        },\n        \"winner\": {\n          \"type\": \"string\",\n          \"description\": \"The winner of the event.\"\n        },\n        \"loser\": {\n          \"type\": \"string\",\n          \"description\": \"The loser of the event.\"\n        },\n        \"title_contested\": {\n          \"type\": \"string\",\n          \"description\": \"The title that was on the line during the event.\"\n        },\n        \"year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the event took place.\"\n        },\n        \"location\": {\n          \"type\": \"string\",\n          \"description\": \"The location where the event took place.\"\n        }\n      },\n      \"required\": [\n        \"event_type\",\n        \"participants\",\n        \"winner\",\n        \"loser\",\n        \"title_contested\",\n        \"year\",\n        \"location\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"common_profession\",\n    \"individuals_involved\",\n    \"shared_event\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "common_profession": {
        "type": "string",
        "description": "The profession shared by both individuals."
      },
      "individuals_involved": {
        "type": "array",
        "description": "Details about the individuals involved.",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "The name of the individual."
            },
            "nationality": {
              "type": "string",
              "description": "The nationality of the individual."
            }
          },
          "required": [
            "name",
            "nationality"
          ],
          "additionalProperties": false
        }
      },
      "shared_event": {
        "type": "object",
        "description": "A specific event in which both individuals participated.",
        "properties": {
          "event_type": {
            "type": "string",
            "description": "The type of event."
          },
          "participants": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "The names of the participants in the event."
          },
          "winner": {
            "type": "string",
            "description": "The winner of the event."
          },
          "loser": {
            "type": "string",
            "description": "The loser of the event."
          },
          "title_contested": {
            "type": "string",
            "description": "The title that was on the line during the event."
          },
          "year": {
            "type": "integer",
            "description": "The year the event took place."
          },
          "location": {
            "type": "string",
            "description": "The location where the event took place."
          }
        },
        "required": [
          "event_type",
          "participants",
          "winner",
          "loser",
          "title_contested",
          "year",
          "location"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "common_profession",
      "individuals_involved",
      "shared_event"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
