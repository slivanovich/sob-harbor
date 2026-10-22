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
Robert Gascoyne-Cecil, 5th Marquess of Salisbury: Robert Arthur James Gascoyne-Cecil, 5th Marquess of Salisbury, (27 August 1893 – 23 February 1972), known as Viscount Cranborne from 1903 to 1947, was a British Conservative politician.

Tory Boy: Tory Boy was a character in a television sketch by comedian Harry Enfield which portrayed a young, male, Conservative MP.  The term has since been used as a caricature of young Conservative MPs.  Tory Boy was a repulsive thirteen-year-old, combining the characteristics of a snobbish, unpopular boy who went to school with Enfield, and those of an imagined younger version of William Hague.  Enfield also claimed to have mixed other recent Conservative politicians such as Michael Howard and Michael Portillo into the character, alleging that they were "Tory Boys who have never grown up."  The traits of "Tory Boy" have also been said to mirror those of a stereotypical member of the Federation of Conservative Students.  The Tory Boy image of a young Conservative MP has damaged some politicians.  William Hague struggled to shake off the stereotype and was often ridiculed for it during his leadership of the party.  Recently it has been argued that Conservative Future has managed to change the image of young Conservatives from that given by the FCS.

Robert Gascoyne-Cecil, 3rd Marquess of Salisbury: Robert Arthur Talbot Gascoyne-Cecil, 3rd Marquess of Salisbury, {'1': ", '2': ", '3': ", '4': "} (3 February 183022 August 1903), styled Lord Robert Cecil before 1865 and Viscount Cranborne from June 1865 until April 1868, was a British Conservative statesman, serving as prime minister three times for a total of over 13 years.  He was the last prime minister to head his full administration from the House of Lords.

James Gascoyne-Cecil, 2nd Marquess of Salisbury: James Brownlow William Gascoyne-Cecil, 2nd Marquess of Salisbury, {'1': ", '2': ", '3': ", '4': "} (17 April 1791 – 12 April 1868), styled Viscount Cranborne until 1823, was a British Conservative politician.  He held office under the Earl of Derby as Lord Privy Seal in 1852 and Lord President of the Council between 1858 and 1859.  He was the father of Robert Gascoyne-Cecil, 3rd Marquess of Salisbury, three times Prime Minister of the United Kingdom.

Robert Gascoyne-Cecil, 7th Marquess of Salisbury: Robert Michael James Gascoyne-Cecil, 7th Marquess of Salisbury, (born 30 September 1946) is a British Conservative politician.  During the 1990s, he was Leader of the House of Lords under his courtesy title of Viscount Cranborne.  Lord Salisbury lives in one of England's largest historic houses, Hatfield House, which was built by an ancestor in the early 17th century, and he currently serves as Chancellor of the University of Hertfordshire.

James Gascoyne-Cecil, 4th Marquess of Salisbury: James Edward Hubert Gascoyne-Cecil, 4th Marquess of Salisbury, (23 October 1861 – 4 April 1947), known as Viscount Cranborne from 1868 to 1903, was a British statesman.

James Cecil, 5th Earl of Salisbury: James Cecil, 5th Earl of Salisbury (8 June 1691 – 9 October 1728), known as Viscount Cranborne from 1691 to 1694, was a British nobleman, politician, and peer.

Robert Gascoyne-Cecil, 6th Marquess of Salisbury: Robert Edward Peter Gascoyne-Cecil, 6th Marquess of Salisbury, DL (24 October 1916 – 11 July 2003), styled Viscount Cranborne from 1947 to 1972, was a British landowner and Conservative politician.

James Cecil, 1st Marquess of Salisbury: James Cecil, 1st Marquess of Salisbury, {'1': ", '2': ", '3': ", '4': "} (4 September 1748 – 13 June 1823), styled Viscount Cranborne until 1780 and known as The Earl of Salisbury between 1780 and 1789, was a British nobleman and politician.

South Dorset by-election, 1941: The South Dorset by-election of 1941 was held on 22 February 1941.  The by-election was held due to the succession to the peerage by writ of acceleration of the incumbent Conservative MP, Robert Gascoyne-Cecil, as Marquess of Salisbury.  It was won by the Conservative candidate Victor Montagu.

Question: Which conservative MP was known as Viscount Cranborne from 1903 to 1947 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_full_name": {
      "type": "string",
      "description": "The full name of the individual."
    },
    "known_as_title": {
      "type": "string",
      "description": "The title the person was known as during the specified period."
    },
    "title_period": {
      "type": "object",
      "properties": {
        "start_year": {
          "type": "integer",
          "description": "The start year of the period the person was known by the title."
        },
        "end_year": {
          "type": "integer",
          "description": "The end year of the period the person was known by the title."
        }
      },
      "required": [
        "start_year",
        "end_year"
      ],
      "additionalProperties": false
    },
    "political_party": {
      "type": "string",
      "description": "The political party the individual belonged to."
    },
    "is_member_of_parliament": {
      "type": "boolean",
      "description": "Indicates if the individual was a Member of Parliament."
    }
  },
  "required": [
    "person_full_name",
    "known_as_title",
    "title_period",
    "political_party",
    "is_member_of_parliament"
  ],
  "additionalProperties": false
}
