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
Aimee Chan: Aimee Chan (born 1 April 1981) or Chan Yan-mei (Traditional Chinese: 陳茵媺) is a Canadian actress based in Hong Kong.  She was the winner of Miss Hong Kong 2006 and was offered a TVB contract shortly after.

Miss Hong Kong 2009: The Miss Hong Kong 2009 pageant, the 37th Miss Hong Kong pageant was held in the Hong Kong Coliseum on August 22, 2009.  Ten delegates completed for the title.  The winner was Sandy Lau and she competed at Miss World 2010, but not Miss Chinese International 2010, because the pageant was postponed until after Sandy Lau crowned her successor.  The first runner-up was Germaine Li, and she represented Hong Kong in the Miss International 2010 pageant.  The second runner-up was Mizuni Hung.

Slow Boat Home: Slow Boat Home (Chinese: 情越海岸線; literally "love exceeds the coastline") is a 2013 Hong Kong romantic comedy television drama produced by Leung Choi-yuen and TVB, starring Raymond Wong Ho-yin, Ruco Chan and Aimee Chan.  The show was conceived in late 2011 by Leung, who aspired to write a youthful television drama for the aging TVB.  "Slow Boat Home" was produced at 25 episodes, and the first episode premiered on TVB Jade on 13 May 2013.

Olivia Cheng: Olivia Cheng (Chinese: 鄭文雅, Pinyin: Zheng Wenya), born 14 February 1960, is a Hong Kong based former actress.  She won the 1979 Miss Hong Kong Pageant and was also elected "Miss Photogenic."  She represented Hong Kong in Miss Universe 1979 in Perth, Western Australia, where she went unplaced but ranked a very respectable 21st place in the preliminary swimsuit competition.  Olivia created a controversy when she joined ATV (the arch-rival of TVB, the organiser of the Miss Hong Kong pageant) immediately after crowning her successor in 1980.  This incident embarrassed TVB so much that in 1981, TVB decided to sign 1.5-year contracts with all Miss Hong Kong winners so that they had to stay with TVB for at least 6 months after their reign was over.

Hoyan Mok: Hoyan Mok (莫可欣) was the winner of the 1993 Miss Hong Kong Pageant and a TVB Hong Kong actress.  She beat Kenix Kwok, who was considered a favourite to win, having won two side awards including Media's Favourite and Potential Artist.  She is Alex Fong Chung-Sun (方中信)'s wife, and has a daughter named Ka Ching.  As Miss Hong Kong, she also competed at the Miss Universe 1994 pageant.  She placed 45th at the pageant, same as her successor Halina Tam.  Mok also competed at the Miss Chinese International Pageant 1994 where she made the top 10 only, becoming the first Miss Hong Kong to not place in the top 3.

Miss Hong Kong 2008: Miss Hong Kong 2008 The 36th Miss Hong Kong Pageant which was televised live internationally from the Hong Kong Convention and Exhibition Centre on 19 July 2008.  Twenty-two-year-old Edelweiss Cheung became the new Miss Hong Kong and the tallest Miss Hong Kong, in the history of the paeant.  Skye Chan the first runner-up and replaced Edelweiss during her duties due to Edelweiss not showing up.  Skye Chan represented Hong Kong in Miss World 2008, and Miss Chinese International 2009.  Second runner-up Sire Ma represented Hong Kong at Miss International 2008

Lee San-san: Lee San-San (, born 9 October 1977, was the winner of the 1996 Miss Hong Kong Pageant and her territory's representative at Miss Universe 1997.  Lee placed 45th at that pageant like former Miss Hong Kongs, Mok Hoi Yan and Halina Tam.  She also competed at the Miss Chinese International 1997 pageant where she finished 2nd.  She signed with TVB, and starred in various Hong Kong television dramas, before leaving the network.  She is a Hakka of Meixian ancestry.

Koni Lui: Koni Lui (呂慧儀) (born 3 September 1982 in Hong Kong) also known as Koni Lui Wai Yee is a model and 2nd runner up at the Miss Hong Kong 2006 pageant.  She represented Hong Kong at Miss International 2006 in Tokyo, Japan and Beijing, China.  She received 2 awards, Most Beautiful Smile and the Miss Friendship award.  She continued the friendly streak as Hong Kong had won four Miss Friendship titles (1981, 2002, 2004, and 2005).  With her win, Hong Kong is tied with Japan as the only nations at Miss International to win more than 4 Miss Friendships and at any international pageant.

Selena Lee (actress): Selena Lee Sze-wa (born 12 February 1981) is a Hong Kong-born Canadian actress and former Miss Hong Kong 2003 contestant.  That year, as a contestant from Toronto, Selena was the winner of Miss Talent and Miss Photogenic.  Prior to entering the Miss Hong Kong pageant, Selena attended the University of Toronto studying for a Bachelor of Business Commerce degree.  She is now an actress with TVB in Hong Kong.  She can speak Cantonese, English, Mandarin.

Miss Hong Kong 2007: Miss Hong Kong 2007 pageant, the 35th Miss Hong Kong pageant was held in the Hong Kong Coliseum on 21 July 2007.  Sixteen delegates competed for the title.  Contestant #3: Kayi Cheung was crowned the winner by outgoing titleholder, Aimee Chan.

Question: Which Miss Hong Kong winner starred in the television drama Slow Boat Home?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actress_name": {
      "type": "string",
      "description": "The name of the actress who starred in the drama."
    },
    "miss_hong_kong_winner_year": {
      "type": "integer",
      "description": "The year the actress won the Miss Hong Kong pageant."
    },
    "drama_title": {
      "type": "string",
      "description": "The title of the television drama."
    },
    "drama_production_year": {
      "type": "integer",
      "description": "The year the television drama was produced."
    }
  },
  "required": [
    "actress_name",
    "miss_hong_kong_winner_year",
    "drama_title",
    "drama_production_year"
  ],
  "additionalProperties": false
}
