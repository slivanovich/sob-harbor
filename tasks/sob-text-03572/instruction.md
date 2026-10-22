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
Hillary Clinton presidential campaign, 2016: The 2016 presidential campaign of Hillary Rodham Clinton was announced in a YouTube video, on April 12, 2015.  Hillary Clinton was the 67th United States Secretary of State and served during the first term of the Obama administration from 2009 to 2013.  She was previously the United States Senator from New York from 2001 to 2009, and is the wife of former President Bill Clinton.  This campaign marked her second bid for the presidency after losing in her first attempt to Barack Obama in the 2008 Democratic primary.

Bush White House email controversy: During the 2007 Congressional investigation of the dismissal of eight U.S. attorneys, it was discovered that administration officials had been using a private Internet domain, called gwb43.com, owned by and hosted on an email server run by the Republican National Committee, for various official communications.  The domain name is an abbreviation for "George W. Bush, 43rd" President of the United States.  The use of this email domain became public when it was discovered that J. Scott Jennings, the White House's deputy director of political affairs, was using a gwb43.com email address to discuss the firing of the U.S. attorney for Arkansas.  Communications by federal employees were also found on georgewbush.com (registered to "Bush-Cheney '04, Inc.") and rnchq.org (registered to "Republican National Committee").  Congressional requests for administration documents while investigating the dismissals of the U.S. attorneys required the Bush administration to reveal that not all internal White House emails were available.  Conducting governmental business in this manner is a possible violation of the Presidential Records Act of 1978.  Over 5 million emails may have been lost.  Greg Palast claims to have come up with 500 of the Karl Rove emails, leading to damaging allegations.  In 2009, it was announced that as many as 22 million emails may have been lost.

Juan Verde: Juan Verde Suárez (born July 7, 1971) is a business and social entrepreneur who worked on the political campaigns of Senator Ted Kennedy, President Bill Clinton, Vice President Al Gore, Senator John Kerry, and Secretary of State Hillary Clinton, besides serving as International Co-Chair for the reelection campaign of President Barack Obama in 2012.  In addition to developing and directing a strategy designed to mobilize millions of American citizens residing outside of the United States, Mr. Verde serves as an advisor to President Obama on international trade, the Hispanic vote as well as sustainability related issues.  Mr. Verde was appointed by President Barack Obama as Deputy Assistant Secretary for Europe and Eurasia at the US Department of Commerce where he served until 2011.

David E. Kendall: David Evan Kendall (born 1944 ) is an American attorney, a graduate of Yale Law School and Oxford University, who clerked with Supreme Court Justice Byron White, worked as associate counsel at the NAACP Legal Defense Fund, and has been a partner at Williams & Connolly LLP of Washington, DC since 1981, where he has provided legal counsel to individuals and corporations on high-profile business and political matters.  He is well known for his roles in the "Coker v. Georgia, Gilmore v. Utah," and other death penalty cases; in the "MGM et al. v. Grokster, et al." and "Tasini et al v. AOL" copyright and contract cases; as well as for various First Amendment cases, including for "The Washington Post."  In addition, he is known for having advised President Bill Clinton during the Lewinsky scandal, and representing him during his impeachment trial.  He served as defense attorney in the successful defense of retired General David Petraeus, and currently represents the former Secretary of State, Hillary Clinton, including in the matter of her use of a private email server while serving as U.S. Secretary of State.

Clinton family: The Clinton family is a prominent American political family related to Bill Clinton, the 42nd President of the United States (1993–2001), and his wife Hillary Clinton, the 67th United States Secretary of State (2009–13), Senator from New York (2001–09) and the First Lady of the United States (1993–2001).  Their immediate family was the First Family of the United States from 1993 to 2001.  In 2016, Hillary Clinton became the first female presidential nominee from a major political party in United States history.  The Clintons (Bill and Hillary) are the first married couple to each be nominated for president.  She was defeated in the election by businessman Donald Trump.

Shefali Razdan Duggal: Shefali Razdan Duggal (born November 22, 1971) is an Indian-born American Democratic political activist in San Francisco who is a Presidential Appointee to President Barack Obama to the United States Holocaust Memorial Council, which supervises the United States Holocaust Memorial Museum, for a term expiring in January 2018.  She was an active fundraiser for the Barack Obama election campaign in 2008 where she was a Trustee for the DNC South Asian American Leadership Council.  She focused on South Asian and Young Professional outreach, co-hosting a number of fundraising events for both the Senator and his surrogates.  She was a member of President Barack Obama's National Finance Committee for his reelection campaign in 2012, a co-chair for Obama Victory Trustees, and the Northern California Finance Committee.  She worked on the Massachusetts Democratic Party, New Hampshire Democratic Party, and Senators Ted Kennedy and Dianne Feinstein.  She also worked on the Al Gore presidential campaign in 2000, and Hillary Clinton’s presidential campaign in 2008.

Cheryl Mills: Cheryl D. Mills (born 1965) is an American lawyer and corporate executive.  She first came into public prominence while serving as deputy White House Counsel for President Bill Clinton, whom she defended during his 1999 impeachment trial.  She has worked for New York University as Senior Vice President, served as Senior Adviser and Counsel for Hillary Clinton's 2008 presidential campaign, and is considered a member of Hillary Clinton's group of core advisers, self-designated as "Hillaryland".  She served as Counselor and Chief of Staff to Hillary Clinton during her whole tenure as United States Secretary of State.  After leaving the State Department in January, 2013, she founded BlackIvy Group, which builds businesses in Africa.

Hillary Clinton email controversy: In March 2015, it became publicly known that Hillary Clinton, during her tenure as United States Secretary of State, had used her family's private email server for official communications, rather than official State Department email accounts maintained on federal secure servers.  Those official communications included over 100 emails which contained classified information at the time they were sent, as well as nearly 2,100 emails which were not marked classified but would retroactively be ranked as classified by the State Department.

Electoral history of Hillary Clinton: Electoral history of Hillary Clinton, 67th United States Secretary of State (2009–2013), United States Senator from New York (2001–2009), First Lady of the United States (1993–2001) and a candidate for the 2008 and 2016 Democratic presidential nomination.  Hillary Clinton is one of few politicians who has won the popular vote in every election she was a candidate.

Hillary Clinton's tenure as Secretary of State: Hillary Clinton served as the 67th United States Secretary of State, under President Barack Obama, from 2009 to 2013, overseeing the department that conducted the Foreign policy of Barack Obama.

Question: Hillary Clinton who served as the 67th United States Secretary of State, under President Barack Obama, used what type of email server for official communications, rather than official State Department email accounts maintained on federal secure servers?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person involved."
    },
    "official_role": {
      "type": "string",
      "description": "The official role held by the person at the time of the event."
    },
    "president_served_under": {
      "type": "string",
      "description": "The name of the President under whom the person served."
    },
    "email_server_used": {
      "type": "string",
      "description": "The type of email server used for official communications."
    },
    "official_server_type_avoided": {
      "type": "string",
      "description": "The type of official email server that was not used."
    }
  },
  "required": [
    "person_name",
    "official_role",
    "president_served_under",
    "email_server_used",
    "official_server_type_avoided"
  ],
  "additionalProperties": false
}
