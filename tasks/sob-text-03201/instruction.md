{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nUbuntu Titling: Ubuntu Titling or Ubuntu-Title is a rounded geometric sans-serif font.  It was created by Andy Fitzsimon for use with the Ubuntu operating system and its derivatives.  It is distributed under the GNU Lesser General Public License.  Prior to the 10.04 release, the typeface was notably used in branding for the Ubuntu operating system and its related projects.  Fitzsimon's design was created without any upper-case letters.  A later release by Christian Robertson (who later created Roboto) added capitals and was released by Robertson at the 'release candidate' stage.  This was called Ubuntu Titling.\n\nXubuntu: Xubuntu ( ) is a Canonical Ltd.–recognized, community-maintained derivative of the Ubuntu operating system.  The name \"Xubuntu\" is a portmanteau of \"Xfce\" and \"Ubuntu\", as it uses the Xfce desktop environment, instead of Ubuntu's Unity.\n\nADMOS-Lite: ADMOS-Lite (previously known as minimalubuntu) is an operating system that features LXDE and lightweight programs based on Ubuntu (operating system), but it is not an official project by Canonical Ltd.  The goal of ADMOS-Lite is to create a distribution based on Ubuntu that is reasonably fast even on limited hardware & consists of 100% free software only.  In contrast to other variants of Ubuntu, ADMOS-Lite is focused on providing a trimmed set of software packages while providing the experience expected by a modern computer user.  Furthermore, the user interface is designed to be usable even at smaller resolutions such as those on older computers and netbooks.\n\nUbuntu (typeface): Ubuntu is an OpenType-based font family, designed to be a modern, humanist-style typeface by London-based type foundry Dalton Maag, with funding by Canonical Ltd.  The font was under development for nearly nine months, with only a limited initial release through a beta program, until September 2010.  It was then that it became the new default font of the Ubuntu operating system in Ubuntu 10.10.  Its designers include Vincent Connare, creator of the Comic Sans and Trebuchet MS fonts.\n\nUnity (Ubuntu): Unity is a graphical shell for the GNOME desktop environment originally developed by Canonical Ltd. for its Ubuntu operating system.  Unity debuted in the netbook edition of Ubuntu 10.10.  It was initially designed to make more efficient use of space given the limited screen size of netbooks, including, for example, a vertical application switcher called the \"launcher\", and a space-saving horizontal multipurpose \"top menu bar\".\n\nUbuntu version history: Ubuntu releases are made semiannually by Canonical Ltd, the developers of the Ubuntu operating system, using the year and month of the release as a version number.  The first Ubuntu release, for example, was Ubuntu 4.10 and was released on 20 October 2004.  Consequently, version numbers for future versions are provisional; if the release is delayed until a different month (or even year) to that planned, the version number will change accordingly.\n\nMark Shuttleworth: Mark Richard Shuttleworth (born 18 September 1973) is a South African entrepreneur who is the founder and CEO of Canonical Ltd., the company behind the development of the Linux-based Ubuntu operating system.  In 2002, he became the first citizen of an independent African country to travel to space as a space tourist.  He currently lives on the Isle of Man and holds dual citizenship from South Africa and the United Kingdom.\n\nClaudie Haigneré: Claudie (André-Deshays) Haigneré (born 13 May 1957) is a French doctor, politician, and former astronaut with the Centre National d'Études Spatiales (1985–1999) and the European Space Agency (1999–2002).\n\nCanonical (company): Canonical Ltd. is a UK-based privately held computer software company founded and funded by South African entrepreneur Mark Shuttleworth to market commercial support and related services for Ubuntu and related projects.  Canonical employs staff in more than 30 countries and maintains offices in London, Austin, Boston, Shanghai, Beijing, Taipei and the Isle of Man.\n\nUbuntu Touch: Ubuntu Touch (also known as Ubuntu Phone) was a mobile version of the Ubuntu operating system that was developed by Canonical Ltd. and the Ubuntu community.  It was designed primarily for touchscreen mobile devices such as smartphones and tablet computers.\n\nQuestion: Who, Claudie Haigneré and Mark Shuttleworth, is the founder and CEO of Canonical Ltd., the company behind the development of the Linux-based Ubuntu operating system?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"company_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the company in question.\"\n    },\n    \"candidate_1\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The full name of the first candidate.\"\n        },\n        \"is_founder_ceo\": {\n          \"type\": \"boolean\",\n          \"description\": \"True if this candidate is the founder and CEO of the company, false otherwise.\"\n        },\n        \"nationality\": {\n          \"type\": \"string\",\n          \"description\": \"The nationality of the candidate.\"\n        },\n        \"known_roles\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"Other significant roles or occupations of the candidate mentioned in the context.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"is_founder_ceo\",\n        \"nationality\",\n        \"known_roles\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"candidate_2\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The full name of the second candidate.\"\n        },\n        \"is_founder_ceo\": {\n          \"type\": \"boolean\",\n          \"description\": \"True if this candidate is the founder and CEO of the company, false otherwise.\"\n        },\n        \"known_roles\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"Other significant roles or occupations of the candidate mentioned in the context.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"is_founder_ceo\",\n        \"known_roles\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"identified_founder_ceo_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person identified as the founder and CEO of the company.\"\n    }\n  },\n  \"required\": [\n    \"company_name\",\n    \"candidate_1\",\n    \"candidate_2\",\n    \"identified_founder_ceo_name\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "company_name": {
        "type": "string",
        "description": "The name of the company in question."
      },
      "candidate_1": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The full name of the first candidate."
          },
          "is_founder_ceo": {
            "type": "boolean",
            "description": "True if this candidate is the founder and CEO of the company, false otherwise."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the candidate."
          },
          "known_roles": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "Other significant roles or occupations of the candidate mentioned in the context."
          }
        },
        "required": [
          "name",
          "is_founder_ceo",
          "nationality",
          "known_roles"
        ],
        "additionalProperties": false
      },
      "candidate_2": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The full name of the second candidate."
          },
          "is_founder_ceo": {
            "type": "boolean",
            "description": "True if this candidate is the founder and CEO of the company, false otherwise."
          },
          "known_roles": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "Other significant roles or occupations of the candidate mentioned in the context."
          }
        },
        "required": [
          "name",
          "is_founder_ceo",
          "known_roles"
        ],
        "additionalProperties": false
      },
      "identified_founder_ceo_name": {
        "type": "string",
        "description": "The name of the person identified as the founder and CEO of the company."
      }
    },
    "required": [
      "company_name",
      "candidate_1",
      "candidate_2",
      "identified_founder_ceo_name"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
