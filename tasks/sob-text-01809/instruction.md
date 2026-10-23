{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nAsian Gymnastics Championships: The Asian Gymnastic Union (AGU) organizes Asian Gymnastics Championships for each of the FIG gymnastic disciplines: men's and women's artistic gymnastics, rhythmic gymnastics, acrobatic gymnastics, aerobic gymnastics and trampoline gymnastics.  This article lists only the senior editions of the Asian Gymnastics Championships, in which competitors must be over 16 years of age.  Specific editions of the Asian Championships also exist for junior athletes; for example, the first edition of the Junior Asian Artistic Gymnastics Championships was held in 1971, but the first senior edition of the tournament was only held in 1996.  Similarly, Junior Asian Trampoline Championships were held in 2010 and 2012, but only in 2014 the Asian Gymnastics Union held a senior tournament in conjunction with the junior championships for the first time.\n\n2016 World Aesthetic Gymnastics Championships: The 2016 World Aesthetic Gymnastics Championships, the 17th edition of the Aesthetic group gymnastics competition, was held in Brno, Czech Republic from June 9 to 12, at the Sport hall Vodova.\n\n2015 World Aesthetic Gymnastics Championships: The 2015 World Aesthetic Gymnastics Championships, the 16th edition, was held in Tórshavn, Faroe Islands, from May 25 to September 7, 2015 at the Ítróttarhøllin á Hálsi.\n\n2017 World Aesthetic Gymnastics Championships: The 2017 World Aesthetic Gymnastics Championships, the 18th edition of the Aesthetic group gymnastics competition, was held in Helsinki, Finland from May 26 to 28, at the Helsinki Ice Hall.\n\nAndrea Coppolino: Andrea Coppolino (born (1979--)19 1979 ) is an Italian male artistic gymnast, representing his nation at international competitions.  He participated at the 2008 Summer Olympics in Beijing, China.  He also competed at world championships, including the 1999 World Artistic Gymnastics Championships, 2001 World Artistic Gymnastics Championships, 2002 World Artistic Gymnastics Championships, 2003 World Artistic Gymnastics Championships, 2005 World Artistic Gymnastics Championships, 2006 World Artistic Gymnastics Championships and 2007 World Artistic Gymnastics Championships.\n\nFour Continents Rhythmic Gymnastics Championships: The Four Continents Rhythmic Gymnastics Championships was a biennial rhythmic gymnastics tournament gathering competitors from four different continents: Africa, the Americas, Asia and Oceania.  The tournament was proposed to the International Gymnastics Federation (FIG) by members of the gymnastics federations of New Zealand and Canada.  The purpose was to provide a corresponding event to the European Rhythmic Gymnastics Championships as a chance for rhythmic gymnasts from non-European nations to compete internationally.  The first edition of the Four Continent Championships was organized in 1978 in Toronto, Canada.  The last edition of the tournament was held in Curitiba, Brazil, in 2001.  All of the editions of the championships were officially organized by FIG; besides the Four Continents Championships, only two other major meets were officially organized by the federation: the World Gymnastics Championships and the FIG World Cup Final (as well as the different stages of the World Cup and World Challenge Cup series).\n\nLin Chaopan: Lin Chaopan (, born 27 August 1995) is a Chinese artistic gymnast who specializes on Parallel Bars.  Lin made his World Championships debut at the 2013 World Artistic Gymnastics Championships in Antwerp, Belgium.  In the parallel bars final, he won the gold with a score of 15.666 at the age of 18.  He also placed 8th at the horizontal bar final and 9th in the Individual All-Around.  He was selected to compete at the 2014 World Artistic Gymnastics Championships in Nanning, China where he helped China win team gold.  Lin failed to qualify for any individual finals.  At the 2015 World Artistic Gymnastics Championships he won team bronze with his teammates and failed to qualify for other finals.  At the 2016 Chinese Gymnastics Championships he won all-around, parallel bars and floor gold.  Lin will compete at the 2016 Summer Olympics after being selected.\n\nTórshavn: Tórshavn (] ; 'Thor's harbour'; Danish: \"Thorshavn\" , ] ) is the capital and largest town of the Faroe Islands.  Tórshavn is in the southern part on the east coast of Streymoy.  To the northwest of the city lies the 347 m mountain Húsareyn, and to the southwest, the 350 m Kirkjubøreyn.  They are separated by the Sandá River.  The town proper has a population of 13,000 (2008), and the greater urban area a population of 19,000.\n\n2014 World Aesthetic Gymnastics Championships: The 2014 World Aesthetic Gymnastics Championships, the 15th edition of the Aesthetic group gymnastics competition, was held in Moscow, Russia from May 23 to 25.\n\nDimitri Karbanenko: Dimitri Karbanenko (born (1973--)19 1973 ) is a French male artistic gymnast, representing his nation at international competitions.  He participated at the 2000 Summer Olympics, 2004 Summer Olympics and 2008 Summer Olympics.  He also competed at world championships, including the 2003 World Artistic Gymnastics Championships, 2006 World Artistic Gymnastics Championships and 2007 World Artistic Gymnastics Championships\n\nQuestion: In which year were World Aesthetic Gymnastics Championships held in the southern part on the east coast of Streymoy?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"championship_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the World Aesthetic Gymnastics Championships were held.\"\n    },\n    \"championship_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the championship event.\"\n    },\n    \"host_city\": {\n      \"type\": \"string\",\n      \"description\": \"The city where the championships were held.\"\n    },\n    \"host_country\": {\n      \"type\": \"string\",\n      \"description\": \"The country where the championships were held.\"\n    },\n    \"location_description_match\": {\n      \"type\": \"string\",\n      \"description\": \"A description of the host city's location that matches the query.\"\n    }\n  },\n  \"required\": [\n    \"championship_year\",\n    \"championship_name\",\n    \"host_city\",\n    \"host_country\",\n    \"location_description_match\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "championship_year": {
        "type": "integer",
        "description": "The year the World Aesthetic Gymnastics Championships were held."
      },
      "championship_name": {
        "type": "string",
        "description": "The full name of the championship event."
      },
      "host_city": {
        "type": "string",
        "description": "The city where the championships were held."
      },
      "host_country": {
        "type": "string",
        "description": "The country where the championships were held."
      },
      "location_description_match": {
        "type": "string",
        "description": "A description of the host city's location that matches the query."
      }
    },
    "required": [
      "championship_year",
      "championship_name",
      "host_city",
      "host_country",
      "location_description_match"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
