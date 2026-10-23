{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nPsychological contract: A psychological contract, a concept developed in contemporary research by organizational scholar Denise Rousseau, represents the mutual beliefs, perceptions, and informal obligations between an employer and an employee.  It sets the dynamics for the relationship and defines the detailed practicality of the work to be done.  It is distinguishable from the formal written contract of employment which, for the most part, only identifies mutual duties and responsibilities in a generalized form.\n\nStrawberry Saroyan: Strawberry Saroyan (born 1970) is a journalist and author.  The daughter of Aram Saroyan and granddaughter of playwright William Saroyan and actress Carol Matthau, she spent her childhood in Bolinas, California.  She has a sister named Cream.  She writes for the New York Times Style section and is the author of \"\".\n\nStrawberry Lagoon: Strawberry Lagoon is an inlet within Richardson Bay, Marin County, California, United States.  This location, particularly on Strawberry Spit, is a winter haul-out area for the Harbor seal.  Pressures of urban development at Strawberry Point along with increases in small boat traffic have diminished the use of this lagoon for seal haul out, noted as early as 1990.\n\nMasturbation: Masturbation is the sexual stimulation of one's own genitals for sexual arousal or other sexual pleasure, usually to the point of orgasm.  The stimulation may involve hands, fingers, everyday objects, sex toys such as vibrators, or combinations of these.  Mutual masturbation (mutual manual stimulation of the genitals between partners) can be a substitute for sexual penetration.  Studies have found that masturbation is frequent in humans of both sexes and all ages, although there is variation.  Various medical and psychological benefits have been attributed to a healthy attitude toward sexual activity in general and to masturbation in particular.  No causal relationship is known between masturbation and any form of mental or physical disorder.\n\nMutual organization: A mutual, mutual organization, or mutual society is an organization (which is often, but not always, a company or business) based on the principle of mutuality.  Unlike a true cooperative, members usually do not contribute to the capital of the company by direct investment, but derive their right to profits and votes through their customer relationship.  A mutual organization or society is often simply referred to as \"a mutual\".\n\nConfianza: Confianza (English: trust) is a Latin American form of mutual reciprocity.  In the context of interpersonal relationships, its presence indicates that both parties recognize a mutual duty to honor their relationship by extending specially favorable treatment.\n\nPuppy love in China: Zaolian (Chinese:早恋; literal meaning \"early love\") in mainland China means \"to have a romantic relationship \"too early\"\" and refers to romantic relationship of adolescents before they go to university.  According to surveys of the recent 20 years , there are actually few people in China who never experience romantic relationship during Junior High and Senior High.  Most people may have unrequited love, and a mutual romantic relationship takes place only when the two adolescents like each other.  However, in China, most parents, who are conservative, and educators supporting examination-based education claim that \"zaolian\" will bring many problems such as it will affect students' study ability and examination marks, or that \"zaolian\" relationship will almost always split in the end.\n\nState Savings Bank (Logan, Iowa): State Savings Bank, also known as Harrison Mutual Insurance Association, is a historic building located in Logan, Iowa, United States.  Founded in 1888, the bank built this building in 1902.  It is a two-story brick structure with terra cotta ornamentation.  Its wrap-around design is made possible for this mid-block building by its alley location.  State Savings Bank was one of four banks that operated in the town over its history.  It failed in 1923.  After the building sat empty for five years Harrison Mutual Insurance Association purchased the building.  It was listed on the National Register of Historic Places in 1985.\n\nDirect coupling analysis: Direct coupling analysis or DCA is an umbrella term comprising several methods for analyzing sequence data in computational biology.  The common idea of these methods is to use statistical modeling to quantify the strength of the direct relationship between two positions of a biological sequence, excluding effects from other positions.  This contrasts usual measures of correlation, which can be large even if there is no direct relationship between the positions (hence the name \"direct\" coupling analysis).  Such a direct relationship can for example be the evolutionary pressure for two positions to maintain mutual compatibility in the biomolecular structure of the sequence, leading to molecular coevolution between the two positions.\n\nHrayr Shahinian: Hrayr Shahinian, M.D., F.A.C.S. is an American skull base surgeon and founder of the Skull Base Institute (SBI).  He was Board Certified by the American Board of Surgery and was licensed to practice in California since 1996.  On August 11, 2016 the Medical Board of California, Department of Consumer Affairs, State of California adopted the decision to revoke the Physician and Surgeon’s Certificate issued to Hrayr Karnig Shahinian, M.D.  The order came into effect on September 9, 2016.\n\nQuestion: Strawberry Saroyan and Hrayr Shahinian, have a relationship with which mutual location?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_1_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the first person mentioned in the question.\"\n    },\n    \"person_2_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the second person mentioned in the question.\"\n    },\n    \"mutual_location_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the location that both individuals have a relationship with.\"\n    },\n    \"location_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of the mutual location (e.g., state, city, country).\"\n    },\n    \"relationship_details\": {\n      \"type\": \"array\",\n      \"description\": \"Details of each person's relationship with the mutual location.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"person_name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the person.\"\n          },\n          \"relationship_description\": {\n            \"type\": \"string\",\n            \"description\": \"A description of how the person is related to the location.\"\n          }\n        },\n        \"required\": [\n          \"person_name\",\n          \"relationship_description\"\n        ],\n        \"additionalProperties\": false\n      }\n    }\n  },\n  \"required\": [\n    \"person_1_name\",\n    \"person_2_name\",\n    \"mutual_location_name\",\n    \"location_type\",\n    \"relationship_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_1_name": {
        "type": "string",
        "description": "The name of the first person mentioned in the question."
      },
      "person_2_name": {
        "type": "string",
        "description": "The name of the second person mentioned in the question."
      },
      "mutual_location_name": {
        "type": "string",
        "description": "The name of the location that both individuals have a relationship with."
      },
      "location_type": {
        "type": "string",
        "description": "The type of the mutual location (e.g., state, city, country)."
      },
      "relationship_details": {
        "type": "array",
        "description": "Details of each person's relationship with the mutual location.",
        "items": {
          "type": "object",
          "properties": {
            "person_name": {
              "type": "string",
              "description": "The name of the person."
            },
            "relationship_description": {
              "type": "string",
              "description": "A description of how the person is related to the location."
            }
          },
          "required": [
            "person_name",
            "relationship_description"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": [
      "person_1_name",
      "person_2_name",
      "mutual_location_name",
      "location_type",
      "relationship_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
