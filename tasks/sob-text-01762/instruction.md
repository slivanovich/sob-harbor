{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nTimeline of the presidency of Donald Trump: Donald Trump was elected President of the United States on November 8, 2016 and was inaugurated on January 20, 2017.  He is currently serving his day in office.  For President Trump's first 100 days in office, see Donald Trump's first 100 days.  For his time as President-elect, see Presidential transition of Donald Trump.  The following articles cover the timeline of the presidency of Donald Trump:\n\nAudrey MacLean: Audrey MacLean (born 1952) is an American businesswoman and entrepreneur.  She has been featured on Forbes’ Midas Touch List, \"Fortune\"’s Most Powerful Women and \"Business Week\"’s Top 50 Business Women in America.\n\nRobert Kiyosaki: Robert Toru Kiyosaki (born April 8, 1947) is an American businessman and author.  Kiyosaki is the founder of the Rich Dad Company, a private financial education company that provides personal finance and business education to people through books and videos.  He is also the creator of the Cashflow board and software games to educate adults and children business and financial concepts.\n\nThe Midas Touch (1997 film): The Midas Touch is a 1997 film directed by Peter Manoogian, starring Trever O'Brien.\n\nJohn Hays Hammond: John Hays Hammond (31 March 1855 – 8 June 1936) was a mining engineer, diplomat, and philanthropist.  Known as the man with the Midas touch, he amassed a sizable fortune before the age of 40.  An early advocate of deep mining, Hammond was given complete charge of Cecil Rhodes' mines in South Africa and made each undertaking a financial success.  But after the dismal failure of the Jameson Raid, Hammond, along with the other leaders of the Johannesburg Reform Committee, was arrested and subsequently sentenced to death.  The Reform Committee leaders were released after paying large fines, but like many of the leaders, Hammond left Africa for good.  He returned to the United States, became a close friend of President William Howard Taft, and was appointed a special United States Ambassador.  At the same time, he continued to develop mines in Mexico and California and, in 1923, he made another fortune while drilling for oil with the Burnham Exploration Company.  His son, John Hays Hammond, Jr., patented over 400 inventions, and is widely regarded as the father of \"radio control\".\n\nEldorado (1988 film): Eldorado (Hungarian: \"Eldorádó\" , also known as The Midas Touch) is a 1988 Hungarian drama film written and directed by Géza Bereményi.\n\nThe Midas Touch (1940 film): The Midas Touch is a 1940 British thriller film directed by David MacDonald and starring Barry K. Barnes, Judy Kelly, Frank Cellier and Bertha Belmore.\n\nThe Midas Touch (2013 film): The Midas Touch is a 2013 Hong Kong comedy film directed by Andrew Fung and starring Chapman To and Charlene Choi as talent managers.\n\nMidas Touch (book): Midas Touch: Why Some Entrepreneurs Get Rich — And Why Most Don't is a non-fiction book about personal finance, co-authored by Donald Trump and Robert Kiyosaki.  The book was published in hardcover format in 2011.  The coauthors became familiar with each other through mutual work at The Learning Annex, and \"The Art of the Deal\".  Trump was impressed by Kiyosaki's writing success with \"Rich Dad Poor Dad\".  The coauthors then wrote \"Why We Want You to be Rich\" together in 2006, and followed it up with \"Midas Touch\" in 2011.\n\nWhy We Want You to Be Rich: Why We Want You to Be Rich: Two Men, One Message is a non-fiction book about personal finance, co-authored by Donald Trump and Robert Kiyosaki.  The book was first published in hardcover format in 2006.  The coauthors became familiar with each other through mutual work at The Learning Annex, and \"The Art of the Deal\" author Trump was impressed by Kiyosaki's writing success with \"Rich Dad Poor Dad\".  Trump and Kiyosaki subsequently co-authored another book together in 2011, \"Midas Touch: Why Some Entrepreneurs Get Rich-And Why Most Don't\".\n\nQuestion: Midas Touch: Why Some Entrepreneurs Get Rich is a book written by Donald Trump and the founder of what company?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"book_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\"\n        },\n        \"publication_year\": {\n          \"type\": \"integer\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"publication_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"primary_authors\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      }\n    },\n    \"company_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"founder_name\": {\n          \"type\": \"string\"\n        },\n        \"company_name\": {\n          \"type\": \"string\"\n        },\n        \"company_description\": {\n          \"type\": \"string\"\n        }\n      },\n      \"required\": [\n        \"founder_name\",\n        \"company_name\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"book_details\",\n    \"primary_authors\",\n    \"company_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "book_details": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string"
          },
          "publication_year": {
            "type": "integer"
          }
        },
        "required": [
          "title",
          "publication_year"
        ],
        "additionalProperties": false
      },
      "primary_authors": {
        "type": "array",
        "items": {
          "type": "string"
        }
      },
      "company_details": {
        "type": "object",
        "properties": {
          "founder_name": {
            "type": "string"
          },
          "company_name": {
            "type": "string"
          },
          "company_description": {
            "type": "string"
          }
        },
        "required": [
          "founder_name",
          "company_name"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "book_details",
      "primary_authors",
      "company_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
