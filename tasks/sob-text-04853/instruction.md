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
Anna Kournikova: Anna Sergeyevna Kournikova (Russian: А́нна Серге́евна Ку́рникова ; ] ; born 7 June 1981) is a Russian former professional tennis player.  Her appearance and celebrity status made her one of the best known tennis stars worldwide.  At the peak of her fame, fans looking for images of Kournikova made her name one of the most common search strings on Google Search.

Ali Vincent: Alison "Ali" Vincent is the winner of the of the fitness reality television show "The Biggest Loser", which aired in early 2008.  Vincent's in-competition weight loss of 112 pounds earned her a $250,000 prize, and the first win by a female of a United States "The Biggest Loser" season.  Vincent is to be featured as a spokeswoman in print and television advertisements for fitness center chain 24 Hour Fitness, Biggest Loser ProteinG manufactured by Designer Whey and Infinity Insurance.

The Biggest Loser Brunei: Lose It All: The Biggest Loser Brunei (season 3): Lose It All is the third season of The Biggest Loser Brunei, which is the Bruneian version of the NBC reality television series The Biggest Loser.  This season called Lose It All because this is the biggest show of this Brunei's series and to prove to people for keep losing weight weather on the ranch or outside the ranch.  This season premiered March 13, 2012.  This season introduce the new trainer, Cristine Phoebe for replacing Juliana Mikael which not return for her third season.

The Biggest Loser (season 11): The Biggest Loser: Couples 4 is the eleventh season of the NBC reality television series entitled "The Biggest Loser".  The contestants competed to win a $250,000 prize, which was awarded to Olivia Ward, the contestant with the highest percentage of weight loss.  It premiered on January 4, 2011.  Along with existing trainers Bob Harper and Jillian Michaels, two new trainers (Cara Castronuova and Brett Hoebel) will be featured who were revealed in Week 3.  One of the featured contestants is Rulon Gardner, a former gold medalist at the 2000 Summer Olympics.  It was the longest season in Biggest Loser history at 20 weeks long.  This season is the second, after , to be filmed in high definition.  This season marks the first time in USA Biggest Loser history that a contestant left the show by choice.  As well, for the first time in The Biggest Loser history, a couple has made the finale together.  And, for the first time in The Biggest Loser history, all 3 finalists are women.

The Biggest Loser South Africa: The Biggest Loser South Africa is a South African reality television show which first aired from 7 January to 14 April 2008 on e.tv.  The show is a spin-off of the American reality television show "The Biggest Loser".  The South African version features Jasmyn Asvat as the host with trainers Bruce Claasen (Blue team) and Lisa Raleigh (Red team).  The premise of the show is similar to other international versions following the format of "temptation", "reward challenge", "weigh-in" and "elimination".  In addition to the 15 regular episodes, there are an additional 10 episodes of "The Biggest Loser Extra" which focuses on the eliminated contestants.

The Biggest Loser Australia: Couples 2: The fifth season of the Australian version of the original NBC American reality television series "The Biggest Loser", known as The Biggest Loser Australia: Couples 2, premiered on 31 January 2010 on Network Ten.  This season saw Australia's first female Biggest Loser.  41-year-old education assistant Lisa was the winner, dropping 56.2 kg from her 121.9 kg starting weight - or 46.10% - to become the first woman to win the competition.  Also, she is the first contestant to double her prize money since she was crowned The Biggest Loser with the Double bracelet on her wrist.

The Biggest Loser (season 12): The Biggest Loser: Battle of the Ages is the twelfth season of the NBC reality television series entitled "The Biggest Loser".  The contestants competed to win a $250,000 prize, which was awarded to John Rhode, the contestant with the highest percentage of weight lost.  It premiered on September 20, 2011.  Along with existing trainer Bob Harper, two new trainers (Anna Kournikova and Dolvett Quince.)  joined this season.  The 15 contestants this season were divided into three groups of five by their ages: those who are 30 and under were initially trained by Quince, those who are between 31–49 were initially trained by Harper, and those who are 50 and over were initially trained by Kournikova.  This season marked the first time since season 5 that America did not have to vote on who would become a finalist.  For the first time ever in Biggest Loser history, all 3 finalists were men.

The Biggest Loser (season 1): The Biggest Loser (season 1) is the first season of the NBC reality television series entitled "The Biggest Loser", which premiered on October 19, 2004.  The show features overweight contestants competing to lose the largest percentage of their body weight and receive the title of 'Biggest Loser,' along with a $250,000 grand prize.  The first season featured twelve contestants divided into two teams of six players.  The teams were each led by a personal trainer, Bob Harper with the Blue Team and Jillian Michaels with the Red Team.  The first season was hosted by Caroline Rhea.

The Biggest Loser Australia (season 8): The eighth season of the Australian version of the original NBC reality television series "The Biggest Loser", known as The Biggest Loser Australia: The Next Generation, premiered on 17 March 2013 on Network Ten.  This particular season has set a worldwide record, introducing the heaviest contestant in all of "Biggest Loser" history, Kevin Moore.  Kevin along with his mother Rosemary have a combined weight of 355 kg (783 lbs).  He weighs 255 kg (562 lbs) himself alone.  It also featured the youngest contestant ever on the Australian series - Todd Nester, who was 15 years old.  Season 8 of The Biggest Loser was won by the Orange team, Robyn & Katie.

The Biggest Loser Australia: Families: The sixth season of the Australian version of the original NBC reality television series "The Biggest Loser", known as The Biggest Loser Australia: Families, premiered on 30 January 2011 on Network Ten.  This season saw the return of trainers Michelle Bridges, Shannan Ponton and Steve Willis (The Commando).  It also introduced a new female trainer, Tiffiny Hall.

Question: Where was the new female trainer on The Biggest Loser born?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "trainer_name": {
      "type": "string",
      "description": "The name of the new female trainer."
    },
    "season_joined": {
      "type": "string",
      "description": "The season of The Biggest Loser where the trainer joined."
    },
    "trainer_role": {
      "type": "string",
      "description": "The role of the individual in the show."
    },
    "country_of_origin": {
      "type": "string",
      "description": "The country where the trainer was born or is from."
    }
  },
  "required": [
    "trainer_name",
    "season_joined",
    "trainer_role",
    "country_of_origin"
  ],
  "additionalProperties": false
}
