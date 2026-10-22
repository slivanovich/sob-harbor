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
Jan Hutchins: Jan Darwin Hutchins (born 1949) is an American TV and radio journalist, producer and media consultant.  Hutchins was born in Danville, Illinois and grew up in Ohio.  He studied at Yale University, graduating with a B.A. in History in 1971.  He started his career in 1972 as a sports journalist at the WIIC TV station in Pittsburgh, Pennsylvania.  After moving to California, Hutchins worked from 1974 to 1990 as a sportscaster on the KPIX TV channel in San Francisco and at KRON (Channel 4).  In 1981, he joined KICU (Channel 36) in San Jose when the San Francisco Bay Area independent television station initiated its news broadcasts, co-anchoring the prime time news program with Ysabel Duron until 1991.  From 1993-1995, Hutchins served as the director of community development for the San Francisco Giants baseball team.  He hosted sports, news and public affairs programs for San Francisco area radio stations (KGO, KCBS, KNBR) and from 1997 to 2000 worked at American Champion Media, which, along with KTEH-TV (Channel 54), produced "Adventures with Kanga Roddy", a children's television series about emotional intelligence that aired on PBS and starred Pat Morita, Jennifer Montana and Karen Lott.  The show won Northern California Area EMMY Awards in 1999 and 2000.  From 1996-1999 Hutchins served on the city council of Los Gatos, CA both as a vice-mayor and mayor and later founded a local yoga center.  He lives currently in San Jose where he works as a media consultant.

Tom Meek: Tom Meek (born 1956) is an American columnist and author of "Another Day In Cyberville" published weekly in The Gainesville Voice, a New York Times regional newspaper, beginning in October, 2000 in The Gainesville Sun.  "Cyberville" deals with issues related to high-tech, computers, New Media and Internet issues.  Meek also writes musical and other occasional features on persons such as trumpeter Wynton Marsalis and American composer Joseph Byrd for publication in print and online, and is the author of online blogs dealing with media and music.  Meek has also served as a media consultant for interests worldwide including the Fox Broadcasting Network, Swedish Televerket and numerous Fortune 500 companies, and is an expert witness certified by the United States Supreme Court on media and copyright issues related to cable television and broadcast television.

Jade: My Autobiography: My Autobiography is a biography written by reality TV star Jade Goody.  It was first published in May 2006 by Harper Collins and a paperback was due for publication in January 2007; however, it never made it to the printers due to Jade being at the centre of minor bad media attention at the time.  The book made it onto The Sunday Times Best Sellers list by December 2006 (only seven months after publication had made Jade nearly £1 million in profits).  In May 2008 (two years after the books publication), Leon Bailey Green, an online media consultant, revealed that the book had sold in excess of 90,000 copies.

Roger Ailes: Roger Eugene Ailes (May 15, 1940 – May 18, 2017) was an American television executive and media consultant.  He was the founder and one-time Chairman and CEO of Fox News and the Fox Television Stations Group, from which he resigned in July 2016 following allegations that he sexually harassed female colleagues.  Ailes was a media consultant for Republican presidents Richard Nixon, Ronald Reagan, and George H. W. Bush, and for Rudy Giuliani's first mayoral campaign.  In 2016, after he left Fox News, he became an adviser to the Donald Trump campaign, where he assisted with debate preparation.

Tim Street: Tim Street is an American writer, producer, director, and new media consultant.  He is one of the pioneers of using the Internet as a story telling device and he is the Creator/Executive Producer of the Popular Viral Video French Maid TV.  CNN referred to Street’s work as “Red Hot”, The Toronto Star said “Prophetic,” Wired News called his first creation, fortheloveofjulie.com, "one of the Internet’s creepiest sites… and one of the most convincing hoaxes to hit the Net."  Street has been elected to sit on the advisory board for the Association for Downloadable Media (ADM), an industry association focused on providing advertising and audience measurement standards for episodic and downloadable media.  In 2009, he was inducted into the International Academy of Web Television.

Jami Bernard: Jami Bernard (born August 10, 1956) is an American author and media consultant, an award-winning film critic for "The New York Post" and "The New York Daily News", and the founder of Barncat Publishing.  She has appeared in documentaries as herself, including the Independent Film Channel's "Indie Sex" series, on which she was a consultant.  Bernard wrote a "Lois Lane" comic for DC Comics in which Lois is based on Bernard's early career at "The New York Post".  Bernard is a frequent guest on TV and radio shows; appearances include on "Oprah", "The Today Show", and "Lynn Samuels" on Satellite Radio.  Her work has been published in numerous magazines, including "Entertainment Weekly", "Seventeen", "Glamour", and "Self".

Russell Schriefer: Russell J. Schriefer is an American political strategist and media consultant who has worked on six out of the last seven presidential campaigns.  In 2012, he was a senior advisor and media consultant on Governor Mitt Romney’s presidential campaign.

Gabriel Sherman: Gabriel Sherman is an American author.  In 2014, he wrote a biography about Fox News Channel president Roger Ailes called "The Loudest Voice in the Room: How the Brilliant, Bombastic Roger Ailes Built Fox News – and Divided a Country", which debuted at #9 on The New York Times Bestseller list.

Rich Cronin (executive): Richard Cronin is a media consultant and former Cable television executive.

Lisa Hickey: Lisa Hickey is an American author, advertising consultant, and social media consultant.  She is the CEO of Good Men Media, Inc. and the Publisher of Good Men Magazine as part of the Good Men Project.

Question: What is the birthdate of this American television executive and media consultant, who was a media consultant and for whom Gabriel Sherman wrote a biography?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The full name of the individual identified."
    },
    "birth_date": {
      "type": "string",
      "description": "The birth date of the individual in 'Month Day, Year' format."
    },
    "primary_roles": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Key professional roles or titles held by the individual, as described in the context."
    },
    "biography_details": {
      "type": "object",
      "properties": {
        "author_name": {
          "type": "string",
          "description": "The name of the author who wrote a biography about the person."
        },
        "book_title": {
          "type": "string",
          "description": "The title of the biography written about the person."
        }
      },
      "required": [
        "author_name",
        "book_title"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "person_name",
    "birth_date",
    "primary_roles",
    "biography_details"
  ],
  "additionalProperties": false
}
