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
Northern Ireland Historical Institutional Abuse Inquiry: Northern Ireland Historical Institutional Abuse Inquiry

Conor Burns: Conor Burns (born 24 September 1972) is a British Conservative Party politician.  He was elected as the Member of Parliament (MP) for Bournemouth West at the 2010 general election.  He was Parliamentary Private Secretary (PPS) to Secretary of State for Northern Ireland between 2010 and 2012, before resigning from the Government due to his opposition to the Lords Reform Bill.  A long-standing ally of Boris Johnson, after serving in several PPS roles, he is now PPS to the Foreign Secretary.

Cameron Inquiry: The Cameron Inquiry, formerly the Commission of Inquiry on Hormone Receptor Testing, is a Canadian public judicial inquiry into the conduct of the Newfoundland and Labrador Eastern Health authority.  The inquiry is investigating whether Eastern Health was at fault in the reporting of erroneous and delayed test results to breast cancer patients between 1997 and 2005, and in then failing to report the full scope of these errors.  The inquiry developed ramifications for regional and national politics as the opposition Liberal Party questioned why the regional Progressive Conservative Party government had not intervened sooner in the crisis, and said that former deputy health minister Robert Thompson, who had been appointed to chair the inquiry, should stand down, prompting Newfoundland and Labrador premier Danny Williams to accuse the Liberals of a smear campaign.  The inquiry, chaired by Justice Margaret Cameron, was called in May 2007 and released a report in March 2009.

Leveson Inquiry: The Leveson inquiry is a judicial public inquiry into the culture, practices and ethics of the British press following the News International phone hacking scandal, chaired by Lord Justice Leveson, who was appointed in July 2011.  A series of public hearings were held throughout 2011 and 2012.  The Inquiry published the Leveson Report in November 2012, which reviewed the general culture and ethics of the British media, and made recommendations for a new, independent, body to replace the existing Press Complaints Commission, which would have to be recognised by the state through new laws.  Prime Minister David Cameron, under whose direction the inquiry had been established, said that he welcomed many of the findings, but declined to enact the requisite legislation.  Part 2 of the inquiry was to be delayed until after criminal prosecutions regarding events at the "News of the World", but the Conservative Party's 2017 manifesto states that the second part of the inquiry will be dropped entirely.

Conservative Muslim Forum: The Conservative Muslim Forum is a group within the British Conservative Party.  It aims to increase Conservative Party's knowledge and comprehension of issues and circumstances that have particular relevance to Muslim communities and develop suitable responses.  It also seeks to increase support for the Conservative Party within the Muslim community.  Anyone who is eligible to vote in British general or local elections regardless of race, colour or creed may become a member of the Conservative Muslim Forum.  It will however be necessary for a person applying for membership of the Conservative Muslim Forum to be an existing member of the Conservative Party or apply for such membership simultaneously. 

92 Group: The 92 Group is a right-wing grouping within the British Conservative Party.  They are so named because they would meet at Conservative MP Sir Patrick Wall's home, 92 Cheyne Walk in Chelsea, London.  It was founded in 1964 in order to "keep the Conservative Party conservative" and membership is by invitation only.  During the period of Margaret Thatcher's leadership of the Conservative Party it was a prominent supporter of her policies.  During John Major's premiership it became a focus for Thatcherite MPs dissatisfied with his leadership and was prominent in supporting John Redwood's unsuccessful candidacy against John Major for the leadership of the Conservative Party in 1995.

Patrick McLoughlin: Sir Patrick Allen McLoughlin (born 30 November 1957) is a British Conservative Party politician.  He first became a Member of Parliament (MP) at the 1986 by-election in West Derbyshire.  The constituency became the Derbyshire Dales for the 2010 general election; McLoughlin has remained the seat's MP.  On 4 September 2012, he was appointed Secretary of State for Transport.  As a former miner, he is one of the few Conservative MPs to have been a manual worker before being elected to Parliament.  On 14 July 2016, he became Chairman of the Conservative Party and Chancellor of the Duchy of Lancaster, under the new administration of Conservative Prime Minister Theresa May.

Kincora Boys' Home: The Kincora Boys' Home was a boys' home in Belfast, Northern Ireland that was the scene of serious organised child sexual abuse, causing a scandal and attempted cover-up in 1980, with allegations of state collusion.  The Northern Ireland Historical Institutional Abuse Inquiry began examining allegations relating to the Home on 31 May 2016, including claims that there was a paedophile ring at the home with links to the intelligence services; Northern Ireland Secretary Theresa Villiers said that all state agencies would co-operate with the inquiry.

Theresa Villiers: Theresa Anne Villiers (pronounced "Villers"; born 5 March 1968 in London) is a British Conservative Party politician.

Shailesh Vara: Shailesh Lakhman Vara (born 4 September 1960) is a British Conservative Party politician.  He was elected Member of Parliament (MP) for North West Cambridgeshire in the 2005 general election, succeeding Brian Mawhinney as the Conservative MP for the seat.  Vara has previously been a Vice-Chairman of the Conservative Party.  In 2006, he was appointed to the shadow ministerial post of Shadow Deputy Leader of the House of Commons.  Following the 2010 general election, he was appointed to the position of Assistant Whip in the coalition government.  On 7 October 2013, he was appointed Parliamentary Under Secretary of State at the Ministry of Justice.

Question: Which British Conservative Party politician said that all state agencies would co-operate with the Northern Ireland Historical Institutional Abuse Inquiry?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "politician_name": {
      "type": "string",
      "description": "The name of the British Conservative Party politician."
    },
    "political_party": {
      "type": "string",
      "description": "The political party the politician belongs to."
    },
    "role_at_time_of_statement": {
      "type": "string",
      "description": "The role or position held by the politician when the statement was made."
    },
    "inquiry_details": {
      "type": "object",
      "properties": {
        "inquiry_name": {
          "type": "string",
          "description": "The name of the inquiry to which the statement refers."
        },
        "cooperation_pledged": {
          "type": "boolean",
          "description": "Indicates whether cooperation was pledged for the inquiry."
        },
        "agencies_involved_in_cooperation": {
          "type": "string",
          "description": "Description of the types of agencies that pledged cooperation."
        }
      },
      "required": [
        "inquiry_name",
        "cooperation_pledged",
        "agencies_involved_in_cooperation"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "politician_name",
    "political_party",
    "role_at_time_of_statement",
    "inquiry_details"
  ],
  "additionalProperties": false
}
