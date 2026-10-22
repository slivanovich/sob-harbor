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
Mary Nolan (politician): Mary Nolan (born 1954) is a Democratic politician from the U.S. state of Oregon.  She represented District 36 (formerly District 11) in the Oregon House of Representatives from 2001 to 2013, and served as the majority leader from 2008-2010.  She ran unsuccessfully for the Portland City Council in 2012.

Sharron Angle: Sharron Elaine Angle (born Sharron Elaine Ott; July 26, 1949) is an American politician who served as a Republican member of the Nevada Assembly from 1999 to 2007.  She ran unsuccessfully as the 2010 Republican nominee for the U.S. Senate seat in Nevada, garnering 45 percent of the vote.  On September 15, 2013 she was unanimously elected the fifth President of the National Federation of Republican Assemblies, and resigned in 2016 to run again for the Nevada U.S. Senator position being vacated by Harry Reid but failed to win the Republican primary.

United States Senate election in Nevada, 2010: The 2010 United States Senate election in Nevada took place on November 2, 2010.  Incumbent Democratic U.S. Senator and Majority Leader Harry Reid won re-election to a fifth term.

Francine Busby: Francine Pocino Busby (born March 3, 1951) is a former member of the school board in Cardiff, California and is the chair of the San Diego County Democratic Party.  She has four times been the Democratic candidate for Congress in California's 50th congressional district, in North San Diego County.  In 2004 she ran unsuccessfully against incumbent Republican Congressman Randy "Duke" Cunningham.  Before his term was up Cunningham resigned due to his conviction on bribery charges, and she ran in the June 2006 special election to replace him; she lost to Republican Brian Bilbray, who again defeated her in the 2006 general election that November.  She also ran unsuccessfully against Bilbray in 2010.

Joseph P. Monaghan: Joseph Patrick Monaghan (March 26, 1906 – July 4, 1985) of Butte, Montana was a U.S. Representative from Montana from 1933 to 1937.  He was a Democrat.  In 1936 he decided not to run for reelection and instead challenged Democratic incumbent United States senator James E. Murray in the Democratic primary.  When Murray won, Monaghan ran in the general election as an independent.  Murray soundly defeated Monaghan and Republican T.O. Larsen.  Murray received 55% of the vote, Larsen 27% of the vote and Monaghan 18%.  At the age of 30, Monaghan's political career came to an end.  He returned to his law practice, and returned to politics only briefly in 1964 when he ran for the Democratic nomination unsuccessfully for the United States Senate in Montana, against Senate Majority leader Mike Mansfield.

Dick Gephardt: Richard Andrew Gephardt (born January 31, 1941) is an American politician who served as a United States Representative from Missouri from 1977 to 2005.  A member of the Democratic Party, he was House Majority Leader from 1989 to 1995 and Minority Leader from 1995 to 2003.  He ran unsuccessfully for the Democratic nomination for President of the United States in 1988 and 2004.  Gephardt was mentioned as a possible vice presidential nominee in 1988, 1992, 2000, 2004, and 2008.

Paul Policastro: Paul Policastro (August 29, 1900 – November 4, 1981) was an American Democratic Party politician who served five terms in the New Jersey General Assembly.  He was a graduate of Lafayette College and Rutgers Law School and served in the U.S. Army during World War II.  He served on the Newark Board of Adjustment from 1953 to 1954.  He first ran for the State Assembly in 1959, but lost.  He ran again in 1961 and won.  He was re-elected in 1963, 1965, 1967, and 1969.  He served as Assistant Majority Leader in 1966 and as Majority Leader in 1967.  Had Democrats not lost the majority in the 1967 election, Policastro was expected to become Assembly Speaker.  In 1971, Policastro lost his bid for re-election to a fifth term, losing to an independent candidate, Newark vigilante leader Anthony Imperiale.  Imperiale received 13,857 votes, followed by Policastro's running mate, incumbent Democratic Assemblyman Frank Megaro with 12,436 votes.  Policastro ran third with 10,825 votes, followed by incumbent Republican Assemblyman C. Richard Fiore with 8,215 votes and Republican challenger Ralph D'Ambola with 7,351 votes.

Michael Shane Neal: Michael Shane Neal (born November 23, 1968) is an American portrait artist.  Neal has created official portraits for the United States Capitol of U.S. Senator Arthur Vandenburg, former Majority Leader and U.S. Senator Robert C. Byrd, 10th Architect of the Capitol Alan Hantman, and over 400 works of art depicting various public figures.  Recent current commissions include Supreme Court Justice Sandra Day O'Connor for the Sandra Day O'Connor School of Law at Arizona State University, former Secretary of Energy Spencer Abraham for the Department of Energy, and U.S. Senator Arlen Specter for Yale Law School.

David Holcomb: David Holcomb was a U.S. State Senator in the Ohio Senate.  He served from January 3, 1967 – December 31, 1972.  In 1970, he ran unsuccessfully for the Republican nomination for U.S. Senator.

Bob Kunst: Bob Kunst (a.k.a. Robert Kunst) is one of America's leading human rights and civil rights activists, he is also known as an anti-Nazi and anti-KKK activist.  Born in 1941, a native of Miami Beach, Florida, Kunst spent much of his adult life since the early 1960s in civil rights activism for African-Americans, Women, LGBT people, especially in the 1976 Miami-Dade County Ordinance for Gay Rights which was passed to protect the civil rights of Lesbians and Gays, and Bisexuals, and later Kunst was involved in activism for people with AIDS.  Kunst was active to opposed Save Our Children, a Dade County, Florida voter-approved county initiative supported by singer Anita Bryant and her then-husband Bob Green, the initiative repealed the previous anti-discrimination ordinances Kunst fought for in employment, especially in public education teaching, and housing based on Sexual Orientation, but this law was eventually repealed by the state Supreme Court of Florida in 2010.  Kunst later became more involved in Gay Rights activism in the United States ever since.  As a Democratic Party politician, Kunst unsuccessfully campaigned against Republican Bob Graham in the 1986 United States Senate elections in Florida.  Kunst also ran unsuccessfully in the 2010 United States House of Representatives Election, this time as an unaffiliated independent, against incumbent Rep. Debbie Wasserman Schultz, a Democrat, in the State of Florida.  Kunst volunteered for the Hillary Rodham Clinton 2008 U.S. presidential campaign in his hometown of Miami, Florida.  Kunst was president (1991-2001) of Shalom International, a Jewish group combating global Neo-Nazism and Neo-fascism movements.  And he was a co-founder of the Oral Majority in 1982, the Liberal and secular counter-protest group of the Religious Right organizations Moral Majority and later the Christian Coalition.  Outside of political causes, Kunst worked in marketing for the Miami Toros professional soccer team in the 1970s.

Question: In 2010, Sharron Angle ran unsuccessfully against which U.S. Senator and Majority Leader?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "candidate_name": {
      "type": "string",
      "description": "The name of the candidate who ran unsuccessfully."
    },
    "election_year": {
      "type": "integer",
      "description": "The year the election took place."
    },
    "opponent": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the opponent."
        },
        "political_party": {
          "type": "string",
          "description": "The political party of the opponent."
        },
        "roles": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Key roles held by the opponent at the time of the election."
        },
        "election_result": {
          "type": "string",
          "description": "The outcome for the opponent in the election."
        }
      },
      "required": [
        "name",
        "political_party",
        "roles",
        "election_result"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "candidate_name",
    "election_year",
    "opponent"
  ],
  "additionalProperties": false
}
