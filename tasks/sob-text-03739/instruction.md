{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nStephen Hadley: Stephen John Hadley (born February 13, 1947) was the 21st U.S. Assistant to the President for National Security Affairs (commonly referred as National Security Advisor), serving under President George W. Bush during the second term of his administration.  Hadley was Deputy National Security Advisor during the Bush's first term.  Before that Hadley served in a variety of capacities in the defense and national security fields.  He has also worked as a lawyer and consultant in private practice.\n\nBrent Scowcroft: Brent Scowcroft ( ; born March 19, 1925) is a retired United States Air Force lieutenant general who was the United States National Security Advisor under U.S. Presidents Gerald Ford and George H. W. Bush.  He also served as Military Assistant to President Richard Nixon and as Deputy Assistant to the President for National Security Affairs in the Nixon and Ford administrations.  He served as Chairman of the President's Foreign Intelligence Advisory Board under President George W. Bush from 2001 to 2005 and assisted President Barack Obama in choosing his national security team.\n\nNational Security Advisor (United States): The Assistant to the President for National Security Affairs (APNSA), commonly referred to as the National Security Advisor (NSA) or at times informally termed the NSC advisor, is a senior aide in the Executive Office of the President, based at the West Wing of the White House, who serves as the chief in-house advisor to the President of the United States on national security issues.  The National Security Advisor is appointed by the President and does not require confirmation by the Senate, but an appointment of a three or four-star general to the role requires Senate reconfirmation of military rank.\n\nJohn O. Brennan: John Owen Brennan (born September 22, 1955) was the Director of the Central Intelligence Agency from March 2013 to January 2017.  He has served as chief counterterrorism advisor to U.S. President Barack Obama; his title was Deputy National Security Advisor for Homeland Security and Counterterrorism, and Assistant to the President.  His responsibilities included overseeing plans to protect the country from terrorism and respond to natural disasters, and he met with the President daily.  Previously, he advised President Obama on foreign policy and intelligence issues during the 2008 presidential campaign and transition.  Brennan withdrew his name from consideration for Director of the Central Intelligence Agency (CIA) in the first Obama administration over concerns about his support for transferring terror suspects to countries where they may be tortured while serving under President George W. Bush.  Instead, Brennan was appointed Deputy National Security Advisor, a position which did not require Senate confirmation.\n\nDeputy National Security Advisor (United States): The Deputy Assistant to the President for National Security Affairs, also known as the Deputy National Security Advisor, is a member of the Executive Office of the President of the United States and the United States National Security Council, serving as deputy to the President's National Security Advisor.\n\nRobert Malley: Robert Malley (born 1963) is an American lawyer, political scientist and specialist in conflict resolution.  He is currently the Vice President for Policy at the International Crisis Group in Washington, DC.  Prior to holding that title, he served at the National Security Council under Barack Obama from February 2014 until January 2017.  Prior to holding that title, he was Program Director for Middle East and North Africa at the International Crisis Group and Assistant to National Security Advisor Sandy Berger (1996–1998) and the Director for Democracy, Human Rights and Humanitarian Affairs at the National Security Council (1994–1996).  Malley is considered an expert on the Israeli–Palestinian conflict and has written extensively on this subject.  As Special Assistant to President Clinton, he was a member of the U.S. peace team and helped organize the 2000 Camp David Summit.  In 2015, the Obama administration appointed Rob Malley as its \"point man\" on the Middle East, leading the Middle East desk of the National Security Council.  In November 2015, Malley was named as President Obama's new special ISIS advisor.\n\nJames L. Jones: James Logan \"Jim\" Jones Jr. (born December 19, 1943) is a retired United States Marine Corps general and the former United States National Security Advisor.\n\nJohn Poindexter: John Marlan Poindexter (born August 12, 1936) is a retired United States naval officer and Department of Defense official.  He was Deputy National Security Advisor and National Security Advisor for the Reagan administration.  He was convicted in April 1990 of multiple felonies as a result of his actions in the Iran–Contra affair, but his convictions were reversed on appeal in 1991.  More recently, he served a brief stint as the director of the DARPA Information Awareness Office for the George W. Bush administration.  He is the father of NASA astronaut and U.S. Navy Captain Alan G. Poindexter.\n\nHomeland Security Advisor: The Assistant to the President for Homeland Security and Counterterrorism, commonly referred to as the Homeland Security Advisor and occasionally holding the title of Deputy National Security Advisor for Homeland Security and Counterterrorism, is a senior aide in the Executive Office of the President, based in the West Wing of the White House, who serves as the chief in-house advisor to the President of the United States on homeland security and counterterrorism issues.  The Homeland Security Advisor is a statutory member of the Homeland Security Council.  Serving at the pleasure of the President, the Homeland Security Advisor does not require Senate confirmation for appointment to the office.\n\nThomas E. Donilon: Thomas E. \"Tom\" Donilon (born May 14, 1955) is an American lawyer and former government official who served as National Security Advisor in the Obama administration.  Previously, he served together with diplomat Wendy Sherman as Agency Review Team Lead for the State Department in the Obama transition, and as Deputy to National Security Advisor James Jones early in the Obama administration.  Donilon replaced Jones as National Security Advisor on October 8, 2010.\n\nQuestion: Thomas E. \"Tom\" Donilon (born May 14, 1955) is an American lawyer and former government official who served as National Security Advisor in the Obama administration, previously, he served as Deputy to which National Security Advisor, and retired United States Marine Corps general? \n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"deputy_role\": {\n      \"type\": \"string\",\n      \"description\": \"The role held by Thomas E. Donilon.\"\n    },\n    \"administration\": {\n      \"type\": \"string\",\n      \"description\": \"The U.S. presidential administration during which Donilon served as Deputy.\"\n    },\n    \"national_security_advisor\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"full_name\": {\n          \"type\": \"string\",\n          \"description\": \"The full name of the National Security Advisor.\"\n        },\n        \"military_rank\": {\n          \"type\": \"string\",\n          \"description\": \"The military rank of the National Security Advisor.\"\n        },\n        \"is_retired\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the military rank is retired.\"\n        }\n      },\n      \"required\": [\n        \"full_name\",\n        \"military_rank\",\n        \"is_retired\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"deputy_role\",\n    \"administration\",\n    \"national_security_advisor\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "deputy_role": {
        "type": "string",
        "description": "The role held by Thomas E. Donilon."
      },
      "administration": {
        "type": "string",
        "description": "The U.S. presidential administration during which Donilon served as Deputy."
      },
      "national_security_advisor": {
        "type": "object",
        "properties": {
          "full_name": {
            "type": "string",
            "description": "The full name of the National Security Advisor."
          },
          "military_rank": {
            "type": "string",
            "description": "The military rank of the National Security Advisor."
          },
          "is_retired": {
            "type": "boolean",
            "description": "Indicates if the military rank is retired."
          }
        },
        "required": [
          "full_name",
          "military_rank",
          "is_retired"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "deputy_role",
      "administration",
      "national_security_advisor"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
