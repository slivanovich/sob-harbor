{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThe Mark Levin Show: The Mark Levin Show is a conservative talk radio show hosted by Mark Levin.  The program is broadcast nationwide on Westwood One and reaches an estimated seven million weekly listeners, according to an estimate from \"Talkers Magazine\".  The \"Talkers\" estimate puts Levin's listenership in a tie with \"The Glenn Beck Radio Program\" for fourth most-listened-to talk radio show in the United States and, counting all radio formats, tied for ninth most-listened-to radio program in the United States.\n\nMark Levin: Mark Reed Levin ( ; born September 21, 1957) is an American lawyer, author, and radio personality.  He is the host of syndicated radio show \"The Mark Levin Show\".  Levin worked in the administration of President Ronald Reagan and was a chief of staff for Attorney General Edwin Meese.  He is president of the Landmark Legal Foundation, has authored seven books, and contributes commentary to various media outlets such as \"National Review Online\".  On September 1, 2015, Levin was named Editor-in-Chief of Conservative Review.\n\nList of Attorneys General of West Virginia: The Attorney General of West Virginia is the chief legal advisor to the West Virginia state government and is the state's chief law enforcement officer.  The office was created by Article VII, Section 1 of the first Constitution of West Virginia in 1863.  Under the current state constitution (1872), the attorney general is an executive department-level state constitutional officer, along with the governor, secretary of state, auditor, treasurer, and commissioner of agriculture.  The attorney general is the \"ex officio\" reporter of the Supreme Court of Appeals of West Virginia.  The constitution further specifies that the attorney general shall reside in the seat of state government, Charleston, during their term of office.  In Charleston, they are to maintain public records, books, and papers pertaining to their office, and perform all duties prescribed by state law.  As of 2012, the attorney general receives a salary of $95,000 per year.\n\nEarth 2 (TV series): Earth 2 is an American science fiction television series which aired on NBC from November 6, 1994 to June 4, 1995.  The show was canceled after one season of 22 episodes.  It follows the journey and settlement of a small expeditionary group called the Eden Project, with the intent to journey to an Earth-like planet called G889 in an attempt to find a cure to an illness called \"the syndrome\".  The series was created by Michael Duggan, Carol Flint, Mark Levin, and Billy Ray, produced by Amblin Entertainment and Universal Television, and filmed primarily in northern New Mexico around the Santa Fe area.  The series' music was composed by David Bergeaud, and the executive producers were Michael Duggan, Mark Levin, and Carol Flint.\n\nAttorney General of New South Wales: The Attorney General of New South Wales, in formal contexts also Attorney-General or Attorney General for New South Wales and usually known simply as the Attorney General, is a minister in the Government of New South Wales who has responsibility for the administration of justice in New South Wales, Australia.  In addition, the Attorney General is one of the Law Officers of the Crown.  Along with the subordinate Solicitor General, Crown Advocate, and Crown Solicitor, the Attorney General serves as the chief legal and constitutional adviser of the Crown and Government of New South Wales.\n\nUnited States Associate Attorney General: The Associate Attorney General of the United States is the third-ranking official in the U.S. Department of Justice.  The Associate Attorney General advises and assists the Attorney General and the Deputy Attorney General in policies relating to civil justice, federal and local law enforcement, and public safety matters.  The Associate Attorney General is appointed by the President and confirmed by the Senate.  The incumbent Associate Attorney General is Rachel Brand.\n\nAttorney General of Myanmar: The Attorney General of Myanmar (Burmese: ပြည်ထောင်စုရှေ့နေချုပ် ) is the Government of Myanmar's chief legal advisor, and also appears on behalf of the Burmese government in civil and criminal cases.  The Office of the Attorney General was established in 1948 under the 1947 Constitution of Myanmar and 1948 Attorney General of the Union Act.  From 1974 through 1988, the post was called the Chairman of the Council of People's Attorney.  The present law, the 2010 Attorney General of the Union Law was promulgated on 28 October 2010.  The Attorney General is appointed by the President of Myanmar.  The Attorney General leads the Office of the Attorney General in Naypyidaw.\n\nEdwin Meese: Edwin Meese III (born December 2, 1931) is an American attorney, law professor, author and member of the Republican Party who served in official capacities within the Ronald Reagan Gubernatorial Administration (1967–1974), the Reagan Presidential Transition Team (1980) and the Reagan White House (1981–1985), eventually rising to hold the position of the 75th Attorney General of the United States (1985–1988).\n\nDonald Regan: Donald Thomas \"Don\" Regan (December 21, 1918 – June 10, 2003) was the 66th United States Secretary of the Treasury from 1981 to 1985 and the White House Chief of Staff from 1985 to 1987 in the Ronald Reagan Administration.  He advocated \"Reaganomics\" and tax cuts to create jobs and stimulate production.  Before serving in the Reagan administration, Regan served as chairman and CEO of Merrill Lynch from 1971 to 1980.  He had worked at Merrill Lynch since 1946, and before this he had studied at Harvard University and served in the United States Marine Corps, achieving the rank of lieutenant colonel.\n\nNorth Carolina Attorney General: The Attorney General of North Carolina is the elected head of the state's Department of Justice.  The North Carolina constitution, in Article III Section 7, provides for the election of the Attorney General.  http://www.ncga.state.nc.us/Legislation/constitution/article3.html By statute, Attorney General's duties include providing legal representation and advice to all state agencies.  The parameters of that duty have been the subject of some debate, when, for example, United States Attorney General Eric Holder suggested that state Attorneys General should not squander their state's resources in defense of laws they know to be unconstitutional.  By statute, in defense of the public interest, the Attorney General may initiate legal action or intervene in proceedings before any courts, regulatory officers, agencies or bodies — either state or federal — on behalf of the state's agencies and citizens.  http://www.ncga.state.nc.us/EnactedLegislation/Statutes/PDF/ByChapter/Chapter_114.pdf The Attorney General also renders legal opinions, either formally or informally, upon all questions of law submitted by the General Assembly, the Governor or any other state officer.  Attorney General opinions may be viewed online.  http://www.ncdoj.gov/About-DOJ/Legal-Services/Legal-Opinions.aspx\n\nQuestion: Mark Levin was a chief of staff for which Reagan Administration Attorney General?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"chief_of_staff_person\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the person who served as chief of staff.\"\n        },\n        \"role\": {\n          \"type\": \"string\",\n          \"description\": \"The specific role held by the person.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"role\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"attorney_general_person\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the Attorney General.\"\n        },\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The official title of the Attorney General.\"\n        },\n        \"term_start_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The start year of the Attorney General's term.\"\n        },\n        \"term_end_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The end year of the Attorney General's term.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"title\",\n        \"term_start_year\",\n        \"term_end_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"administration\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the presidential administration during which the roles were held.\"\n    }\n  },\n  \"required\": [\n    \"chief_of_staff_person\",\n    \"attorney_general_person\",\n    \"administration\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "chief_of_staff_person": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the person who served as chief of staff."
          },
          "role": {
            "type": "string",
            "description": "The specific role held by the person."
          }
        },
        "required": [
          "name",
          "role"
        ],
        "additionalProperties": false
      },
      "attorney_general_person": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the Attorney General."
          },
          "title": {
            "type": "string",
            "description": "The official title of the Attorney General."
          },
          "term_start_year": {
            "type": "integer",
            "description": "The start year of the Attorney General's term."
          },
          "term_end_year": {
            "type": "integer",
            "description": "The end year of the Attorney General's term."
          }
        },
        "required": [
          "name",
          "title",
          "term_start_year",
          "term_end_year"
        ],
        "additionalProperties": false
      },
      "administration": {
        "type": "string",
        "description": "The name of the presidential administration during which the roles were held."
      }
    },
    "required": [
      "chief_of_staff_person",
      "attorney_general_person",
      "administration"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
