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
A Quiet Place (film): A Quiet Place is an upcoming American supernatural horror film directed by John Krasinski.  The film stars Emily Blunt and John Krasinski.  The film will be produced by Michael Bay through his Platinum Dunes banner.

The Hollars: The Hollars is a 2016 American comedy-drama film directed by John Krasinski and written by James C. Strouse.  The film stars an ensemble cast led by Krasinski, starring Sharlto Copley, Charlie Day, Richard Jenkins, Anna Kendrick and Margo Martindale.  The film had its world premiere at the Sundance Film Festival on January 24, 2016.  The film was released on August 26, 2016, by Sony Pictures Classics.

Detroit (film): Detroit is a 2017 American period crime drama film directed by Kathryn Bigelow and written by Mark Boal.  Based on the Algiers Motel incident during Detroit's 1967 12th Street Riot, the film's release commemorated the 50th anniversary of the event.  The film stars John Boyega, Will Poulter, Algee Smith, Jason Mitchell, John Krasinski and Anthony Mackie.

Promised Land (2012 film): Promised Land is a 2012 American drama film directed by Gus Van Sant and starring Matt Damon, John Krasinski, Frances McDormand and Hal Holbrook.  The screenplay is written by Damon and Krasinski based on a story by Dave Eggers.  "Promised Land" follows two corporate salespeople who visit a rural town in an attempt to buy drilling rights from the local residents.

John Krasinski: John Burke Krasinski ( ; born October 20, 1979) is an American actor and filmmaker.  He is widely known for his role as Jim Halpert on the NBC sitcom "The Office" (2005–2013), for which he received critical acclaim and won numerous awards.  He also served as a producer and occasional director of the show.

List of Lip Sync Battle episodes: "Lip Sync Battle" is an American musical reality competition series which premiered on April 2, 2015, on the Spike cable network.  The show is based on an idea initially introduced to "Late Night with Jimmy Fallon" by John Krasinski.  In each episode, two celebrities compete against each other using lip sync, and after two rounds, the audience decides the winner of the night.  The show is hosted by rapper LL Cool J, while model Chrissy Teigen serves as color commentator.  Several broadcasters opted to pass on the game show before it was eventually picked up by the American cable channel Spike, which was in the middle of rebranding.  The show has been a big success for the network and well received by both the critics and the audiences.  In April 2015, "Lip Sync Battle" was renewed for a second season, which premiered on January 7, 2016.  In January 2016, the show was renewed for a third season.

Aloha (film): Aloha is a 2015 American romantic comedy-drama film written, produced and directed by Cameron Crowe.  The film, starring Bradley Cooper, Emma Stone, Rachel McAdams, Bill Murray, John Krasinski, Danny McBride and Alec Baldwin, was released on May 29, 2015.  The film received negative reviews from critics and has grossed only $26 million against a budget of $37 million, making the film a box office bomb.

Born in China: Born in China (我們誕生在中國) is a 2016 nature documentary film directed by Lu Chuan.  A co-production between Disneynature and Shanghai Media Group, the film was released in China on August 12, 2016 and in the United States on April 21, 2017, one day before Earth Day.  The film focuses on a female snow leopard named Dawa and her cubs, a young golden snub-nosed monkey named Tao Tao, a female giant panda named Ya Ya along with her daughter Mei Mei, and a herd of chiru.  The American release of the film is narrated by John Krasinski and the Chinese release is narrated by Zhou Xun.

Big Miracle: Big Miracle is a 2012 British-American drama film directed by Ken Kwapis, and stars Drew Barrymore and John Krasinski.  The film is based on Tom Rose's 1989 book "Freeing the Whales", which covers Operation Breakthrough, the 1988 international effort to rescue gray whales trapped in ice near Point Barrow, Alaska.

Big Miracle (book): Big Miracle tells the true story of three gray whales trapped beneath Arctic ice in the fall of 1988, and of Operation Breakthrough, the collaborative efforts to free them by oil company executives, activists, Inupiat people, the U.S. military, and Soviet ice-breakers.  Written by journalist Tom Rose (who covered the event for a Japanese news channel at the time), the book was originally published in 1989, titled "Freeing the Whales: How the Media Created the World's Greatest Non-Event".  It was re-released under its current title by St. Martin’s Press in 2011.

Question: What country of origin does Big Miracle and John Krasinski have in common?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "entity_1_name": {
      "type": "string",
      "description": "The name of the first entity."
    },
    "entity_1_origin_countries": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of countries of origin for the first entity."
    },
    "entity_2_name": {
      "type": "string",
      "description": "The name of the second entity."
    },
    "entity_2_origin_country": {
      "type": "string",
      "description": "The country of origin for the second entity."
    },
    "common_country_of_origin": {
      "type": "string",
      "description": "The country of origin that both entities have in common."
    }
  },
  "required": [
    "entity_1_name",
    "entity_1_origin_countries",
    "entity_2_name",
    "entity_2_origin_country",
    "common_country_of_origin"
  ],
  "additionalProperties": false
}
