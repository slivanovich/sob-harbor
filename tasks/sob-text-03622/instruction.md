{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nPFA Team of the Year (1970s): The Professional Footballers' Association Team of the Year (often called the PFA Team of the Year, or simply the Team of the Year) is an annual award given to a set of 44 footballers in the top four tiers of English football; the Premier League, the Championship, League One and League Two, who are seen to be deserving of being named in a \"Team of the Year\".  Peter Shilton currently holds the most appearances in the PFA Team of the Year in the top division with 10 appearances.  Steven Gerrard currently holds the most appearances in the PFA Team of the Year in the Premier League era with eight appearances.\n\nPFA Team of the Year (2000s): The Professional Footballers' Association Team of the Year (often called the PFA Team of the Year, or simply the Team of the Year) is an annual award given to a set of 44 footballers in the top four tiers of English football; the Premier League, the Championship, League One and League Two, who are seen to be deserving of being named in a \"Team of the Year\".  Peter Shilton currently holds the most appearances in the PFA Team of the Year in the top division with 10 appearances.  Steven Gerrard currently holds the most appearances in the PFA Team of the Year in the Premier League era with eight appearances.\n\nList of American Idol finalists: \"American Idol\" is an American talent reality television series that first aired in 2002.  As of May 2015, there have been fourteen seasons.  Each season, the final round of competition features ten to thirteen singers.  A total of 178 contestants have reached the finals of their season.  The show's age requirements have varied year-to-year.  Of the finalists, 55 of them were under the age of 20, including three winners and five runners-up.  Season-one-winner Kelly Clarkson currently holds the record for the highest-selling album sales worldwide, with more than 25 million copies, while season-four-winner Carrie Underwood currently holds the record for the highest-selling album sales in the United States, with more than 13 million copies.\n\nAntonietta Di Martino: Antonietta Di Martino (born 1 June 1978 in Cava de' Tirreni) is a retired Italian high jumper.  She currently holds the Italian national women's high jump record at 2.03 metres for outdoor events and 2.04 metres for indoor events.  She also currently holds the women's all-time highest jump-differential, meaning she has jumped the highest (0.35 metres) more than her own height.\n\nIan Gundry-White: Ian Malcolm Gundry-White, (21 December 1918 – 15 September 1961) was a Royal Air Force officer of the Second World War and Cold War period, who served as the Chief of Air Staff of the Ghana Air Force from September 1960 to March 1961.\n\nChief of Air Staff (Ghana): Chief of Air Staff is the official title of the highest ranking air force personnel of the Ghana Air Force.  The current Chief of Air Staff is Air Vice Maxwell Mantsebi-Tei Nagai.\n\nPFA Team of the Year: The Professional Footballers' Association Team of the Year (often called the PFA Team of the Year, or simply the Team of the Year) is an annual award given to a set of 44 footballers in the top four tiers of English football; the Premier League, the Championship, League One and League Two, who are seen to be deserving of being named in a \"Team of the Year\".  Peter Shilton currently holds the most appearances in the PFA Team of the Year in the top division with 10 appearances.  Steven Gerrard currently holds the most appearances in the PFA Team of the Year in the Premier League era with 8 appearances.\n\nPFA Team of the Year (1980s): The Professional Footballers' Association Team of the Year (often called the PFA Team of the Year, or simply the Team of the Year) is an annual award given to a set of 44 footballers in the top four tiers of English football; the Premier League, the Championship, League One and League Two, who are seen to be deserving of being named in a \"Team of the Year\".  Peter Shilton currently holds the most appearances in the PFA Team of the Year in the top division with 10 appearances.  Steven Gerrard currently holds the most appearances in the PFA Team of the Year in the Premier League era with eight appearances.\n\nPFA Team of the Year (2010s): The Professional Footballers' Association Team of the Year (often called the PFA Team of the Year, or simply the Team of the Year) is an annual award given to a set of 55 footballers across the top four tiers of men's English football; the Premier League, the Championship, League One and League Two, as well as the women's FA WSL, who are seen to be deserving of being named in a \"Team of the Year\".  Peter Shilton currently holds the most appearances in the PFA Team of the Year in the top division with 10 appearances.  Steven Gerrard currently holds the most appearances in the PFA Team of the Year in the Premier League era with eight appearances.\n\nI-500: The I-500 is an American snowmobile race associated with the USCC Racing Association (USCC) which starts at the Seven Clans Casino in Thief River Falls, Minnesota.  The cross-country race is a 3-day event and is 500 miles long (170 miles a day).  The race was first ran in 1966 and was then ran from Winnipeg, Manitoba to St. Paul, Minnesota.  The race is now started in Thief River Falls and is run through the Red Lake Indian Reservation and finishes again at the starting line.  The I-500 has been known to be the most grueling snowmobile race of all time next to the Iron Dog in Alaska.  Ski-Doo racer Bryan Dyrdahl currently holds the Pro 600 record at the I-500 at 5 wins (2000, 2004, 2006, 2008, 2009).  Arctic Cat racer Justin Morken currently holds the record as the youngest racer to ever finish the I-500 (14 years, 16 days old in 2007).  On April 18, 2009, USCC Racing president Pat Mach announced at the USCC year-end awards ceremony in the Arrowood resort in Alexandria, Minnesota, that the USCC plans to race the original I-500 from Winnipeg to St. Paul in 2012.  That would be the 40th anniversary for the I-500.\n\nQuestion: Who currently holds the same title that Ian Gundry-White held in 1961?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"title_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the official title or position.\"\n    },\n    \"former_holder\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the person who previously held the title.\"\n        },\n        \"start_year_of_service\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the former holder started their service in this role.\"\n        },\n        \"end_year_of_service\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the former holder ended their service in this role.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"start_year_of_service\",\n        \"end_year_of_service\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"current_holder\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the person who currently holds the title.\"\n        }\n      },\n      \"required\": [\n        \"name\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"title_name\",\n    \"former_holder\",\n    \"current_holder\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "title_name": {
        "type": "string",
        "description": "The name of the official title or position."
      },
      "former_holder": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the person who previously held the title."
          },
          "start_year_of_service": {
            "type": "integer",
            "description": "The year the former holder started their service in this role."
          },
          "end_year_of_service": {
            "type": "integer",
            "description": "The year the former holder ended their service in this role."
          }
        },
        "required": [
          "name",
          "start_year_of_service",
          "end_year_of_service"
        ],
        "additionalProperties": false
      },
      "current_holder": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the person who currently holds the title."
          }
        },
        "required": [
          "name"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "title_name",
      "former_holder",
      "current_holder"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
