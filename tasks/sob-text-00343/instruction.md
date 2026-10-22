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
NY Nunca Duerme Reality Show: Ny Nunca Duerme translated as "The City that never sleeps" is a reality show based in the Hispanic community of New York.  This show is about six women that are trying to make it in their respective career in the city that never sleeps.  This show was first aired April 1, 2016 on Telemicro Internacional a Dominican television station seen in the United States by cable carriers Direct TV and Time Warner Cable.

Talk Soup: Talk Soup is a television show produced for cable network E! that debuted on January 7, 1991, and aired until August 2002.  "Talk Soup" aired selected clips of the previous day's daily talk shows—ranging from daytime entries like "The Jerry Springer Show" and to celebrity interview shows like "The Tonight Show"—surrounded by humorous commentary delivered by the host.  Although "Talk Soup" poked fun at the talk shows, it also advertised the topics and guests of upcoming broadcasts.  Despite this, several talk shows, including "The Oprah Winfrey Show", refused to allow clips of their shows to be shown on the series.  During its run, "Talk Soup" was nominated for five Daytime Emmy Awards, winning once in 1995 for Outstanding Special Class Program.  It remains the only E! show to ever win an Emmy.  A show based on it, "The Soup", aired from 2004 to 2015.

Big Brother (Thai TV series): Big Brother is the Thai version of the "Big Brother" reality television show based on the Dutch television series of the same name originally created by John de Mol in 1997.  It is shown on iTV and TrueVisions channel 20. The show follows a group of House Guests living together 24 hours a day in the "Big Brother" house, isolated from the outside world but under constant surveillance with no privacy for three months.In 2 seasons of the show, 27 different people have entered the Big Brother house so far.  Since its debut in 2005, Big Brother Thailand has run continuously with at least one season of the show airing each year, Big Brother was renewed for a 2nd season.

Islands (miniseries): Islands is an American animated miniseries based on the show "Adventure Time" by Pendleton Ward.  It aired as part of the show's eighth season on Cartoon Network from January 30, 2017, to February 2, 2017.  "Adventure Time" follows the adventures of Finn (voiced by Jeremy Shada), a human boy, and his best friend and adoptive brother Jake (voiced by John DiMaggio), a dog with magical powers to change shape, grow and shrink at will.  In this limited event series, Finn, Jake, BMO (voiced by Niki Yang) and Susan Strong (voiced by Jackie Buscarino) leave Ooo and travel across the ocean to solve the mystery of Finn's past.  During their trip, they encounter various creatures, new friends, and a variety of mysterious islands.  The trip culminates with a visit to Founder's Island, where Finn meets his biological mother, Minerva Campbell (voiced by Sharon Horgan), and discovers what happened to the remainder of the human race.

The Contender Australia: The Contender Australia is a reality television show based on the sport of boxing, but with an added element of insight into the competitor's lives and relationships with each other within the show's living quarters.  The series was filmed in Sydney, Australia and was first aired on Australian Pay-Television channel Fox8 on 3 November 2009.  The winner will win the Contender Australia title and a A$250,000 prize-"fight" with Anthony Mundine.

List of Adventure Time episodes: "Adventure Time" is an American animated television series created by Pendleton Ward for Cartoon Network.  The series follows the adventures of Finn (voiced by Jeremy Shada), a human boy, and his best friend and adoptive brother Jake (voiced by John DiMaggio), a dog with magical powers to change shape and grow and shrink at will.  Finn and Jake live in the post-apocalyptic Land of Ooo.  Throughout the series, they interact with the show's other main characters: Princess Bubblegum (voiced by Hynden Walch), the sovereign of the Candy Kingdom; the Ice King (voiced by Tom Kenny), a demented but largely misunderstood ice wizard; Marceline the Vampire Queen (voiced by Olivia Olson), a thousand-year-old vampire and rock music enthusiast; Lumpy Space Princess (voiced by Ward), a melodramatic and immature princess made out of "irradiated stardust"; BMO (voiced by Niki Yang), a sentient video game console-shaped robot that lives with Finn and Jake; and Flame Princess (voiced by Jessica DiCicco), a flame elemental and ruler of the Fire Kingdom.  The pilot first aired in 2007, and it was later re-aired on the incubator series "Random!  Cartoons" on Nicktoons Network.  The pilot eventually leaked onto the internet and became a cult hit on YouTube.  After Nickelodeon declined to turn the short into a full-fledged show, Cartoon Network purchased the rights, and "Adventure Time" launched as a series on April 5, 2010.

First Dates (U.S. TV series): First Dates is an American reality television show based on the British version of the show of the same name.  It first aired on the NBC network on April 7, 2017.  Ellen DeGeneres is the executive producer and Drew Barrymore narrates.

Stakes (miniseries): Stakes is an American animated miniseries based on the show "Adventure Time" by Pendleton Ward.  It aired as part of the show's seventh season from November 16, 2015 to November 19, 2015 on Cartoon Network.  "Adventure Time" follows the adventures of Finn (voiced by Jeremy Shada), a human boy, and his best friend and adoptive brother Jake (voiced by John DiMaggio), a dog with magical powers to change shape, grow and shrink at will.  In this limited event series, Princess Bubblegum (voiced by Hynden Walch) removes Marceline the Vampire Queen's (voiced by Olivia Olson) vampiric essence, which unleashes five recently resurrected vampires onto Ooo.  Marceline, Bubblegum, Finn, Jake, and Peppermint Butler (voiced by Steve Little) are forced to deal with the fallout.

Elements (miniseries): Elements is an American animated miniseries based on the show "Adventure Time" by Pendleton Ward.  It aired as part of the show's ninth season on Cartoon Network from April 24 to April 27, 2017.  "Adventure Time" follows the adventures of Finn (voiced by Jeremy Shada), a human boy, and his best friend and adoptive brother Jake (voiced by John DiMaggio), a dog with magical powers to change shape, grow and shrink at will.  In this limited event series, which itself follows the events of the "Islands" miniseries, Finn, Jake, and BMO return home to discover that Ooo has been turned into a veritable dystopia thanks to extreme elemental magic.  Finn and Jake team up with Ice King (voiced by Tom Kenny), Betty (voiced by Felicia Day), and Lumpy Space Princess (voiced by Ward) to set things straight.

Rachael Ray's Tasty Travels: Rachael Ray's Tasty Travels is a television show based on cook Rachael Ray and her travels around the world (somewhat similar to her 2002 Food Network show, "$40 a Day").  However, in this show she is not restricted by a budget and showcases food from more upscale eateries.  She tries different types of food from each place she visits, and gives a "Hot List of Values", which includes some of her favorite places visited from "$40 a Day".  The show airs on the Food Network and is her fourth Food Network program.  It first aired on August 26, 2005.  She provides voiceovers for most of the show and is shown at only one or two places.  Her husband, John Cusimano, usually accompanies her at the one or two restaurants she visits per episode.  The show was developed with Producer Wade Sheeler following the success of her first travel show on Food Network, "$40 a Day".

Question: The television show that follows the show based on "Adventure Time" first aired in what year?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "followed_show_name": {
      "type": "string",
      "description": "The name of the television show that follows another show based on 'Adventure Time'."
    },
    "followed_show_air_year": {
      "type": "integer",
      "description": "The year the followed television show first aired."
    },
    "preceding_show_name": {
      "type": "string",
      "description": "The name of the television show that the 'followed_show_name' explicitly follows."
    },
    "base_show_name": {
      "type": "string",
      "description": "The name of the original show that both the preceding and followed shows are based on."
    }
  },
  "required": [
    "followed_show_name",
    "followed_show_air_year",
    "preceding_show_name",
    "base_show_name"
  ],
  "additionalProperties": false
}
