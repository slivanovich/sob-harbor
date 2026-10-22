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
Juan Carlos Raffo Frávega: Juan Carlos Raffo Frávega (born 30 July 1894, date of death unknown) was a Uruguayan politician.  He was President of the Senate of Uruguay from March 1, 1959 to March 1, 1963.  Raffo Frávega was a member of the National Party (Uruguay).

ReDRagon: reDRagon is a professional wrestling tag team consisting of Bobby Fish and Kyle O'Reilly.  They are currently signed to WWE, where they performs in its developmental branch NXT.  The duo is best known for their work in Ring of Honor (ROH), where they are former three-time ROH World Tag Team Champions, and have also appeared in New Japan Pro Wrestling (NJPW) through ROH's talent exchange partnership, where they are former two-time IWGP Junior Heavyweight Tag Team Champions.

Michael Whalley: Michael D. Whalley (November 16, 1953 – March 1, 2008) was a Republican member of the New Hampshire House of Representatives, representing the Belknap 5th District since 2002, after having served the towns of Bow and Dunbarton since 1992.  He served as the House Republican Leader during the 2007–2008 House session until his death on March 1, 2008.  Whalley had previously served as Vice Chairman of the Resources, Recreation & Development Committee, Vice Chairman and later Chairman of the Election Law Committee, Majority Whip and Deputy Speaker.

Long March 1: The Long March 1 (长征一号), also known as the Changzheng-1 (CZ-1), is the first member of China's Long March 1 (rocket family).

Kyle O'Reilly: Kyle Greenwood (born March 1, 1987) is a Canadian professional wrestler better known by the ring name Kyle O'Reilly, he is currently signed to WWE, where he performs in its developmental branch NXT.  He is best known for his time in with Ring of Honor (ROH).  He also worked for New Japan Pro Wrestling and competed for several independent promotions, most notably Pro Wrestling Guerrilla.  O'Reilly is a former one-time ROH World Champion, three-time ROH World Tag Team Champion alongside Bobby Fish as reDRagon, while in PWG he is a former one-time World Champion and the winner of the promotion's 2013 Battle of Los Angeles.

Pierre Ramampy: Pierre Ramampy (1897 – March 1, 1961) was a politician from Madagascar.  Born in Vohitraveotra, Madagascar in 1897, he served in the French Senate from 1952-1958.  Ramampy died on March 1, 1961 aged 63–64.

John Breaux: John Berlinger Breaux ( ; born March 1, 1944) was a member of the United States Senate from Louisiana from 1987 until 2005.  He was also a member of the US House of Representatives from 1972 to 1987.  He was considered one of the more conservative national legislators from the Democratic Party.  Breaux was a member of the New Democrat Coalition.  After his congressional tenure, he became a lobbyist, co-founding the Breaux-Lott Leadership Group.  The firm was later acquired by law and lobbying firm Patton Boggs, now Squire Patton Boggs.

Clarence Buckman: Clarence Bennett Buckman (April 1, 1851 – March 1, 1917) a Representative from Minnesota; born in Doylestown, Bucks County, Pennsylvania; attended the public and normal schools; moved to Minnesota in 1872 and settled in what is now known as Buckman; engaged in agricultural pursuits and in the lumber business; appointed justice of the peace in 1873; member of the Minnesota House of Representatives 1881 – 1883; served in the Minnesota Senate 1887 – 1891 and 1899 – 1903; elected as a Republican to the Fifty-eighth and Fifty-ninth congresses (March 4, 1903 – March 3, 1907); unsuccessful candidate for renomination in 1906; deputy United States marshal 1912 – 1917; resumed the lumber business in Little Falls, Morrison County, Minnesota; died in Battle Creek, Michigan, March 1, 1917; interment in Oakland Cemetery, Little Falls, Minnesota.

Curtis Shaw: Curtis L. Shaw (March 1, 1888 – February 19, 1944) was mayor of Murray, Utah from 1942-1943.  He was born in Union, Utah March 1, 1888.  He was educated in the Fort Union area and was a farmer up to the time he moved to Murray in 1921.  He was a general construction contractor since 1908 where he built homes as well as two power plants in Murray and one in Bountiful Canyon.  He was a member of the Murray Lions Club for 14 years and was the chapter’s vice president.

Lefty Webb: Lefty Webb (March 1, 1885 – January 12, 1958) was a baseball player for the Pittsburgh Pirates in 1910.  His full name is Cleon Earl Webb.  He was a switch hitter and threw left-handed.  He was 5'11 and 165 pounds.  He went to Ohio Wesleyan University.  He was born on March 1, 1885 in Mount Gilead, Ohio.  He died on January 12, 1958 in Circleville, Ohio.

Question: Which ReDRagon member was born on March 1, 1987 ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person born on the specified date."
    },
    "birth_date": {
      "type": "string",
      "description": "The birth date of the person in YYYY-MM-DD format."
    },
    "team_affiliation": {
      "type": "string",
      "description": "The professional wrestling tag team the person is a member of."
    }
  },
  "required": [
    "person_name",
    "birth_date",
    "team_affiliation"
  ],
  "additionalProperties": false
}
