{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nJoe Miller (Alaska politician): Joseph Wayne Miller (born May 10, 1967) is an American attorney and politician.\n\nFundamental error: Fundamental error is a legal term provided by United State Courts to describe an error which occurs whenever a judgement violates a federal fundamental right.  In United States constitutional law, fundamental rights have special significance under the U.S. Constitution.  Those rights enumerated in the U.S. Constitution are recognized as \"fundamental\" by the U.S. Supreme Court.  State courts within the United States may define fundamental error rules independently of the federal courts.  State fundamental error rules may include errors which violate rights in additional to those rights guaranteed by the U.S. Constitution, but these rules may not infringe upon federal fundamental rights.  Any law restricting such a right must both serve a compelling state purpose and be narrowly tailored to that compelling purpose.\n\nProcedural default: Procedural default is a concept in American federal courts law that requires a state prisoner seeking a writ of Habeas Corpus in federal court to have \"present[ed] his federal law argument to the state courts in compliance with state procedural rules.  Failure to do so will bar any attempt to present that argument to the federal courts on collateral review.  A petitioner may evade this bar only by showing 'cause' and 'prejudice' for the default -- that is, by stating a good reason for not presenting the federal claim to the state courts, and by showing that the federal error worked to the petitioner's 'actual and substantial disadvantage.'\"\n\nCharles Rollin Keyes: Charles Rollin Keyes (1864–1942) was a U.S. geologist and in 1918 was a U.S. Senate candidate in Iowa.  Born in Des Moines, Iowa, he graduated from the State University of Iowa in 1887.  He worked for the United States Geological Survey.  He earned a Ph.D. from Johns Hopkins University in 1892.  He served as Assistant State Geologist of Iowa, Director of the Bureau of Geology and Mines of Missouri and was president of the New Mexico Institute of Mining and Technology at Socorro.  Keyes was also an avid ornithologist, publishing the first detailed listing of birds in Iowa in 1889.  In 1918 he was the Democratic candidate for the U.S. Senate from Iowa, losing to William S. Kenyon.\n\nMontauk Point land claim: The Montauk Point land claim was a series of three lawsuits brought by Chief Wyandank Pharaoh, nephew of the Stephen Talkhouse who died in the same year (1879) that the tribe lost the last remaining vestige of their territory in the New York state courts, claiming Montauk Point on behalf of the Montaukett Indians, against the Long Island Rail Road (LIRR) and its predecessors in title.\n\nFederal common law: Federal common law is a term of United States law used to describe common law that is developed by the federal courts, instead of by the courts of the various states.  The United States is the only country to combine the creation of common law doctrines with a complete federalism, wherein the national supreme court has virtually no power to review state court decisions to determine whether the state courts have followed state laws.  The High Court of Australia is sometimes said to have federal common law, but because all state and territorial courts are directly appealable to the High Court, this is indistinguishable from a general common law.  In contrast, the United States Supreme Court has effectively barred the creation of federal common law in areas traditionally under the authority of state courts.  Nevertheless, there are several areas where federal common law continues to govern.\n\nAlexander Snitker: Alexander Snitker (born August 6, 1975) was the Libertarian Party candidate in the 2010 Florida U.S. Senate election for the seat being vacated by Republican George LeMieux.  He was the first Libertarian U.S. Senate candidate to appear on the ballot in Florida's history.\n\nMiller v. Campbell: Miller v. Campbell is a series of three lawsuits filed by U.S. Senate candidate, Joe Miller, in both federal and Alaska state courts, that dispute vote-counting methods and other procedures conducted by the Alaska Division of Elections relating to the November 2, 2010 general election.\n\nRepublic of Austria v. Altmann: Republic of Austria v. Altmann, 541 U.S. 677 (2004), was a case in which the Supreme Court of the United States held that the Foreign Sovereign Immunities Act, or FSIA, applies retroactively.  It is one of the most recent cases that deals with the \"anti-retroactivity doctrine\", which is a doctrine that holds that courts should not construe a statute to apply retroactively (to apply to situations that arose before it was enacted) unless there is a clear statutory intent that it should do so.  This means that, regarding lawsuits filed after its enactment, the FSIA standards of sovereign immunity and its exceptions apply even to conduct that took place before 1976.\n\nDuPre Excelsior Mill: Located at 695 North Avenue in Atlanta, the Dupre Excelsior Mill (the actual name as of 1911 was \"Du Pree Manufacturing Company Excelsior Factory\"), may have been built as early as 1890 by DuPre (also spelled Du Pree) Manufacturing Company.  However, the mill fails to appear on Atlanta city maps in 1892 and 1899, which both show the property as vacant.  The first possible reference to the mill exist in the report of the death of Hubert Neal on July 17, 1899.  According to the report, his accident occurred at the Atlanta Excelsior Works (which may or may not be the same facility since at the time there were three excelsior factories in Atlanta).  The earliest concrete confirmation of the mill seems to be three lawsuits filed against Dupre in 1907 for accidents that occurred at the facility.  The mill does appear on the Sanborn-Perris Fire Insurance map of 1911 (section 250).  At that time, the only road connecting it was Angier Street.  It was noted to have been heated by steam power, no lighting, and a private water supply from a well 10 feet in diameter and 40 feet deep.  A watchman made hourly rounds to seven stations.\n\nQuestion: Miller v. Campbell is a series of three lawsuits filed by U.S. Senate candidate, Joe Miller, in both federal and in which U.S. state courts?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"lawsuit_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the series of lawsuits.\"\n    },\n    \"number_of_lawsuits\": {\n      \"type\": \"integer\",\n      \"description\": \"The total number of lawsuits in the series.\"\n    },\n    \"plaintiff\": {\n      \"type\": \"string\",\n      \"description\": \"The plaintiff in the lawsuits.\"\n    },\n    \"courts_involved\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"federal_courts\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if federal courts were involved.\"\n        },\n        \"state_courts_involved\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if state courts were involved.\"\n        },\n        \"state_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the U.S. state where state courts were involved.\"\n        }\n      },\n      \"required\": [\n        \"federal_courts\",\n        \"state_courts_involved\",\n        \"state_name\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"dispute_details\": {\n      \"type\": \"string\",\n      \"description\": \"A description of what the lawsuits dispute.\"\n    },\n    \"election_date\": {\n      \"type\": \"string\",\n      \"description\": \"The date of the general election related to the dispute.\"\n    }\n  },\n  \"required\": [\n    \"lawsuit_name\",\n    \"number_of_lawsuits\",\n    \"plaintiff\",\n    \"courts_involved\",\n    \"dispute_details\",\n    \"election_date\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "lawsuit_name": {
        "type": "string",
        "description": "The name of the series of lawsuits."
      },
      "number_of_lawsuits": {
        "type": "integer",
        "description": "The total number of lawsuits in the series."
      },
      "plaintiff": {
        "type": "string",
        "description": "The plaintiff in the lawsuits."
      },
      "courts_involved": {
        "type": "object",
        "properties": {
          "federal_courts": {
            "type": "boolean",
            "description": "Indicates if federal courts were involved."
          },
          "state_courts_involved": {
            "type": "boolean",
            "description": "Indicates if state courts were involved."
          },
          "state_name": {
            "type": "string",
            "description": "The name of the U.S. state where state courts were involved."
          }
        },
        "required": [
          "federal_courts",
          "state_courts_involved",
          "state_name"
        ],
        "additionalProperties": false
      },
      "dispute_details": {
        "type": "string",
        "description": "A description of what the lawsuits dispute."
      },
      "election_date": {
        "type": "string",
        "description": "The date of the general election related to the dispute."
      }
    },
    "required": [
      "lawsuit_name",
      "number_of_lawsuits",
      "plaintiff",
      "courts_involved",
      "dispute_details",
      "election_date"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
