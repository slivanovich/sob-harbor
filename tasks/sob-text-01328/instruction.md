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
Strictly Slots: Strictly Slots is a monthly magazine aimed at slot machine and video poker players.  The magazine was founded in 1998.  Strictly Slots is published by the Casino Player Publishing, which also publishes "Casino Player" magazine.  The magazine include articles about the following: history of slot machine, the principle of slot machine work, new strategies for playing video poker, casino reviews and latest casino news etc.  It features regular articles from notable gambling authors, including:

JoJo Wright: JoJo Wright (“JoJo On The Radio”) is an American radio personality, Internet show host, celebrity commentator, and film actor.  He hosts the Top 40 radio show, “JoJo On The Radio,” which airs on the number one station in Los Angeles, KIIS-FM, and is nationally syndicated in more than 60 markets.  In addition, JoJo co-hosts the MSN Internet show, “Go See This Movie,” and has been a celebrity commentator on numerous shows including: CNN’s “Showbiz Tonight”, MTV’s “US Weekly’s Top 10 Moments of ‘The Hills’ special,” “KTLA Morning News”, “E! News,” and TV Guide specials.  Also, he is featured in two upcoming films, "Battlefield America" and "The Helpers".  He also made a guest appearance as himself on "Big Time Rush".

Robert Caplin: Robert Caplin (born 1983, United States) is an American photographer and cinematographer.  Since 2005, Caplin has photographed over 800 assignments for "The New York Times" and has contributed to and has been published by hundreds of local, national, and international newspapers and magazines including "National Geographic", "Los Angeles Times", "Sports Illustrated", "ESPN The Magazine", "USA Today", "The Sunday Times", "Newsweek", "Time", "Us Weekly", and "Vanity Fair".  In 2010 Caplin spent six months on the road with and documented the international pop singer Justin Bieber and along with HarperCollins, put together Bieber's illustrated biography consisting of Bieber's words and Caplin's photos.  The biography, "Justin Bieber: First Step 2 Forever: My Story" spent 14 weeks on The New York Times Best Seller list and has sold over 1 million copies in 25 languages.  Caplin's video documentation of Bieber on tour was released as part of Paramount Pictures' movie "".

Us Weekly: Us Weekly is a weekly celebrity and entertainment magazine based in New York City.  "Us Weekly" was founded in 1977 by The New York Times Company, who sold it in 1980.  It was acquired by Wenner Media in 1986.  The publication covers topics ranging from celebrity relationships to the latest trends in fashion, beauty, and entertainment.  Along with Jann Wenner, the individuals currently in charge of "Us Weekly" are editor-in-chief James Heidenry and publisher Victoria Lasdon Rose.  As of 2013, its circulation averaged over two million.

Buck Wolf: Buck Wolf is the executive editor of crime and weird news at The Huffington Post, and a former member of the Us Weekly Fashion Police.

Allison Lynn: Allison Lynn (born 1971) is an American novelist.  She is best known for "Now You See It" (Simon & Schuster, 2004), which tells the story of an American woman's disappearance and her husband's search for her.  The novel won the William Faulkner Award and the Bronx Chapter One Prize.  US Weekly named the novel a "hot book pick" in the summer of 2004.

Frank Legato: Frank Legato is an American author born in 1956 in Pittsburgh, PA.  He is best known for his book "How to Win Millions Playing Slot Machines...or Lose Trying".  He is also well known for founding and editing "Casino Gaming" magazine and writing a monthly humorous column about slot machines for "Strictly Slots" magazine.

Ian Drew: Ian Drew is Entertainment Director for American celebrity magazine, Us Weekly.  He speaks about celebrities, music and fashion on television shows including CNN, Good Morning America, The Early Show, MSNBC, and Fox News.  He interviewed Janet Jackson for one of Us Weekly's best-selling issues.

Book Magazine: Book Magazine (later retitled "Barnes & Noble Presents Book") was an American bi-monthly popular literary magazine founded in 1998 by Mark Gleason and Jerome Kramer and published by West Egg Communications.  Described by its editor as "the "Rolling Stone"—not the "Billboard"—of the book industry", "MediaBistro.com" said it was "also the "Us Weekly" of the industry, offering up juicy tidbits of what passes for gossip in this relatively respectable trade", noting for prospective writers that it was aimed at "enthusiastic leisure readers".  The "New York Times" said "Book" "profiles authors and their works in much the way that "People" magazine reports on celebrities".

Cassandra Bankson: Cassandra Bankson (born November 11, 1992) is an American model and online personality from San Francisco, California.  She has been featured on "Good Morning America", "The Today Show", and "The Anderson Cooper Show", among other international television shows.  She has been featured in magazines including "Vogue", "Seventeen", "Glamour", "Forbes", "In Touch Weekly", "Us Weekly", and the cover of "Reveal Magazine" and newspapers "The New York Post", "The Sun", and "Pleasanton Weekly".

Question: Which was founded first Us Weekly or Strictly Slots?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "magazine_comparison": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "magazine_name": {
            "type": "string"
          },
          "founding_year": {
            "type": "integer"
          }
        },
        "required": [
          "magazine_name",
          "founding_year"
        ],
        "additionalProperties": false
      }
    },
    "first_founded_magazine": {
      "type": "string"
    },
    "year_difference": {
      "type": "integer"
    }
  },
  "required": [
    "magazine_comparison",
    "first_founded_magazine",
    "year_difference"
  ],
  "additionalProperties": false
}
