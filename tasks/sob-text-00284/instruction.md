{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nPanabo Christian School: Panabo Christian School (PCS) is a private nonsectarian institution located at San Francisco, Panabo City, Philippines, founded in 1987.\n\nOhio Wesleyan University: Ohio Wesleyan University (also known as Wesleyan or OWU) is a private liberal arts college in Delaware, Ohio, United States.  It was founded in 1842 by Methodist leaders and Central Ohio residents as a nonsectarian institution, and is a member of the Ohio Five — a consortium of Ohio liberal arts colleges.  Ohio Wesleyan has always admitted students irrespective of religion or race and maintained that the university \"is forever to be conducted on the most liberal principles.\"\n\nTufts University: Tufts University is a private research university incorporated in the municipality of Medford, Massachusetts, United States.  Tufts College was founded in 1852 by Christian Universalists who worked for years to open a nonsectarian institution of higher learning.  Charles Tufts donated the land for the campus on Walnut Hill, the highest point in Medford, saying that he wanted to set a \"light on the hill\".  The name was changed to Tufts University in 1954, although the corporate name remains \"the Trustees of Tufts College\".  For more than a century, Tufts was a small New England liberal arts college until its transformation into a larger research university in the 1970s.  Tufts is a charter member of the New England Small College Athletic Conference (NESCAC).  In 2017, the university accepted 14.8% of undergraduate applicants from a pool of 21,101.  In 2016, it was ranked 27th nationally and 156th internationally by \"U.S. News & World Report\".\n\nSwoon (artist): Originally known for her street art, Swoon (born Caledonia Dance Curry in 1977) is a mixed media artist who specializes in life-size wheatpaste prints and paper cutouts of human figures.  She studied at the Pratt Institute in Brooklyn, receiving a BA in fine arts in 2002.  She started to gain recognition for her street art around 1999 and large-scale installations soon thereafter; in 2005, she was the subject of an eponymous solo exhibition mounted by now-mentor Jeffrey Deitch.  Swoon has since been featured in major museums including a 2014 solo show, \"Submerged Motherlands\", at the Brooklyn Museum.\n\nGregory Van Maanen: Gregory Van Maanen (born November 3, 1937, Paterson, New Jersey) is an artist who has been exhibiting work since 1988.  He has had several solo shows at Cavin-Morris Gallery in New York as well as a solo show at Rutgers University.  His work has been widely shown in group exhibitions and Van Maanen’s art is in the permanent collections of the New Orleans Museum of Art, First Bank of Minneapolis, National Vietnam Veterans Art Museum, New Jersey State Council of the Arts, Jersey City Museum, Morris Museum, and others.\n\nLong Island University: Long Island University (LIU) is a private, coeducational, nonsectarian institution of higher education with locations and programs spanning the New York metropolitan area, overseas, and online.  The university offers more than 500 academic programs at two main campuses, LIU Post and LIU Brooklyn, as well as non-residential programs at LIU Brentwood, LIU Riverhead, and LIU Hudson at Rockland and Westchester.  LIU has NCAA Division I and II athletics and hosts the annual George Polk Awards in Journalism.\n\nJane Livingston: Jane Livingston is an American art curator.  She is known for organizing a major museum exhibition of Chicano art, and, together with Marcia Tucker, the first major museum exhibition of Bruce Nauman.  Other exhibitions include her show of National Geographic, \"illustrative\" photography; she and curator John Beardsley, also curated an exhibition of black outsider artists in 1982.  This show \"marked an explosion of interest in the work of African American artists.\"  Livingston curated a show of John Alexander's works at the Smithsonian in 2008.\n\nHelene Fuld College of Nursing: The Helene Fuld College of Nursing is an American private, nonsectarian institution of higher learning that offers associate and comprehensive baccalaureate science degrees as continuing education to Licensed Practical and Registered Nurses who aspire to elevate their academic and professional credentials.  The college is located in New York City in the East Harlem section of Manhattan in the Mount Morris Park Historic District at Marcus Garvey Park.  It was founded years ago – in 1945.\n\nShakir Ali Museum: Shakir Ali Museum or Official Birthplace of Artist Shakir Ali is a family home museum in Lahore, Punjab, Pakistan.  The museum was inaugurated in 1975 after the death of famous artist and painter Shakir Ali.\n\nPratt Institute: Pratt Institute is a private, nonsectarian, non-profit institution of higher learning located in the Clinton Hill neighborhood of Brooklyn, New York, United States, with a satellite campus located at 14th Street in Manhattan and an extension campus in Utica, New York (Pratt MWP).  It originated in 1887 with programs primarily in engineering, architecture, and fine arts.  Comprising six schools, the Institute is primarily known for its highly ranked programs in architecture, interior design, and industrial design, and offers both undergraduate and Master's degree programs in a variety of fields with a strong focus on research.\n\nQuestion: Which private, nonsectarian institution has a famous artist featured in major museum solo shows?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"institution_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the private, nonsectarian institution.\"\n    },\n    \"institution_attributes\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"is_private\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the institution is private.\"\n        },\n        \"is_nonsectarian\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the institution is nonsectarian.\"\n        },\n        \"location\": {\n          \"type\": \"string\",\n          \"description\": \"The primary location of the institution.\"\n        }\n      },\n      \"required\": [\n        \"is_private\",\n        \"is_nonsectarian\",\n        \"location\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"associated_artist\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"artist_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the artist associated with the institution.\"\n        },\n        \"education_details\": {\n          \"type\": \"object\",\n          \"properties\": {\n            \"degree\": {\n              \"type\": \"string\",\n              \"description\": \"The degree received by the artist from the institution.\"\n            },\n            \"year_received\": {\n              \"type\": \"integer\",\n              \"description\": \"The year the degree was received.\"\n            }\n          },\n          \"required\": [\n            \"degree\",\n            \"year_received\"\n          ],\n          \"additionalProperties\": false\n        },\n        \"major_museum_solo_shows\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"object\",\n            \"properties\": {\n              \"show_title\": {\n                \"type\": \"string\",\n                \"description\": \"The title of the solo exhibition.\"\n              },\n              \"museum_name\": {\n                \"type\": \"string\",\n                \"description\": \"The name of the museum where the solo exhibition was held.\"\n              },\n              \"year\": {\n                \"type\": \"integer\",\n                \"description\": \"The year the solo exhibition took place.\"\n              }\n            },\n            \"required\": [\n              \"show_title\",\n              \"museum_name\",\n              \"year\"\n            ],\n            \"additionalProperties\": false\n          },\n          \"description\": \"A list of major museum solo shows featuring the artist.\"\n        }\n      },\n      \"required\": [\n        \"artist_name\",\n        \"education_details\",\n        \"major_museum_solo_shows\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"institution_name\",\n    \"institution_attributes\",\n    \"associated_artist\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "institution_name": {
        "type": "string",
        "description": "The name of the private, nonsectarian institution."
      },
      "institution_attributes": {
        "type": "object",
        "properties": {
          "is_private": {
            "type": "boolean",
            "description": "Indicates if the institution is private."
          },
          "is_nonsectarian": {
            "type": "boolean",
            "description": "Indicates if the institution is nonsectarian."
          },
          "location": {
            "type": "string",
            "description": "The primary location of the institution."
          }
        },
        "required": [
          "is_private",
          "is_nonsectarian",
          "location"
        ],
        "additionalProperties": false
      },
      "associated_artist": {
        "type": "object",
        "properties": {
          "artist_name": {
            "type": "string",
            "description": "The name of the artist associated with the institution."
          },
          "education_details": {
            "type": "object",
            "properties": {
              "degree": {
                "type": "string",
                "description": "The degree received by the artist from the institution."
              },
              "year_received": {
                "type": "integer",
                "description": "The year the degree was received."
              }
            },
            "required": [
              "degree",
              "year_received"
            ],
            "additionalProperties": false
          },
          "major_museum_solo_shows": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "show_title": {
                  "type": "string",
                  "description": "The title of the solo exhibition."
                },
                "museum_name": {
                  "type": "string",
                  "description": "The name of the museum where the solo exhibition was held."
                },
                "year": {
                  "type": "integer",
                  "description": "The year the solo exhibition took place."
                }
              },
              "required": [
                "show_title",
                "museum_name",
                "year"
              ],
              "additionalProperties": false
            },
            "description": "A list of major museum solo shows featuring the artist."
          }
        },
        "required": [
          "artist_name",
          "education_details",
          "major_museum_solo_shows"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "institution_name",
      "institution_attributes",
      "associated_artist"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
