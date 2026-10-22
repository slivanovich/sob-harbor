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
Dinerral Shavers: Dinerral "Dick" Shavers (born c. 1981, died 28 December 2006) was a jazz drummer and educator from New Orleans, Louisiana.  Shavers was best known musically as a founding member of the Hot 8 Brass Band.  He also taught at a local high school and created music programs for poor local youths.  He appeared in the Spike Lee film "When the Levees Broke" discussing the devastation of his family home in the Lower 9th Ward.

When the Levees Broke: When the Levees Broke: A Requiem in Four Acts is a 2006 documentary film directed by Spike Lee about the devastation of New Orleans, Louisiana following the failure of the levees during Hurricane Katrina.  It was filmed in late August and early September 2005, and premiered at the New Orleans Arena on August 16, 2006 and was first aired on HBO the following week.  The television premiere aired in two parts on August 21 and 22, 2006 on HBO.  It has been described by Sheila Nevins, chief of HBO's documentary unit, as "one of the most important films HBO has ever made."  The title is a reference to the blues tune, "When the Levee Breaks", by Kansas Joe McCoy and Memphis Minnie, about the Great Mississippi Flood of 1927.

David Blair (rugby union): David Blair, (born 14 July 1985) was a Scottish rugby union player who played Stand Off and played for Sale Sharks from 2003-2007 and then Edinburgh Gunners in the Magners League from 2007- 2011.  David was captain and highest points scorer for Scotland Under 21 ever.  He is the younger brother of Scotland captain Mike Blair who also plays for Edinburgh.  David Blair started at Sale Sharks and then moved to Edinburgh to join up with his brother.  David has also represented Scotland A team on several occasions.

Pledge Across America: The synchronized Pledge Across America is conducted each year on September 17th - Constitution Day.  Pledge Across America is the nationally synchronized recitation of the Pledge of Allegiance in schools.  In 2001 shortly after September 11 the President of the United States and the United States Secretary of Education and both the United States Senate and House of Representatives joined over 52 million students in the synchronized Pledge of Allegiance to the flag.  September 17, 2008 marked the 17th year the Pledge Across America takes place, and it also marked 117 years since Francis Bellamy wrote and first recited the Pledge of Allegiance in 1892.

Spoons Across America: Spoons Across America is a national non-profit organization founded in 2001 providing children's food, nutrition, education, and networking for providers.  Spoons Across America is a member of America's Charities.

Captain Mike Across America: Captain Mike Across America is a film written, directed and narrated by Michael Moore.  It was filmed prior to the 2004 election, when the polling margin between candidates George W. Bush and John Kerry could have tipped either way.  It debuted at the Toronto International Film Festival on September 7 and 8, 2007.  The film was re-edited by Moore into "Slacker Uprising", which was released for free on the Internet on September 23, 2008.

John Gore (theater producer): John Gore (born 1962) is the sole owner, Chairman and Chief Executive Officer of The John Gore Organization formerly known as Key Brand Entertainment, Inc. (KBE), a leading developer, producer, and distributor of live theatre in North America.  Gore founded KBE in 2004 to develop theatrical properties in the US.  Broadway Across America (BAA) was acquired in January 2008, from the music company Live Nation, while the e-commerce theatre website Broadway.com was acquired in December 2010, from Hollywood Media Corp.  In 2008, Broadway Across America and Broadway Across Canada sold over 6.4 million tickets throughout its 40 theatres in the United States and Canada.

Australian cricket team in Australia in 1974–75: The 1974–75 Australians beat the touring England team 4–1 in the 1974-75 Ashes series.  Labelled the "Ugly Australians" for their hard-nosed cricket, sledging and hostile fast bowling they are regarded as one of the toughest teams in cricket history.  Don Bradman ranked them just after his powerful teams of the late 1940s, and Tom Graveney third amongst post-war cricket teams after the 1948 Australians and 1984 West Indians.  The spearhead of the team was the fast-bowling duo of Dennis Lillee, whose hatred of English batsmen was well known, and Jeff Thomson, who outraged old fashioned cricketers by saying he liked to see "blood on the wicket". " Wisden" reported that "never in the 98 years of Test cricket have batsmen been so grievously bruised and battered by ferocious, hostile, short-pitched balls".  "Behind the batsmen, Rod Marsh and his captain Ian Chappell would vie with each other in profanity", but the predatory wicketkeeper and Australian slip cordon snapped up most chances that came their way.  Their batting line up was also impressive with the opener Ian Redpath spending over 32 hours at the crease in the series, followed by Rick McCosker, Ian and Greg Chappell, Doug Walters and Ross Edwards.  Ironically, in the last Test of the series Lillee and Thomson were injured, the out of form England captain Mike Denness made 188 and England won by an innings.

Swim Across America: Swim Across America Inc., (SAA) is a non-profit 501(c)(3) organization that is dedicated to raising money and awareness for cancer research, prevention and treatment by hosting open water and pool benefit swim events across the US.  SAA, whose events often include Olympians such as Michael Phelps, Jenny Thompson and Dara Torres, has raised over $65 million since its inception.  Money raised by SAA supports world-renowned hospitals, laboratories and clinics, including the Swim Across America lab at Memorial Sloan-Kettering Cancer Center, which played a key role in developing the first drug to treat metastatic melanoma approved by the FDA in 13 years.  Swim Across America’s events are community oriented and attract swimmers of all ages and skill levels.  SAA has been sponsored by corporate giants such as Verizon, Speedo, Balance Bar, Bank of America and Chobani.

Slacker Uprising: Slacker Uprising is a movie of Michael Moore's tour of colleges in swing states during the 2004 election, with a goal to encourage 18- to 29-year-olds to vote, and the response it received.  The film is a re-edited version of "Captain Mike Across America", which played at the Toronto International Film Festival in 2007.

Question: Was When the Levees Broke filmed after Captain Mike Across America?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_comparison_result": {
      "type": "boolean",
      "description": "True if 'When the Levees Broke' was filmed after 'Captain Mike Across America', false otherwise."
    },
    "film_1_name": {
      "type": "string",
      "description": "The name of the first film mentioned in the question."
    },
    "film_1_filming_period": {
      "type": "string",
      "description": "The period when the first film was filmed."
    },
    "film_2_name": {
      "type": "string",
      "description": "The name of the second film mentioned in the question."
    },
    "film_2_filming_period": {
      "type": "string",
      "description": "The period when the second film was filmed."
    },
    "reasoning": {
      "type": "string",
      "description": "Explanation of the chronological comparison between the two films' filming periods."
    }
  },
  "required": [
    "film_comparison_result",
    "film_1_name",
    "film_1_filming_period",
    "film_2_name",
    "film_2_filming_period",
    "reasoning"
  ],
  "additionalProperties": false
}
