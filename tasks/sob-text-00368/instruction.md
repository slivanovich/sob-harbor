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
Keiichi Kitagawa: Keiichi Kitagawa (北川圭一 , Kitagawa Keiichi , born 24 March 1967 in Kyoto, Kyoto Prefecture) is a retired Grand Prix motorcycle road racer from Japan.  He was runner-up in the 1993 F1 All-Japan Road Racing Championship.  He won the 1998 Superbike World Championship round at Sugo as a wild card rider for Suzuki.  Kitagawa coming 16th in the season's overall standings.  He was a semi-regular in the Superbike World Championship in 1995 , finishing 17th overall with a best finish of 4th, on a Kawasaki.  Kitagawa finished 2nd in the Suzuka 8 Hours race, teamed with Akira Ryo.  He was also a three-time winner of the Bol d'or endurance race.  He retired from racing at the end of 2003, after winning the 2002 and 2003 Endurance World Championship.

Laetitia du Couëdic: Laetitia du Couëdic de Kerérant (born 6 June 1996) is a Franco-Swiss equestrian rider.  Her specialty is show jumping, either individually or as part of a team.  She was Swiss junior champion in Lugano Switzerland in August 2013, a month after she won a gold medal at The European championship (Swiss team) at Vejer de la Frontera Spain.  Laetitia du Couëdic started her official CSI programme in 2015 at the CSI5* in Zurich riding Elisa followed by Cagnes-sur-mer France on her recently acquired (From French Champion Kevin Staut, her mentor) Cheyenne 111 Z HDC.  In October 2013, she won the Grand Prix U25 CSI at Chevenez (JU) and was a wild card entry for the CHI Geneva in Geneva where she was the youngest rider.  Laetitia du Couëdic is ambassador of Hermès, the French Luxury goods maker.  She is also an ambassador of JustWorld international, a charity project.  In 2017 she won the Fontainebleau Grand Prix (CSIOY - Fontainebleau (FRA) (04/05/2017 - 07/05/2017) and was Bronze medal at Swiss championships (young riders).  Laetitia is selected for the Swiss team competing at the European Championships in Samorin (Slovakia)

Jeremy Koling: Jeremy “Big Jerm” Koling is an American disc golfer from Charlotte, NC.  He is a member of the PDGA National Tour, Disc Golf Pro Tour, and Disc Golf World Tour.  Among his most notable accomplishments are his 2008 PDGA Amateur World Championship win and his 2016 United States Disc Golf Championship win.  Koling is the only male player to win the PDGA Amateur World Championships and earn the PDGA Male Rookie of the Year Award in back-to-back years (2008 and 2009).

Maya Jansen: Maya Jansen (27 May 1994) is an American tennis player.  Together with Canadian player, Erin Routliffe, she won the 2014 and 2015 NCAA women's doubles championship as members of the tennis team of the University of Alabama.  She also won the 2015 US Open National playoffs women's doubles championship, earning her a wild card entry to the US Open women's doubles tournament.

Lin Dan: Lin Dan (born October 14, 1983) is a Chinese professional badminton player.  He is a two-time Olympic champion, five-time World champion, as well as a six-time All England champion.

Takehiro Yamamoto: Takehiro Yamamoto (山本 剛大 , Yamamoto Takehiro , born 26 February 1993) is a Japanese motorcycle racer.  He currently competes in the Asia Road Race AP250 Championship aboard a Honda CBR250RR.  He has raced in the GP125 and J-GP3 classes of the All Japan Road Race Championship and in 2015 he was the Asia Road Racing Production 250 champion.  He has also appeared in the 125cc World Championship as a wild card entry.

2007 New York Giants season: The 2007 New York Giants season was the 83rd season for the New York Giants in the National Football League.  The Giants finished the regular season 10–6 and in second place in the NFC East, improving upon their 8–8 record in 2006 in which they finished third in their division.  They qualified for the playoffs as a wild-card team as the #5 seed, and beat the #4 seed Tampa Bay Buccaneers (9–7), the top-seeded Dallas Cowboys (13–3), and the #2 seed Green Bay Packers (13–3) to become the National Football Conference representative in Super Bowl XLII.  There, they defeated the heavily favored and previously undefeated 18–0 New England Patriots and spoiled their perfect season.  The 2007 New York Giants became the 9th wild card team in NFL history to reach the Super Bowl and the 5th wild card team to win the Super Bowl, and the very first NFC wild card to accomplish the feat.  They were the third team in history to win three road playoff games en route to a Super Bowl and set a league record for most consecutive road wins in a single season (11), though the Super Bowl is played on a neutral field rather than an opponent's stadium.  It was the 7th league championship season for the New York Giants and their first since they won Super Bowl XXV in 1991.

Hiromichi Kunikawa: Hiromichi Kunikawa (國川 浩道 , Kunikawa Hiromichi , born 5 November 1981) is a Japanese motorcycle racer.  At national level he has competed in the GP250 and ST600 classes of the MFJ All Japan Road Race Championship.  In 2010 he was signed by Bimota M Racing to replace Niccolò Canepa for the last races of the Moto2 World Championship season.  In 2016 he made a wild card appearance in the Supersport World Championship.  In 2017 he competes in the European rounds of the Supersport World Championship aboard a Honda CBR600RR.

2014 BWF World Championships – Men's singles: The Men's Singles tournament of the 2014 BWF World Championships took place from August 25–31.  Lin Dan was not given wild card entry into the 2014 World Championships, as they did in 2013.

Collin Altamirano: Collin Altamirano is an American tennis player from Yuba City, California.  Altamirano won the 2013 USTA Boys 18 National Championship as an unseeded player, the first ever to do so, and thus earned a wild card entry into the 2013 U.S. Open.  In the final he defeated Jared Donaldson 6-1, 6-2, 6-4.  At the 2013 U.S. Open, Altamirano lost to 22-seed Philipp Kohlschreiber of Germany in the first round.  Prior to the 2013 U.S. Open, Altamirano had only played in six professional-level matches, all at the ITF Men's Circuit level (commonly referred to as Futures), and had lost all six.

Question: How many times did the player who was given a wild card entry to the 2013 World Championship win the World Championship ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_name": {
      "type": "string",
      "description": "The name of the player who received the wild card entry."
    },
    "wild_card_event_year": {
      "type": "integer",
      "description": "The year the player received a wild card entry for a specific championship."
    },
    "wild_card_event_name": {
      "type": "string",
      "description": "The name of the championship for which the player received a wild card entry."
    },
    "sport": {
      "type": "string",
      "description": "The sport the player competes in."
    },
    "world_championship_wins": {
      "type": "integer",
      "description": "The total number of times the player won the World Championship."
    }
  },
  "required": [
    "player_name",
    "wild_card_event_year",
    "wild_card_event_name",
    "sport",
    "world_championship_wins"
  ],
  "additionalProperties": false
}
