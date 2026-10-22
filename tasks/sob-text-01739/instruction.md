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
Scott T. Rupp: Scott T. Rupp (born October 17, 1973) is a former Republican member of the Missouri Senate, representing the 2nd District from 2006 to 2014.  Previously he was a member of the Missouri House of Representatives from 2002 through 2006.  In the Missouri Senate, Rupp represented all of Lincoln County and portions of St. Charles County.  Elected to the Missouri Senate in a special election in April 2006, Scott was re-elected in November 2006 to serve his first full term.  He was re-elected in November 2010 to his second full term in the Missouri Senate.  Previously, he was twice elected to represent the citizens of northwest St. Charles County in the Missouri House of Representatives and received more than 65 percent of the vote in 2002 and 2004.  In 2014 Rupp could not run for re-election due to term limits.  In April 2014 he retired early to take a position on the Missouri Public Service Commission.

Michael R. Gibbons: Michael R. Gibbons is a former Republican member of the Missouri Senate, representing the 15th District from 2001-2009.  He served as "President pro tempore".  Previously he was a member of the Missouri House of Representatives from 1993 through 2000.  In 2008 he ran for Missouri Attorney General, losing to the Democratic nominee Chris Koster.

Ed Martin (Missouri politician): Edward Robert Martin Jr. is an American politician and attorney from the state of Missouri.  He is president of Phyllis Schlafly Eagles, and a CNN contributor.

Philippine presidential election, 1969: Presidential, legislative and local elections were held on November 11, 1969 in the Philippines.  Incumbent President Ferdinand Marcos won an unprecedented second full term as President of the Philippines.  Marcos was the last president in the entire electoral history who ran for and won a second term.  His running mate, incumbent Vice President Fernando Lopez was also elected to a third full term as Vice President of the Philippines.  An unprecedented twelve candidates ran for president, however ten of those were nuisance candidates.

Missouri attorney general election, 2012: The Missouri attorney general election of 2012 was held on November 6, 2012, alongside the presidential and gubernatorial elections.  The current Missouri Attorney General Chris Koster, a Democrat, won re-election for a second full term against Republican attorney Ed Martin.

Philippine general election, 1969: Presidential, legislative and local elections were held on November 11, 1969 in the Philippines.  Incumbent President Ferdinand Marcos won an unprecedented second full term as President of the Philippines.  Marcos was the last president in the entire electoral history who ran and won for a second term.  His running mate, incumbent Vice President Fernando Lopez was also elected to a third full term as Vice President of the Philippines.  An unprecedented twelve candidates ran for president, however ten of those were nuisance candidates.

Chris Koster: Chris Koster (born August 31, 1964) is an American lawyer who served as the 41st Attorney General of Missouri from 2009 to 2017.  Before he was elected attorney general, he had served in the Missouri Senate since 2005 representing the 31st Senatorial District as a Republican until August 1, 2007, when he switched to the Democratic Party.

Henry McIver (chief justice): Henry McIver was a chief justice on the South Carolina Supreme Court.  He was born on September 25, 1826, near Society Hill, South Carolina to Alexander McIver and Mary Hanford McIver.  He moved to Cheraw, South Carolina in 1836 with his family.  In 1846, he graduated from South Carolina College (now the University of South Carolina).  He studied law with his father after college, and he was admitted to practice law in December 1847.  he married Caroline H. Powe on June 7, 1849.  When McIver's father died in July 1850, Governor Seabrook appointed McIver to complete his father's term as the solicitor (prosecutor) for the eastern circuit of the state.  At the end of the term, McIver did not run for a full term; however, the successor himself died in office, and McIver was again appointed to conclude the unexpired term.  At the end of that second term, McIver was elected to a full term.  He continued being re-elected to the position until 1868 when he was removed from office as part of Reconstruction.  McIver served in the Confederate army and returned to his law practice after the Civil War.  On May 19, 1877, he was elected as an associate justice of the South Carolina Supreme Court to fill the unexpired term of the Justice Willard who had become chief justice of the court.  The General Assembly elected McIver unanimously to a full term in December 1879.  He served in that position until he was elected and immediately sworn in as chief justice on December 1, 1891, replacing Chief Justice Simpson.

United States Senate election in Montana, 1942: The 1942 United States Senate election in Montana took place on November 3, 1942.  Incumbent United States Senator James E. Murray, who was first elected to the Senate in a special election in 1934 and was re-elected in 1936, ran for re-election.  Following his victory in a competitive Democratic primary, Murray advanced to the general election, where he was opposed by former United States Attorney for the District of Montana Wellington D. Rankin, the Republican nominee and brother of representative Jeannette Rankin.  In a closely fought election, Murray narrowly defeated Rankin to win re-election to his third term and his second full term in the Senate.

Kim Holland: Kim Holland (born August 6, 1955) is an American politician and insurance professional from the U.S. state of Oklahoma.  Holland served as the Oklahoma Insurance Commissioner until January 2011.  She was appointed to that position by Governor Brad Henry in 2005, following the indictment and resignation of her predecessor, Carroll Fisher.  The second woman to serve as the state insurance commissioner, she was re-elected in 2006 to her own four-year term.  In 2010, attempting to gain her second full term in office, Holland faced Republican nominee John D. Doak, who defeated her in November's general election.  Doak assumed office on January 10, 2011.

Question: Which American politician and attorney from the state of Missouri did General Chris Koster won re-election for a second full term against

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "election_details": {
      "type": "object",
      "properties": {
        "year": {
          "type": "integer",
          "description": "The year the election took place."
        },
        "office": {
          "type": "string",
          "description": "The office for which the winner was re-elected."
        }
      },
      "required": [
        "year",
        "office"
      ],
      "additionalProperties": false
    },
    "winner": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the politician who won re-election."
        },
        "party": {
          "type": "string",
          "description": "The political party of the winner."
        }
      },
      "required": [
        "name",
        "party"
      ],
      "additionalProperties": false
    },
    "opponent": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the American politician and attorney from Missouri who lost the election."
        },
        "description": {
          "type": "string",
          "description": "A description of the opponent's background as an American politician and attorney from Missouri."
        }
      },
      "required": [
        "name",
        "description"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "election_details",
    "winner",
    "opponent"
  ],
  "additionalProperties": false
}
