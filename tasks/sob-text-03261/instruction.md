{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nFuller ministry (1921): The Fuller ministry (1921) or First Fuller ministry was the 39th ministry of the New South Wales Government, and was led by the 22nd Premier, the Honourable Sir George Fuller KCMG, MLA.  This ministry is the shortest of any ministry in the history of self-government in the state, lasting just seven hours.\n\nElectoral district of Fuller: Fuller was an electoral district of the Legislative Assembly in the Australian state of New South Wales, created in 1968 in the Ryde area and named after George Fuller, Premier of New South Wales, 1922-1925.  It was abolished in 1981 and largely replaced by Gladesville.\n\nGeorge Fuller (British politician): Fuller was born at Baynton, Wiltshire, the eldest surviving son of John Bird Fuller, a partner in Fuller Smith & Turner, brewers, and his wife Sophia Hanning, daughter of John Hanning.  He was educated at Winchester, where he played in the 1st XI cricket for two years, and at Christ Church, Oxford.  During his time at Oxford he represented the Oxford University Cricket Club and played in the Varsity match in 1854 and 1855.  He played nine innings in six first class matches with an average of 10.44 and a top score of 40.  He bowled ten overs and took 6 first-class wickets.\n\nFuller ministry (1922–25): The Fuller ministry (1922–1925) or Second Fuller ministry was the 41st ministry of the New South Wales Government, and was led by the 22nd Premier, the Honourable Sir George Fuller KCMG, MLA.  This ministry was the second of two occasions where Fuller was Premier.\n\nHerbert Fuller: Herbert George Fuller (4 October 1856 – 2 January 1896) was an English born rugby union forward who played club rugby for Cambridge University and won four international caps for the England national rugby union team between 1882 and 1884.\n\nGeorge Godfrey (journalist): George Fuller Godfrey CBE (5 November 1904 – 16 September 1989) was an English-born Australian journalist and trade unionist.\n\nFuller's Brewery: Fuller's Brewery (Fuller, Smith & Turner plc) is an independent family regional brewery founded in 1845 in Chiswick, West London.\n\nGeorge Fuller Miller Sr.: George Fuller Miller Sr. (born March 19, 1903 in Indianapolis, Indiana) was a long-time Boy Scouts of America executive, the recipient of the Distinguished Eagle Scout Award and a founding father of the American Humanics Foundation.\n\nWhite Rats of America: The White Rats was an organization formed by vaudeville performers, led by George Fuller Golden, as a labor union to support the rights of male performers.  It was a Men's Club only.  Women were not allowed to join.  It also attempted to combat the monopolistic practices of the United Booking Office (UBO) and the Vaudeville Managers Association (VMA), groups formed by vaudeville theater managers to keep performers' wages low and control when and where performers were allowed to work.  It was based on the Water Rats, a British entertainment industry charity.  It received a charter from the American Federation of Labor in 1910.  The union staged several strikes but ultimately disbanded.\n\nHenry Keep (American football): Henry Keep (July 19, 1872 – December 1965) was an American football coach.  He served as the first head football coach at Michigan Agricultural College, now known as Michigan State University, from 1897 to 1898, compiling a record of 8–5–1.  He served as the school's football and track coach while also attending the college as an engineering student.  Keep was a student at the University of Michigan during the 1893–94 academic year before transferring to Michigan Agricultural.  As of 1901, he was working for the George Fuller & Co. in New York.  Keep and his wife, Esther Maude Durgin had a daughter, Margaret in 1914 in Bellefonte, Pennsylvania.  He also later worked for the Carnegie Steel Company in Pittsburgh.\n\nQuestion: George Fuller's father founded a brewery in what year?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"george_fuller_identifier\": {\n      \"type\": \"string\",\n      \"description\": \"An identifier for the specific George Fuller referenced in the context.\"\n    },\n    \"father_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of George Fuller's father.\"\n    },\n    \"brewery_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the brewery.\"\n        },\n        \"founding_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the brewery was founded.\"\n        },\n        \"father_role\": {\n          \"type\": \"string\",\n          \"description\": \"The role of George Fuller's father in the brewery.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"founding_year\",\n        \"father_role\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"george_fuller_identifier\",\n    \"father_name\",\n    \"brewery_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "george_fuller_identifier": {
        "type": "string",
        "description": "An identifier for the specific George Fuller referenced in the context."
      },
      "father_name": {
        "type": "string",
        "description": "The name of George Fuller's father."
      },
      "brewery_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the brewery."
          },
          "founding_year": {
            "type": "integer",
            "description": "The year the brewery was founded."
          },
          "father_role": {
            "type": "string",
            "description": "The role of George Fuller's father in the brewery."
          }
        },
        "required": [
          "name",
          "founding_year",
          "father_role"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "george_fuller_identifier",
      "father_name",
      "brewery_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
