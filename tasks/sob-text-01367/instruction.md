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
Abdul Hafeez Kardar: Abdul Hafeez Kardar (Urdu: عبد الحفیظ کاردار ‎ )    or Abdul Kardar (17 January 1925 – 21 April 1996) was an international cricketer, who is one of the only three players to have played Test cricket for both India and Pakistan, the other two being Amir Elahi and Gul Mohammad.  He became the first captain of the Pakistan cricket team and is widely regarded as a father figure of Pakistan's cricket.  He received the Pride of Performance Award from the Government of Pakistan in 1958.

Shoaib Malik: Shoaib Malik (Punjabi, Urdu: ‎ ; born 1 February 1982) is a Pakistani cricketer and former captain of the Pakistani side.  He made his One-Day International debut in 1999 against the West Indies and his Test debut in 2001 against Bangladesh.  On 3 November 2015, he announced his retirement from Test cricket and says his focus is to play in the 2019 Cricket World Cup.

National Stadium, Karachi: The National Stadium (Urdu: نیشنل اسٹڈیم‎ ) is a cricket stadium in Karachi, Pakistan.  It is currently used for cricket matches, it is the home ground of Karachi Kings, Pakistan Super League second expensive team and is home to many other Karachi's domestic cricket teams.  The stadium is able to hold 34,228 spectators, Its widely criticised that the city of this size with a population of over 15 million having such a small capacity stadium.  In the recent past, PCB has announced on different occasions that the capacity of the stadium will be increased to 90,000 but this approval looks a bit stale at the moment.

Anil Dalpat: Anil Dalpat Sonavaria (born September 20, 1963) is the first Hindu ever to play Test cricket for Pakistan.  Dalpat was a lower-order batsman and wicket keeper, and represented Pakistan for a brief interval in the early 1980s, when Wasim Bari was injured.  Dalpat has had a wider first-class cricket experience and career, and is the cousin of Danish Kaneria, Pakistan's first-choice spin bowler and only the second Hindu to play for Pakistan.  He lives in the metropolis of Karachi, and is of Rajasthani heritage.  The first Hindu to play Test cricket for Pakistan, Anil Dalpat was one of several wicketkeepers given a chance after the retirement of Wasim Bari.

Warne–Muralidaran Trophy: The Warne–Muralitharan Trophy is awarded to the winner of the Australia–Sri Lanka Test cricket series from 2007–08 season onwards.  The trophy is named after the two leading wicket takers in Test cricket, Sri Lanka's Muttiah Muralitharan (who prefers to romanise his name as "Muralidaran") and Australia's Shane Warne.  The trophy celebrates the 25th anniversary of Australia–Sri Lanka Test cricket.  The trophy features casts of the two bowlers' right hands and match-used cricket balls bowled by them during their careers.  Sri Lanka Cricket, the governing body of cricket in Sri Lanka had written to its Australian counterpart, Cricket Australia, that the winner of the series should be awarded a trophy named after the two bowlers.  Cricket Australia had responded positively to the Sri Lankans' proposal.  In unveiling the trophy, Cricket Australia said in a statement,

List of Pakistan Test cricket records: Test cricket is the oldest form of cricket played at international level.  A Test match is scheduled to take place over a period of five days, and is played by teams representing Full Member nations of the International Cricket Council (ICC).  Pakistan obtained Full Member status of the ICC in 1952, becoming the seventh nation eligible to play Test cricket.  The Pakistan national cricket team played their first Test match on 16 October 1952 against India which they lost by an innings and 70 runs.  They recorded their first victory in their second ever match against India on 23 October 1952.  Since then, they have played 410 matches, against every other Test-playing nation.  s of 2017 , Pakistan is fourth most successful team in Test cricket with an overall winning percentage of 32.19, ahead of Australia (47.00), South Africa (36.86) and England (35.89).

List of Sri Lanka Test cricket records: Test cricket is the oldest form of cricket played at international level.  A Test match takes place over a period of five days, and is played by teams representing Full Member nations of the International Cricket Council (ICC).  Sri Lanka obtained Full Member status of the ICC in 1981, becoming the eighth nation eligible to play Test cricket.  The Sri Lanka national cricket team played their first Test match on 17 February 1982 against England, and recorded their first victory in a match against India on 6 September 1985.  Since then, they have played nearly 200 matches, against every other Test-playing nation.  Sri Lanka holds the world record for the highest team score, which was established against India in 1997.  The highest partnership in Test cricket was also established by two Sri Lankan batsmen; Mahela Jayawardene and Kumar Sangakkara.  Sri Lankan players also hold the highest partnership scores for the second and third wickets.

Ricky Ponting: Ricky Thomas Ponting, AO (born 19 December 1974), nicknamed Punter, is a former Australian cricketer, and two World Cup winning captain in 2003 and 2007.  Widely regarded as one of the greatest batsmen and captains in the history of cricket, Ponting was captain of the Australia national cricket team during its 'golden era'; between 2004 and 2011 in Test cricket and 2002 and 2011 in One Day International cricket.  He is a specialist right-handed batsman, slips and close catching fielder, as well as a very occasional bowler.  Ponting holds the record of being the only cricketer in the history of Test cricket to be a part of 100 Test match wins.  He was named "Cricketer of the decade 2000".  He led Australia to victory at the 2003 and 2007 Cricket World Cups and was also a member of the 1999 World Cup winning team under Steve Waugh.

Karachi Kings in 2016: The Karachi Kings is a franchise cricket team that represents Karachi in the Pakistan Super League.  They are one of the five teams that had a competition in the 2016 Pakistan Super League.  The team was captained by Shoaib Malik and then by Ravi Bopara, and they stand on fourth position after winning just two matches from their eight matches in the PSL 2016.

Shaiza Khan: Shaiza Said Khan (born March 18, 1969) is a former female cricket player from Pakistan.  She was a member of the national Women's team in Pakistan and the Punjab Women Cricket Team.  Shaiza Khan was the pioneer of Women's Cricket in Pakistan.  She was the first captain of Pakistan Women's ODI and Test matches.  Shaiza Khan is currently a World Record Holder.  She holds the world record for Highest Wickets in a Test Match (13 wickets) against West Indies in 2004 in Karachi.  During her 13 wicket haul she also got a Hatrick which is only the second in women's test history after Betty Wilson. She still holds the record for the best bowling in a test match(13-226)

Question: When did the first captain of the Karachi Kings in 2016 announce his retirement from Test cricket?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person."
    },
    "role": {
      "type": "string",
      "description": "The role of the person in the context of the question."
    },
    "retirement_details": {
      "type": "object",
      "properties": {
        "cricket_format": {
          "type": "string",
          "description": "The format of cricket from which the person retired."
        },
        "retirement_date": {
          "type": "string",
          "description": "The date when the person announced retirement from the specified cricket format."
        }
      },
      "required": [
        "cricket_format",
        "retirement_date"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "person_name",
    "role",
    "retirement_details"
  ],
  "additionalProperties": false
}
