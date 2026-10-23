{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSignature in the Cell: Signature in the Cell: DNA and the Evidence for Intelligent Design is a 2009 book about intelligent design by philosopher and intelligent design advocate Stephen C. Meyer.  The book was well received by some within the conservative, intelligent design and evangelical communities, but several other reviewers were critical and wrote that Meyer's claims are incorrect.\n\nJonathan Wells (intelligent design advocate): John Corrigan \"Jonathan\" Wells (born 1942) is an American molecular biologist, author and advocate of the pseudoscientific argument of intelligent design.  Wells joined the Unification Church in 1974, and subsequently wrote that the teachings of church founder Sun Myung Moon, his own studies at the Unification Theological Seminary and his prayers convinced him to devote his life to \"destroying Darwinism.\"  The term \"Darwinism\" is often used by intelligent design proponents to refer to the scientific consensus on evolution.  He gained a PhD in religious studies at Yale University in 1986, then became Director of the Unification Church’s inter-religious outreach organization in New York City.  In 1989, he studied at the University of California, Berkeley, where he earned a PhD in molecular and cellular biology in 1994.  He became a member of several scientific associations and has published in academic journals.\n\nCreationism's Trojan Horse: Creationism's Trojan Horse: The Wedge of Intelligent Design is a 2004 book by Barbara Forrest and Paul R. Gross on the origins of intelligent design, specifically the Discovery Institute's Center for the Renewal of Science and Culture and its wedge strategy.  The authors are highly critical of what they refer to as intelligent design creationism, and document the intelligent design movement's fundamentalist Christian origins and funding.\n\nUncommon Dissent: Uncommon Dissent: Intellectuals Who Find Darwinism Unconvincing is a 2004 anthology edited by William A. Dembski in which fifteen intellectuals, eight of whom are leading intelligent design proponents associated with the Discovery Institute's Center for Science and Culture (CSC) and the International Society for Complexity, Information and Design (ISCID), criticise \"Darwinism\" and make a case for intelligent design.  It is published by the publishing wing of the paleoconservative Intercollegiate Studies Institute.  The foreword is by John Wilson, editor of the evangelical Christian magazine \"Christianity Today\".  The title is a pun on the principle of biology known as common descent.  The Discovery Institute is the engine behind the intelligent design movement.\n\nDiscovery Institute intelligent design campaigns: The Discovery Institute has conducted a series of related public relations campaigns which seek to promote intelligent design while attempting to discredit evolutionary biology, which the Institute terms \"Darwinism.\"  The Discovery Institute is the driving force behind the pseudoscientific intelligent design movement and the Institute directs the campaigns through its Center for Science and Culture division with guidance from its public relations firm, Creative Response Concepts.\n\nStephen C. Meyer: Stephen C. Meyer (born 1958) is an advocate of the pseudoscientific principle of intelligent design.  He helped found the Center for Science and Culture (CSC) of the Discovery Institute (DI), which is the main organization behind the intelligent design movement.  Before joining the DI, Meyer was a professor at Whitworth College.  Meyer is currently a Senior Fellow of the DI and Director of its Center for Science and Culture (CSC).\n\nUnlocking the Mystery of Life: Unlocking the Mystery of Life is a 2003 intelligent design documentary film promoted and produced by Illustra Media (linked to Discovery Media, successor to the Moody Bible Institute's \"Moody Institute of Science\") and Focus on the Family.  The film's script was written by Stephen C. Meyer, who is director of the Center for Science and Culture at the Discovery Institute, and it includes fellows of the institute such as Jonathan Wells and Michael Behe arguing for intelligent design and against evolution.\n\nTruth in Science: Truth in Science is a United Kingdom-based creationist organization which promotes the Discovery Institute's \"Teach the Controversy\" campaign, which it uses to try to get pseudoscientific intelligent design creationism taught alongside evolution in school science lessons.  The organization claims that there is scientific controversy about the validity of Darwinian evolution, a view rejected by the United Kingdom's Royal Society and over 50 Academies of Science around the world.  The group is affiliated with the Discovery Institute, the hub of the intelligent design movement, following its strategy and circulating the Institute's promotional materials.\n\nMichael Behe: Michael J. Behe ( ; born January 18, 1952) is an American biochemist, author, and intelligent design (ID) advocate.  He serves as professor of biochemistry at Lehigh University in Pennsylvania and as a senior fellow of the Discovery Institute's Center for Science and Culture.  Behe is best known for his argument for his stance on irreducible complexity (IC), which argues that some biochemical structures are too complex to be explained by known evolutionary mechanisms and are therefore probably the result of intelligent design.  Behe has testified in several court cases related to intelligent design, including the court case \"Kitzmiller v. Dover Area School District\" that resulted in a ruling that intelligent design was not science and was religious in nature.\n\nGuillermo Gonzalez (astronomer): Guillermo Gonzalez (born 1963 in Havana, Cuba) is an astrophysicist, proponent of intelligent design, and an assistant professor at Ball State University, a public research university, in Muncie, Indiana.  He is a senior fellow of the Discovery Institute's Center for Science and Culture, considered the hub of the intelligent design movement, and a fellow with the International Society for Complexity, Information and Design, which also promotes intelligent design.\n\nQuestion:  Unlocking the Mystery of Life, a 2003 intelligent design documentary film promoted and produced by Illustra Media, is written by Stephen C. Meyer, who is director of the Center for Science and Culture at the Discovery Institute, which includes what fellow, who is an American molecular biologist, author and advocate of the pseudoscientific argument of intelligent design?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_information\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the documentary film.\"\n        },\n        \"year\": {\n          \"type\": \"integer\",\n          \"description\": \"The release year of the film.\"\n        },\n        \"writer\": {\n          \"type\": \"object\",\n          \"properties\": {\n            \"name\": {\n              \"type\": \"string\",\n              \"description\": \"The name of the film's scriptwriter.\"\n            },\n            \"role\": {\n              \"type\": \"string\",\n              \"description\": \"The role of the writer within the associated organization.\"\n            }\n          },\n          \"required\": [\n            \"name\",\n            \"role\"\n          ],\n          \"additionalProperties\": false\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"year\",\n        \"writer\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"associated_organization\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the main organization behind the intelligent design movement.\"\n        },\n        \"division\": {\n          \"type\": \"string\",\n          \"description\": \"The specific division of the organization.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"division\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"featured_fellow\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the fellow featured in the film.\"\n        },\n        \"profession\": {\n          \"type\": \"string\",\n          \"description\": \"The primary profession of the fellow.\"\n        },\n        \"advocacy\": {\n          \"type\": \"string\",\n          \"description\": \"The pseudoscientific argument the fellow advocates for.\"\n        },\n        \"organization_role\": {\n          \"type\": \"string\",\n          \"description\": \"The role of the fellow within the associated organization.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"profession\",\n        \"advocacy\",\n        \"organization_role\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"film_information\",\n    \"associated_organization\",\n    \"featured_fellow\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_information": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the documentary film."
          },
          "year": {
            "type": "integer",
            "description": "The release year of the film."
          },
          "writer": {
            "type": "object",
            "properties": {
              "name": {
                "type": "string",
                "description": "The name of the film's scriptwriter."
              },
              "role": {
                "type": "string",
                "description": "The role of the writer within the associated organization."
              }
            },
            "required": [
              "name",
              "role"
            ],
            "additionalProperties": false
          }
        },
        "required": [
          "title",
          "year",
          "writer"
        ],
        "additionalProperties": false
      },
      "associated_organization": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the main organization behind the intelligent design movement."
          },
          "division": {
            "type": "string",
            "description": "The specific division of the organization."
          }
        },
        "required": [
          "name",
          "division"
        ],
        "additionalProperties": false
      },
      "featured_fellow": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the fellow featured in the film."
          },
          "profession": {
            "type": "string",
            "description": "The primary profession of the fellow."
          },
          "advocacy": {
            "type": "string",
            "description": "The pseudoscientific argument the fellow advocates for."
          },
          "organization_role": {
            "type": "string",
            "description": "The role of the fellow within the associated organization."
          }
        },
        "required": [
          "name",
          "profession",
          "advocacy",
          "organization_role"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "film_information",
      "associated_organization",
      "featured_fellow"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
