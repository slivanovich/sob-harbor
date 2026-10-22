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
Government of Puntland: The Government of Puntland (Somali: "Dowlada Buntlaand" ) is the supreme governing authority of the semi-autonomous region of Puntland.  The legal structure of Puntland consists of the judiciary, legislative (House of Representatives) and the executive (the President and his nominated council of Ministries) branches of government.  Puntland has conducted four presidential elections (1998, 2004, 2009, 2014).  Presidents are elected by a 66-member unicameral parliament.  Since 1998, the governing bodies have been located in the regional capital of Garowe.

The Roosevelts (film): The Roosevelts: An Intimate History is a 2014 American documentary film directed and produced by Ken Burns.  It covers the lives and times of the Roosevelt family, including Theodore Roosevelt, a Republican and the 26th President of the United States; Franklin D. Roosevelt, a Democrat and the 32nd President of the United States, a cousin of Theodore; and Eleanor Roosevelt, the longest-serving First Lady of the United States, a niece of Theodore who had wed Franklin.  As a result of the influence of Theodore and Franklin as Presidents, as well as Eleanor as First Lady, a modern democratic state of equal opportunity was begun in the United States.  The documentary film begins with the birth of Theodore in 1858 and ends with the death of Eleanor in 1962.

Moumouni Adamou Djermakoye: Moumouni Adamou Djermakoye (May 22, 1939 – June 14, 2009) was a Nigerien politician and the President of the Nigerien Alliance for Democracy and Progress (ANDP-Zaman Lahiya).  He was an important minister during the regime of Seyni Kountché and subsequently served as Niger's Ambassador to the United States from 1988 to 1991; later, after founding the ANDP, he served as President of the National Assembly of Niger from 1993 to 1994.  He was the ANDP's candidate in four presidential elections, beginning in 1993; he was also a deputy in the National Assembly from 1999 to 2009 and the President of the High Court of Justice from 2005 to 2009.

Thomas E. Dewey: Thomas Edmund Dewey (March 24, 1902 – March 16, 1971) was an American lawyer, prosecutor, and politician.  He served as the 47th Governor of New York from 1943 to 1954.  In 1944, he was the Republican Party's nominee for President.  He lost the 1944 election to President Franklin D. Roosevelt in the closest of Roosevelt's four presidential elections.  He was again the Republican presidential nominee in 1948, but lost to President Harry S. Truman in one of the greatest upsets in presidential election history.  Dewey played a large role in winning the Republican presidential nomination for Dwight D. Eisenhower in 1952, and helped Eisenhower win the presidential election that year.  He also played a large part in the choice of Richard M. Nixon as the Republican vice-presidential nominee in 1952 and 1956.

Franklin D. Roosevelt: Franklin Delano Roosevelt ( , his own pronunciation, or ; January 30, 1882 – April 12, 1945), commonly known as FDR, was an American statesman and political leader who served as the 32nd President of the United States from 1933 until his death in 1945.  A Democrat, he won a record four presidential elections and emerged as a central figure in world events during the mid-20th century.  He directed the United States government during most of the Great Depression and World War II.  As a dominant leader of his party, he built the New Deal Coalition, realigning American politics into the Fifth Party System and defining American liberalism throughout the middle third of the 20th century.  He is often rated by scholars as one of the three greatest U.S. Presidents, along with George Washington and Abraham Lincoln.

Manfred Reyes Villa: Manfred Reyes Villa (born April 19, 1954) is a Bolivian politician former military officer and a successful Business man.  He was Elected mayor of the city of Cochabamba four consecutive times, and became the first Elected Governor of the Department of Cochabamba from 2006 until 2008 when his mandate was revoked by an unconstitutional referendum dictated by Evo Morales.  He was the second runner in both for the Presidential elections of the Republic in 2002 and 2009.  Reyes-Villa currently Resides in Washington DC area.  He is the leader of the Opposition to Morales and the preferred candidate for the 2020 Presidential Elections.

Elections in Iowa: The number of elections in Iowa varies from year to year.  Presidential elections are held every four years.  Since 1972, Iowa has been the first state to vote in presidential primaries, with their caucuses.  As with presidential elections, gubernatorial elections are held every four years - but are staggered such that they are held on general elections independently of the presidential election.  Members of the Iowa Senate are elected every four years, with half of the Senate elected at each general election; all members of the Iowa House of Representatives are elected every two years.  Additionally, elections for various government officials, judicial retention elections, and elections on referenda occur as part of various elections in Iowa.

Charles Pinckney (South Carolina chief justice): Charles Pinckney (died October 29, 1758) was a noted South Carolina politician and colonial agent.  He was also the father of two candidates for Vice-President and President.  For four presidential elections in a row, from 1796 to 1808, one of his sons would receive votes in the Electoral College.

Colombian presidential election, 1958: Presidential elections were held in Colombia on 4 May 1958.  They were the first presidential elections since 1949, following a military coup against President Laureano Gómez in 1953.  Following the coup, the two main parties (the Conservative Party and the Liberal Party) came to an agreement on holding office for alternating periods of four years.  The agreement, known as the National Front, was approved in a 1957 referendum.

Presidency of Franklin D. Roosevelt: The presidency of Franklin D. Roosevelt began on March 4, 1933, when he was inaugurated as the 32nd President of the United States, and ended upon his death on April 12, 1945, a span of (4422 days).  Roosevelt assumed the presidency in the midst of the Great Depression.  Starting with his landslide victory over Republican President Herbert Hoover in the 1932 election.  He won a record four presidential terms, and became a central figure in world affairs during World War II.  His program for relief, recovery and reform, known as the New Deal, involved a great expansion of the role of the federal government in the economy.  Under his steady leadership, the Democratic Party built a "New Deal Coalition" of labor unions, big city machines, white ethnics, African Americans, and rural white Southerners, that would significantly realign American politics for the next several decades in the Fifth Party System and also define modern American liberalism.

Question: Which documentary film featured the Democrat who won a record four presidential elections?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "documentary_title": {
      "type": "string",
      "description": "The title of the documentary film."
    },
    "director": {
      "type": "string",
      "description": "The director of the documentary film."
    },
    "featured_president": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the president featured in the documentary."
        },
        "political_party": {
          "type": "string",
          "description": "The political party of the featured president."
        },
        "elections_won_count": {
          "type": "integer",
          "description": "The number of presidential elections won by the featured president."
        }
      },
      "required": [
        "name",
        "political_party",
        "elections_won_count"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "documentary_title",
    "director",
    "featured_president"
  ],
  "additionalProperties": false
}
