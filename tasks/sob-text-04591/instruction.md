{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nRobert Ray (prosecutor): Robert William Ray (born April 4, 1960) is an American lawyer practicing in the New York office of the Dallas-based law firm of Thompson & Knight, LLP.  As the successor to Ken Starr as the head of the Office of the Independent Counsel (1999 to 2002) he investigated and issued the final reports on the Whitewater scandal, the White House travel office controversy, and the White House FBI files controversy.  Before that he was Deputy Independent Counsel investigating former Secretary of Agriculture Mike Espy and before that Assistant United States Attorney for the Southern District of New York.\n\nGregory B. Craig: Gregory Bestor \"Greg\" Craig (born March 4, 1945) is an American lawyer and former White House Counsel under President Barack Obama from 2009 to 2010.  A former attorney at the Washington, D.C. law firm of Williams & Connolly, Craig has represented numerous high-profile clients.  Prior to becoming White House Counsel, Craig served as assistant to the President and special counsel in the White House of President Bill Clinton, where he directed the team defending Clinton against impeachment.  Craig also served as a senior advisor to Senator Edward Kennedy and Secretary of State Madeleine Albright.\n\nJane C. Sherburne: Jane C. Sherburne is a prominent American lawyer, currently serving as Senior Executive Vice President and General Counsel to The Bank of New York Mellon and as a member of the Council of the Administrative Conference of the United States.  Sherburne is known primarily for her experience in crisis management, her work in civil rights, and her counseling to corporate boards and major financial institutions.  Sherburne was Special Counsel to President Bill Clinton and managed the White House response to ethics investigations by the Independent Counsel, most notably during the Whitewater controversy.\n\nWilliam H. Kennedy III: William H. Kennedy III is an American lawyer from Arkansas.  He served as a senior partner in the Rose Law Firm of Little Rock, Arkansas, with Hillary Clinton where he focused on commercial, corporate, real estate, and banking law.  From 1993 until 1995, he served as an associate counsel to President Bill Clinton before returning to Little Rock.  Two other Rose Law Firm partners, Vince Foster and Webb Hubbell, also joined the Clinton administration, but Kennedy was the only one to return to Little Rock without a scandal.\n\nKatherine Archuleta: Katherine L. Archuleta (born c.1949) is an American teacher and a political executive.  She was the director of the United States Office of Personnel Management.  President Barack Obama appointed her on May 23, 2013.  She was sworn in on November 4, 2013.  She had previously served as National Political Director for Obama's 2012 reelection campaign.  Prior to that, she had been Executive Director of the National Hispanic Cultural Center Foundation in New Mexico, had co-founded the Latina Initiative, had worked at a Denver law firm, and had worked in the Clinton Administration as chief of staff to the Secretary of Transportation, Federico Peña.  She became embroiled in controversy after the disclosure of a massive national security breach in June 2015.  The hack involved the theft of millions of federal employee records and included security-clearance details dating back 15 years, which prompted lawmakers from both political parties to demand that she resign.  On July 10, 2015, Archuleta tendered her resignation.\n\nDavid Adelman: David I. Adelman (born May 24, 1964) is an American lawyer, diplomat, and legislator.  He was the United States Ambassador to the Republic of Singapore from 2010 to 2013.  Currently, he is a partner in the global law firm Reed Smith LLP working out of the firm's New York office and regularly traveling to the firm's offices in Asia.  Adelman is an advisor to venture capital firm OurCrowd.\n\nHenry Cisneros payments controversy: The Henry Cisneros payments controversy was a lengthy investigation begun in 1995 into allegations that Henry Cisneros, United States Secretary of Housing and Urban Development during the Presidency of Bill Clinton, had lied to the FBI background check investigators about payments he had made to his former mistress.  Independent Counsel David Barrett was appointed to investigate the matter.  In 1995 Cisneros was indicted; in 1997 he pleaded guilty to a misdemeanor; in 2001 he was pardoned by President Bill Clinton.  The Independent Counsel investigation continued, however, focusing on allegations of obstruction of justice by the Clinton administration.  It issued a final report, known as the Barrett Report, in 2006 that did little to resolve matters.\n\nDrew S. Days III: Drew Saunders Days III (born August 29, 1941) is an American lawyer, who served as United States Solicitor General from 1993 to 1996 under President Bill Clinton.  He also served as the first African American Assistant Attorney General for the Civil Rights Division in the Carter Administration from 1977 to 1980.  He is the Alfred M. Rankin Professor of Law at Yale Law School, assuming that post in 1992, and joining the Yale Law faculty in 1981.  Since 1997, he has also headed the Supreme Court and appellate practice at Morrison & Foerster LLP and was of counsel at the firm's Washington, D.C. office until his retirement from the firm in December, 2011.  He earned his law degree at Yale Law School in 1966.  He has been admitted to practice law before the United States Supreme Court, and in the states of Illinois and New York.\n\nGordon Davis: Gordon Jamison Davis, a partner in the New York office of the law firm Venable LLP, was born in Chicago in 1941 and has been a resident of New York City since his graduation from Harvard Law School in 1967.  Mr. Davis has been a prominent leader in New York City's public, civic, and legal affairs for four decades.  He was Mayor Ed Koch’s first commissioner of parks and recreation and is considered one of New York’s most successful parks commissioners.  He was one of the first African Americans to become a partner in a major New York corporate law firm (Lord Day & Lord, 1983).  He is the Founding Chairman of Jazz at Lincoln Center, one of the four Founding Trustees of the Central Park Conservancy, a Founding Member in the first class inducted into the Performing Arts Hall of Fame at Lincoln Center, a Life Trustee of the New York Public Library, an appointee of President Barack Obama to the board of the Kennedy Center for the Performing Arts, and a recipient of an honorary degree (LL.D.)  and the Bicentennial Medal from his alma mater, Williams College.\n\nWhite House FBI files controversy: The White House FBI files controversy of the Clinton Administration, often referred to as Filegate, arose in June 1996 around improper access in 1993 and 1994 to FBI security-clearance documents.  Craig Livingstone, director of the White House's Office of Personnel Security, improperly requested, and received from the FBI, background reports concerning several hundred individuals without asking permission.  The revelations provoked a strong political and press reaction because many of the files covered White House employees from previous Republican administrations, including top presidential advisors.  Under criticism, Livingstone resigned from his position.  Allegations were made that senior White House figures, including First Lady Hillary Clinton, may have requested and read the files for political purposes, and that the First Lady had authorized the hiring of the underqualified Livingstone.\n\nQuestion:  Robert William Ray (born April 4, 1960) is an American lawyer practicing in the New York office of the Dallas-based law firm of Thompson & Knight, LLP, as the successor to Ken Starr, as the head of the Office of the Independent Counsel (1999 to 2002) he investigated and issued the final reports on the White House FBI files controversy of the Clinton Administration, often referred to as which term, arose in June 1996 around improper access in 1993 and 1994 to FBI security-clearance documents?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"entity_name\": {\n      \"type\": \"string\",\n      \"description\": \"The formal name of the controversy.\"\n    },\n    \"common_term\": {\n      \"type\": \"string\",\n      \"description\": \"The term the controversy is often referred to as.\"\n    },\n    \"key_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"administration\": {\n          \"type\": \"string\",\n          \"description\": \"The US presidential administration during which the controversy occurred.\"\n        },\n        \"start_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the controversy arose.\"\n        },\n        \"improper_access_years\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"integer\"\n          },\n          \"description\": \"Years when improper access to documents occurred.\"\n        },\n        \"subject_of_access\": {\n          \"type\": \"string\",\n          \"description\": \"Description of the documents that were improperly accessed.\"\n        },\n        \"investigator\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the person who investigated the controversy.\"\n        },\n        \"investigator_role\": {\n          \"type\": \"string\",\n          \"description\": \"The role of the investigator during the investigation.\"\n        },\n        \"investigation_period\": {\n          \"type\": \"string\",\n          \"description\": \"The period during which the investigation was conducted.\"\n        }\n      },\n      \"required\": [\n        \"administration\",\n        \"start_year\",\n        \"improper_access_years\",\n        \"subject_of_access\",\n        \"investigator\",\n        \"investigator_role\",\n        \"investigation_period\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"entity_name\",\n    \"common_term\",\n    \"key_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "entity_name": {
        "type": "string",
        "description": "The formal name of the controversy."
      },
      "common_term": {
        "type": "string",
        "description": "The term the controversy is often referred to as."
      },
      "key_details": {
        "type": "object",
        "properties": {
          "administration": {
            "type": "string",
            "description": "The US presidential administration during which the controversy occurred."
          },
          "start_year": {
            "type": "integer",
            "description": "The year the controversy arose."
          },
          "improper_access_years": {
            "type": "array",
            "items": {
              "type": "integer"
            },
            "description": "Years when improper access to documents occurred."
          },
          "subject_of_access": {
            "type": "string",
            "description": "Description of the documents that were improperly accessed."
          },
          "investigator": {
            "type": "string",
            "description": "The name of the person who investigated the controversy."
          },
          "investigator_role": {
            "type": "string",
            "description": "The role of the investigator during the investigation."
          },
          "investigation_period": {
            "type": "string",
            "description": "The period during which the investigation was conducted."
          }
        },
        "required": [
          "administration",
          "start_year",
          "improper_access_years",
          "subject_of_access",
          "investigator",
          "investigator_role",
          "investigation_period"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "entity_name",
      "common_term",
      "key_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
