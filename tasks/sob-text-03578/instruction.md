Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
Peter W. Bodde: Peter William Bodde (born October 1954) is a member of the United States Foreign Service, and is the current United States Ambassador to Libya.  He has served as the United States Ambassador to Nepal and as the United States Ambassador to Malawi, during which time he was credited for promoting HIV/AIDS.

Ian C. Kelly: Ian Crawford Kelly (born 1953) is an American politician and senior foreign service officer who is the current United States Ambassador to Georgia.  He previously served as the U.S. Ambassador to the Organization for Security and Cooperation in Europe (OSCE) from 2010 to 2013.  Prior to his ambassadorship, Kelly held a variety of high-level roles at the U.S. State Department, including serving as the department spokesman under Secretary Hillary Clinton, and has extensive experience working on issues relating to NATO, Russia, and the Balkans.

Peter R. Huntsman: Peter R. Huntsman is a business executive, currently serving as the President and CEO of Huntsman Corporation.  He is part of the Huntsman family dynasty, with father Jon Meade Huntsman the founder of Huntsman Corporation and his brother Jon Huntsman Jr., former United States Ambassador and former Governor of Utah.  Huntsman was named as a "Who's Who in Energy" honoree by the Houston Business Journal in 2015.

Pamela L. Spratlen: Pamela Leora Spratlen (born 1954) is a U.S. diplomat.  She is the current United States Ambassador to Uzbekistan and former United States Ambassador to Kyrgyzstan.

Jon Huntsman Jr.: Jon Meade Huntsman Jr. (born March 26, 1960) is an American politician, businessman, and diplomat who serves as the current United States ambassador to Russia.  Huntsman was also the former governor of Utah from 2005 to 2009, and as United States Ambassador to Singapore from 1992 to 1993, and China from 2009 to 2011.  He has served in the administrations of five U.S. Presidents and was a candidate for the 2012 Republican presidential nomination.  In January 2014, Huntsman was named Chairman of the Washington-based foreign policy think-tank the Atlantic Council.  In March 2017 it was reported that he would be appointed as the next Ambassador to Russia.  This nomination was submitted to the Senate on July 20, 2017 and confirmed on September 28, 2017.

Sung Kim: Sung Y. Kim (born 1960) is a South Korean-born American diplomat and the current United States Ambassador to the Philippines as well as the former United States Special Representative for North Korea Policy.  He previously served as the United States Ambassador to South Korea and the U.S. Special Envoy for the Six-Party Talks.

P. Michael McKinley: Peter Michael McKinley (born January 1954) is an American diplomat who is the current United States Ambassador to Brazil and is the former United States Ambassador to Afghanistan.

Karen B. Stewart: Karen Brevard Stewart (born 1952) is an American diplomat who is the current United States Ambassador to the Marshall Islands.  She was nominated by President Barack Obama to be United States Ambassador to the Marshall Islands on November 5, 2015 was confirmed by the U.S. Senate on May 17, 2016.  Stewart also served as United States Ambassador to Belarus from August 14, 2006 to March 12, 2008 and as United States Ambassador to Laos from November 2010 to August 2013.

Tulinabo S. Mushingi: Tulinabo Salama Mushingi (born August 4, 1956) is an American diplomat who currently serves a joint appointment as United States Ambassador to Senegal and United States Ambassador to Guinea-Bissau.  He previously served as the United States Ambassador to Burkina Faso from 2013 to 2016.  He also served in the executive offices of Secretaries of State John F. Kerry and Hillary Clinton.  In February 2017, President Donald Trump nominated Mushingi to serve concurrently as United States Ambassador to Senegal and United States Ambassador to Guinea-Bissau.  Mushingi had originally been nominated for the position by outgoing President Barack Obama in January 2017.  When Trump took office, he withdrew Mushingi's nomination before renominating him for the same position.  He was confirmed by the United States Senate by voice vote on May 18, 2017.

Harry K. Thomas Jr.: Harry Keels Thomas Jr. (born June 3, 1956 in the Harlem section of New York City) is an American diplomat and current United States Ambassador to Zimbabwe.  He served as the United States Ambassador to the Philippines from 2010 to 2013.  A former United States Ambassador to Bangladesh (serving from 2003 to 2005) and Director General of the United States Foreign Service (serving from 2007 to 2009), Thomas was designated by US President Barack Obama on November 19, 2009 to replace Kristie Kenney as Ambassador to the Philippines—the first African American to serve at that post.  He was confirmed by the United States Senate on March 19, 2010 and presented his credentials to Philippine president Gloria Macapagal-Arroyo on April 27, 2010 He was then nominated and confirmed as the United States Ambassador to Zimbabwe on October 22, 2015.  He was sworn in on December 8, 2015.

Question: Who is the father of the current United States ambassador to Russia?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "ambassador_to_russia": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the current United States Ambassador to Russia."
        },
        "current_role": {
          "type": "string",
          "description": "The current diplomatic role of the individual."
        }
      },
      "required": [
        "name",
        "current_role"
      ],
      "additionalProperties": false
    },
    "father": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the father of the ambassador."
        },
        "relationship_to_ambassador": {
          "type": "string",
          "description": "The relationship of this person to the ambassador."
        },
        "other_roles": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Other notable roles or affiliations of the father."
        }
      },
      "required": [
        "name",
        "relationship_to_ambassador"
      ],
      "additionalProperties": false
    },
    "family_dynasty_context": {
      "type": "string",
      "description": "Contextual information about the family's prominence."
    }
  },
  "required": [
    "ambassador_to_russia",
    "father",
    "family_dynasty_context"
  ],
  "additionalProperties": false
}
