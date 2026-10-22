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
Dan Bull: Daniel G. L. "Dan" Bull (born 27 March 1986 in Bromsgrove, England) is an English rapper and songwriter known best for his raps about video games, which he publishes on his YouTube channel, Dan Bull.  His videos feature him playing various games with fellow artist Dave Brown and fellow YouTube personalities such as Michelle 'The RPG Minx', Markiplier, and Adam Montoya.  Bull's music was featured in the British press as part of attempts to save BBC Radio 6, campaign against the Digital Economy Bill, and protest in favour of filesharing.  He has Asperger's syndrome, which is referenced in some of his raps, such as "A Portrait of The Autist".

Gold (Ricky Dillon album): Gold (stylized as G O L D), is the debut studio album by American YouTube personality Ricky Dillon, released on January 15, 2016.  The album features the singles, "Steal the Show" featuring American singer and YouTube personality Trevor Moran and "Problematic" featuring American rapper Snoop Dogg.

Roman Atwood: Roman Bernard Atwood (born May 28, 1983) is an American YouTube personality, comedian, vlogger and pranker.  He is best known for his vlogs, where he posts updates about his life on a daily basis.  His vlogging channel, "RomanAtwoodVlogs", has a total of 3.6 billion views and 13 million subscribers.  The channel is currently the 50th most subscribed channel on YouTube.  He also has another YouTube channel called "RomanAtwood", where he posts pranks.  His prank videos have gained over 1.4 billion views and 10.4 million subscribers.  Both of these channels are in the top 100 most subscribed on YouTube, and he became the second YouTuber after Germán Garmendia to receive two Diamond Play Buttons for his two channels.

Markiplier: Mark Edward Fischbach (born June 28, 1989), known online as Markiplier, is an American YouTube personality.  Originally from Honolulu, Hawaii, he began his career in Cincinnati, Ohio, and is currently based in Los Angeles, California.

Lilly Singh: Lilly Singh (born 26 September 1988) is a Canadian YouTube personality, vlogger, comedian, writer, and actress.  She is better known by her YouTube username IISuperwomanII.  Since beginning her channel in October 2010, her videos have received over 2 billion views, and her channel has accumulated over 12 million subscribers.  In 2016, she was ranked 3rd on the "Forbes" list of the world's highest paid YouTube stars (behind Roman Atwood and PewDiePie), earning a reported $7.5 million in 2016.  Singh has featured in the annual YouTube Rewind every year since 2014.  She ranked 1st on 2017 Forbes Top Influencers List in the entertainment category.

Wengie: Wendy Ayche (born January 9 1986) known professionally as Wengie, is an Australian YouTube personality and vlogger.  She was born in Guangzhou, China.  She got the nickname "Wengie" at a dance class when two people gave her a nickname inspired by her Chinese name, Wén Jié.  Since starting her channel on February 11 2013, her videos have received over 281 million views, and her channel has accumulated over 11 followers In the January 2016 edition of "ElleGirl Japan", she was nominated as a channel to watch.  In August 2016, she was ranked the 5th Fastest growing channel in the world.  Ayche was featured in the annual YouTube Rewind in 2016 and was also singled out by Google as one of the top beauty creators in the Asia region.  Ayche reached 5 million YouTube subscribers in January 2017, and her channel is currently in the 12th most subscribed How-To & Style Channel on YouTube.  She is also currently a board member of the Internet Creators Guild, a non-profit focused on providing the protection, representation and guidance to online creators.  Her YouTube channel also recently got awarded with "Best Channel" as well as "Overall Winner" for the Australian Online Video Awards.

Joey Graceffa: Joseph Michael Graceffa ( ; born May 16, 1991) is an American YouTube personality, actor, author, producer, and singer.  He has two active YouTube channels, both of which are named after him.  One of them is for vlogging and the other is used for video gaming content.  They both have a combined total of more than 1.7 billion views.  His other YouTube channel, which he no longer uses, called WinterSpringPro, has 60 million views (as of August 2017).  He was a contestant on 22nd and 24th seasons of "The Amazing Race" and has appeared in short films (as web films) and short web television series on YouTube and its subscription-only service YouTube Red.

Skylar Kergil: Skylar Kergil (born May 19, 1991) is an American transgender activist, singer-songwriter, public speaker, YouTube personality, and artist.  Kergil has been documenting his transition from female-to-male on YouTube since 2009, and in doing so helping to educate viewers about gender identity, hormones, surgeries, and life.  As of April 2016, he has over 100,000 YouTube subscribers and over 9 million views.  He began taking testosterone and putting videos on YouTube while attending Acton-Boxborough Regional High School and continued making videos while he was a student at Skidmore College.  Kergil currently resides in Cambridge, MA while continuing to make regular YouTube updates and pursuing his music and speaking opportunities.

Ryan Higa: Ryan Higa (born June 6, 1990), also known by his YouTube username nigahiga ( ), is an American comedian, YouTube personality, and actor.  He is known for his comedy videos on YouTube, which have been viewed over 3 billion times.  Higa's YouTube channel, nigahiga, was the most subscribed channel on YouTube for 677 consecutive days from 2009–2011, longer than any other channel besides PewDiePie.  s of 2017 , he has over 20 million subscribers, making his channel the 20th most subscribed on YouTube.

Adande Thorne: Adande Thorne, known by his YouTube username Swoozie (stylized sWooZie), is a Trinidadian-born YouTube personality.  As of July 2017, his YouTube channel has more than 700 million views.  As a professional gamer he competed in "Dead or Alive 4" for the Los Angeles Complexity in the Championship Gaming Series and the reality series "WCG Ultimate Gamer".  In 2015, he signed with the Creative Artists Agency.  In January 2016, he was one of three people who interviewed President Barack Obama during a YouTube livestream.  In 2017, he had a minor role in the film "The Space Between Us".

Question: What is the name of the YouTube personality that is originally from Honolulu, Hawaii?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "youtube_personality_name": {
      "type": "string",
      "description": "The online name of the YouTube personality."
    },
    "full_name": {
      "type": "string",
      "description": "The full given name of the YouTube personality."
    },
    "original_location": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city where the personality is originally from."
        },
        "state": {
          "type": "string",
          "description": "The state where the personality is originally from."
        }
      },
      "required": [
        "city",
        "state"
      ],
      "additionalProperties": false
    },
    "current_base_location": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city where the personality is currently based."
        },
        "state": {
          "type": "string",
          "description": "The state where the personality is currently based."
        }
      },
      "required": [
        "city",
        "state"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "youtube_personality_name",
    "full_name",
    "original_location",
    "current_base_location"
  ],
  "additionalProperties": false
}
