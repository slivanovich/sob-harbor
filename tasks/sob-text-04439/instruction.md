{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThe Perfect Husband: The Laci Peterson Story: The Perfect Husband: The Laci Peterson Story is a 2004 TV movie based on the life of Laci Peterson that stars Dean Cain, Sarah Brown, Tracy Middendorf and Tom O'Brien.\n\nScott Peterson: Scott Lee Peterson (born October 24, 1972) is an American former fertilizer salesman awaiting execution on death row in San Quentin State Prison, convicted of the first degree murder of his pregnant wife, Laci Peterson, and the second degree murder of their unborn son, Connor, in Modesto, California in 2002.  He was sentenced to death by lethal injection the following year.  His case is currently on appeal to the Supreme Court of California.\n\nMandate (criminal law): A criminal court may impose a \"mandate\" as part of a legal process on a person accused of a crime consisting of an obligation to engage in certain conditions or activities in exchange for suspension or reduction in penalty; such as, conditions of probation, conditional discharges, or other conditional sentences.  For example, a defendant convicted of driving while intoxicated or drug possession may be mandated to engage in alcoholism or substance abuse rehabilitation.  The term is paradoxical because acceptance of the \"mandate\" is a voluntary act by the defendant, who also has the option of serving what would most generally (though the relative weight is a matter determined by the individual's perspective and readiness to change) be viewed as a harsher alternative, such as incarceration.  In this sense, the mandate is not truly \"mandatory\", but is instead a type of legal fiction wherein the court assumes an illusion of power which, in actuality, is constrained by the defendant's free will.\n\nDefendant: A defendant is a person accused of a crime in criminal prosecution or with a person against whom some type of civil relief is being sought in a civil case.\n\nDietrich v The Queen: Dietrich v The Queen, is an important legal case, stemming from an incident that took place on 17 December 1986, that was decided in the High Court of Australia on 13 November 1992.  It concerned the nature of the right to a fair trial, and under what circumstances indigent defendants (defendants who cannot afford legal representation) should be provided with legal aid by the state.  The case determined that although there is no absolute right to have publicly funded counsel, in most circumstances a judge should grant any request for an adjournment or stay when an accused is unrepresented.  It is an important case in Australian criminal law, and also in Australian constitutional law, since it is one of many cases in which some members of the High Court have found implied human rights in the Australian Constitution.\n\nRick Distaso: Joseph Richard (Rick) Distaso was the Stanislaus County, California senior deputy district attorney who served as the lead prosecutor in the case against Scott Peterson, charged with and later convicted of murdering his wife Laci Peterson and their unborn child Conner Peterson in 2002.  Laci was eight months pregnant with Conner at the time of the murder.\n\nLegal case: A legal case is a dispute between opposing parties resolved by a court, or by some equivalent legal process.  A legal case may be either civil or criminal.  In each legal case there is an accuser and one or more defendants.\n\nMurder of Laci Peterson: Laci Denise Peterson (née Rocha; May 4, 1975 December 24, 2002) was an American woman who was the subject of a highly publicized murder case after she disappeared while eight months pregnant with her first child.  She was reportedly last seen alive on December 24, 2002.  Her husband, Scott Peterson, was later convicted of murder in the first degree for her death, and in the second degree for the death of their prenatal son, Conner.  Scott is on death row at San Quentin State Prison.\n\nEvans v. Michigan: Evans v. Michigan, 568 U.S. ___ (2013) , was a United States Supreme Court case in which the Court held that if a person accused of a crime receives a directed acquittal, the Double Jeopardy Clause bars a second trial of that person for the same crime, even if the person was acquitted in error.\n\nReview of court decision in Indonesia: Review of court decision or abbreviated PK (Indonesian: \"Peninjauan Kembali\" ) is a legal action that can be taken by the convict (the person subject to the penalty) in a legal case against a court decision final and binding on the judicial system in Indonesia.  The court ruling has called legally enforceable decision of the District Court is not filed an appeal, the decision of the High Court was not filed an appeal (legal action in the Supreme Court), or the decision of the Supreme Court.  PK can not be taken to court decisions that have permanent legal force if the decision was a decision that states the defendant (person charged in the proceedings) are free from all charges.\n\nQuestion: What is the legal case status of the person accused for having murdered Laci Denise Peterson?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"defendant_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person accused in the legal case.\"\n    },\n    \"case_status\": {\n      \"type\": \"string\",\n      \"description\": \"The current legal status of the defendant's case.\"\n    },\n    \"appealing_court\": {\n      \"type\": \"string\",\n      \"description\": \"The court where the case is currently on appeal.\"\n    },\n    \"conviction_details\": {\n      \"type\": \"object\",\n      \"description\": \"Details about the defendant's conviction.\",\n      \"properties\": {\n        \"crimes_convicted_of\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"A list of crimes the defendant was convicted of.\"\n        },\n        \"victims\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"object\",\n            \"properties\": {\n              \"name\": {\n                \"type\": \"string\"\n              },\n              \"relationship_to_defendant\": {\n                \"type\": \"string\"\n              }\n            },\n            \"required\": [\n              \"name\"\n            ],\n            \"additionalProperties\": false\n          },\n          \"description\": \"A list of victims in the case.\"\n        },\n        \"current_sentence\": {\n          \"type\": \"string\",\n          \"description\": \"The current sentence imposed on the defendant.\"\n        },\n        \"prison_location\": {\n          \"type\": \"string\",\n          \"description\": \"The prison where the defendant is incarcerated.\"\n        }\n      },\n      \"required\": [\n        \"crimes_convicted_of\",\n        \"victims\",\n        \"current_sentence\",\n        \"prison_location\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"defendant_name\",\n    \"case_status\",\n    \"appealing_court\",\n    \"conviction_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "defendant_name": {
        "type": "string",
        "description": "The name of the person accused in the legal case."
      },
      "case_status": {
        "type": "string",
        "description": "The current legal status of the defendant's case."
      },
      "appealing_court": {
        "type": "string",
        "description": "The court where the case is currently on appeal."
      },
      "conviction_details": {
        "type": "object",
        "description": "Details about the defendant's conviction.",
        "properties": {
          "crimes_convicted_of": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "A list of crimes the defendant was convicted of."
          },
          "victims": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "name": {
                  "type": "string"
                },
                "relationship_to_defendant": {
                  "type": "string"
                }
              },
              "required": [
                "name"
              ],
              "additionalProperties": false
            },
            "description": "A list of victims in the case."
          },
          "current_sentence": {
            "type": "string",
            "description": "The current sentence imposed on the defendant."
          },
          "prison_location": {
            "type": "string",
            "description": "The prison where the defendant is incarcerated."
          }
        },
        "required": [
          "crimes_convicted_of",
          "victims",
          "current_sentence",
          "prison_location"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "defendant_name",
      "case_status",
      "appealing_court",
      "conviction_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
