{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nChristian Science Center: The Christian Science Center is a 14.5 acre site on the corner of Massachusetts Avenue and Huntington Avenue in the Fenway neighborhood of Boston, Massachusetts.  A popular tourist attraction, the center is owned by the Church of Christ, Scientist (the Christian Science church), which refers to it as Christian Science Plaza.  The complex, including most of the landscape was designated as a Boston Landmark by the Boston Landmarks Commission in 2011.\n\nChristian Science Center- Belvidere/ Dalton: The Belvidere/Dalton tower is a planned 60-story, 699' tower on the grounds of Boston's Christian Science Center adjacent to the Prudential Tower complex on a small, triangular open space owned by the Christian Science Center above the entrance ramps to the complex's parking garage.  There will also be a mid-rise, 285' tower built across the street on a current parking lot.  The taller tower will be of mixed hotel/residential usage with first-floor retail, while the mid-rise tower will be fully residential with first-floor retail as well.\n\nThe Herald of Christian Science: The Herald of Christian Science was first published in 1903 in response to the demand for a monthly publication on Christian Science in Germany.  Due to an increasing demand for Christian Science Literature from other countries, the \"Herald\" grew to include twelve different languages.  Until the 90’s the magazine was bilingual, with English and translated texts side by side.  Currently the \"Herald\" is available in fourteen languages, giving readers around the world an understanding of Christian Science practice.  Along with articles and accounts of healing, each issue includes a directory of Christian Science churches, practitioners and other listings applicable to each language.  \"The Herald\" is also produced as a radio program in five languages.\n\nChristian Science Pleasant View Home: The Christian Science Pleasant View Home is a historic senior citizen residential facility located at 227 Pleasant Street in Concord, New Hampshire, in the United States, It was built in 1927 by the Christian Science Board of Directors as a retirement home for aged Christian Science practitioners and other workers in the cause of Christian Science and occupies the site of \"Pleasant View\", Mary Baker Eddy's last home before moving to Chestnut Hill, Massachusetts, in 1908.  It is now Pleasant View Retirement, a senior independent living facility.  On September 19, 1984, it was added to the National Register of Historic Places.\n\nChurch of Christ, Scientist: The Church of Christ, Scientist was founded in 1879 in Boston, Massachusetts, by Mary Baker Eddy, author of \"Science and Health with Key to the Scriptures,\" and founder of Christian Science.  The church was founded \"to commemorate the word and works of [Christ Jesus]\" and \"reinstate primitive Christianity and its lost element of healing\".  Sunday services are held throughout the year and weekly testimony meetings are held on Wednesday evenings, where following brief readings from the Bible and the Christian Science textbook, those in attendance are invited to give testimonies of healing brought about through Christian Science prayer.\n\nChristian Science practitioner: A Christian Science practitioner is an individual who prays for others according to the teachings of Christian Science.  Treatment is non-medical, rather it is based on the Bible and the Christian Science textbook, \"Science and Health with Key to the Scriptures\" (1875) by Mary Baker Eddy (1821–1910), who \"discovered\" Christian Science in 1866 and founded the Christian Science church in 1879.  According to the church, Christian Science practitioners address physical conditions, as well as relationship or financial difficulties and any other problem or crisis.  Practitioners are either \"listed\" or \"unlisted,\" a designation that refers to a form of international accreditation maintained by The Mother Church, in Boston, Massachusetts.\n\nReader (Christian Science Church): A Reader in a Christian Science church is a member of the congregation who has been elected to serve in one of two positions responsible for church services.  Each week's sermon in Christian Science churches is outlined in the \"Christian Science Quarterly\", prepared months in advance, and is the same in all Christian Science churches, worldwide.  A lay church, it has no clergy; rather, the sermons consist of passages from the \"Bible\" and the Christian Science textbook, are studied as lessons during the week and are read aloud to the congregation on the Sunday following.\n\nEighth Church of Christ, Scientist: Eighth Church of Christ, Scientist is an historic Christian Science church located at 4359 S. Michigan Avenue / 112 E. 44th street (Michigan Avenue at 44th Street) in Chicago, Illinois, United States.  It was built between 1910 and 1911 by Leon E. Stanhope.  The church has the distinction of being one of the oldest African-American Christian Science congregations in the United States.  It was designated a Chicago Landmark on June 9, 1993.  It is still an active Christian Science church.\n\nChristian Science Reading Room: A Christian Science Reading Room is a place operated as a public service by a Christian Science church in the community where that church exists.  The Mother Church (The First Church of Christ, Scientist) in Boston, Massachusetts, maintains these rooms as a place where one may study and contemplate the Bible and Christian Science literature in a quiet atmosphere, similar to a library.\n\nChristian Science Sentinel: The Christian Science Sentinel (originally the \"Christian Science Weekly\") is a magazine published by the Christian Science Publishing Society based in Boston, Massachusetts.  The magazine was launched by Mary Baker Eddy in 1898.  It includes articles, editorials, and accounts of healings from a Christian Science point of view.\n\nQuestion: Who founded the church that owns the Christian Science Center in Boston, Massachusetts?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"founder\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the individual who founded the church.\"\n        }\n      },\n      \"required\": [\n        \"name\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"church\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the church.\"\n        },\n        \"founding_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the church was founded.\"\n        },\n        \"founding_location\": {\n          \"type\": \"string\",\n          \"description\": \"The city and state where the church was founded.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"founding_year\",\n        \"founding_location\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"property_owned\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the property owned by the church.\"\n        },\n        \"location\": {\n          \"type\": \"string\",\n          \"description\": \"The city and state where the property is located.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"location\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"founder\",\n    \"church\",\n    \"property_owned\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "founder": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the individual who founded the church."
          }
        },
        "required": [
          "name"
        ],
        "additionalProperties": false
      },
      "church": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the church."
          },
          "founding_year": {
            "type": "integer",
            "description": "The year the church was founded."
          },
          "founding_location": {
            "type": "string",
            "description": "The city and state where the church was founded."
          }
        },
        "required": [
          "name",
          "founding_year",
          "founding_location"
        ],
        "additionalProperties": false
      },
      "property_owned": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the property owned by the church."
          },
          "location": {
            "type": "string",
            "description": "The city and state where the property is located."
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
      "founder",
      "church",
      "property_owned"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
