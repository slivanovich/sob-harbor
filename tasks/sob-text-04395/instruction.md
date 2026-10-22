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
Men's 100 metres world record progression: The first record in the 100 metres for men (athletics) was recognised by the International Amateur Athletics Federation, now known as the International Association of Athletics Federations, in 1912.  The record now is 9.58 seconds which was run by Usain Bolt.

1990 IAAF Grand Prix Final: The 1990 IAAF Grand Prix Final was the sixth edition of the season-ending competition for the IAAF Grand Prix track and field circuit, organised by the International Association of Athletics Federations.  It was held on 7 September at the Olympic Stadium (Athens) in Athens, Greece.  Leroy Burrell (100 metres) and Merlene Ottey (200 metres) were the overall points winners of the tournament.  This was Ottey's second series win (having previously won in 1987) and made her the second woman to win the honour twice, after Paula Ivan.  The number of athletics events in the programme reached eighteen for the first time, with ten for men and eight for women.

Angela Williams (sprinter born 1965): Angela Williams (born May 15, 1965 in Laventille, Trinidad) is a retired track and field sprinter.  She began running at age 10 after her family moved to Brooklyn, New York.  A highly recruited high school athlete, she ran first for Tennessee State University, then later Seton Hall University.  She opted to run internationally for her native Trinidad and Tobago, getting her first taste of international competition while still in high school at the 1982 Central American and Caribbean Games, winning a gold medal in the 4x100 metres relay and an individual silver medal in the 200 metres, Later that year she also ran at the 1982 Commonwealth Games, the relay team finishing in 6th place.  The next year she also ran the 200 and anchored the relay at the 1983 Pan American Games, winning a silver medal in the 4 x 100 metres.  And as a 19 year old seasoned veteran, anchored their team in the 4x100 metres relay at the 1984 Olympics.  She also ran in the 100 metres making it to the quarterfinal round, but well behind the three American sprinters, Evelyn Ashford Alice Brown would win the Gold and Silver and later set the world record in the relay.  She was the third fastest Angela in the 100 metres after Canadians Angela Bailey and Angella Taylor.  Four years later she ran in the 1988 Olympics again making it to the quarter final round in the 100 metres before being eliminated behind eventual silver medalist Ashford and again behind Bailey and Taylor now named Issajenko.  In the 200 metres she also made it to the quarter final round.

Willie Williams (athlete): Willie Williams (born September 12, 1931) is a former American sprinter who set the 100 metres world record in 1956, with a new time of 10.1s, one-tenth of second faster than previous record held jointly by 8 men. .

2014 IAAF Hammer Throw Challenge: The 2014 IAAF Hammer Throw Challenge was the fifth edition of the annual, global series of hammer throw competitions organised by the International Association of Athletics Federations.  The winners were Krisztián Pars of Hungary (244.84 metres) and Anita Włodarczyk (232.52 metres) of Poland.  This was Włodarczyk's second title, defending her win from the previous year, and a third career win for Pars (the 2011 and 2012 winner).  Pars also regained the position of challenge record holder, improving on the total set by Paweł Fajdek in 2013.  Włodarczyk was the stand out courtesy of her hammer throw world record of 79.58 m (261 ft floor(((79.58)*3.28084)−(floor((79.58)*3.28084)) *12) in) at the ISTAF Berlin meet.

2015 IAAF Hammer Throw Challenge: The 2015 IAAF Hammer Throw Challenge was the sixth edition of the annual, global series of hammer throw competitions organised by the International Association of Athletics Federations.  The winners were Paweł Fajdek (248.01 metres) and Anita Włodarczyk (235.28 metres), both of Poland.  This was Włodarczyk's third straight title and Fajdek's second title, after his win in 2013.  Fajdek and Włodarczyk each improved the challenge record totals.  Włodarczyk twice broke the hammer throw world record that year, but these marks were achieved outside of the series.

Men's 400 metres world record progression: The first world record in the 400 m for men (athletics) was recognized by the International Amateur Athletics Federation, now known as the International Association of Athletics Federations, in 1912.  The IAAF ratified Charles Reidpath's 48.2 performance set at that year's Stockholm Olympics as a world record, but it also recognized the superior mark over 440 yards (402.34 metres) run by Maxie Long in 1900 as a world record.

Half marathon world record progression: The world record in the half marathon has been officially recognised since 1 January 2004 by the International Association of Athletics Federations (IAAF), the international governing body for the sport of athletics.  A total of five men's world records and six women's world records have been officially ratified since that date.  The IAAF officially recognised the fastest times prior to that date as a "world best" from 1 January 2003 onwards.  Before that date, the IAAF did not recognise any road running world records, though the concept of a world record was recognised by other organisations, such as the Association of Road Racing Statisticians (ARRS).

1987 IAAF Grand Prix Final: The 1987 IAAF Grand Prix Final was the third edition of the season-ending competition for the IAAF Grand Prix track and field circuit, organised by the International Association of Athletics Federations.  It was held on 11 September at the King Baudouin Stadium in Brussels, Belgium.  Tonie Campbell (110 metres hurdles) and Merlene Ottey (100 metres) were the overall points winners of the tournament.

Women's 100 metres world record progression: The first world record in the 100 metres sprint for women was recognised by the Fédération Sportive Féminine Internationale (FSFI) in 1922.  The FSFI was absorbed by the International Association of Athletics Federations (IAAF) in 1936.  The current record is 10.49 seconds set by Florence Griffith-Joyner in 1988.

Question: In what year did Willie Williams set the 100 metres world record that was recorded by the International Association of Athletics Federations?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "athlete_name": {
      "type": "string",
      "description": "The name of the athlete who set the record."
    },
    "event": {
      "type": "string",
      "description": "The athletic event in which the record was set."
    },
    "record_year": {
      "type": "integer",
      "description": "The year the world record was set."
    },
    "recognizing_body": {
      "type": "string",
      "description": "The organization that recognized the world record."
    }
  },
  "required": [
    "athlete_name",
    "event",
    "record_year",
    "recognizing_body"
  ],
  "additionalProperties": false
}
