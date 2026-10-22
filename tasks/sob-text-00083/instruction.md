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
Bob Casey Jr.: Robert Patrick Casey Jr. (born April 13, 1960) is an American attorney and politician, currently the senior United States Senator from Pennsylvania.  He previously served as Pennsylvania Auditor General from 1997 to 2005 and as Pennsylvania Treasurer from 2005 to 2007.

Email Privacy Act: The Email Privacy Act is a bill introduced in the United States Congress.  The bipartisan proposed federal law is sponsored by Representative Kevin Yoder, a Republican from Kansas, and Representative Jared Polis, a Democrat of Colorado.  The law is designed to update and reform existing online communications law, specifically the Electronic Communications Privacy Act (ECPA) of 1986.  In the 113th Congress (2013-14), the bill never made it out of subcommittee.  In the 114th Congress (2015-16), the bill was unanimously passed by the House, but was derailed in the Senate following a series of weakening amendments offered by Republican Senator John Cornyn of Texas, the Senate Majority Whip.  In the 115th Congress (2017-18), it was passed by the House on a voice vote.

Global food security index: The global food security index consists of a set of indices from 105 countries.  It measures food security across most of the countries of the world.  Countries that score top rating are the United States, Denmark, Norway and France.

Cyber Intelligence Sharing and Protection Act: The Cyber Intelligence Sharing and Protection Act (CISPA (112th Congress), (113th Congress), (114th Congress)) is a proposed law in the United States which would allow for the sharing of Internet traffic information between the U.S. government and technology and manufacturing companies.  The stated aim of the bill is to help the U.S. government investigate cyber threats and ensure the security of networks against cyberattacks.

State Marriage Defense Act: The State Marriage Defense Act ( , in the 113th Congress, , in the 114th Congress) is a proposed law introduced by Republican Senators Ted Cruz of Texas and Mike Lee of Utah that defines the terms "spouse" and "marriage" as used in federal laws to always follow the definition used in the particular state where the law is applied.  The bill is advocated by conservative and Christian Right organizations after "United States v. Windsor", including the National Organization for Marriage, the Ethics & Religious Liberty Commission, Concerned Women for America, the Family Research Council and Heritage Action.

Global Food Security Act of 2009: The Global Food Security Act of 2009, also known as the Lugar-Casey Food Security Bill, is a bill introduced February 5, 2009 in the 111th Congress by Richard Lugar (Indiana-R) and sponsored by Robert Casey (Pennsylvania-D), Mark Begich (Alaska-D), Roland Burris (Illinois-D), Susan Collins (Maine-R), Richard Durbin (Illinois-D), Thomas Harkin (Iowa-D), John Kerry (Massachusetts-D), and Mary Landrieu (Louisiana-D) to the United States Senate as .

Nancy Stetson: Nancy Stetson is the United States Special Representative for Global Food Security, responsible for leading all aspects of U.S. diplomacy related to food security and nutrition, appointed by U.S. Secretary of State John Kerry on June 23, 2014.  She is also the Deputy Coordinator for Diplomacy for Feed the Future - the US government's global hunger and food security initiative.  In October 2016, Ambassador Stetson was the deputy head of delegation for the U.S. party to Habitat III - the United Nations Conference on Housing and Sustainable Urban Development.

Cybersecurity Information Sharing Act: The Cybersecurity Information Sharing Act (CISA [113th Congress], [114th Congress]) is a United States federal law designed to "improve cybersecurity in the United States through enhanced sharing of information about cybersecurity threats, and for other purposes".  The law allows the sharing of Internet traffic information between the U.S. government and technology and manufacturing companies.  The bill was introduced in the U.S. Senate on July 10, 2014, and passed in the Senate October 27, 2015.  Opponents question CISA's value, believing it will move responsibility from private business to the government, thereby increasing vulnerability of personal private information, as well as dispersing personal private information across seven government agencies, including the NSA and local police.

Patrick Leahy: Patrick Joseph Leahy (born March 31, 1940) is an American politician and the senior United States Senator from Vermont, since 1975.  A member of the Democratic Party, Leahy served as the President pro tempore of the United States Senate from December 17, 2012, to January 6, 2015.  As President pro tempore, he was third in the presidential line of succession.  He is the most senior senator and took office at 34 years old, younger than any other current senator.  Leahy received the title of President pro tempore emeritus upon the commencement of the 114th Congress.  He is the last remaining member of the Senate to have served prior to the 1976 election of President Jimmy Carter.

Global Food Security Act of 2016: The Global Food Security Act of 2016 (Pub.L.  114–195 ), is a law introduced on March 24, 2015 in the 114th Congress by Representative Christopher Henry "Chris" Smith (New Jersey-R) and on May 7, 2015 by Senator Robert Patrick "Bob" Casey Jr. (Pennsylvania-D), and signed by President Barack Obama on July 20, 2016.

Question: The Global Food Security Act of 2016, is a law introduced on March 24, 2015 in the 114th Congress by which Senator of Pennsylvania, who is an American attorney and politician, currently the senior United States Senator from Pennsylvania?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "act_name": {
      "type": "string",
      "description": "The full name of the act."
    },
    "congress_number": {
      "type": "integer",
      "description": "The number of the Congress in which the act was introduced."
    },
    "introduction_details": {
      "type": "object",
      "properties": {
        "introduction_date": {
          "type": "string",
          "format": "date",
          "description": "The date the act was introduced by the specified senator."
        },
        "introducer_type": {
          "type": "string",
          "description": "The type of legislator who introduced the act (e.g., Senator, Representative)."
        }
      },
      "required": [
        "introduction_date",
        "introducer_type"
      ],
      "additionalProperties": false
    },
    "senator_information": {
      "type": "object",
      "properties": {
        "full_name": {
          "type": "string",
          "description": "The full name of the senator."
        },
        "nickname": {
          "type": "string",
          "description": "The common nickname of the senator."
        },
        "state": {
          "type": "string",
          "description": "The state the senator represents."
        },
        "political_party": {
          "type": "string",
          "description": "The political party of the senator."
        },
        "current_role": {
          "type": "string",
          "description": "The current role or position of the senator."
        },
        "profession": {
          "type": "string",
          "description": "The profession(s) of the senator."
        }
      },
      "required": [
        "full_name",
        "nickname",
        "state",
        "political_party",
        "current_role",
        "profession"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "act_name",
    "congress_number",
    "introduction_details",
    "senator_information"
  ],
  "additionalProperties": false
}
