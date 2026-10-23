{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBob Kempainen: Robert \"Bob\" Kempainen, MD (born June 18, 1966 in Minneapolis, Minnesota) is a retired long-distance runner from the United States, who represented his native country twice at the Summer Olympics, in 1992 (Barcelona, Spain) and in 1996 (Atlanta, United States).  He made his marathon debut in 1991 at the Twin Cities Marathon in Minnesota, where he finished 2nd in a time of 2:12:12.  In 1992, he qualified for the Olympic Games by finishing third, in a time of 2:12:54, in the Olympic Trials marathon, held in Columbus, Ohio.  He finished 2nd at the 1993 New York City Marathon in a time of 2:11:03.  His best time for the marathon was 2:08:47 at the 1994 Boston Marathon, where he finished 7th.  In 1995, he finished 2nd at the Los Angeles Marathon, in a time of 2:11:59.  He was the 1996 Olympic Trials Marathon (held in Charlotte, North Carolina) champion, winning in a time of 2:12:45.\n\n1982 NCAA Indoor Track and Field Championships: The 1982 NCAA Indoor Track and Field Championships were contested March 12−13, 1982 at the Pontiac Silverdome in Pontiac, Michigan at the 18th annual NCAA-sanctioned track meet to determine the individual and team national champions of men's collegiate indoor track and field events in the United States.  This was the first championship not hosted at Detroit's Cobo Arena, the venue of the previous 17 events.\n\n1984 NCAA Indoor Track and Field Championships: The 1984 NCAA Indoor Track and Field Championships were contested March 9−10, 1984 at the Carrier Dome at Syracuse University in Syracuse, New York to determine the individual and team national champions of men's and women's NCAA collegiate indoor track and field events in the United States.  These were the 20th annual men's championships and the 2nd annual women's championships.\n\nGilliam Indoor Track Stadium: The Gilliam Indoor Track Stadium is the home of the Texas A&M Aggies men's and women's collegiate indoor track and field teams.  Opened on January 24, 2009, the facility hosted the 2009 Big 12 Conference indoor track championships as well as the 2009 NCAA Division I indoor track national championships.\n\nFrances Koons: Frances Koons (born April 2, 1986, Bethlehem, Pennsylvania) is an American middle distance runner who attended Villanova University and now runs professionally for New Balance.  Koons finished 2nd to Sally Kipyego at the 2009 NCAA Indoor Track 5000m race, and 3rd to Angela Bizzarri and Nicole Blood at the 2009 NCAA Outdoor Track 5000m race.  Koons ran the 1200m opening leg for the Villanova team that won the 2004 Penn Relays Championship of America distance medley relay.  She earned 10 NCAA All-American honors in Cross Country and Track & Field while at Villanova.  Koons also earned 5 individual and 2 team Big East titles during her career.  Koons graduated from Villanova University in 2009 with a Bachelor of Science degree in Mathematics.  In April 2010 at the Penn Relays Koons won the women's Olympic Development event at 5,000 meters and qualified for U.S. Outdoor Track and Field Championships.\n\n1978 NCAA Indoor Track and Field Championships: The 1978 NCAA Indoor Track and Field Championships were contested March 10−11, 1978 at Cobo Arena in Detroit, Michigan at the 14th annual NCAA-sanctioned track meet to determine the individual and team national champions of men's collegiate indoor track and field events in the United States.\n\nLee Emanuel: Lee Emanuel (born 24 January 1985) is an English middle-distance runner.  He represented Great Britain at the 2014 and 2016 World Indoor Championships.  In addition he won a silver medal at the 2015 European Indoor Championships.  Lee attended the University of New Mexico where he won 2 indoor Mile titles in NCAA Indoor Track and Field.\n\n1983 NCAA Indoor Track and Field Championships: The 1983 NCAA Indoor Track and Field Championships were contested March 11−12, 1983 at the Pontiac Silverdome in Pontiac, Michigan to determine the individual and team national champions of men's and, for the first time, women's NCAA collegiate indoor track and field events in the United States.  These were the 19th annual men's championships and the 1st annual women's championships.\n\n1981 NCAA Indoor Track and Field Championships: The 1981 NCAA Indoor Track and Field Championships were contested March 13−14, 1981 at Cobo Arena in Detroit, Michigan at the 17th annual NCAA-sanctioned track meet to determine the individual and team national champions of men's collegiate indoor track and field events in the United States.  This was Cobo Arena's final time hosting the event after hosting all previous seventeen indoor championships.\n\nSally Kipyego: Sally Jepkosgei Kipyego (born 19 December 1985) is a Kenyan long- and middle-distance runner.  She was the silver medallist in the 10,000 metres at the 2011 World Championships in Athletics and the silver medalist in the same race at the 2012 Summer Olympic Games in London.  She has a personal record of 30:38.35 minutes for that event and her 5000 metres best of 14:30.42 minutes makes her the second fastest Kenyan woman for the distance.\n\nQuestion: What was the birth date of the Kenyan runner that Frances Koons finished 2nd to at the 2009 NCAA Indoor Track 5000m race?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"runner_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the runner.\"\n    },\n    \"runner_nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The nationality of the runner.\"\n    },\n    \"event_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"event_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the event where Frances Koons finished second to the runner.\"\n        },\n        \"event_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the event took place.\"\n        }\n      },\n      \"required\": [\n        \"event_name\",\n        \"event_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"birth_date\": {\n      \"type\": \"string\",\n      \"description\": \"The birth date of the runner in 'Day Month Year' format.\"\n    }\n  },\n  \"required\": [\n    \"runner_name\",\n    \"runner_nationality\",\n    \"event_details\",\n    \"birth_date\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "runner_name": {
        "type": "string",
        "description": "The name of the runner."
      },
      "runner_nationality": {
        "type": "string",
        "description": "The nationality of the runner."
      },
      "event_details": {
        "type": "object",
        "properties": {
          "event_name": {
            "type": "string",
            "description": "The name of the event where Frances Koons finished second to the runner."
          },
          "event_year": {
            "type": "integer",
            "description": "The year the event took place."
          }
        },
        "required": [
          "event_name",
          "event_year"
        ],
        "additionalProperties": false
      },
      "birth_date": {
        "type": "string",
        "description": "The birth date of the runner in 'Day Month Year' format."
      }
    },
    "required": [
      "runner_name",
      "runner_nationality",
      "event_details",
      "birth_date"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
